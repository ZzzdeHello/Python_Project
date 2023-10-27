import os
import shutil
import sys
import time

# 执行dir命令

if __name__ == '__main__':
    # 查看当前目录文件和文件夹列表
    now_path = os.system('dir')
    print(now_path)
    if not os.path.exists('demo'):
        print('存在demo文件目录')
        sys.exit()

    pwd = os.getcwd()
    print("当前目录路径" + pwd)
    # 当前文件的父路径
    # father_path = os.path.abspath(os.path.dirname(pwd) + os.path.sep + ".")
    # print("父目录路径" + father_path)
    src_file = os.path.abspath("demo")
    print("源目录路径" +src_file)
    # 获取当前时间
    fileName = time.strftime("%Y%m%d-%H-%M-%S", time.localtime())
    # 在当前目录下创建文件夹
    # os.mkdir(fileName)

    dst_file = os.path.join(pwd,fileName)
    print("目标目录路径" + dst_file)

    shutil.copytree(src_file,dst_file)
