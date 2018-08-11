#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
desc:
创建socket对象 监听端口
回复客户端请求
"""

import socket

def handle_response(client):
	buf = client.recv(1024) # 获取http请求体
	client.send("HTTP/1.1 200 OK\r\n\r\n".encode("utf8"))
	with open("index.html", "rb") as f:
		data = f.read()
	client.send(data)

def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(("localhost", 8088))
	sock.listen(5)

	while True:
		connection, address = sock.accept()
		handle_response(connection)
		connection.close()

if __name__ == '__main__':
	main()