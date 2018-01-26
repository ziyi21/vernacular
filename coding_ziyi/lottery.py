#!/usr/bin/python
#coding=utf-8

import random
import sys
import csv

print('年终抽奖--你会是下一个幸运者吗')
#定义抽奖的类
class Lottery:
    #初始化所有抽奖人的名单地址
    def __init__(self,filepath):
        self.datasource = filepath
    def Get_people(self):
    #获取待抽奖的用户的名单和用户个数
    #获取方式，本次按照读取csv文件形式操作（也可以读取数据库等）
        people_list = []
        with open(self.datasource) as source :
            all_people = csv.reader(source)
            for people in all_people:
                people_list.append(people)
            people_num = len(people_list)
        print('本次共有 {} 人参与抽奖'.format(people_num))
    #用户输入确认抽奖的等级（一等奖、二等奖、三等奖）,并且判断每个等级的奖品人数合理（不超过总人数）
        level = int(input('请输入本次抽奖分几等：'))
        level_dict = {}
        sum_level = 0
        for i in range(level):
            print('请输入第 {} 等级的抽奖'.format(i+1)+'数：')
            one_level = int(sys.stdin.readline())
            sum_level = sum_level + one_level
            if sum_level <= people_num:
                level_dict[i] = one_level
            else:
                sum_origin = sum_level - one_level
                cha = people_num - sum_origin
                # print('输入人数超额，请重新输入小于%s的数'%cha)
                while one_level > cha:
                    print('人数超额，请重新输入小于 %s 的数' %cha)
                    one_level = int(sys.stdin.readline())
                sum_level = sum_origin + one_level
                level_dict[i] = one_level
        print('每个等级及对应人数',level_dict)

    # 抽取每个等级的获奖用户名单
        for i in range(len(level_dict)):
            level_peoples = []
            for j in range(int(level_dict[i])):
                level_people = random.choice(people_list)
                level_peoples.append(level_people)
                people_list.remove(level_people)
            print('第 %s 等级下被抽中的人员为：' % (i + 1 ))
            print(level_peoples)

#类功能定义完毕，初始化并使用
if __name__ == '__main__':
    peoples = Lottery(r'D:\vernacular\data\5.csv')
    peoples.Get_people()





