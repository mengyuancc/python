#codding = utf8

from wxpy import *

#bot = Bot()
#保存登录信息 
bot = Bot(cache_path=True) 

#使用文件助手发送消息
#bot.file_helper.send("监控登录成功")

# @bot.register()
# def print_message(msg):
# 	print(msg.text)
# 	return "你好 孟老师不在 一会回复你"

# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
	print(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
my_friend = bot.friends()
print(my_friend)
@bot.register(my_friend)
def reply_my_friend(msg):
	return "你好 孟老师不在 一会回复你"

#进入python命令行 让程序保持运行
embed()