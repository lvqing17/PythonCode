from wxpy import *
import time
import requests


bot = Bot(cache_path= True)
apikey = "fbb41e250e7c4c38aca935be9859bfc5"
my_friend = ensure_one(bot.search('颜齐'))

tuling = Tuling(apikey)

# @bot.register(my_friend) # 注册消息
# def reply_my_friend(msg):
#     print(msg)
#     tuling.do_reply(msg)
# embed()




