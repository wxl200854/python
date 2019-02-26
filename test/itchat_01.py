import itchat
import time

@itchat.msg_register(itchat.content.TEXT)
def reply_msg(msg):
    print("收到一条信息：", msg.text)

if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    time.sleep(5)
    itchat.send("文件助手你好", toUserName="filehelper")
    result = itchat.search_friends(name="阳光普照")
    print(result)
    itchat.run()