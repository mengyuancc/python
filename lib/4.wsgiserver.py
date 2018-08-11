#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
desc:
封装了简单web服务器 
负责创建socket连接 监听端口 解析封装http请求体
"""

from wsgiref.simple_server import make_server

def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	return [b'<h1>hello world</h1>']

httpd = make_server('localhost', 8080, application)

print('Server HTTP on port 8080')

httpd.serve_forever()