#!/usr/bin/python
# coding=utf-8
import re
string="""🔥🔥🔥[Hitales监控-告警]
告警等级: Warning
告警信息: nh_service 发现Error日志
告警主机数: 1
告警主机：
47.102.139.97  告警次数:1
告警主机组: ['hitales']
告警时间: 2019.08.08 13:38:07
持续时间: 0m
监控项目: "log[/data/logs/nh_service/national-service-error.log,@nh_service_error,,,skip,,]"
监控取值: [2019-08-08 13:37:53.603] [http-nio-8080-exec-20] [ERROR] [ThirdPartyController.java:53] - [TAG:3jWTSUdxhYXQGGKWu7BGOuG7Wk75ucHZ75A2SBsAKcJ1rcJrNwU2VWdZkIw3ZrTb][desc=指标ID不在约定范围] HisAlertPojo.Create(id=5843618, patientId=, createTime=Thu Aug 08 13:37:44 CST 2019, quotaChinese=ST_aVR, quotaEnglish=ST_aVR, alertDesc=*ECG导联脱落, deviceId=1, deviceName=MR, type=MONITOR, quotaId=108)
告警详情: <a href="http://monitor.hitales.ai:8080/h-monitor/history.php?period=3600&isNow=1&itemids[0]=39997&period=10800">点击查看监控数据</a>
"""

item_key = string.strip().split('监控项目:')[1].split('\n')[0].strip()
#print string.split('监控项目')[1]
#if item_key == "log[/data/logs/nh_service/national-service-error.log,\@nh_service_error,,,skip,,]":
if "/data/logs/nh_service/national-service-error.log" in item_key:
    print item_key
a = re.sub(r'告警详情.*$','告警详情: <a href="http://monitor.hitales.ai:8887">点击查看日志系统</a>',string)
print a
