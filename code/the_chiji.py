import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import json

header = {
    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
    "Host":'www.365yg.com'
    # "Refer":"http://www.365yg.com/c/user/6873569478/"
}
# url = 'http://www.365yg.com/c/user/6873569478/'
url = "http://www.365yg.com/c/user/article/?user_id=6873569478&max_behot_time=0&max_repin_time=0&count=20&page_type=0"
base_url = "http://www.365yg.com/i" 
temp = "/#mid=6873569478"
# r = requests.get(url,headers = header)
# r.encoding = 'utf-8'
# # html = r.text
# # print(r.text)
# other = json.loads(r.text)
#print(len(other['data']))
# print(other['data'][0]['group_id'])
# soup = BeautifulSoup(html,'lxml')
# other = soup.find("div",{'class':"tt-tabs__content"})
# print(other)
# temp = other.find_all("a")
# links = []
# for i in other['data']:
#     #print(base_url + i['group_id'] + temp)
#     links.append(base_url + i['group_id'] + temp)
#     pass

# links = []
# for i in temp:
#     print(i["href"])

def get_content(url,header):
    """
    输入一个url，获取所有的id_url,返回一个list，包含所有的url
    """
    r = requests.get(url,headers = header)
    r.encoding = 'utf-8'
    other = json.loads(r.text)
    # urlretrieve('other[')
    links = []
    for i in other['data']:
        #print(base_url + i['group_id'] + temp)
        links.append(base_url + i['group_id'] + temp)
    return links


# others = get_content(url,header)
# print(others)
urls = 'http://www.365yg.com/i6557326455401873928/#mid=6873569478'
r1 = requests.get(urls,headers = header)
# print(r1.text)
r1.encoding = 'utf-8'
html = r1.text
soup = BeautifulSoup(html,'lxml')
other1 = soup.find("video",{'class':"vjs-tech"})
print(other1)



