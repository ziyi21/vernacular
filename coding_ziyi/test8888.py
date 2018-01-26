# coding=utf-8
'''
#下载网上音乐的方式
import requests
import urllib.request
music_url = 'http://mp3-cdn2.luoo.net/low/luoo/radio966/05.mp3'
print(music_url)
music2 = requests.get(music_url).text.encode('utf-8')
music1 = urllib.request.urlopen(music_url).read()
music = bytes(requests.get(music_url).text,'utf-8')

print(type(music))
print('...............................','/n')
print(type(music1))
print(type(music2))
print(music1)
with open(r'E:song\3.mp3','wb') as f:
    f.write(music1)
'''

#下载网上音乐的方式

# def add(a,b):
#     "计算加法"
#     c = a + b
#     print(c)
#
# add(3,6)
# print(add.__doc__)


a = [1,2,4]
b = [i for i in a]
print(b)

try:
    print('可能出现异常的具体代码')
    print('可能出现异常的其他函数')
except ValueError as e:
    print(e)
except(ValueError,TypeError,):
    print('元组包括多个异常判断')
except Exception as e:
    print('任何异常原因',e)
except:
    print('异常通配符，无法知道原因')
finally:
    print('程序正常执行')
    print('其他小bug别跑，程序报错')
