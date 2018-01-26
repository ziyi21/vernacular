__author__ = 'ziyi'
#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

def new_guess():
    number = random.randint(0, 100)
    # print(number)
    return number
def new_game():
    number = new_guess()
    n = 0
    while True:
        n += 1
        try:
            guess_num = int(input('请输入你要尝试的次数：'))
        except ValueError:
            guess_num = 10
            print('输入的次数不合法，默认最多猜10次')
        for i in range(guess_num):
            guess = int(input('请输入你猜的数字：'))
            if guess > number:
                print('你猜的数字大了，不要灰心，继续加油！')
            elif guess < number:
                print('你猜的数字小了，不要灰心，继续努力！')
            else:
                if i < 3:
                    print('真厉害，这么快就猜对了！')
                else:
                    print('终于猜对了，恭喜恭喜！')
                number = new_guess()
                break
            if i == guess_num-1:
                print('很遗憾！在{}次中你均未猜出'.format(guess_num))
        next_game = input('是否继续游戏？请输入 yes or no：')
        if next_game == 'no':
            break
        else:
            print('开始下一轮游戏！')
            continue
    print('你一共玩了{}轮游戏哦'.format(n))

if __name__ == '__main__':
    print('猜数字小游戏!')
    new_game()

#
#
# """对上面例子的一个扩展"""
#
# print("=======欢迎进入狗狗年龄对比系统========")
# while True:
#     try:
#         age = int(input("请输入您家狗的年龄:"))
#         print(" ")
#         age = float(age)
#         if age < 0:
#             print("您在逗我？")
#         elif age == 1:
#             print("相当于人类14岁")
#             break
#         elif age == 2:
#             print("相当于人类22岁")
#             break
#         else:
#             human = 22 + (age - 2)*5
#             print("相当于人类：",human)
#             break
#     except ValueError:
#         print("输入不合法，请输入有效年龄")
# ###退出提示
# input("点击 enter 键退出")