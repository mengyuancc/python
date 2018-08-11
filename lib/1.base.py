#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#第一个python程序
#输入 输出
'''
age = input("请输入您的年龄：")
age = int(age)
if age > 20:
	print('少年 你好',age)
else:
	print('小伙 你好',age)

sum = 0;
#循环
for x in range(10000000000000):
	sum = sum + x
print(sum)

sum = 0;
for x in range(1000):
	print(x)
'''
#函数
'''
def my_abs(x):
	if x >= 0:
		return x
	else:
		return -x
		
a = my_abs(-10)
print(a)
'''
'''
#修改元组的数据
a = (1,2,3,4)
def change(a, position, value):
	b = list(a)
	b[position] = value
	a = tuple(b)
	return a
change(a, 2, 5)
print(a)

a = (1,2,3,4)
b = list(a)
b[2] = 5
a = tuple(b)
print(a)

for x in tuple(range(1, 1000000, 2)):
    print('第%d遍'%x)

i = 1
while True:
	i += 1
	a = list(range(i))
	print(a)
'''

#1.修改元组
'''
a = (1,2,3,4)
def changes(position, v, *a):
	b = list(a)
	position = int(position)
	b[position] = v
    c = tuple(b)
	return c
c = changes(3, 5, *a)
print(c)
'''
#2. n*n*n
'''
def my_power(x, n=2):
	a = 1
	while n > 0:
		a = x * a
		n = n - 1
	return a
c = my_power(3, 2000)
print(c)
'''
#3. 关键字参数
'''
def person(name, age, **k):
	#print('name:', name, 'age:', age, 'k:', k);
	print('name is %s age is %d '%(name,age))

person('mengyaun', 15, city='河南', sex=1)
'''
#4. 命名关键字参数
'''
def person(name, age, *, city, sex):
	#print('name:', name, 'age:', age, 'k:', k);
	print('name is %s age is %d city is %s sex is %d'%(name,age, city, sex))

person('mengyaun', 15, city='河南', sex=1)

def person(name, age, *args, city, sex):
	#print('name:', name, 'age:', age, 'k:', k);
	print('name is %s age is %d city is %s sex is %d'%(name,age, city, sex))

#person('mengyaun', 15, city='河南', sex=1)
person('mengyaun', 15, '河南', 1) # error
'''
#5.列表生成式
# t = [(x,y) for x in range(2) for y in range(2)]  #生成元组组成的列表
# t = dict([(x,y) for x in range(2) for y in range(2)]) 
#print(t)
''' 遍历当前目录下的所有文件
import os
dir = [d for d in os.listdir('../../')]
print(dir)
'''
#6. 生成器
#g = (x*x for x in range(1,100))
#for x in g:
#	print(x)

#斐波拉契数列
'''
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a+b
		n = n + 1
	#return 'done'

g = fib(100)

for x in g:
	print(x)
'''
#7.异常处理  范例
'''
import urllib
sth_url = "http://www.baidu.com"
c= dir(urllib)
print(c)
try:
	d = urllib.urlopen(sth_url)
except IOError:
	print("urloprn error")
#except:
#    print('demo')  可以多次except
else:
	content = d.read()
	print(content)
finally:
	d.close()
'''
#8.多线程操作 处理海量数据
'''
import threading
import time

def test(p):
	#做一些想做的事
	time.sleep(0.001)
	return p
ts = []  #处理后数据存储的地方
#fork多个进程进行处理
for i in xrange(0,15):
	th = threading.Thread(target=test,args=[i])
	th.start()
	ts.append(th)

#for i in ts:
#	i.join()
#接下来的语句
print ts
print "hoho,end!!!!!"
'''

