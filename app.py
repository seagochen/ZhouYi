# -*- coding: utf-8 -*-

from utils.load_gua import load_gua
from utils.toss_gua import get_toss_results, yao_to_binary
from utils.query_gua import get_gua_info, generate_gua_image


# 主程序
if __name__ == "__main__":

    # 按照二进制顺序排列的六十四卦
    gua_dict = load_gua("data/gua")

    toss_results = get_toss_results()
    # toss_results = ['8', '6', '8', '7', '7', '7']
    print("投掷结果：", toss_results)

    # 构建本卦和变卦的二进制表示
    ben_gua_binary = yao_to_binary(toss_results)
    bian_gua_binary = yao_to_binary(toss_results, changing=True)

    # 查找卦象信息
    ben_gua_info = get_gua_info(ben_gua_binary, gua_dict)
    bian_gua_info = get_gua_info(bian_gua_binary, gua_dict)

    # 生成卦象图案
    ben_gua_image = generate_gua_image(ben_gua_binary)
    bian_gua_image = generate_gua_image(bian_gua_binary)

    # 输出结果
    print("\n=== 占卜结果 ===")
    print(f"本卦：{ben_gua_info['name']}（{ben_gua_binary}）")
    print(f"卦辞：{ben_gua_info['description']}")
    print(f"卦象：\n{ben_gua_image}")
    print(f"\n变卦：{bian_gua_info['name']}（{bian_gua_binary}）")
    print(f"卦辞：{bian_gua_info['description']}")
    print(f"卦象：\n{bian_gua_image}")
