__author__ = 'ziyi'
#!/usr/bin/python
# -*- coding: utf-8 -*-
#按格式输出九九乘法表

for i in range(1,10):
    for j in range(1,i+1):
        multip = i * j
        print('{}*{}={}'.format(j,i,multip),end=' ')
    print('')


