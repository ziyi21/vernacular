__author__ = 'ziyi'
#!/usr/bin/python
# -*- coding: utf-8 -*-
#问题描述：使用递归调用的方法计算某个数的阶乘
import sys
def Factorial(num):
    if num == 1 :
        return 1
    else:
        result = num * Factorial(num-1)
        return result

if __name__ == '__main__' :
    print('请输出你要计算的数: ')
    first_num = int(sys.stdin.readline( ))
    # first_num = int(input('请输入你要计算的数: '))
    result = Factorial(first_num)
    print('{}的阶乘是：{}'.format(first_num, result))
