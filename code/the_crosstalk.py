import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import json

header = {
    "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    "Host":'www.ximalaya.com'
}

# header = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
#     # "Referer": "http://www.ximalaya.com/qita/qita/12749134/88436518",
#     "Host":"www.ximalaya.com"
# }

# url = 'http://www.ximalaya.com/lishi/lishi/3325122/'
print("+++++++++++++++++++输入下载的链接++++++++++++++++")
print("如:http://www.ximalaya.com/lishi/lishi/3325122/")
url = input("请输入:")
base_url = 'http://www.ximalaya.com'
third_url = 'http://www.ximalaya.com/revision/play/tracks?trackIds='

r = requests.get(url,headers = header)
r.encoding = 'utf-8'
html = r.text
#print(r.text)

soup = BeautifulSoup(html,'lxml')
other = soup.find("div",{'class':"e-2304105070 sound-list"})
#print(other)
lists = []
names = []
temp = other.find_all("a")
for i in temp:
    # lists.append(base_url + i['href'])
    # names.append(i.text)
    # print(base_url + i['href'])
    lists.append(i['href'].split("/")[-1])
    names.append(i.text)
    #print(third_url + i['href'].split("/")[-1])
    # print(i.text)

# def down_mp3(url,header,name):
#     r = requests.get(url,headers = header)
#     other = json.loads(r.text)
#     request.urlretrieve(other['data']['tracksForAudioPlay'][0]['src'],'./music/' + name + ".mp3")

# r1 = requests.get(lists[0],headers = header)
# print(r1.text)
# other = json.loads(r1.text)
# print(other['data']["tracksForAudioPlay"][0]['src'])
#request.urlretrieve(other['data'][])

# r2 = requests.get(lists[1],headers = header)
#print(r2.text)
# other2 = json.loads(r2.text)
# print(other2["data"]["tracksForAudioPlay"][0]['src'])

# for i,links in enumerate(lists):
#     urlretrieve()

def load_mp3(url,header,names):
    r = requests.get(url,headers = header)
    other = json.loads(r.text)
    urlretrieve(other['data']["tracksForAudioPlay"][0]['src'],'./music/crosstalk/' + names + '.mp3')
    
for i,k in enumerate(lists):
    m_url = third_url + k
    print(m_url,names[i])
    load_mp3(m_url,header,str(i + 1)+names[i])