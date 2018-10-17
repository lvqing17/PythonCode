import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


url = 'https://so.mgtv.com/so/k-%E5%90%91%E5%BE%80%E7%9A%84%E7%94%9F%E6%B4%BB%20%E7%AC%AC%E4%BA%8C%E5%AD%A3'
r = requests.get(url)
r.encoding = 'utf-8'
html = r.text
# print(r.text)
soup = BeautifulSoup(html,'lxml')
other = soup.find('div',{'class':"detail-videos detail-videos-imgo detail-videos-8928adbeff485dc844c3217203fb0bae-2018 clearfix"})
# print(other)
temp = other.find_all('a')

for i in temp:
    print("https://" + i['href'].split('//')[-1])
    # urlretrieve(i['href'].split('//')[-1],'./movie/WatchTV/' + i['title'] )


