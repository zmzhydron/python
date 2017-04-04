# -*- coding:utf-8 -*-
#daytwo
from functools import reduce
#迭代
  #dict 类似于js的对象
me = {"name": "zmz", "age": 34, "sex": "male"}

for d in me.values():
  # print('打印出来的是dict的值: %s' %d)
  pass

for d in me:
  # print('打印出来的是dict的键: %s' %d)
  pass

for key, value in me.items():
  # print('同时打印出来的是dict的键和值: %s %s' %(key,value))
  pass

#切片 和使用数组下标
list10 = [x for x in range(0,100)][-20::5]
# print(list10)
for index, value in enumerate(list10):
  # print("使用enumerate方法使遍历list数组的时候获取--下标: %s --值: %s" %(index, value))
  pass

#列表生成式 变量开始名称为co
colist2 = [x+m+z for x in 'abcd' for m in '123' for z in '大']
# print(colist2)
L1 = ['Hello', 'World', 18, 'Apple', None]
l2 = [x.lower() for x in L1 if isinstance(x,str) ]
# print(l2)

#generator

gen = ( x for x in range(1,10))
for index,value in enumerate(gen):
  # print("index: %s value: %s"%(index,value))
  pass  

def fib(num):
  count =0
  a=1
  b=2
  while(count<num):
    yield a
    a,b = b,a+b
    count = count + 1
  return 'none'

for s in fib(10):
  # print(s)
  pass

#杨辉三角
def yanghuitri(num):
  count = 1
  cur = [1]
  while(count < num):
    yield cur
    #居然可以这样拼接数组？？？？ 牛逼的呀
    cur = [1]+[v+cur[i+1] for i,v in enumerate(cur) if i<(len(cur)-1)]+[1]
    count = count + 1
  return 'none'

yhr = yanghuitri(15)
for s in yhr:
  # print(s)
  pass

#map and reduce 变量名称m
ml1 = ['adam', 'LISA', 'barT']
def mpro(name):
  return name.lower().capitalize()
  pass
ml2 = list(map(mpro, ml1))
print(ml2)
#reduce
def mprod(lists):
  def innerCore(a,b):
    return a*b
  return reduce(innerCore, lists)
mresult = mprod([1,2,3])
print(mresult)
#reduce to float
def splitdot(str):
  dotCount = -1
  strList = list(str)
  for i,j in enumerate(strList):
    if j==".":
      dotCount = i
  a = strList[:dotCount]
  b = strList[dotCount+1:]
  return a,b
def str2float(str):
  splitdotr = splitdot(str)
  def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
  def core(a,b):
      return a*10+b
  def getop(num):
    count = 0
    r = 1
    while(count < num):
      count = count + 1
      r = r*0.1
    return -r
  lista = reduce(core,map(char2num, splitdotr[0]))
  listb = reduce(core,map(char2num, splitdotr[1]))
  return lista+getop(len(splitdotr))*listb
  pass
str2floatresult = str2float('123.123');
print(str2floatresult)

# tiangan = '甲乙丙丁戊己庚辛壬癸'
# dizhi = '子丑寅卯辰巳午未申酉戌亥'
# jiazi = [m + n for i,m in enumerate(tiangan) for j,n in enumerate(dizhi) if (i%2==1 and j%2==1) or (i%2==0 and j%2==0) ]
# print(jiazi)
