import requests 
from bs4 import BeautifulSoup
import json
import re
from urllib import request


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    # "Referer": "http://www.ximalaya.com/qita/qita/12749134/88436518",
    "Host":"www.ximalaya.com"
}

# url = "http://www.ximalaya.com/revision/play/tracks?trackIds=89028415"
# # url = 'http://www.ximalaya.com/waiyu/11873814/92564292'
# r = requests.get(url,headers = header)
# print(r.text)
# other = json.loads(r.text)
# print(other)
# print(other['data']['tracksForAudioPlay'][0]['src'])
# request.urlretrieve(other['data']['tracksForAudioPlay'][0]['src'],"./temp/" + "other" + '.mp3' )


def down_mp3(url,header,name):
    r = requests.get(url,headers = header)
    other = json.loads(r.text)
    request.urlretrieve(other['data']['tracksForAudioPlay'][0]['src'],'./music/talking/' + name + ".mp3")



url = "http://www.ximalaya.com/xiangsheng/xiangsheng/11219250/p1/"
down_url = "http://www.ximalaya.com/revision/play/tracks?trackIds="

r = requests.get(url,headers = header)
# print(r.text)
soup = BeautifulSoup(r.text,"lxml")
other = soup.find("ul",{"class":"e-2304105070"})
# print(other)
links = []
names = []
for i in other.find_all('a'):
    # print(i.text)
    names.append(i.text)
    links.append(i['href'].split('/')[-1])
# print(links)

for j,k in enumerate(links):
    temp_url = down_url + k
    print("down load ", j + 1,names[j],temp_url)
    # 下面的这一句呢是下载的语句，我们可以先注释掉，观察一下每个temp_url，其实每个temp_url是json链接，用来抓取mp3的url的
    # 观察上来说，每个json的url都是对的啊
    # 怀疑你的网速有问题,代码没问题的
    down_mp3(temp_url,header,names[j])
