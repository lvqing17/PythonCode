import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


url = 'http://www.58pic.com/c/14147037'
r = requests.get(url)
r.encoding = 'gbk'
html = r.text
#print(r.text)
soup = BeautifulSoup(html,'lxml')
other = soup.find('div',{'class':"w1200 "})
#print(other)
temp = other.find_all("img")
# print(temp)
for j,i in enumerate(temp):
   urlretrieve(i['src'],'./tutu/pictureg/' + str(j) + i['alt'] + '.jpg')
    # print(i['src'])
    # print(i.text)