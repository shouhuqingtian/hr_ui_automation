from datetime import datetime, timedelta
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

class WebPageProcessor:
    def __init__(self, driver_path, firefox_path, url, start_main_menu_text, start_sub_menu_text):
        self.service = Service(driver_path)
        self.options = Options()
        self.options.binary_location = firefox_path
        self.driver = webdriver.Firefox(service=self.service, options=self.options)
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()
        self.url = url
        self.start_main_menu_text = start_main_menu_text
        self.start_sub_menu_text = start_sub_menu_text
        self.start_main_menu_processing = False
        self.start_sub_menu_processing = False
        self.pause_times = ["06:55", "23:55"]
        self.pause_duration = timedelta(minutes=20)
        self.last_pause_time = None

    def load_page(self):
        self.driver.get(self.url)
        if "404" in self.driver.title or "Not Found" in self.driver.page_source:
            print("页面加载失败，出现 404 错误。")
        else:
            print("页面加载成功。")

    def check_pause_time(self):
        current_time = datetime.now().strftime("%H:%M")
        if current_time in self.pause_times and (self.last_pause_time is None or self.last_pause_time != current_time):
            print(f"当前时间 {current_time} 达到暂停时间，暂停 20 分钟...")
            self.last_pause_time = current_time
            time.sleep(self.pause_duration.total_seconds())
            print("恢复执行...")
            self.last_pause_time = None

    def login(self, access_code):
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "access-code")))
            self.driver.find_element(By.CLASS_NAME, "access-code").send_keys(access_code)
            self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "access-code-button")))
            self.driver.find_element(By.CLASS_NAME, "access-code-button").click()
        except Exception as e:
            print(f"登录失败: {e}")

    def expand_and_collect_text(self, element):
        try:
            item_text = element.text.strip()

            if item_text == self.start_main_menu_text:
                self.start_main_menu_processing = True
                print(f"找到起始主菜单项 '{item_text}'，开始处理后续菜单项")

            if not self.start_main_menu_processing:
                print(f"跳过主菜单项: {item_text}")
                return

            if "FIG." in item_text:
                if not self.start_sub_menu_processing:
                    if item_text == self.start_sub_menu_text:
                        self.start_sub_menu_processing = True
                        print(f"找到起始子菜单项 '{item_text}'，开始处理后续 FIG. 标签项")
                    else:
                        print(f"跳过 FIG. 标签: {item_text}")
                        return

                if self.start_sub_menu_processing:
                    print(f"处理 FIG. 标签: {item_text}")
                    self.driver.execute_script("arguments[0].scrollIntoView();", element)
                    time.sleep(1)

                    try:
                        element.click()
                        time.sleep(2)
                        print_icon = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//md-icon[@class='material-icons md-light md-24 ng-scope' and text()='print']")))
                        print_icon.click()

                        print_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='popupCloseButton md-raised md-button md-ink-ripple' and text()='PRINT']")))
                        print_button.click()

                        time.sleep(2)
                        pyautogui.hotkey('ctrl', 's')
                        time.sleep(2)
                        pyautogui.press('enter')

                        time.sleep(1)
                        pyautogui.press('left')
                        pyautogui.press('enter')

                        time.sleep(2)
                        first_tab_handle = self.driver.window_handles[0]
                        second_tab_handle = self.driver.window_handles[1]
                        self.driver.switch_to.window(second_tab_handle)
                        self.driver.close()
                        self.driver.switch_to.window(first_tab_handle)
                        print("已切换回第一个标签页:", self.driver.title)

                        self.check_pause_time()

                    except Exception as e:
                        print("打印操作失败：", e)
                        print("当前时间:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    return

            expand_button = element.find_element(By.XPATH, ".//md-icon[contains(@class, 'ng-scope')]")
            expand_button.click()
            time.sleep(1)

            sub_items = element.find_elements(By.XPATH, ".//ul[@class='leftpadding ng-scope']/li")
            for sub_item in sub_items:
                self.expand_and_collect_text(sub_item)

        except Exception as e:
            print("Error:", e)

    def process_menu(self):
        try:
            root_items = self.driver.find_elements(By.XPATH, "//ul[@class='leftpadding ng-scope']/li")
            for root_item in root_items:
                self.expand_and_collect_text(root_item)
        finally:
            time.sleep(10)
            self.driver.quit()

if __name__ == "__main__":
    processor = WebPageProcessor(
        driver_path=r"C:\Users\liu51\Documents\PycharmProjects\web-ui-main\driver\windows\geckodriver.exe",
        firefox_path=r"C:\Program Files\Mozilla Firefox\firefox.exe",
        url="http://airnavx.hnatechnic.com/airnavx/document/680101_SGML_C/toc?itemId=680101_SGML_C_EN11210701001&parentId=680101_SGML_C_EN11210701&itemType=SHEET&wc=actype:A330;customization:CHH;doctype:IPC",
        start_main_menu_text="chevron_right 55 - STABILIZERS",
        start_sub_menu_text="chevron_right description FIG. 55-41-11-11A - TIP-RUDDER (Jan 01/17)"
    )
    processor.load_page()
    processor.login("qweasd")
    processor.process_menu()
