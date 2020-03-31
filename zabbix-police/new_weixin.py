#!/usr/local/bin/python
#_*_coding:utf-8 _*_
import requests,sys,json
requests.packages.urllib3.disable_warnings()
#import urllib3
#urllib3.disable_warnings()
from config import *
reload(sys)
sys.setdefaultencoding('utf-8')
import os

#获取Token
def GetToken(Corpid,Secret):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    Data = {
        "corpid": Corpid,
        "corpsecret": Secret
    }
    r = requests.get(url=Url,params=Data,verify=False)
    Token = r.json()['access_token']
    return Token

#将获取到的趋势图，上传至企业微信临时素材，返回MediaId发送图文消息是使用
def GetImageUrl(Token,Path):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=%s&type=image" % Token
    data = {
        "media": open(Path,'r')
        }
    r = requests.post(url=Url,files=data)
    dict = r.json()
    return dict['media_id']

#文本消息    
def SendTextMessage(Token,User,Agentid,Content):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
    Data = {
        "touser": User,                                 # 企业号中的用户帐号
        "msgtype": "text",                          # 消息类型
        "agentid": Agentid,                             # 企业号中的应用id
        "text": {
            "content": Content
        },
    "safe": "0"
    }
    r = requests.post(url=Url,data=json.dumps(Data),verify=False)
    return r.text


#卡片消息    
def SendCardMessage(Token,User,Agentid,Subject,Content):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
    Data = {
        "touser": User,                                 # 企业号中的用户帐号
        "msgtype": "textcard",                          # 消息类型
        "agentid": Agentid,                             # 企业号中的应用id
        "textcard": {
            "title": Subject,
            "description": Content,
            "url": zabbix_host,          #点击详情后打开的页面
            "btntxt": "详情"
        },
    "safe": "0"
    }
    r = requests.post(url=Url,data=json.dumps(Data),verify=False)
    return r.text

#图文消息news
def SendnewsMessage(Token,User,Agentid,Subject,Content,History_url,Pic_url):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
    Data = {
            "touser": User,                                 # 企业号中的用户帐号
            "msgtype": "news",                            # 消息类型
            "agentid": Agentid,                             # 企业号中的应用id
            "news": {
                    "articles": [
                    {
                            "title": Subject,
                            "description": Content,
                            "picurl": Pic_url,
                            "url": History_url,      #点击阅读原文后，打开趋势图大图，第一次需要登录
                    }
                    ]
            },
            "safe": "0"
    }
    headers = {'content-type': 'application/json'}
    data = json.dumps(Data,ensure_ascii=False).encode('utf-8')
    r = requests.post(url=Url,headers=headers,data=data)
    return r.text

#图文消息mpnews
def SendmpnewsMessage(Token,User,Agentid,Subject,Content,Media_id,history_url):
    Url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s" % Token
    Data = {
            "touser": User,                                 # 企业号中的用户帐号
            "msgtype": "mpnews",                            # 消息类型
            "agentid": Agentid,                             # 企业号中的应用id
            "mpnews": {
                    "articles": [
                    {
                            "title": Subject,
                            "thumb_media_id": Media_id,
                            "content": Content,
                            "content_source_url": history_url,      #点击阅读原文后，打开趋势图大图，第一次需要登录
                            "digest": Content,
                            "show_cover_pic": "1"
                    }
                    ]
            },
            "safe": "1"
    }
    headers = {'content-type': 'application/json'}
    data = json.dumps(Data,ensure_ascii=False).encode('utf-8')
    r = requests.post(url=Url,headers=headers,data=data)
    return r.text
   
