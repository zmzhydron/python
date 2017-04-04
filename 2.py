# -*- coding:utf-8 -*-
#daytwo

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
lista = []
count = 0
while count<100:
  count = count+1
  lista.append(count)

list10 = lista[-20:-10:3]
print(list10)
for index, value in enumerate(list10):
  # print("使用enumerate方法使遍历list数组的时候获取--下标: %s --值: %s" %(index, value))
  pass

#列表生成式 变量开始名称为co
colist2 = [ x+m+z for x in 'abcd' for m in '123' for z in '大' ]
print(colist2)
L1 = ['Hello', 'World', 18, 'Apple', None]
l2 = [x.lower() for x in L1 if isinstance(x,str) ]
print(l2)

