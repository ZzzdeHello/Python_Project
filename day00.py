import dis

a = 1257
# is 和 == 的区别 ；is 比较的是 内存地址是否一致 == 比较的是指是否一致

def main():
    b = 1257  # 第6行
    c = 1257  # 第7行
    print(b is c)  # True
    print(a is b)  # True
    print(a is c)  # True
    print(b == c)  # True
    print(a == b)  # True
    print(a == c)  # True
    print('---字符串---')  # True
    s = 'hello'
    s1 = 'hello'
    print(s is s1)
    print(s == s1)

    s2 = 'hello  world 111111'
    s3 = 'hello  world 111111'
    print(s2 is s3)
    print(id(s2))
    print(s2 == s3)
    print(id(s3))
    print('---数组---')  # True
    array1 = [1, 2, 3, 4]
    array2 = [1, 2, 3, 4]
    print(array1 is array2)
    print(array1 == array2)


if __name__ == "__main__":
    main()
    # dis.dis(main) 字符串编译
