#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
desc:
正则匹配
"""

import re

def main():
	ret = re.search("(?P<id>\d{3})/(?P<name>\w{3})", 'weer34fd123/uuu')
	print(ret.group())
	print(ret.group('id'))
	print(ret.group('name'))

if __name__ == '__main__':
	main()