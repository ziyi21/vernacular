#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：ax2 + bx + c = 0  的两个解。
#!/usr/bin/python
#coding=utf-8

import math
# result = math.sqrt(4)D:\vernacular\coding_ziyi
# print(result)
def quadratic(a,b,c):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)) or not isinstance(c,(int,float)):
        raise TypeError('字符类型不符合要求')
    have_result = b**2-(4*a*c)
    # print(have_result)
    if have_result >= 0  and a != 0:
        result1 = (-b + (math.sqrt(b**2 - 4*a*c)))/(2*a)
        result2 = (-b - (math.sqrt(b ** 2 - 4 * a * c))) / (2 * a)
        return result1,result2
    elif a == 0:
        result = -c/b
        return result
    else:
        return '无实根'
result = quadratic(2,1,1)
print(result)