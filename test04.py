import os
import time
import pyautogui
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from pywinauto import Application

# 启动 Firefox 浏览器
driver_path = r"C:\Users\liu51\Documents\PycharmProjects\web-ui-main\driver\windos\geckodriver.exe"  # 替换为实际的 geckodriver 路径
firefox_options = Options()
driver = webdriver.Firefox(executable_path=driver_path, options=firefox_options)

# 最大化窗口
driver.maximize_window()

# 访问页面并登录
url = "http://airnavx.hnatechnic.com/airnavx/document/680101_SGML_C/toc?itemId=680101_SGML_C_EN11210701001&parentId=680101_SGML_C_EN11210701&itemType=SHEET&wc=actype:A330;customization:CHH;doctype:IPC"
driver.get(url)
driver.find_element(By.CLASS_NAME, "access-code").send_keys("qweasd")
driver.find_element(By.CLASS_NAME, "access-code-button").click()
time.sleep(3)  # 等待加载

# 创建保存文件夹
if not os.path.exists("images"):
    os.makedirs("images")

# 保存页面的SVG图像和表格信息
def save_page_content():
    # 下载所有的SVG图片
    svg_elements = driver.find_elements(By.XPATH, "//img[contains(@src, '.SVG')]")
    for svg in svg_elements:
        src = svg.get_attribute("src")
        full_url = url.rsplit("/", 1)[0] + "/" + src  # 构造完整URL
        file_name = os.path.join("images", os.path.basename(src))
        response = requests.get(full_url)
        with open(file_name, "wb") as f:
            f.write(response.content)

# 递归函数：跳过指定文本并逐级展开节点
def expand_and_collect_text(element):
    try:
        item_text = element.text.strip()
        if "MANUAL FRONT MATTER" in item_text:
            return  # 跳过 "MANUAL FRONT MATTER"

        print(f"当前节点文本: {item_text}")  # 输出当前节点文本以进行调试

        # 检查 FIG. 标签的条件
        if "FIG." in item_text:
            print(f"找到 FIG. 标签: {item_text}，准备点击以展开")
            try:
                # 点击 FIG. 节点以展开内容
                element.click()
                time.sleep(2)  # 等待 FIG. 页面内容加载

                # 定位并点击打印图标
                print_icon = driver.find_element(By.XPATH,
                                                 "//md-icon[@class='material-icons md-light md-24 ng-scope' and text()='print']")
                print_icon.click()
                time.sleep(1)

                # 点击弹出窗口中的 PRINT 按钮
                print_button = driver.find_element(By.XPATH,
                                                   "//button[@class='popupCloseButton md-raised md-button md-ink-ripple' and text()='PRINT']")
                print_button.click()
                time.sleep(3)

                # 使用 pyautogui 进行 PDF 保存操作
                # 打开系统打印窗口后，模拟键盘操作以选择 "保存为 PDF" 并保存文件
                time.sleep(2)  # 等待系统打印窗口打开
                pyautogui.hotkey('ctrl', 's')  # 打开打印选项（视系统配置可能需要手动调整）
                time.sleep(2)  # 等待打印窗口响应
                pyautogui.press('enter')  # 确认“保存为网页”
                time.sleep(2)
                pyautogui.typewrite(f"saved_page_{int(time.time())}.pdf")  # 输入保存文件名
                time.sleep(2)
                pyautogui.press('enter', presses=2)  # 确认保存


                # 保存页面内容（图片和表格）
                save_page_content()

                # 切换回原始标签页
                driver.switch_to.window(driver.window_handles[0])
                time.sleep(2)
            except Exception as e:
                print("打印操作失败：", e)
            return  # 打印完成后退出当前递归

        # 展开当前项
        expand_button = element.find_element(By.XPATH, ".//md-icon[contains(@class, 'ng-scope')]")
        expand_button.click()
        time.sleep(1)

        # 遍历子级
        sub_items = element.find_elements(By.XPATH, ".//ul[@class='leftpadding ng-scope']/li")
        for sub_item in sub_items:
            expand_and_collect_text(sub_item)

    except Exception as e:
        print("Error:", e)

# 定位根节点并递归展开
root_items = driver.find_elements(By.XPATH, "//ul[@class='leftpadding ng-scope']/li")
for root_item in root_items:
    expand_and_collect_text(root_item)

# 关闭浏览器
time.sleep(10)
driver.quit()
