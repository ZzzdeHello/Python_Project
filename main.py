# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import demo.demo001
import demo.demo002

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name = input()
    if (name == 'zhuhangxuan'):
        print_hi('got-'+ name)
    elif(name == 'ceshi'):
        print_hi(name)
    else :
        pass
    print_hi(name)

    #  包引入的方式 import 包名1.包名2...模块名
    #  from ... import ...
    # from 包名1.包名2... import 模块名
    # from 包名1.包名2...模块名 import 变量名/函数名

    demo.demo001.DemoClass()
    demo.demo002.getAge(21)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
