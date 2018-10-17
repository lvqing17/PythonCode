import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

header = {
    "Host":'maoyan.com',
    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
}

url = 'http://maoyan.com/board/4?offset=0'
base_url = 'http://maoyan.com/board/4?offset='
r = requests.get(url,headers = header)
r.encoding = 'utf-8'
html = r.text
# print(html)

soup = BeautifulSoup(html,'lxml')
other = soup.find('dl',{"class":'board-wrapper'})
# print(other)


img = other.find_all('img',{"class":'board-img'})
stars = other.find_all('p',{"class":'star'})
names = other.find_all('a',{'class':'image-link'})
score = other.find_all('p',{"class":'score'})

# for i in img:
#     # print(i['data-src'])
#     urlretrieve(i['data-src'], './movie/picture/' + i['alt'] + '.jpg') 

# for i in stars:
#     # print(i.text)
#     with open('./movie/stars/stars.txt', 'a') as f:
#         f.write(i.text)
        
# for i in names:
#     # print(i['title'])
#     with open('./movie/names/names.txt','a') as f:
#         f.write(i['title'] + '\n')

# for i in score:
#     # print(i.text)
#     with open('./movie/score/score.txt', 'a') as f:
#         f.write(i.text + '\n')
      


def write_content(img,stars,names,score):
    for i in img:
    # print(i['data-src'])
        urlretrieve(i['data-src'], './movie/picture/' + i['alt'] + '.jpg') 

    # for i in stars:

    # # print(i.text)
    #     with open('./movie/stars/stars.txt', 'a') as f:
    #          f.write(i.text)
        
    # for i in names:
    # # print(i['title'])
    #     with open('./movie/names/names.txt','a') as f:
    #          f.write(i['title'] + '\n')

    # for i in score:
    # # print(i.text)
    #     with open('./movie/score/score.txt', 'a') as f:
    #          f.write(i.text + '\n')
    for i in range(10):
        # print(names[i],stars[i],score[i])
        with open('./movie/movie.txt','a') as f:
            f.write(names[i]['title'] +  ' ' + stars[i].text.replace(" ","").strip() + ' ' + score[i].text + '\n')
    pass


def get_content(url):
    r = requests.get(url,headers = header)
    r.encoding = 'utf-8'
    html = r.text

    soup = BeautifulSoup(html,'lxml')
    other = soup.find('dl',{"class":'board-wrapper'})

    img = other.find_all('img',{"class":'board-img'})
    stars = other.find_all('p',{"class":'star'})
    names = other.find_all('a',{'class':'image-link'})
    score = other.find_all('p',{"class":'score'})

    write_content(img,stars,names,score)
    pass

for i in range(10):
    urls = base_url + str(i) + '0'
    print(urls)

    get_content(urls)