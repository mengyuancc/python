#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
desc:
封装了简单web服务器 
负责创建socket连接 监听端口 
解析封装http请求体
根据将不同的url请求映射给不同的方法进行处理
引入简单的模板原理
user mengyuan 
time 2018-04-18
"""

from wsgiref.simple_server import make_server
import time

#对应路由写接口
def current_time(request):
	cur_time = time.ctime(time.time())
	with open("index.html", "rb") as f:
		data = f.read()
	#print(data)
	data = str(data, "utf8").replace("!current_time!", str(cur_time))
	return [data.encode("utf8")]

#设置路由
def routers():
	urlpatterns = (
		("/current_time", current_time), #就算是一个元素 也要加逗号 否则会报错
		)
	return urlpatterns

#接受并解析http请求映射对应的方法 返回响应头
def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	path = environ['PATH_INFO']
	urlpatterns = routers()
	func = None
	for iterm in urlpatterns:
		if iterm[0] == path:
			func = iterm[1]
			break
	if func:
		return func(environ)
	else:
		return [b'<h1>404</h1>']

#监听端口
httpd = make_server('localhost', 8080, application)

print('Server HTTP on port 8080')

httpd.serve_forever()