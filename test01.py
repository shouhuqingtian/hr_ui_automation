import json

# 加载 JSON 文件
with open('directory_structure.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


# 过滤函数：仅保留以 "expand_more" 开头的项的第一个反斜杠之前的内容
def filter_structure(data):
    for item in data:
        # 检查并替换 name 字段
        if "name" in item and item["name"].startswith("expand_more"):
            # 仅保留第一个反斜杠之前的内容
            original_name = item["name"]
            item["name"] = item["name"].split("\\")[0]
            print(f"过滤后的名称: {item['name']}")  # 打印过滤后的 name 字段

        # 递归处理 sub_items
        if "sub_items" in item:
            filter_structure(item["sub_items"])


# 应用过滤
filter_structure(data)

# 将过滤后的数据保存到新文件
with open('directory_structure_filtered2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("过滤完成并保存为 'directory_structure_filtered.json'")
