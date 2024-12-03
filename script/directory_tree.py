import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# 设置 Firefox 驱动
service = Service(r"C:\Users\liu51\Documents\PycharmProjects\web-ui-main\driver\windows\geckodriver.exe")  # 替换为你的 geckodriver 路径
options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # 修改为你的 Firefox 安装路径

# 启动 Firefox 浏览器
driver = webdriver.Firefox(service=service, options=options)

# 最大化窗口
driver.maximize_window()

# 打开 URL 并验证页面是否加载成功
url = "http://airnavx.hnatechnic.com/airnavx/document/680101_SGML_C/toc?itemId=680101_SGML_C_EN11210701001&parentId=680101_SGML_C_EN11210701&itemType=SHEET&wc=actype:A330;customization:CHH;doctype:IPC"
driver.get(url)

# 确保页面加载后继续操作
try:
    driver.find_element(By.CLASS_NAME, "access-code").send_keys("qweasd")
    driver.find_element(By.CLASS_NAME, "access-code-button").click()
    time.sleep(3)  # 等待加载

    # 递归函数：跳过指定文本并逐级展开节点，并收集数据
    def expand_and_collect_text(element, current_level_data):
        try:
            item_text = element.text.strip()

            # 打印节点文本用于调试
            print(f"当前节点文本: {item_text}")

            # 根据层级添加结构
            new_data = {"name": item_text, "sub_items": []}

            # 检查 FIG. 标签，直接作为子节点添加
            if "FIG." in item_text:
                print(f"找到 FIG. 标签: {item_text}，准备点击以展开")
                current_level_data.append(new_data)
                return

            # 将当前节点添加到上一级的数据结构中
            current_level_data.append(new_data)

            # 定位到扩展按钮并滚动到视图中
            expand_button = element.find_element(By.XPATH, ".//md-icon[contains(@class, 'ng-scope')]")
            # 滚动到元素位置
            driver.execute_script("arguments[0].scrollIntoView();", expand_button)
            time.sleep(0.5)
            expand_button.click()
            time.sleep(1)

            # 遍历子级并递归处理
            sub_items = element.find_elements(By.XPATH, ".//ul[@class='leftpadding ng-scope']/li")
            for sub_item in sub_items:
                expand_and_collect_text(sub_item, new_data["sub_items"])

        except Exception as e:
            print("Error:", e)

    # 过滤函数，在保存前清洗数据
    def filter_data(data):
        for item in data:
            # 如果 name 以 expand_more 开头，过滤斜杠后的内容
            if item["name"].startswith("expand_more"):
                item["name"] = item["name"].split("\\")[0]
            # 递归处理 sub_items
            filter_data(item["sub_items"])

    # 初始化数据结构
    data = []

    # 定位根节点并递归展开，跳过第一个菜单项
    root_items = driver.find_elements(By.XPATH, "//ul[@class='leftpadding ng-scope']/li")
    for index, root_item in enumerate(root_items):
        if index == 0:
            print("跳过第一个主菜单项")
            continue
        expand_and_collect_text(root_item, data)

    # 在保存之前过滤数据
    filter_data(data)

    # 将收集的数据保存为 JSON 文件
    with open("directory_structure.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print("数据已保存到 directory_structure.json 文件中")

finally:
    # 关闭浏览器
    time.sleep(10)
    driver.quit()
