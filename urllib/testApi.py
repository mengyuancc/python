#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'urlpost module '

__author__ = 'yuan meng'

"""
### url
http://www.11zz.club/wind/api/addMachineData

### param
token : a3788c8c64fd65c470e23e7534c3ebc8
uid:	57
batch_id:	风场id	1529463124242
machine_name:  风机序号	554167
time:	时间	2018-01-01 12:00
speed:	风机风速	100
power:	风机功率	1000
"""
from urllib import request,parse
import time

now_time = time.localtime()
font_time = time.strftime('%Y-%m-%d %H:%M',now_time)

url = 'http://www.11zz.club/wind/api/addMachineData' 
def cuspost():
	# request post请求
	print('request api start...')
	login_data = parse.urlencode([
	    ('uid', 57),
	    ('token', 'a3788c8c64fd65c470e23e7534c3ebc8'),
	    ('batch_id', 1529463124242),
	    ('machine_name', 554167),
	    ('time', font_time),
	    ('speed', '100'),
	    ('power', '100')
	])
	req = request.Request(url)
	req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
	"""
	req.add_header('Origin', 'https://passport.weibo.cn')
	req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')
	"""
	with request.urlopen(req, data=login_data.encode('utf-8')) as f:
	    print('Status:', f.status, f.reason)
	    for k, v in f.getheaders():
	        print('%s: %s' % (k, v))
	    print('Data:', f.read().decode('utf-8'))


if __name__=='__main__':
	cuspost()