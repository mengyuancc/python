#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'urlget module '

__author__ = 'yuan meng'

from urllib import request
url = 'http://182.92.170.3/ai-stock/test?stockId='
def cusget():
	#测口测试 get请求
	with request.urlopen(url) as f:
	    data = f.read()
	    print('Status:', f.status, f.reason)
	    for k, v in f.getheaders():
	        print('%s: %s' % (k, v))
	    print('Data:', data.decode('gbk'))


if __name__=='__main__':
	cusget()