from wxpy import *
import time
import requests
from apscheduler.schedulers.blocking import BlockingScheduler
import json


url1 ='http://www.nmc.cn/f/rest/real/54511?_=1527909591213'
r = requests.get(url1)
r.encoding = 'utf-8'
html = r.text
# print(r.text)

data = json.loads(r.text)
# print(data)
# print(data['station']['city'],str(data['weather']['temperature']) + '度',data['weather']['airpressure'],data['weather']['info'],data['wind']['direct'],data['wind']['power'])


task_list = [
    ("15:09","今天好热,天气状况如下，聪明可爱的晴宝宝为您播报：\n"),
    # ("11:06",""),
    ("15:10",str(data['station']['city']) + '   '  + str(data['weather']['temperature']) + '度'+ '   '  + str(data['weather']['airpressure'])+ '   '  + str(data['weather']['info'])+ '   '  + str(data['wind']['direct'])+ '   '  + str(data['wind']['power']))
   
]


bot = Bot(cache_path = True)
wangjc = ensure_one(bot.search('颜齐'))

def task_run():
    for task in task_list:
        task_time = task[0]
        task_content = task[1]
        # print(task_time,task_content)
        if time.strftime("%H:%M",time.localtime()) == task_time:
            print(task_time,task_content)
            wangjc.send(task_content)

def main():
    task_run()
    # 加入时间调度算法
    sched = BlockingScheduler()
    #   这里把之前那个函数当作一个任务，循环查询
    sched.add_job(task_run,'cron',second = 0)
    sched.start()


    # embed()

if __name__ == '__main__':
    main()
    embed()


