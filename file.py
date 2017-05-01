#-*- encoding: utf-8 -*-
#filesystem,and test of time
#date:4.15

import os
import time
import calendar

url22 = "C:/22"
def mapss(name):
  return os.path.splitext(name)[1] == '.avi'
L = [ x for x in os.listdir(url22) if mapss(x)]
Dir = [x for x in os.listdir(url22) if os.path.isdir(url22+"/"+x)]
print(Dir)
#url22+"/OnlyTease.com.17.01.22.Maria.XXX.IMAGESET-IEVA[rarbg]"
print(os.rename(os.getcwd()+"/fuck baby!", 'c:/22/pussy cat'))


#time.time() 指当前时间的毫秒数
#time.localtime(毫秒数) 取得格式化的时间，有参数代表取得对应时间，没有参数，当前时间
# now = time.localtime()
# print(now, "localtime")
# print(time.asctime(now))
# print(time.strftime("%Y-%m-%d  %H:%M:%S",now))
# print(calendar.month(2017,4))
