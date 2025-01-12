# 投掷结果转换为爻
def toss_to_yao(toss):
    """
    将三枚硬币投掷结果转换为爻值
    :param toss: list[str] 投掷结果（正或反）
    :return: str 爻值
    """
    yao_value = sum([3 if coin == '正' else 2 for coin in toss])
    if yao_value == 6:
        return '6'  # 老阴
    elif yao_value == 7:
        return '7'  # 少阳
    elif yao_value == 8:
        return '8'  # 少阴
    elif yao_value == 9:
        return '9'  # 老阳


# 交互式获取投掷结果
def get_toss_results():
    toss_results = []
    print("请依次输入六次投掷结果，每次输入三个硬币的结果（正或反），用空格分隔。")
    for i in range(6):
        toss = input(f"第{i+1}次投掷结果（例如：正 反 正）：").split()

        # 输入检查, 三个硬币的结果必须为正或反
        while len(toss) != 3 or not all(coin in ['正', '反'] for coin in toss):  #
            toss = input("输入有误，请重新输入（正或反，用空格分隔）：").split()

        # 将投掷结果转换为爻值
        toss_results.append(toss_to_yao(toss))

    return toss_results



# 爻值转换为二进制表示
def yao_to_binary(yao_list, changing=False):
    binary = ''
    for yao in yao_list:
        if yao in ['7', '9']:  # 阳爻
            if changing and yao == '9':
                binary += '0'  # 老阳变阴
            else:
                binary += '1'
        else:  # 阴爻
            if changing and yao == '6':
                binary += '1'  # 老阴变阳
            else:
                binary += '0'
    return binary[::-1] # 反转
