import os
import shutil
import sys
import time

# 执行dir命令

if __name__ == '__main__':
    pwd = os.getcwd()
    src_file = os.path.abspath("demo")
    dst_file = os.path.join(pwd,'20231020-15-49-33')
    print("源目录路径" +src_file)
    src = src_file + '\demo001.py'
    dst = dst_file + '\demo001.py'
    shutil.copy2(src,dst)
