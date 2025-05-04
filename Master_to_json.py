import json

def convert_txt_to_json(input_file, output_file):
    # 读取文本文件（改用UTF-16编码）
    with open(input_file, 'r', encoding='utf-16') as f:
        lines = f.readlines()
    
    # 跳过标题行，处理数据行
    data = []
    for line in lines[1:]:
        # 使用更可靠的分割方式
        parts = line.strip().split(maxsplit=1)
        if len(parts) == 2:
            code, name = parts
            data.append({
                "专业代码": code.strip(),
                "专业名称": name.strip()
            })
    
    # 写入JSON文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    input_path = r'd:\FZGZ\硕士2022.txt'
    output_path = r'd:\FZGZ\master.json'
    convert_txt_to_json(input_path, output_path)
    print(f'转换完成，已保存至 {output_path}')