# python 中没有数组 有List ,可以存放任意类型的数据类型，同一个列表的内部数据类型也可以不同。？

# python 中tuple 元组, 元组内的元素不可变，结构为不可变的列表

if __name__ == '__main__':
    _l = [0, 'de', 0.204]
    for i in _l:
        print(i)

    print(_l[2])  # 0,1,2
    # 添加元素
    _l.append("新家元素")
    print(_l)
    # 修改元素
    _l[0] = 120
    print(_l)
    # 删除元素
    _l[0] = 120
    del _l[0]
    print(_l)

    # list 常用方法
    print(_l.count('de'))  # 计算某元素出现次数
    print(_l.index('新家元素'))  # 查询某元素首次出现的索引


if __name__ == '__main__':
    _tuple = (2312, 'yrtw', 0.438295)
    for i in _tuple:
        print(i)
    #  计算长度
    a = len(_tuple)
    print(a)

    # tuple() 将列表转化为元组
    # max() 和 min() 获取元组最大最小值
