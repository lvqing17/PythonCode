import requests
# from bs4 import BeautifulSoup
import json

header = {
     "Host":'search.bilibili.com',
     "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
}

url = 'https://search.bilibili.com/all?keyword=%E5%82%B2%E5%A8%87&from_source=banner_search'
url1 = 'https://search.bilibili.com/api/search?search_type=all&keyword=%E5%82%B2%E5%A8%87&from_source=banner_search'
r = requests.get(url1,headers = header)
r.encoding = 'utf-8'
html = r.text
# print(r.text)

# soup = BeautifulSoup(html,'lxml')
# other = soup.find('ul',{'class':"video-contain clearfix"})
# # print(other)
# temp = other.find_all("a")
# for i in temp:
#     print(i['href'])

other = json.loads(r.text)
# print(other['result']['video'][0]['arcurl'])
for i in range(20):
    print(other['result']['video'][i]['arcurl'])