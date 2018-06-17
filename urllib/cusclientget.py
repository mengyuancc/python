#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'urlphoneget module '

__author__ = 'yuan meng'

from urllib import request
url = 'http://182.92.170.3/ai-stock/test?stockId='
def cusget():
	#测口测试 模拟浏览器发起get请求
	rep = request.Request(url)
	rep.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
	with request.urlopen(rep) as f:
	    print('Status:', f.status, f.reason)
	    for k, v in f.getheaders():
	        print('%s: %s' % (k, v))
	    print('Data:', f.read().decode('utf-8'))

if __name__=='__main__':
	cusget()