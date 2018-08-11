#codding = utf8
#高阶函数

#1.map #迭代元素格式化
'''
#map返回惰性对象 使用list将列表转换出来
#将列表内的元素 x*x
def f(x):
	return x*x
l = list(map(f, range(10000))) 
print(l)
strl = list(map(f, [1,2,3,4,5,6,7]))  #简写
print(strl)
'''

#2.reduce #计算元素总和
'''
#等同于sum  sum(range(1, 100))
from functools import reduce
def add(x, y):
	return x+y
s = reduce(add, range(1, 100))
print(s)
#数列转整数
def change(x, y):
	return x*10+y
s = reduce(change, [1,4,5,0]
print(s)
#字符串转整数
from functools import reduce
def change(x, y):
	return x*10+y
def char2num(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s]
s = reduce(change, map(char2num, '1230'))
print(s)
'''

#3.filter #过滤
'''
#去除数列中的奇数
def is_odd(x):
	return x % 2 == 0
s = list(filter(is_odd, [1,2,3,4,5,6,7,8,9,10]))
print(s)
#去除数列中的空字符串
def not_empty(x):
	return x and x.strip()
s = list(filter(not_empty, ['xiao', '', 'mengyuan', None, '123']))
print(s)
'''

#4.sorted #排序 自定义排序
'''
s = sorted([4,8,1,7,2])
print(s)
#按照绝对值排序
s = sorted([4,-8,-1,7,-2], key=abs)
print(s)
#转换为小写按照ascii码顺序排序
s = sorted(['abs','fgf','ZXz','zxsd','xcv'], key=str.lower, reverse=True)
print(s)
'''

#5.返回函数 闭包操作
'''
def lazy_sum(*args):
	def sum():
		ax = 0
		for x in args:
			ax = ax + x
		return ax
	return sum

f = lazy_sum(1,2,3,4) 
print(f())
'''

#6.匿名函数 
'''
s = list(map(lambda x: x*x, [1,2,3,4,5,6]))
print(s)

f = lambda x: x+x
print(f(2))

def build(x, y): #闭包操作 匿名函数当作返回值返回
	return lambda: x*x+y*y
s = build(2,3)
print(s())
'''
#7.模块


