# Python中的set集合，只存储不重复的key


if __name__ == '__main__':
    # 创建set集合 ,set中重复的集合会被过滤掉
    s = {'a', 'b', 'c'}
    s1 = set(['a1', 'a2', 'a3'])
    # 构建空set集合
    s2 = set()
    s2.add('water')
    s2.add('fire')
    s2.update('fire2')  # 将一个集合中的元素添加到当前集合中，update()可以传递序列或字典作为参数，字典只会使用键
    s2.update(s)
    print(s2)
    _l = len(s2)
    print('长度', _l)
    # s2.pop()
    print(s2)
    s2.remove('fire')  # 删除set中不存在的集合会报错，故需要添加一个校验
    print(s2)
    s2.clear()  # 删除set中所有集合
    print('测试', s2, '.')  # 测试 set() .
