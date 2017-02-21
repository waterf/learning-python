# -*-coding:utf8-*-

#  chatroom_reply

import time
import re
import itchat
from itchat.content import *


@itchat.msg_register([TEXT])# register注册
def text_reply(msg):
    if re.search(u'金', msg['Content']):
        itchat.send(msg['Content']+u'朱金杰你个智障', msg['FromUserName'])
    elif re.search(u'师父', msg['Content']):
        itchat.send(msg['content']+u'现在有事稍后回复', msg['FromUserName'])
    else:
        itchat.send(u'哈哈哈哈哈哈', msg['FromUserName'])


@itchat.msg_register([PICTURE, RECORDING, VIDEO, SHARING])
def other_reply(msg):
    itchat.send(u'这图好丑丑的没边', msg['FromUserName'])

@itchat.msg_register(TEXT, isGroupChat = True)
def Text_reply(msg):
    itchat.send(u'@%s I received:%s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])


itchat.auto_login(enableCmdQR=True, hotReload=True)# hotReload短时间重新开启不必重新登录
itchat.run(debug=True)
