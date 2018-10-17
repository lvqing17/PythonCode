import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


url = 'http://xiaohua.zol.com.cn/new/'
# r = requests.get(url)
# r.encoding = 'gbk'

# html = r.text
# #print(r.text)

# soup = BeautifulSoup(html,'lxml')
# other = soup.find("ul",{'class':"article-list"})
#print(other.text)

# 或者用这个txt文件夹，或者再重新建一个文件夹,这里是个全路径（绝对路径），下载到你的Project里面,你可以试试
# with open("/Users/lvqing/Project/others/xiaohua.txt",'w') as f:
#     f.write(other.text)


def writetxt(content,filename):
    # 在这里面我们不设定追加，直接就用w，不过，需要提供一下文件名，如果有100个文件名不一样，那不就能建100个文件了么，
        with open("./txt/xiaohua/" + filename +".txt",'w') as f:
            f.write(content)



def get_content(url,flag):
   r = requests.get(url)
   r.encoding = 'gbk'
   html = r.text
   soup = BeautifulSoup(html, 'lxml')
   other = soup.find("ul",{'class':"article-list"})

   writetxt(other.text,flag)
   pass

# 这里的100是个可以调节的数，我们可以设定，爬取哪些页面
for i in range(100):
   # print(url + str(i + 1)+".html")
   urls = url + str(i + 1) + ".html"
   #print(urls)
   print(i,urls)
   get_content(urls, str(i))
