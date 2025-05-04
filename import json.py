import json

with open('d:/FZGZ/major.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(f"共转换 {len(data)} 个专业")
    print("前3个专业示例：")
    for item in data[:3]:
        print(f"{item['code']} - {item['name']}")