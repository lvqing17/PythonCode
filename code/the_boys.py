import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


url = 'http://www.shuaia.net/mingxing/'
r = requests.get(url)
r.encoding = 'utf-8'
html = r.text

#print(r.text)
soup = BeautifulSoup(html,'lxml')
other = soup.find("div",{'id':"content"})

# print(other)

img = other.find_all("img")
#for i in img :
 #   print (i)

for i in img:
   urlretrieve(i['src'],'./tutu/boys/' + i['alt'] + '.jpg')
   # print(i['src'],'./tutu/boys/' + i['alt'] + '.jpg')