# -*- coding: utf-8 -*-

# 完整的六十四卦信息
gua_dict = {
    '111111': {'name': '乾为天', 'description': '元亨利贞。'},
    '000000': {'name': '坤为地', 'description': '元亨利牝马之贞。'},
    '100010': {'name': '否', 'description': '否之匪人，不利君子贞，大往小来。'},
    '010001': {'name': '同人', 'description': '同人于野，亨。利涉大川。'},
    '111010': {'name': '大有', 'description': '元亨。'},
    '010111': {'name': '谦', 'description': '亨。君子有终。'},
    '110111': {'name': '明夷', 'description': '利艰贞。'},
    '111001': {'name': '家人', 'description': '利女贞。'},
    '101111': {'name': '无妄', 'description': '元亨利贞。其匪正有眚，不利有攸往。'},
    '111101': {'name': '大畜', 'description': '利贞。不家食吉，利涉大川。'},
    '000111': {'name': '贲', 'description': '亨。小利有攸往。'},
    '111000': {'name': '剥', 'description': '不利有攸往。'},
    '001111': {'name': '复', 'description': '亨。出入无疾，朋来无咎。反复其道，七日来复。利有攸往。'},
    '100110': {'name': '离', 'description': '利贞亨。畜牝牛吉。'},
    '011001': {'name': '噬嗑', 'description': '亨。利用狱。'},
    '010010': {'name': '坎', 'description': '习坎。有孚维心亨，行有尚。'},
    '101101': {'name': '艮', 'description': '艮其背，不获其身，行其庭，不见其人，无咎。'},
    '110110': {'name': '兑', 'description': '亨，利贞。'},
    '001010': {'name': '节', 'description': '亨。苦节不可贞。'},
    '010100': {'name': '中孚', 'description': '豚鱼吉，利涉大川，利贞。'},
    '101001': {'name': '小过', 'description': '亨，利贞。可小事，不可大事。飞鸟遗之音，不宜上宜下，大吉。'},
    '100100': {'name': '既济', 'description': '亨，小利贞。初吉终乱。'},
    '001001': {'name': '未济', 'description': '亨。小狐汔济，濡其尾，无攸利。'},
    '110000': {'name': '大壮', 'description': '利贞。'},
    '000110': {'name': '观', 'description': '盥而不荐，有孚顒若。'},
    '111011': {'name': '晋', 'description': '康侯用锡马蕃庶，昼日三接。'},
    '110101': {'name': '豫', 'description': '利建侯行师。'},
    '101000': {'name': '归妹', 'description': '征凶，无攸利。'},
    '000101': {'name': '临', 'description': '元亨，利贞。至于八月有凶。'},
    '101010': {'name': '损', 'description': '有孚，元吉，无咎，可贞。利有攸往，曷之用二簋，可用享。'},
    '010101': {'name': '益', 'description': '利有攸往，利涉大川。'},
    '000100': {'name': '恒', 'description': '亨。无咎。利贞。利有攸往。'},
    '100000': {'name': '大有', 'description': '元亨。'},
    '000001': {'name': '泰', 'description': '小往大来，吉亨。'},
    '100111': {'name': '大过', 'description': '栋桡，利有攸往，亨。'},
    '001100': {'name': '井', 'description': '改邑不改井，无丧无得。往来井井，汔至亦未繘井，羸其瓶，凶。'},
    '011010': {'name': '革', 'description': '已日乃孚，元亨利贞，悔亡。'},
    '010011': {'name': '鼎', 'description': '元吉，亨。'},
    '101011': {'name': '震', 'description': '亨。震来虩虩，笑言哑哑。震惊百里，不丧匕鬯。'},
    '110100': {'name': '渐', 'description': '女归吉，利贞。'},
    '001011': {'name': '蛊', 'description': '元亨，利涉大川。先甲三日，后甲三日。'},
    '010110': {'name': '咸', 'description': '亨，利贞。取女吉。'},
    '011100': {'name': '恒', 'description': '亨，无咎，利贞。利有攸往。'},
    '100101': {'name': '颐', 'description': '贞吉。观颐，自求口实。'},
    '011011': {'name': '兑为泽', 'description': '亨，利贞。'},
    '001110': {'name': '夬', 'description': '扬于王庭，孚号，有厉，告自邑。不利即戎，利有攸往。'},
    '011110': {'name': '姤', 'description': '女壮，勿用取女。'},
    '110001': {'name': '困', 'description': '亨，贞大人吉，无咎。有言不信。'},
    '101110': {'name': '升', 'description': '元亨，用见大人，勿恤，南征吉。'},
    '011101': {'name': '井', 'description': '改邑不改井，无丧无得。往来井井，汔至亦未繘井，羸其瓶，凶。'},
    '101100': {'name': '蹇', 'description': '利西南，不利东北。利见大人，贞吉。'},
    '110011': {'name': '讼', 'description': '有孚窒惕，中吉。终凶。利见大人，不利涉大川。'},
    '100011': {'name': '遁', 'description': '亨，小利贞。'},
}

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
    return binary

# 交互式获取投掷结果
def get_toss_results():
    toss_results = []
    print("请依次输入六次投掷结果，每次输入三个硬币的结果（正或反），用空格分隔。")
    for i in range(6):
        toss = input(f"第{i+1}次投掷结果（例如：正 反 正）：").split()
        while len(toss) != 3 or not all(coin in ['正', '反'] for coin in toss):
            toss = input("输入有误，请重新输入（正或反，用空格分隔）：").split()
        toss_results.append(toss_to_yao(toss))
    return toss_results

# 根据二进制查询卦象信息
def get_gua_info(binary):
    return gua_dict.get(binary, {'name': '未知', 'description': '暂无解释'})

# 主程序
if __name__ == "__main__":
    toss_results = get_toss_results()

    # 构建本卦和变卦的二进制表示
    ben_gua_binary = yao_to_binary(toss_results)[::-1]  # 反转
    bian_gua_binary = yao_to_binary(toss_results, changing=True)[::-1]  # 反转

    # 查找卦象信息
    ben_gua_info = get_gua_info(ben_gua_binary)
    bian_gua_info = get_gua_info(bian_gua_binary)

    # 输出结果
    print("\n=== 占卜结果 ===")
    print(f"本卦：{ben_gua_info['name']}（{ben_gua_binary}）")
    print(f"卦辞：{ben_gua_info['description']}")
    print(f"\n变卦：{bian_gua_info['name']}（{bian_gua_binary}）")
    print(f"卦辞：{bian_gua_info['description']}")
