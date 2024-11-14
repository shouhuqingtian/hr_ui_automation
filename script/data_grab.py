from datetime import datetime, timedelta
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

# 指定 geckodriver 路径
service = Service(r"C:\Users\liu51\Documents\PycharmProjects\web-ui-main\driver\windows\geckodriver.exe")
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

# 启动 Firefox 浏览器
driver = webdriver.Firefox(service=service, options=options)
wait = WebDriverWait(driver, 20)  # 设置全局显式等待时间为 20 秒

# 最大化窗口
driver.maximize_window()

# 尝试打开 URL 并验证页面是否加载成功
url = "http://airnavx.hnatechnic.com/airnavx/document/680101_SGML_C/toc?itemId=680101_SGML_C_EN11210701001&parentId=680101_SGML_C_EN11210701&itemType=SHEET&wc=actype:A330;customization:CHH;doctype:IPC"
driver.get(url)
# 检查页面是否加载正确
if "404" in driver.title or "Not Found" in driver.page_source:
    print("页面加载失败，出现 404 错误。")
else:
    print("页面加载成功。")

# 定义全局变量，标记是否已找到起始主菜单项
start_main_menu_processing = False
start_main_menu_text = "chevron_right 55 - STABILIZERS"
start_sub_menu_processing = False
start_sub_menu_text = "chevron_right description FIG. 55-41-11-11A - TIP-RUDDER (Jan 01/17)"

# 定义暂停的时间点和持续时间
pause_times = ["06:55", "23:55"]  # 需要暂停的时间点
pause_duration = timedelta(minutes=20)  # 暂停20分钟
last_pause_time = None  # 记录上次暂停的时间

# 检查当前时间是否达到暂停时间
def check_pause_time():
    global last_pause_time
    current_time = datetime.now().strftime("%H:%M")  # 精确到分钟

    # 检查当前时间是否等于暂停时间，并确保没有重复暂停
    if current_time in pause_times and (last_pause_time is None or last_pause_time != current_time):
        print(f"当前时间 {current_time} 达到暂停时间，暂停 20 分钟...")
        last_pause_time = current_time  # 更新最后的暂停时间
        time.sleep(pause_duration.total_seconds())  # 暂停 20 分钟
        print("恢复执行...")
        last_pause_time = None  # 重置 last_pause_time 以便下次暂停

# 确保页面加载后继续操作
try:
    # 等待访问码输入框出现
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "access-code")))
    driver.find_element(By.CLASS_NAME, "access-code").send_keys("qweasd")

    # 等待访问按钮可点击
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "access-code-button")))
    driver.find_element(By.CLASS_NAME, "access-code-button").click()

    # 递归函数：逐级展开主菜单和子菜单，并进行相应的处理
    def expand_and_collect_text(element):
        global start_main_menu_processing, start_sub_menu_processing
        try:
            item_text = element.text.strip()

            # 检查是否达到起始主菜单项
            if item_text == start_main_menu_text:
                start_main_menu_processing = True
                print(f"找到起始主菜单项 '{item_text}'，开始处理后续菜单项")

            # 如果没有找到起始主菜单项，则跳过该主菜单项的子菜单




            if not start_main_menu_processing:
                print(f"跳过主菜单项: {item_text}")
                return  # 跳过，直到找到目标主菜单项

            # 仅当主菜单达到标准时才进行子菜单的处理
            if start_main_menu_processing:
                # 检查 FIG. 标签的条件
                if "FIG." in item_text:
                    # 如果未找到指定子菜单项，检查是否是指定的开始子菜单项
                    if not start_sub_menu_processing:
                        if item_text == start_sub_menu_text:
                            start_sub_menu_processing = True  # 找到起始子菜单项，开始处理后续 FIG.
                            print(f"找到起始子菜单项 '{item_text}'，开始处理后续 FIG. 标签项")
                        else:
                            print(f"跳过 FIG. 标签: {item_text}")
                            return  # 跳过 FIG. 标签但不匹配的项

                    # 如果 start_sub_menu_processing 为 True，则执行 FIG. 的保存操作
                    if start_sub_menu_processing:
                        print(f"处理 FIG. 标签: {item_text}")

                        # 使用 JavaScript 滚动到该元素的位置
                        driver.execute_script("arguments[0].scrollIntoView();", element)
                        time.sleep(1)  # 等待页面滚动完成

                        try:
                            # 点击 FIG. 标签展开内容
                            element.click()
                            time.sleep(2)  # 等待 FIG. 页面内容加载

                            # 定位并点击打印图标，等待其出现并可点击
                            print_icon = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                                "//md-icon[@class='material-icons md-light md-24 ng-scope' and text()='print']")))
                            print_icon.click()

                            # 点击弹出窗口中的 PRINT 按钮，等待其出现并可点击
                            print_button = wait.until(EC.element_to_be_clickable((By.XPATH,
                                                                                  "//button[@class='popupCloseButton md-raised md-button md-ink-ripple' and text()='PRINT']")))
                            print_button.click()

                            # 使用 pyautogui 进行网页保存操作
                            time.sleep(2)  # 等待系统保存窗口打开
                            pyautogui.hotkey('ctrl', 's')  # 打开保存选项
                            time.sleep(2)
                            pyautogui.press('enter')  # 点击保存

                            # 检查是否出现覆盖确认窗口并自动选择覆盖
                            time.sleep(1)
                            pyautogui.press('left')  # 选择“是”确认覆盖已有文件
                            pyautogui.press('enter')  # 确认覆盖

                            time.sleep(2)

                            # 强制使用 JavaScript 切换回第一个标签页
                            first_tab_handle = driver.window_handles[0]
                            second_tab_handle = driver.window_handles[1]
                            driver.switch_to.window(second_tab_handle)
                            driver.close()
                            driver.switch_to.window(first_tab_handle)  # 切换到第一个窗口
                            print("已切换回第一个标签页:", driver.title)

                            # 每次展开项之前检查是否需要暂停
                            check_pause_time()

                        except Exception as e:
                            print("打印操作失败：", e)
                            print("当前时间:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                        return  # 打印完成后退出当前递归

            # 如果不是 FIG. 标签，展开当前项
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
