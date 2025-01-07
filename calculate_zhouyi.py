# -*- coding: utf-8 -*-

# 按照二进制顺序排列的六十四卦
gua_dict = {
    '000000': {'name': '坤为地', 'description': '元亨利牝马之贞。'},
    '000001': {'name': '地雷复', 'description': '亨。出入无疾，朋来无咎。反复其道，七日来复。利有攸往。'},
    '000010': {'name': '地水师', 'description': '贞，丈人吉，无咎。'},
    '000011': {'name': '地泽临', 'description': '元亨，利贞。至于八月有凶。'},
    '000100': {'name': '地山谦', 'description': '亨。君子有终。'},
    '000101': {'name': '地火明夷', 'description': '利艰贞。'},
    '000110': {'name': '地风升', 'description': '元亨，用见大人，勿恤，南征吉。'},
    '000111': {'name': '地天泰', 'description': '小往大来，吉亨。'},
    '001000': {'name': '雷地豫', 'description': '利建侯行师。'},
    '001001': {'name': '震为雷', 'description': '亨。震来虩虩，笑言哑哑。震惊百里，不丧匕鬯。'},
    '001010': {'name': '雷水解', 'description': '亨。利西南，无所往，其来复吉。有攸往，夙吉。'},
    '001011': {'name': '雷泽归妹', 'description': '征凶，无攸利。'},
    '001100': {'name': '雷山小过', 'description': '亨，利贞。可小事，不可大事。飞鸟遗之音，不宜上宜下，大吉。'},
    '001101': {'name': '雷火丰', 'description': '亨。王假之，勿忧，宜日中。'},
    '001110': {'name': '雷风恒', 'description': '亨，无咎，利贞。利有攸往。'},
    '001111': {'name': '雷天大壮', 'description': '利贞。'},
    '010000': {'name': '水地比', 'description': '吉。原筮，元永贞，无咎。不宁方来，后夫凶。'},
    '010001': {'name': '水雷屯', 'description': '元亨，利贞。勿用有攸往，利建侯。'},
    '010010': {'name': '坎为水', 'description': '习坎。有孚维心亨，行有尚。'},
    '010011': {'name': '水泽节', 'description': '亨。苦节不可贞。'},
    '010100': {'name': '水山蹇', 'description': '利西南，不利东北。利见大人，贞吉。'},
    '010101': {'name': '水火既济', 'description': '亨，小利贞。初吉终乱。'},
    '010110': {'name': '水风井', 'description': '改邑不改井，无丧无得。往来井井，汔至亦未繘井，羸其瓶，凶。'},
    '010111': {'name': '水天需', 'description': '有孚，光亨，贞吉。利涉大川。'},
    '011000': {'name': '泽地萃', 'description': '亨。王假有庙，利见大人，亨，利贞。'},
    '011001': {'name': '泽雷随', 'description': '元亨利贞，无咎。'},
    '011010': {'name': '泽水困', 'description': '亨，贞大人吉，无咎。有言不信。'},
    '011011': {'name': '兑为泽', 'description': '亨，利贞。'},
    '011100': {'name': '泽山咸', 'description': '亨，利贞。取女吉。'},
    '011101': {'name': '泽火革', 'description': '已日乃孚，元亨利贞，悔亡。'},
    '011110': {'name': '泽风大过', 'description': '栋桡，利有攸往，亨。'},
    '011111': {'name': '泽天夬', 'description': '扬于王庭，孚号，有厉，告自邑。不利即戎，利有攸往。'},
    '100000': {'name': '山地剥', 'description': '不利有攸往。'},
    '100001': {'name': '山雷颐', 'description': '贞吉。观颐，自求口实。'},
    '100010': {'name': '山水蒙', 'description': '亨。匪我求童蒙，童蒙求我。初噬告，再三渎，渎则不告。利贞。'},
    '100011': {'name': '山泽损', 'description': '有孚，元吉，无咎，可贞。利有攸往，曷之用二簋，可用享。'},
    '100100': {'name': '艮为山', 'description': '艮其背，不获其身，行其庭，不见其人，无咎。'},
    '100101': {'name': '山火贲', 'description': '亨。小利有攸往。'},
    '100110': {'name': '山风蛊', 'description': '元亨，利涉大川。先甲三日，后甲三日。'},
    '100111': {'name': '山天大畜', 'description': '利贞。不家食吉，利涉大川。'},
    '101000': {'name': '火地晋', 'description': '康侯用锡马蕃庶，昼日三接。'},
    '101001': {'name': '火雷噬嗑', 'description': '亨。利用狱。'},
    '101010': {'name': '火水未济', 'description': '亨。小狐汔济，濡其尾，无攸利。'},
    '101011': {'name': '火泽睽', 'description': '小事吉。'},
    '101100': {'name': '火山旅', 'description': '小亨。旅贞吉。'},
    '101101': {'name': '离为火', 'description': '利贞亨。畜牝牛吉。'},
    '101110': {'name': '火风鼎', 'description': '元吉，亨。'},
    '101111': {'name': '火天大有', 'description': '元亨。'},
    '110000': {'name': '风地观', 'description': '盥而不荐，有孚顒若。'},
    '110001': {'name': '风雷益', 'description': '利有攸往，利涉大川。'},
    '110010': {'name': '风水涣', 'description': '亨。王假有庙，利涉大川，利贞。'},
    '110011': {'name': '风泽中孚', 'description': '豚鱼吉，利涉大川，利贞。'},
    '110100': {'name': '风山渐', 'description': '女归吉，利贞。'},
    '110101': {'name': '风火家人', 'description': '利女贞。'},
    '110110': {'name': '巽为风', 'description': '小亨，利有攸往，利见大人。'},
    '110111': {'name': '风天小畜', 'description': '亨。密云不雨，自我西郊。'},
    '111000': {'name': '天地否', 'description': '否之匪人，不利君子贞，大往小来。'},
    '111001': {'name': '天雷无妄', 'description': '元亨利贞。其匪正有眚，不利有攸往。'},
    '111010': {'name': '天水讼', 'description': '有孚窒惕，中吉。终凶。利见大人，不利涉大川。'},
    '111011': {'name': '天泽履', 'description': '履虎尾，不咥人，亨。'},
    '111100': {'name': '天山遁', 'description': '亨，小利贞。'},
    '111101': {'name': '天火同人', 'description': '同人于野，亨。利涉大川，利君子贞。'},
    '111110': {'name': '天风姤', 'description': '女壮，勿用取女。'},
    '111111': {'name': '乾为天', 'description': '元亨利贞。'}
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
    if binary in gua_dict:
        return gua_dict[binary]
    else:
        return {'name': '未知卦象', 'description': f'二进制表示 {binary} 未找到对应卦象信息。'}


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
