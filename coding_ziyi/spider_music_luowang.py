#获取落网音乐网站的每个期刊的相关数据
#!/usr/bin/python
#coding=utf-8

import requests
from bs4 import BeautifulSoup
import re
import time
import  urllib.request

class DownloadSong(object):
    def __init__(self,base_url):
        self.url = base_url
        self.pageIndex = 1
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',}
        self.music_url = ''
    # def GetonePage(self,):
    #     #获取音乐的单个期刊页面的所有信息
    #     try:
    #         music_page = requests.get(self.url, **{'headers': self.headers}).text
    #         # music_page = requests.get(sel:f.url, headers=self.headers).text
    #         soup = BeautifulSoup(music_page,'html.parser')
    #         return soup
    #     except Exception as e:
    #
    #         print(e)

    def getPage(self, index, vol_url):
        if index != 0:
            url = self.url + '?p=' + str(index)
        else:
            url = vol_url
        try:
            music_page = requests.get(url, **{'headers': self.headers}).text
            # music_page = requests.get(sel:f.url, headers=self.headers).text
            soup = BeautifulSoup(music_page,'html.parser')
            return soup
        except Exception as e:
            print(e)
            return None

    # def GetnextPage(self):
    #     #获取音乐杂志总的页面数
    #     onepage = self.GetonePage()
    #     if not onepage:
    #         return None
    #     totalpage = onepage.find_all('a',class_="page")[-1].text
    #     print(totalpage)
    #     return totalpage
####
    #获取总页面数
    def getTotalPage(self):
        soup = self.getPage(self.pageIndex, '')
        if not soup:
            return None
        totalPage = soup.find_all('a', class_='page')[-1].get_text().strip()
        return totalPage

    #处理歌曲的名称
    def delSongName(self, songName):
        return songName.split('.')[1].lstrip().encode('utf-8')

    #获取每个期刊URL与频道的对应关系
    def getReation(self, pageIndex):
        soup = self.getPage(pageIndex, '')
        vols = {}
        pattern = re.compile('[0-9]+')
        if not soup:
            return None
        vol_lists = soup.find_all('div', class_='meta')
        for vol in vol_lists:
            vol1 = re.search(pattern, str(vol.a.get_text())).group()
            vols[vol1.strip()] = vol.a['href']
        return vols

    #获取每首歌的名称和url
    def getSongInfo(self, vols):
        songInfos = {}
        for vol in vols.keys():
            url = vols[vol]
            soup = self.getPage(0, url)
            total = len(soup.find_all('li', class_='track-item'))
            songNames = soup.find_all('a', class_='trackname')
            for i in range(1, total+1):
                songName = self.delSongName(songNames[i - 1].get_text())
                if i < 10:
                    songURL = self.music_url + 'radio' + str(vol).lstrip('0') + '/0' + str(i) + '.mp3'
                else:
                    songURL = self.music_url + 'radio' + str(vol).lstrip('0') + '/' + str(i) + '.mp3'
                songInfos[songName] = songURL
        return songInfos

    #下载歌曲
    def downloadSong(self):
        totalPage = self.getTotalPage()
        for pageIndex in range(1, int(totalPage)+1):
            vols = self.getReation(pageIndex)
            songInfos = self.getSongInfo(vols)
            for songName, songURL in songInfos.items():
                time.sleep(5)  #适当的减慢下载速度，不要给人家服务器造成压力。
                print('%s 正在下载中。。。' %(songName))
                songURL = 'http://mp3-cdn2.luoo.net/low/luoo/{}'.format(songURL)
                print(songURL)
                try:
                    data = urllib.request.urlopen(songURL).read()
                    print(songURL)
                    # data1 = requests.get(songURL)
                    # data2 = urllib.request.urlretrieve(songURL,r'E:song\%s.mp3' % songName)
                    with open((r'E:song\%s.mp3' % (songName)), 'wb') as f:
                        f.write(data)
                except :
                    print("{}######链接不存在，继续下载下一首########".format(songName))


if __name__ == '__main__':
    url = 'http://www.luoo.net/music/classical'  #传入古典期刊的url
    downloadsong = DownloadSong(url) #生成一个对象
    downloadsong.downloadSong()  #调用downloadSong方法来正式下载额。

# if __name__ == '__main__':
#     url = 'http://www.luoo.net/music/'
#     downloadmusic = DownloadMusic(url)
#     downloadmusic.GetnextPage()




