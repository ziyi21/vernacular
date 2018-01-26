#!/usr/bin/python
#coding=utf-8
# -*- coding: utf-8 -*-
import csv
import sys
import random
print("开始进行抽奖")
#定义个抽奖类，功能有输入抽奖级别和个数，打印出每个级别的抽奖员工号码
class Choujiang:
    #定义scv文件路径
    def __init__(self,filepath):
        self.empfile = filepath
    def creat_num(self):
        emplist = []
        with open(self.empfile) as f:
            empf = csv.reader(f)
            for emp in empf:
                emplist.append(emp)
        print('共有 %s 人参与抽奖' % len(emplist))
        levels = int(input('抽奖分几个层次，请输入：'))
        #定义一个字典
        level_dict = {}
        for i in range(0,levels):
            print('请输入 %s 等奖对应的奖品个数' % ( i + 1))
            str_level_dict_key = sys.stdin.readline()
            int_level_dict_key = int(str_level_dict_key)
            level_dict[i] = int_level_dict_key
            #循环完成后抽奖层次字典构造完毕
        #进行抽奖开始
        print('抽奖字典设置为: %s' % level_dict)
        for i in range(0,len(level_dict)):
            winers = []
            #产生当前抽奖层次i对应的抽奖个数
            for j in range(0,int(level_dict[i])):
                #利用random模块中的choice函数从列表中随机产生一个
                winer = random.choice(emplist)
                winers.append(winer)
                emplist.remove(winer)
            print('抽奖层次 %s 下产出的获奖人员有：' % (i + 1 ))
            print(winers)

#类功能定义完毕，开始初始化并使用
if __name__ == '__main__':
    peoples = Choujiang(r'D:\vernacular\data\1.csv')
    peoples.creat_num()
