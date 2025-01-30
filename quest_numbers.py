# -*- coding: utf-8 -*-
import sys

from utils.query_gua import get_gua_from_numbers

if __name__ == "__main__":
    # 获取命令行参数
    if len(sys.argv) != 2:
        print("用法: python3 quest_numbers.py <6个数字，例如 698696>")
        sys.exit(1)

    # 解析输入的数字字符串
    input_str = sys.argv[1]
    
    if len(input_str) != 6 or not all(c in "6789" for c in input_str):
        print("错误：输入的数字必须是6位，并且范围只能是 6, 7, 8, 9")
        sys.exit(1)

    # 转换为数字列表
    numbers = [int(c) for c in input_str]

    try:
        gua_result = get_gua_from_numbers(numbers)
        
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
