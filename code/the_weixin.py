from wxpy import *
import time


# 这样可以不用每次扫码登陆了
bot = Bot(cache_path=True)
# bot.self.add()
# bot.self.accept()
# 好友:Friend
# 群聊：Group
# 公众号：MP
friend_0 = bot.friends().search('颜齐')[0]
# friend_1 = bot.friends().search('李瑞杰')[1]
print(friend_0.nick_name)
# print(friend_1.nick_name)

# group = bot.groups().search()
for i in range(200):
    # 这里是个时间函数，1s发一次，防止被微信自动屏蔽
    time.sleep(1)
    end = friend_0.send("1.晚上跑10公里2.明早交200字检查")
    # friend_1.send("给我买棒棒糖，大黑炭。")
    print(i,end)