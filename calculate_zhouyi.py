# -*- coding: utf-8 -*-

# 定义六十四卦的名称和卦辞（这里只列出部分作为示例，完整的需要添加所有卦的信息）
gua_dict = {
    '111111': {'name': '乾为天', 'description': '元亨，利贞。'},
    '000000': {'name': '坤为地', 'description': '元亨，利牝马之贞。'},
    # 需要补充完整的六十四卦信息
}

# 定义函数，将投掷结果转换为爻
def toss_to_yao(toss):
    # 将正面（阳面）记为3，反面（阴面）记为2
    yao_value = sum([3 if coin == '正' else 2 for coin in toss])
    if yao_value == 6:
        return '6'  # 老阴
    elif yao_value == 7:
        return '7'  # 少阳
    elif yao_value == 8:
        return '8'  # 少阴
    elif yao_value == 9:
        return '9'  # 老阳

# 定义函数，将爻值转换为二进制表示
def yao_to_binary(yao_list, changing=False):
    binary = ''
    for yao in yao_list:
        if yao in ['7', '9']:  # 阳爻
            if changing and yao == '9':
                binary += '0'  # 变爻，老阳变阴
            else:
                binary += '1'
        else:  # 阴爻
            if changing and yao == '6':
                binary += '1'  # 变爻，老阴变阳
            else:
                binary += '0'
    return binary

# 输入六次投掷结果
toss_results = []
print("请依次输入六次投掷结果，每次输入三个硬币的结果（正或反），用空格分隔。")
for i in range(6):
    toss = input(f"第{i+1}次投掷结果（例如：正 反 正）：").split()
    while len(toss) != 3 or not all(coin in ['正', '反'] for coin in toss):
        toss = input("输入有误，请重新输入（正或反，用空格分隔）：").split()
    toss_results.append(toss_to_yao(toss))

# 构建本卦和变卦的二进制表示
ben_gua_binary = yao_to_binary(toss_results)
bian_gua_binary = yao_to_binary(toss_results, changing=True)

# 将二进制字符串反转（因为卦是从下往上）
ben_gua_binary = ben_gua_binary[::-1]
bian_gua_binary = bian_gua_binary[::-1]

# 查找对应的卦信息
ben_gua_info = gua_dict.get(ben_gua_binary, {'name': '未知', 'description': '暂无解释'})
bian_gua_info = gua_dict.get(bian_gua_binary, {'name': '未知', 'description': '暂无解释'})

# 输出结果
print("\n=== 占卜结果 ===")
print(f"本卦：{ben_gua_info['name']}")
print(f"卦辞：{ben_gua_info['description']}")
print(f"\n变卦：{bian_gua_info['name']}")
print(f"卦辞：{bian_gua_info['description']}")

