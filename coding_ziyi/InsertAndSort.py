__author__ = 'ziyi'
#!/usr/bin/python
# -*- coding: utf-8 -*-

#问题描述：生成一组不重复的数组，并进行排序
import random

def ori_data(start, stop, length):
    #准确指定起始范围由小到大
    start,stop = (int(start),int(stop)) if start <= stop else (int(stop),int(start))
    length = int(abs(length)) if length else 0
    if int(abs(start-stop)) < length:
        print('所选范围不符合要求，请重新指定')
        return None
    else:
        #利用随机函数生成随机数组，并且保证数值唯一
        random_list = []
        for i in range(length):
            one_number = random.randint(start, stop)
            while one_number in random_list:
                one_number = random.randint(start,stop)
                print('有重复，已经重新生成')
            random_list.append(one_number)
        random_list = sorted(random_list)
        return random_list

if __name__ == '__main__':
    ori_data = ori_data(38,22,10)
    print('新生成的数组为：{}'.format(ori_data))




