# -*- coding: utf-8 -*-
# @Time    : 2024/8/12
# @Author  : Bin
# @Software: PyCharm
# @File    : test01.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

# 启动Chrome浏览器
driver = webdriver.Chrome()

# 存储所有页的数据
all_data = []

# 遍历79页
for page in range(1, 80):  # 假设页面从1开始到79
    # 打开每一页的网址，注意修改分页参数
    driver.get(f'http://xmyzl.com/?mod=search&keyword=B737-8&page={page}')  # 修改为实际的URL

    # 等待表格加载完毕
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'table'))
    )

    # 获取页面的HTML内容
    html = driver.page_source

    # 使用BeautifulSoup解析页面内容
    soup = BeautifulSoup(html, 'html.parser')

    # 查找表格
    table = soup.find('table', {'class': 'table'})

    # 确保找到表格再进行后续操作
    if table:
        for row in table.find_all('tr')[1:]:  # 跳过表头
            cols = row.find_all('td')
            cols = [col.text.strip() for col in cols]
            all_data.append(cols)
    else:
        print(f"在第{page}页未找到表格")

    # 等待一小段时间再翻页，避免被网站识别为爬虫
    time.sleep(2)

# 关闭浏览器
driver.quit()

# 将数据保存到Excel
df = pd.DataFrame(all_data,
                  columns=['机号', '状态', '机型', '发动机', '航空公司', '归属', '引进时间', '首次交付', '序列号',
                           '备注信息'])
df.to_excel('aircraft_data.xlsx', index=False)
print("数据已保存到 aircraft_data.xlsx")
