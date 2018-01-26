#!/usr/bin/python
#coding=utf-8
#问题描述：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

sum_ten = []
for i in range(10):
    each = 2*100/(2**i)
    # each_up = 50/(2**i)
    sum_ten.append(each)
print('第 {} 次反弹的高度为：{}'.format(10,sum_ten[-1]/4))

print('它落地第10次时，共经过 {} 米'.format(sum(sum_ten,-100)))

