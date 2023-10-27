# 字典结构 dict key-value的格式存在的


if __name__ == '__main__':
    _dict = {'name': '小明', 'age': 12}
    # 赋值
    print(_dict)

    _d2 = {}
    # 赋值
    _d2['name'] = '小王'
    _d2['age'] = 14
    print(_d2)

    print(_dict)  # 输出完整的字典
    print(_dict.keys())  # 输出所有键
    print(_dict.values())  # 输出所有值

    print(repr(_dict))  # 输出所有值
