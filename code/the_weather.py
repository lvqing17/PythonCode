import requests
from bs4 import BeautifulSoup
import json
import datetime
import time


url = 'http://www.nmc.cn/publish/forecast/ABJ/beijing.html'
url1 ='http://www.nmc.cn/f/rest/real/54511?_=1527909591213'
r = requests.get(url1)
r.encoding = 'utf-8'
html = r.text
# print(r.text)

data = json.loads(r.text)
print(data)
print(data['station']['city'],str(data['weather']['temperature']) + '度',data['weather']['airpressure'],data['weather']['info'],data['wind']['direct'],data['wind']['power'])
# print(data['weatherinfo']['city'],data['weatherinfo']['temp'],data['weatherinfo']['WD'],data['weatherinfo']['WS'],data['weatherinfo']['SD'],data['weatherinfo']['WSE'],data['weatherinfo']['time'],data['weatherinfo']['isRadar'],data['weatherinfo']['Radar'],data['weatherinfo']['njd'],data['weatherinfo']['qy'],data['weatherinfo']['rain'])

# # current_time = datetime.datetime.now()
# # now_time = time.strftime("%H:%M",time.localtime())
# # print(now_time)
# print(data['weatherinfo']['city']+"\t"+data['weatherinfo']['temp']+"\t"+data['weatherinfo']['WD']+"\t"+data['weatherinfo']['WS']+data['weatherinfo']['SD']+data['weatherinfo']['WSE']+data['weatherinfo']['time']+data['weatherinfo']['isRadar']+data['weatherinfo']['Radar']+data['weatherinfo']['njd']+data['weatherinfo']['qy']+data['weatherinfo']['rain'])