import itchat 
import time

def after():
    user_info = itchat.search_friends(name="阳光普照")
    if len(user_info) > 0:
        user_name = user_info[0]['UserName']
        itchat.send_msg("你好", user_name)
        time.sleep(10)
        itchat.send_image('cat.jpg', user_name)
        time.sleep(10)
        itchat.send_file('123.txt', user_name)
        time.sleep(10)
        itchat.send_video('1111.mp4', user_name)

if __name__ == "__main__":
    itchat.auto_login(loginCallback=after)
    itchat.run()