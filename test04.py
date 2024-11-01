import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# 指定 ChromeDriver 路径
service = Service(r"C:\Users\liu51\Documents\chrome-win\chromedriver.exe")  # 请将此路径替换为你的 ChromeDriver 路径
driver = webdriver.Chrome(service=service)

# 最大化窗口
driver.maximize_window()

# 尝试打开 URL 并验证页面是否加载成功
url = "http://airnavx.hnatechnic.com/airnavx/document/680101_SGML_C/toc?itemId=680101_SGML_C_EN11210701001&parentId=680101_SGML_C_EN11210701&itemType=SHEET&wc=actype:A330;customization:CHH;doctype:IPC"
driver.get(url)

# 检查页面标题和 URL 以验证是否正确加载
print("页面标题:", driver.title)
print("当前 URL:", driver.current_url)

# 检查页面是否加载正确
if "404" in driver.title or "Not Found" in driver.page_source:
    print("页面加载失败，出现 404 错误。")
else:
    print("页面加载成功。")

# 确保页面加载后继续操作
try:
    driver.find_element(By.CLASS_NAME, "access-code").send_keys("qweasd")
    driver.find_element(By.CLASS_NAME, "access-code-button").click()
    time.sleep(3)  # 等待加载

    # 创建保存文件夹
    if not os.path.exists("images"):
        os.makedirs("images")

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
                    print_icon = driver.find_element(By.XPATH, "//md-icon[@class='material-icons md-light md-24 ng-scope' and text()='print']")
                    print_icon.click()
                    time.sleep(1)

                    # 点击弹出窗口中的 PRINT 按钮
                    print_button = driver.find_element(By.XPATH, "//button[@class='popupCloseButton md-raised md-button md-ink-ripple' and text()='PRINT']")
                    print_button.click()
                    time.sleep(3)

                    # 使用 pyautogui 进行网页保存操作
                    time.sleep(2)  # 等待系统保存窗口打开
                    pyautogui.hotkey('ctrl', 's')  # 打开保存选项
                    time.sleep(2)
                    pyautogui.press('enter', presses=2)  # 确认保存
                    time.sleep(5)

                    # 强制使用 JavaScript 切换回第一个标签页
                    first_tab_handle = driver.window_handles[0]
                    # driver.close()
                    driver.switch_to.window(first_tab_handle)  # 切换到第一个窗口
                    print("已切换回第一个标签页:", driver.title)

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

finally:
    # 关闭浏览器
    time.sleep(10)
    driver.quit()
