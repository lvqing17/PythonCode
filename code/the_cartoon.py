import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


url = 'http://www.ivsky.com/tupian/gongqijun_t21531/'
r = requests.get(url)
r.encoding = 'utf-8'

html = r.text

#print(r.text)
soup = BeautifulSoup(html,'lxml')
other = soup.find("ul",{'class':"pli"})

#print(other)
img = other.find_all("img")

for k,i in enumerate(img):
#    print(k,i['src'],i['alt'])
   urlretrieve(i['src'],'./tutu/cartoon/' + i['alt']+ str(k) + '.jpg')