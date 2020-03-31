#coding: utf-8

#------ zabbix 配置--------------------------------------------
#zabbix数据库IP                                                
zabbix_db_host = ""
#zabbix数据库端口                                              
zabbix_db_port = 3306 
#zabbix数据库名称                                       
zabbix_db_name = "" 
#zabbix数据库登录用户名                                   
zabbix_db_username = ""
#zabbix数据库登录密码                             
zabbix_db_password = "" 
#在zabbix 可以找到告警收敛的动作ID（actionid）                 
actionid = 8                                            
#图片保存地址
image_path = "/data/zabbix_sendimg/"
#zabbix host
zabbix_host = ""
#zabbix web 登录用户名
zabbix_username = "admin"
#zabbix web 登录密码
zabbix_password = ""
#--------------------------------------------------------------

#------ redis 配置----------------
#redis IP           
redis_host = "192.168.3.128" 
#redis PORT                       
redis_port = 6379 
#---------------------------------

#--------- 企业微信配置 ---------------------------------
#发送微信给运维人员 
Users = '@all'
#企业微信CropID                                         
CorpID = '' 
#企业微信告警群1  Secret                            
Secret_1 = '' 
#企业微信告警群1 agentid    
Agentid_1 = "1000012" 

#专门发错误日志的告警群
#企业微信告警群2  Secret                            
Secret_2 = '' 
#企业微信告警群2 agentid    
Agentid_2 = "1000019" 
#--------------------------------------------------------

#------ 日志目录配置----------------
log_path = '/data/logs/zabbix'
#--------------------------------------------------------
