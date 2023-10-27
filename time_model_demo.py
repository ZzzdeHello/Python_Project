"""
    块注解
    时间相关模块
"""
import time
import datetime
import calendar

if __name__ == '__main__':
    now = time.localtime()
    print(now)
    print(now.tm_year)
    print(now.tm_mon)
    print(now.tm_mday)
    print(now.tm_hour)
    time.sleep(1)  # 当前线程睡眠
    print(time.time())  # 返回当前时间的时间戳
    print('datetime 模块api')
    # datetime 模块重新封装了time，更多的接口更加易用
    td = datetime.date.today()
    print(td.replace(year=1945, month=8, day=15))
    print(td.timetuple())
    print(td.weekday())
    print(td.isoweekday())
    print(td.isocalendar())
    print(td.isoformat())
    print(td.strftime('%Y %m %d %H:%M:%S %f'))
    print(td.year)
    print(td.month)
    print(td.day)
    #  calendar 模块 日历数据格式化的方法
    print('calendar 模块')
    calendar.setfirstweekday(1)
    print(calendar.firstweekday())
    print(calendar.isleap(2019))
    print(calendar.leapdays(1945, 2019))
    print(calendar.weekday(2019, 12, 1))
    print(calendar.monthrange(2019, 12))
    print(calendar.month(2019, 12))
    print(calendar.prcal(2019))

    #  日历html文件生成
    print('-------------------')
    hc = calendar.HTMLCalendar()
    print(hc.formatyear(2023))

    #  日历存文本文件生成
    print('-------------------')
    tc2 = calendar.TextCalendar()
    print(tc2.formatmonth(2023, 12))
    print(tc2.formatyear(2023))

    # __ 两个下划线开头的函数是声明该属性为私有