import json
import os
from typing import List


def load_gua(gua_folder: str):

    data_dict = {}

    for file in os.listdir(gua_folder):
        if file.endswith('.json'):
            with open(os.path.join(gua_folder, file), 'r', encoding='utf-8') as f:
                data = json.load(f)
                data_dict.update(data)

    return data_dict


def get_gua_info(yao_code, gua_dict):
    if yao_code in gua_dict:
        return gua_dict[yao_code]
    else:
        return {'name': '未知卦象', 'description': f'二进制表示 {yao_code} 未找到对应卦象信息。'}


def generate_gua_image(yao_code: str) -> str:
    image = []
    for bit in yao_code:
        if bit == '1':  # 阳爻
            image.append('---')
        else:  # 阴爻
            image.append('- -')
    return '\n'.join(image)


def numbers_to_gua_code(yao_list: List[int], changing=False) -> str:
    """
    把爻转换成二进制字符串
    :param yao_list: 6个数字（6,7,8,9）
    :param changing: 是否计算变卦（6变阳, 9变阴）
    :return: 6位二进制字符串（低位在前）
    """
    binary_str = ""
    for yao in yao_list:
        if changing:  # 计算变卦
            if yao == 6:
                binary_str += "1"  # 6 变 阳（⚊）
            elif yao == 9:
                binary_str += "0"  # 9 变 阴（⚋）
            elif yao == 7:
                binary_str += "1"  # 7 保持 阳（⚊）
            elif yao == 8:
                binary_str += "0"  # 8 保持 阴（⚋）
        else:  # 计算本卦
            if yao in [6, 8]:
                binary_str += "0"  # 6、8 是阴（⚋）
            elif yao in [7, 9]:
                binary_str += "1"  # 7、9 是阳（⚊）

    return binary_str[::-1]  # 易经卦象低位在前，高位在后，需反转


def get_gua_from_numbers(numbers: List[int]):
    """
    根据用户输入的六个数字（6-9），计算对应的本卦和变卦，并仅包含变爻的爻辞
    :param numbers: List[int] 长度为6的列表，包含6-9
    :return: dict 包含本卦、变卦的信息，及变爻爻辞
    """
    if len(numbers) != 6 or not all(num in [6, 7, 8, 9] for num in numbers):
        raise ValueError("输入的数字必须是6个，并且范围只能是 6, 7, 8, 9")

    # 读取卦象数据
    gua_dict = load_gua("data/gua")

    # 转换为二进制卦象
    src_gua_code = numbers_to_gua_code(numbers)
    dst_gua_code = numbers_to_gua_code(numbers, changing=True)

    # 获取卦象信息
    ben_gua_info = get_gua_info(src_gua_code, gua_dict)
    bian_gua_info = get_gua_info(dst_gua_code, gua_dict)

    # 生成卦象图
    ben_gua_image = generate_gua_image(src_gua_code)
    bian_gua_image = generate_gua_image(dst_gua_code)

    # 确保爻辞存在，否则给默认值
    ben_yaoci = ben_gua_info.get("yaoci", ["无爻辞"] * 6)

    # 记录变爻（6、9 变）
    changing_lines = [(idx + 1, ben_yaoci[idx]) for idx, num in enumerate(numbers) if num in [6, 9]]

    # 返回结果
    return {
        "ben_gua": {
            "name": ben_gua_info["name"],
            "binary": src_gua_code,
            "description": ben_gua_info["description"],
            "image": ben_gua_image,
        },
        "bian_gua": {
            "name": bian_gua_info["name"],
            "binary": dst_gua_code,
            "description": bian_gua_info["description"],
            "image": bian_gua_image,
        },
        "changing_lines": changing_lines  # 仅包含变爻的爻辞
    }
