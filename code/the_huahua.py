import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

header = {
    "Host":'music.163.com',
    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

url = 'http://music.163.com/artist?id=861777'
# base_url = 'http://music.163.com/song/media/outer/url?id=' + id +'.mp3'
base_url = 'http://music.163.com/song/media/outer/url?id='
r = requests.get(url,headers = header)
r.encoding = 'utf-8'
html = r.text
# print(r.text)
soup = BeautifulSoup(html,'lxml')
other = soup.find('ul',{'class':"f-hide"})
# print(other)
temp = other.find_all('a')

# links = []

# for i in temp:
#     links.append(base_url + i['href'].split('=')[-1] + '.mp3')
    # print(i.text)

for j,i in enumerate(temp):
    urlretrieve(base_url + i['href'].split('=')[-1] + '.mp3','./music/song/'+ i.text + '.mp3') 