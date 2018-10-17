import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve


# 网站一般都有反爬虫机制，嗯嗯，好的，晚上讲，

header = {
    "Referer:":'http://www.boting.co/book/15689.htm',
    "Host":"www.boting.co",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
}

url = 'http://www.boting.co/book/15689.htm'
base_url = 'http://www.boting.co'
# r = requests.get(url,header)
# # 这里注意一下哈，基本是所有的网页，都是gbk或者utf-8的编码，用这两个就行
# r.encoding = 'utf-8'

# html = r.text
# # print(r.text)

# soup = BeautifulSoup(html,'lxml')
# # 你刚才写的是对的
# other = soup.find("div",{'class':"audiodownloadbtn"})
# #print(other.text)
# temp = other.find_all("a")

# links = []

# for i in temp:
#     # links.append(url + i["href"])
#     print(base_url + i["href"])

# second_url = 'http://www.boting.co//download/downloadfile15689.html'

# sec_r = requests.get(second_url)
# sec_r.encoding = 'utf-8'
# html = sec_r.text

# #print(sec_r.text)
# soup = BeautifulSoup(html,'lxml')
# sec_other = soup.find("div",{'class':"downloadlist clearfix"})  
# #print(sec_other.text) 
# sec_temp = sec_other.find_all("a")

# sec_links = []

# for i in sec_temp:
#    # print( i["href"])
# #    这里记得用list的时候添加不是赋值哈
#    sec_links.append(i["href"])

def get_url(url,header):
    """
    输入一个url，输出一个下载页面的url
    """
    r = requests.get(url,header)
    r.encoding = 'utf-8'
    html = r.text
    soup = BeautifulSoup(html,'lxml')
    other = soup.find("div",{"class":"audiodownloadbtn"})
    temp = other.find('a')
    return base_url + temp['href']

def get_securl(url,header):
    sec_r = requests.get(url,header)
    sec_r.encoding = 'utf-8'
    html = sec_r.text
    sec_soup = BeautifulSoup(html,'lxml')
    sec_other = sec_soup.find("div",{'class':"downloadlist clearfix"})
    sec_temp = sec_other.find_all('a')
    # 需注意sec_temp是个list
    # 我们整理的更好看一点
    sec_links = []
    for i,link in enumerate(sec_temp):
        sec_links.append(link['href'])

    return sec_links

    

# 这里呢，我先看看前10个链接对不对，打印出来，如果对了，就去下载
# for k,i in enumerate(sec_links):
#     if k < 10:
#         print(k,i)
#         urlretrieve(i,'./music/talkingBook/' + str(k) + '.mp3')

xx = get_url(url,header)
yy = get_securl(xx,header)
print(yy)