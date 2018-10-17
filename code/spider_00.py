import requests
from bs4 import BeautifulSoup
import json
import urllib
import re



def get_html(urls):
    header = {
        "Referer":"http://music.163.com",
        "Host":"music.163.com",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
    }
    try:
        res_text = requests.get(urls,headers = header).text
        return res_text
    except :
        print("Error")
    pass


def download_song(num,song_name,song_id):
    url = "http://music.163.com/song/media/outer/url?id={}.mp3".format(song_id)
    try:
        print(url)
        pass
    except expression as identifier:
        pass

    pass

def download_lyric(num,song_name,song_id):
    url = "http://music.163.com/api/song/lyric?" + "id=" + str(song_id) + "&lv=1&kv=1&tv=-1"
    text = get_html(url)
    # print('text ',text)
    json_obj = json.loads(text)
    # print('json_obj',json_obj)
    init_lrc = json_obj['lrc']['lyric']
    regex = re.compile(r'\[.*\]')
    final_lrc = re.sub(regex,'',init_lrc).strip()
    print(num,'下载歌词:\t{}'.format(song_name))
    with open("./music/lyric/{0}.txt".format(song_name),'w',encoding = 'utf-8') as f:
        f.write(final_lrc)
    

def get_singer_info(html):
    soupObj = BeautifulSoup(html,'lxml')
    links = soupObj.find('ul',attrs={"class","f-hide"})
    song_names = []
    song_ids = []
    for music in links.find_all('a'):
        music_name = music.text
        music_link = music['href'].split('=')[-1]
        song_names.append(music_name)
        song_ids.append(music_link)
    return zip(song_names,song_ids)
    pass



def main(urls):
    res_text = get_html(urls)
    singer_infos = get_singer_info(res_text)
    # print(singer_info)
    for i,singer in enumerate(singer_infos):
        # 下载音乐的歌词
        download_lyric(i,singer[0],singer[1])
        # 下载音乐
        # download_song(i+1,singer[0],singer[1])
        pass

    pass

if __name__ == '__main__':
    # urls = 'http://music.163.com/playlist?id=317113395'
    urls1 = "http://music.163.com/playlist?id=3778678"
    main(urls1)



"""
程序是如何运行的呢？
首先理解，所有的网络信息都是数据，不论是图片还是视频或者文字，
基于这个思想，我们就能处理视频图片和文字，此外互联网，就是所有人的电脑，连在一起
通过某种交互协议来通信，也就是tcp和http协议，因此，按照这个协议，我们就能获取所有的数据信息了，
比如美女图片，淘宝物品，12306抢票。懂了么？？？？如此一定能懂得，对吗？对的！
"""