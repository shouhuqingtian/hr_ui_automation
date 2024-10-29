# -*- coding: utf-8 -*-
# @Time    : 2024/10/22
# @Author  : Bin
# @Software: PyCharm
# @File    : test03.py
"""
import pandas as pd

# 读取 Excel 文件
df = pd.read_excel('aircraft_data.xlsx')

# 去掉含有任何空白值的行
df_cleaned = df.dropna(how='all')

# 将清理后的数据保存回 Excel 文件
df_cleaned.to_excel('B737-8飞机数据.xlsx', index=False)

print("清理完毕，数据已保存到 cleaned_B737-8飞机数据.xlsx")
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

# 要抓取的初始URL（修改为实际URL）
base_url = 'http://xmyzl.com/?mod=search&keyword=B737-8&page='

# 用于保存所有数据
all_data = []

# 循环遍历页面，假设共有79页
for page in range(1, 80):
    # 构造请求的URL
    url = base_url + str(page)
    response = requests.get(url)

    # 使用BeautifulSoup解析页面
    soup = BeautifulSoup(response.content, 'html.parser')

    # 找到表格（通过类名或table标签定位）
    table = soup.find('table', {'class': 'table'})

    # 遍历表格中的每一行
    for row in table.find_all('tr')[1:]:  # 跳过表头
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]  # 获取列数据并去掉空格
        all_data.append(cols)
    sleep(0.5)
# 将数据转为DataFrame
df = pd.DataFrame(all_data,
                  columns=['机号', '状态', '机型', '发动机', '航空公司', '归属', '引进时间', '首次交付', '序列号',
                           '备注信息'])

# 保存到Excel
df.to_excel('aircraft_data.xlsx', index=False)

print("数据已保存到aircraft_data.xlsx")
