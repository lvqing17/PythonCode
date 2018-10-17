import requests
from bs4 import BeautifulSoup

urls = 'https://www.555zw.com/book/37/37394/'
r = requests.get(urls)
r.encoding='gbk'

html = r.text
#print(r.text)
soup = BeautifulSoup(html, 'lxml')
other = soup.find("div",{'class':"dir"})
# print(other.text)
# print(other)
temp = other.find_all("a")
# print(temp)
for i in temp:
    print(i.text,urls+i['href'])