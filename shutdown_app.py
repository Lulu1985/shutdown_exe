import easygui
import os

def autoShutDown():
    choices = ['同意', '不同意（电脑将在5秒后自动销毁）']
    reply = easygui.choicebox('请问你可以做我的男朋友吗？？？',title= '这是一封表白信！',choices = choices)
    if (reply == choices[1]):
        os.system("shutdown -s -t 5") #执行关机命令
        return False
    elif(reply == choices[0]):
        easygui.msgbox('恭喜你成为我的男朋友，余生请多指教。')
        return False
    else:
        return True

isLoop=True
easygui.msgbox('你好，我是宇宙无敌的超级美少女！')
while(isLoop):
    isLoop=autoShutDown()
    if(isLoop is not True):
        break
    else:
        continue
