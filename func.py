#-*- coding: utf8 -*-

#匿名函数

L = [ "key is %s value is %s "%(str(k), str(v)) for k,v in enumerate(range(0,100))][20:30]
LL = map(lambda x: str(x) + "this is lambda", L);
print(LL)

#偏函数 don't know

def wrapper(fn,arg):
	return fn;
# print(wrapper.__name__)

#函数装饰器

def log(func):
	def wrapper(*l,**kw):
		print("fuck you ,you bigass bitch, and func name is %s"%func.__name__)
		func(*l,**kw)
	return wrapper;
@log
def hello(name,age):
	print("hello %s and your age is %s"%(name,age))

hello('zmz',28)
