#!/usr/bin/python
#coding:utf-8
import datetime,time
from collections import Counter 
#告警合并
def mergeproblem(originallist):
    problemlist=[]
    normalist=[]
    Unknown=[]
    triggerkeylist=[]
    sorts=[]
    alarminfo=[]
    #告警or恢复
    for origina in originallist:
        if origina['triggervalue']=='1' :            
            problemlist.append(origina)
            if origina['triggerkey'] not in triggerkeylist:
                triggerkeylist.append(origina['triggerkey'])
        else :
            Unknown.append(origina)

    for triggerkey in triggerkeylist:
        for problem in problemlist:
            if problem['triggerkey']==triggerkey:
                sorts.append(problem)
        alarminfo.append(sorts)
        sorts=[]
    return alarminfo
#恢复合并
def mergenormal(originallist):
    normallist=[]
    Unknown=[]
    triggerkeylist=[]
    sorts=[]
    alarminfo=[]
    #告警or恢复
    for origina in originallist:

        if origina['triggervalue']=='0' :            
            normallist.append(origina)
            if origina['triggerkey'] not in triggerkeylist:
                triggerkeylist.append(origina['triggerkey'])
        else :
            Unknown.append(origina)

    for triggerkey in triggerkeylist:
        for normal in normallist:
            if normal['triggerkey']==triggerkey:
                sorts.append(normal)
        alarminfo.append(sorts)
        sorts=[]
    return alarminfo

#告警压缩
def compress(alarminfo,zabbix_host,alert_type):
    currenttime=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    messagelist=[]
    
    for info in alarminfo:
        hostlist=[]
        hostgroup=[]
        itemids = []
        eventtimelist=[]
        infonum=len(info)
        eventlist=[]

        for host in info:
            #eventid
            eventid = host['eventid']
            #triggervalue
            triggervalue = host['triggervalue']
            #eventid+triggervalue
            event = "%s_%s" %(eventid, triggervalue)

            if event not in eventlist:
                eventlist.append(event)
            #告警信息
            triggername=host['triggername']
            #告警等级
            triggerseverity=host['triggerseverity']
            #告警最新值
            itemvalue=host['itemvalue']
            #持续时间
            eventage=host['eventage']
            #告警键值
            triggerkey=host['triggerkey']
            #告警时间
            if host['eventtime'] not in eventtimelist:
                eventtimelist.append(host['eventtime'])
            #hostinfo=host['hostname']+':'+host['ipaddress']
            #主机名
            #hostname=host['hostname']
            hostip=host['ipaddress']
            hostlist.append(hostip)
            #主机组
            if host['hostgroup'] not in hostgroup:
                hostgroup.append(host['hostgroup'])
            #告警键值ID
            if host['itemid'] not in itemids:
                itemids.append(host['itemid'])
        #取最早的告警时间
        eventtimelist.sort()
        eventtime = eventtimelist[0]
        #统计告警次数
        res = Counter(hostlist)
        hosts = ''
        for key,value in res.items():
            if alert_type == "alert":
                hosts += key + '  告警次数:' + str(value) + '\n'
            elif alert_type == "recovery":
                hosts += key + '  恢复次数:' + str(value) + '\n'
        #获取告警链接
        string = ''
        for i,value in enumerate(itemids):
            string += 'itemids[%d]=%s&' %(i,value)
        history_url = '%s/history.php?period=3600&isNow=1&%speriod=10800' %(zabbix_host,string)
        #判断是告警还是恢复,alert, recovery
        #告警信息
        if alert_type == "alert":
            if infonum <= 6:        
                message = """🔥🔥🔥[Hitales监控-告警]
告警等级: %s
告警信息: %s
告警主机数: %s
告警主机：\n%s
告警主机组: %s
告警时间: %s
持续时间: %s
监控项目: "%s"
监控取值: %s
告警详情: <a href=\"%s\">点击查看监控数据</a>
""" %(triggerseverity, triggername, str(len(res)), hosts.strip(), hostgroup, eventtime, eventage, triggerkey, itemvalue, history_url)
                messagelist.append({'mes': message, 'event': eventlist})
                #messagelist.append({'mes': message, 'event': eventlist, 'triggerkey': triggerkey, 'itemvalue': itemvalue})
            else:
                alert_url = "%s/zabbix.php?action=problem.view&ddreset=1"
                message = """🔥🔥🔥[Hitales监控-告警]
告警等级: %s
告警信息: %s
告警主机数: %s
告警主机："当前存在大量相同告警项,可能发生网络故障!!详情请点击告警详情链接，在监控系统中查看!!"
告警主机组: %s
告警时间: %s
持续时间: %s
监控项目: "%s"
监控取值: %s
告警详情: <a href=\"%s\">点击查看监控数据</a>
""" %(triggerseverity, triggername, str(len(res)), hostgroup, eventtime, eventage, triggerkey, itemvalue, alert_url)
                #messagelist.append(message)
                messagelist.append({'mes': message, 'event': eventlist})
                #messagelist.append({'mes': message, 'event': eventlist, 'triggerkey': triggerkey, 'itemvalue': itemvalue})
        #恢复信息
        elif alert_type == "recovery":
            if infonum <= 6:        
                message = """✅✅✅[Hitales监控-恢复]
恢复等级: %s
恢复信息: %s
恢复主机数: %s
恢复主机：\n%s
恢复主机组: %s
恢复时间: %s
持续时间: %s
监控项目: "%s"
监控取值: %s
恢复详情: <a href=\"%s\">点击查看监控数据</a>
""" %(triggerseverity, triggername, str(len(res)), hosts.strip(), hostgroup, eventtime, eventage, triggerkey, itemvalue, history_url)
                #messagelist.append(message)
                messagelist.append({'mes': message, 'event': eventlist})
                #messagelist.append({'mes': message, 'event': eventlist, 'triggerkey': triggerkey, 'itemvalue': itemvalue})
            else:
                alert_url = "%s/zabbix.php?action=problem.view&ddreset=1"
                message = """✅✅✅[Hitales监控-恢复]
恢复等级: %s
恢复信息: %s
恢复主机数: %s
恢复主机："当前存在大量相同告警项,可能发生网络故障!!详情请点击恢复详情链接，在监控系统中查看!!"
恢复主机组: %s
恢复时间: %s
持续时间: %s
监控项目: "%s"
监控取值: %s
恢复详情: <a href=\"%s\">点击查看监控数据</a>
""" %(triggerseverity, triggername, str(len(res)), hostgroup, eventtime, eventage, triggerkey, itemvalue, alert_url)
                #messagelist.append(message)
                messagelist.append({'mes': message, 'event': eventlist})
                #messagelist.append({'mes': message, 'event': eventlist, 'triggerkey': triggerkey, 'itemvalue': itemvalue})
    return messagelist


