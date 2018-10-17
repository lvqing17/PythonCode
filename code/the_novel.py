import requests
from bs4 import BeautifulSoup


#urls = 'https://www.555zw.com/book/37/37394/7945668.html'
urlsm = 'https://www.555zw.com/book/37/37394/'
# r = requests.get(urls)
r1 = requests.get(urlsm)
# r.encoding='gbk'
r1.encoding = 'gbk'

# html = r.text
html1 = r1.text
#print(r.text)

soup1 = BeautifulSoup(html1,'lxml')
otherm = soup1.find("div",{'class':"dir"})
# with open("./txt/novel.txt","w") as f:
#     f.write(other.text)

temp = otherm.find_all("a")
links = []
names = []
for i in temp:
    links.append(urlsm+i['href'])
    # 这句话是用来保存超链接的名字的，虽然没有，但是以后，会有用的。
    names.append(i.text)

# with open("./txt/novel.txt","a") as f:
# #     f.write("\n".join(names))
# for i,j in zip(names,links):
#     with open("./txt/novel.txt","a") as f:
#         f.write(i+'\t'+j+"\n")


def write2txt(content,flag):
    """
    函数说明：函数接收content内容，存到本地，根据，flag判断是用w（完全新建），还是用a（追加内容）
    """
    if flag == 0:    
        with open("./txt/noval.txt",'w') as f:
            f.write(content)
    else :
        with open("./txt/noval.txt","a") as f:
            f.write(content)
    pass



# 这个url是章节链接的话，怎么来考虑呢？就把之前的代码写上就行
def get_content(url,flag = 0):
    """
    函数说明：传入url，下载章节内容
    """
    r = requests.get(url)
    r.encoding = 'gbk'
    html = r.text
    soup = BeautifulSoup(html,'lxml')
    other = soup.find("div",{"id":"content"})
    # dongleme 
    write2txt(other.text,flag)
    pass


# print(links[:10])
for i,j in enumerate(links):
    # print(i)
    print(i,j)
    get_content(j,i)