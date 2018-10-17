import requests
from bs4 import BeautifulSoup
import json
import urllib
import re


urls = 'https://www.xs8.cn/chapter/8327340004310503/24763715544782535'
url1 = 'https://www.qisuu.la/du/36/36893/9968724.html'
r = requests.get(url1)
r.encoding='utf-8'

html = r.text
# print(r.text)
soup = BeautifulSoup(html,'lxml')
other = soup.find("div",{'id':"content1"})
print(other)



# def get_html(urls):
#     header = {
#         "Referer"
#     }