__author__ = 'ziyi'
#!/usr/bin/python
# -*- coding: utf-8 -*-

name = input('请输出的学生的姓名：')
scores = int(input('请输入{}的成绩:'.format(name)))
if scores >= 90:
    print('{}的等级是：A'.format(name))
elif scores >= 70:
    print('{}的等级是：B'.format(name))
elif scores >= 60:
    print('{}的等级是：C'.format(name))
else:
    print('{}的等级是：D'.format(name))
