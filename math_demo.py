import math
import random

"""
    def 函数名(参数):
        函数体
        return 返回值
	def 函数名(*参数): * 参数可以用来保存多个不定长的参数
	函数体
	return 返回值
	
	lambda 定义匿名函数
"""


def calculate_sum(a, b):
    return a + b


def calculate_exp(a):
    return math.exp(a)


def inputNum():
    while True:
        num = input("请输入整数:")
        try:
            inputData = eval(num)
            if type(inputData) == int:
                return inputData
        except:
            pass


def inputNum02():
    while True:
        num = input("请输入整数:")
        try:
            num = int(num)
        except:
            pass
        if type(num) == int:
            return num


# 简单的（eval 去除字符串）数字输入与加法运算
# if __name__ == '__main__':
#     a =  inputNum()
#     b =  inputNum()
#     print(a)
#     print(b)
#     print(calculate_sum(a,b))

# 简单的（类型转化）数字输入与加法运算
# if __name__ == '__main__':
#     a =  inputNum02()
#     print(a)
#     print(calculate_exp(a))

# random 方法返回 0,1 之间的实数 uniform: 生成 1,100之间的实数
# if __name__ == '__main__':
#     a = inputNum()
#     _r = random.random()
#     _uniform = random.uniform(1,100)
#     print(_r)
#     print(_uniform)
#     b = int(10 * _r)
#     c = int(_uniform)
#     print(calculate_sum(a, b))
#     print(calculate_sum(a, c))

# 字符串
if __name__ == '__main__':
    a = "test"
    print(a[0])  # 访问单个字符串
    print(a * 2)  # 重复输出字符串

    a1 = "test"
    print(a1[0:3])  # 0和3 均为数组索引位置  不像java 不会出现数组越界问题
    print(a1[0:6])  # 0和6 均为数组索引位置  不像java 不会出现数组越界问题
    print(a1[0:4:2])  # start:end:steps 步长
    # len() 计算序列的长度
    # max() 找出序列中的最大元素
    # min() 找出序列中的最小元素
    # list() 将序列转换为列表
    # str() 将序列转换为字符串
    # sum() 计算元素的和
    # sorted() 对元素进行排序
    # enumerate() 将序列组合为一个索引序列，多用在 for 循环中
    sorted_str = sorted(a1)
    print("sorted ", sorted_str)  # 返回一个排序过的数组
    enumerate_str = enumerate(a1)
    print("enumerate ", enumerate_str)  # 返回一个排序过的数组
    for e in enumerate_str:
        print("enumerate in e ", e)  # (0, 't') (1, 'e') (2, 's')(3, 't')

    a2 = "c"
    print(ord(a2))  # 返回字符串编码

    d = 99
    print(chr(d))  # 编码转字符

    # 字符串包含算法
    if 's' in a:
        print("字符串包含s")
    if 's' not in a:
        print("字符串不包含s")

    # 字符串格式化 ，占位符
    print('字符串:%s' % '格式化')
    print('浮点数:%f' % 10.1023894)
    print('整数:%d' % 12)
    print('整数:%d' % 12)
    # format 函数来格式化内容
    print('{0} {1}'.format('Hello', 'Python'))
