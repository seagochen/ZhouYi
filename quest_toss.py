# -*- coding: utf-8 -*-
from typing import List

from utils.query_gua import get_gua_from_numbers


# 投掷结果转换为爻
def toss_to_yao(toss):
    """
    将三枚硬币投掷结果转换为爻值
    :param toss: list[str] 投掷结果（正或反）
    :return: str 爻值
    """
    yao_value = sum([3 if coin == '正' else 2 for coin in toss])
    return yao_value


# 交互式获取投掷结果
def get_toss_results() -> List[int]:
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


# 主程序
if __name__ == "__main__":

    toss_results = get_toss_results()
    print("投掷结果：", toss_results)

    # 对投掷结果进行处理，将正反转换为阴阳，得到六个爻值
    try:
        gua_result = get_gua_from_numbers(toss_results)

        # 输出本卦信息
        print("\n=== 本卦 ===")
        print(f"名称：{gua_result['ben_gua']['name']}（{gua_result['ben_gua']['binary']}）")
        print(f"卦辞：{gua_result['ben_gua']['description']}")
        print(f"卦象：\n{gua_result['ben_gua']['image']}")

        # 输出变卦信息
        print("\n=== 变卦 ===")
        print(f"名称：{gua_result['bian_gua']['name']}（{gua_result['bian_gua']['binary']}）")
        print(f"卦辞：{gua_result['bian_gua']['description']}")
        print(f"卦象：\n{gua_result['bian_gua']['image']}")

        # 输出变爻信息（仅变动爻的爻辞）
        if gua_result["changing_lines"]:
            print("\n=== 变爻爻辞 ===")
            for line, yaoci in gua_result["changing_lines"]:
                print(f"第 {line} 爻：{yaoci}")

    except ValueError as e:
        print(f"输入错误：{e}")
