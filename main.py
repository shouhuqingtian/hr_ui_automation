from openpyxl import load_workbook, Workbook

# 读取excel
wb = load_workbook(r'C:\Users\liu51\Desktop\Test\00 资料\9_python自动化\testcase_api_wuye.xlsx')

# 获取工作表
sheet = wb['register']

# 读取所有字段数据
for row in sheet.iter_rows(min_row=2, values_only=True):
    print(row)

# 测试
