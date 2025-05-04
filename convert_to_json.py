import json

def convert_txt_to_json(input_file, output_file):
    # 修改编码为utf-16-le并处理BOM
    with open(input_file, 'r', encoding='utf-16-le') as f:
        lines = [line.strip() for line in f if line.strip()]  # 过滤空行
    
    majors = []
    for line in lines[1:]:  # 跳过标题行
        try:
            code, name = line.split('\t')
            majors.append({
                "专业代码": code,
                "专业名称": name
            })
        except ValueError:
            print(f"跳过格式错误的行: {line}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(majors, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    input_path = r'd:\FZGZ\大学本科2024.txt'
    output_path = r'd:\FZGZ\bachelor.json'
    convert_txt_to_json(input_path, output_path)
    print(f'转换完成，已保存至 {output_path}')