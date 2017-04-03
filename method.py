def fuckyou():
  name = input("bitch name: ")
  print("fuck you bitch: %s" %name)
  return name
#默认参数
def morencanshu(name,age,salary="11000",fucking="180"):
  print(name,age,salary,fucking)
  return '默认参数'
#模仿JavaScript方法的arguments
def javascrptFn(*fuckyou):
  for i in fuckyou:
    print("a HA: %s"%i)
  return '模仿JavaScript方法的arguments'
#关键字参数
def guanjianziFn(name,sex, **kw):
  print("关键字参数：", kw)
  return ("关键字参数")
#命名关键字参数
def minmingguanjianzicanshufn(name,sex, *, salary, fucking):
  print(salary, fucking)
  return ("命名关键字参数")
# 递归
def reducer(num):
  if num == 0:
    return num
  else:
    return reducer(num-1)+num
