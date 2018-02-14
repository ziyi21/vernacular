__author__ = 'ziyi'
#!/usr/bin/python
# -*- coding: utf-8 -*-
from datetime import *

def time_manage(n):
    today = datetime.now()
    print("当前日期是：" ,today)
    n = int(n)
    memory = today + timedelta(days=n)
    print(n,"天后的日期是：" , memory)

if __name__ == '__main__':
    n = input("请输入你要查询的天数：")
    time_manage(n)
