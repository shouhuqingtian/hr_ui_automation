import os
import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException

# 设置 GeckoDriver 路径
geckodriver_path = r"C:\Users\liu51\Documents\PycharmProjects\web-ui-main\driver\windos\geckodriver.exe"
firefox_binary_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # 替换为 Firefox 浏览器的实际路径

# 配置 Firefox 浏览器
firefox_options = Options()
firefox_options.binary_location = firefox_binary_path  # 显式指定 Firefox 二进制文件路径
firefox_options.add_argument("--private")
service = Service(geckodriver_path)

# 启动浏览器
driver = webdriver.Firefox(service=service, options=firefox_options)

# 打开登录页面并输入验证码
url = "http://airnavx.hnatechnic.com/airnavx/document/680101_SGML_C/toc?itemId=680101_SGML_C_EN11210701001&parentId=680101_SGML_C_EN11210701&itemType=SHEET&wc=actype:A330;customization:CHH;doctype:IPC"
driver.get(url)
driver.find_element(By.CLASS_NAME, "access-code").send_keys("qweasd")
driver.find_element(By.CLASS_NAME, "access-code-button").click()
time.sleep(3)

# 初始化数据列表，用于存储页面信息
data_list = []

# 定义函数以提取表格数据
def extract_table_data():
    table_data = []
    table_rows = driver.find_elements(By.XPATH, "//tr")  # 定位表格行

    # 遍历每一行并提取内容
    for row in table_rows:
        row_data = []
        columns = row.find_elements(By.XPATH, ".//td")  # 定位每一行的列
        for column in columns:
            row_data.append(column.text.strip())  # 获取每个单元格的文本
        if row_data:  # 只添加非空行
            table_data.append(row_data)

    return table_data

# 定义递归函数
def expand_and_collect_text(element):
    try:
        # 获取元素文本
        item_text = element.text.strip()
        if "MANUAL FRONT MATTER" in item_text:
            return

        print(f"当前节点文本: {item_text}")

        # 检查 FIG. 标签的条件
        if "FIG." in item_text:
            print(f"找到 FIG. 标签: {item_text}，准备点击以展开")
            try:
                # 等待元素可点击并点击
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//md-icon[contains(@class, 'ng-scope')]")))
                element.click()
                time.sleep(2)

                # 重新获取并滚动到图标元素
                print_icon = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//md-icon[@class='material-icons md-light md-24 ng-scope' and text()='print']"))
                )
                driver.execute_script("arguments[0].scrollIntoView();", print_icon)
                print_icon.click()
                time.sleep(1)

                # 切换到新标签页
                driver.switch_to.window(driver.window_handles[-1])

                # 等待 PRINT 按钮可点击
                print_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@class='popupCloseButton md-raised md-button md-ink-ripple' and text()='PRINT']"))
                )

                # 提取当前页面的表格数据
                page_data = extract_table_data()
                data_list.extend(page_data)  # 添加到总的数据列表中
                print("页面表格内容已保存")

                # 点击打印按钮
                print_button.click()
                time.sleep(3)

                # 尝试查找和保存图片
                try:
                    image_element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, "//img[@class='imageWidth']"))
                    )
                    img_src = image_element.get_attribute("src")
                    if img_src and not img_src.startswith("http"):
                        img_src = f"http://airnavx.hnatechnic.com/{img_src}"

                    # 获取动态名称并保存图片
                    img_name = f"{item_text.replace(' ', '_')}.svg"
                    img_path = os.path.join("images", img_name)
                    print(f"尝试保存图片: {img_name} from {img_src}")

                    # 下载并保存图片
                    img_data = requests.get(img_src).content
                    with open(img_path, "wb") as img_file:
                        img_file.write(img_data)
                        print(f"图片已保存: {img_name}")
                except (NoSuchElementException, TimeoutException) as e:
                    print("未找到图片，跳过保存。", e)

                # 关闭新标签页并切回原始标签页
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(2)
            except StaleElementReferenceException:
                print("元素已变更，需要重新查找")
            except Exception as e:
                print("打印操作失败：", e)
            return

        # 重新查找并展开当前项
        try:
            expand_button = element.find_element(By.XPATH, ".//md-icon[contains(@class, 'ng-scope')]")
            expand_button.click()
            time.sleep(1)
        except StaleElementReferenceException:
            print("展开失败，重新获取元素")
            return  # 或者重试获取该元素

        # 遍历子级
        sub_items = element.find_elements(By.XPATH, ".//ul[@class='leftpadding ng-scope']/li")
        for sub_item in sub_items:
            expand_and_collect_text(sub_item)

    except StaleElementReferenceException:
        print("检测到 StaleElementReferenceException，重新获取元素")
    except Exception as e:
        print("Error:", e)

# 定位根节点并递归展开
root_items = driver.find_elements(By.XPATH, "//ul[@class='leftpadding ng-scope']/li")
for root_item in root_items:
    expand_and_collect_text(root_item)

# 保存数据到 Excel 文件
df = pd.DataFrame(data_list)
df.to_excel("page_data.xlsx", index=False, header=False)  # 保存到 Excel 文件中
print("页面内容已保存到 page_data.xlsx")

# 关闭浏览器
driver.quit()
