import requests
from bs4 import BeautifulSoup

from urllib.request import urlretrieve

header = {
      "Host":'image.baidu.com',
      "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

# urls = 'http://travel.quanjing.com/tag/10004/%E9%98%BF%E5%B0%94%E5%8D%91%E6%96%AF%E5%B1%B1'
# r = requests.get(urls)
# url = 'http://travel.quanjing.com/'
url = 'https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1526269427171_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A3%81%E7%BA%B8'
r = requests.get(url,headers = header)
r.encoding = 'utf-8'
html = r.text
# print(html)
soup = BeautifulSoup(html,'lxml')
other = soup.find("ul",{'class':"imglist clearfix pageNum0"})
print(other)

# img = other.find_all("img")

# #  with open("./tutu/mountain",'w') as f:
# #       f.write(other.text)
# #print(other)
# # print(img)

# #  参数说明如下
# # urlretrieve(下载链接，文件保存位置及名字)
# # urlretrieve()
# for i in img:
#       # print(i['src'])
#       # img['src']
#       urlretrieve(i['src'],'./tutu/mountain/' +  i['alt']+ '.jpg')