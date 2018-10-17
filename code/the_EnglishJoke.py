import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

url = "http://xiaohua.zol.com.cn/yingyu/"
#r = requests.get(url)
#r.encoding = 'gbk'

#html = r.text
#print(r.text)

#soup = BeautifulSoup(html,'lxml')
#other = soup.find("ul",{'class':"article-list"}) 

#print(other.text)

def writetxt(content,filename):
    with open("./txt/EnglishJoke/" + filename + ".txt", 'w') as f:
        f.write(content)

def get_content(url,name):
    r = requests.get(url)
    r.encoding = 'gbk'
    html = r.text
    soup = BeautifulSoup(html,'lxml')
    other = soup.find("ul",{'class':"article-list"})

    writetxt(other.text,name)

    pass

for i in range(100):
    urls = url  + str(i+1) + ".html"

    # print(i,urls)
    # 缩进的问题
    get_content(urls,str(i))

    
