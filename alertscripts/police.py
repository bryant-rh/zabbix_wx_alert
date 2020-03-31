#!/usr/bin/env python
#coding:utf-8
import redis
import sys
subject=sys.argv[1]
r = redis.StrictRedis(host='192.168.3.128', port=6379)
r.set(subject,subject)

