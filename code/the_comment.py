import requests
from bs4 import BeautifulSoup


url = 'https://book.douban.com/subject/3259440/comments/'
base_url = 'https://book.douban.com/subject/3259440/comments/hot?p='
r = requests.get(url)
r.encoding = 'utf-8'
html = r.text
# print(r.text)

soup = BeautifulSoup(html,'lxml')
# 这里，你的操作太简单粗暴了，，，
other = soup.find('div',{'id':"comment-list-wrapper"})
# print(other.text)
for i in other.find_all("p",{'class':"comment-content"}):
    # print(i.text,'\n')
    pass

def write(comment,flag):
    if flag == 1 :
        with open('./txt/comment.txt','w') as f:
            f.write(comment)
    else :
        with open('./txt/comment.txt','a') as f:
            f.write(comment)
    pass

def get_comment(url,flag):
    r = requests.get(url)
    r.encoding = 'utf-8'
    html = r.text

    soup = BeautifulSoup(html,'lxml')
    other = soup.find('div',{'id':"comment-list-wrapper"})
    context = []
    for i in other.find_all("p",{'class':"comment-content"}):
        context.append(i.text)

    write("\n\n".join(context),flag)
    pass

for i in range(1,3):
    """
    这里的i，应该从1开始，对不对，这次应该可以啦
    """
    urls = base_url + str(i + 1)
    # 能打印出来看看中间的过程
    print(urls)
    get_comment(urls,i) 