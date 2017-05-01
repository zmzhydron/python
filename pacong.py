#-*- encoding: utf-8 -*-

#4-21 爬虫啊

from urllib import request
from html.parser import HTMLParser
import os
import sys


worddir = os.getcwd()
imglist = []

pacongRules = {
  "autohome": {
    "key": "data-original"
  },
  "normal": {
    "key": "src"
  }
}

def downloadImage(src):
  req = request.Request(src)
  req.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
  with request.urlopen(req) as img:
    with open(worddir+"/imgs/"+str(k)+".jpg",'wb') as image:
      image.write(img.read())
class pacong(HTMLParser):
    def handle_starttag(self,tag,attrs):
      
      if(tag == 'img'):
        rules = pacongRules['normal']['key']
        # rules = pacongRules['autohome']['key']
        img = [x for x in attrs if x[0] == 'src']
        # print(attrs)
        if len(img) != 0:
          img = img[0][1].strip()
          imglist.append(img)
      pass
    def handle_endtag(self,tag):
      # print("tag is %s attrs is %s"%(tag,atts))
      pass
    def handle_data(self,data):
      data = data.strip()
      
      if len(data) and self.lasttag != "script" and self.lasttag != 'style' and self.lasttag != 'link':
        # print(data)
        pass
      pass
    # def handle_startendtag(self,tag,attrs):
    #   if(self.lasttag == 'img'):
    #     rules = pacongRules['normal']['key']
    #     # rules = pacongRules['autohome']['key']
    #     img = [x for x in attrs if x[0] == 'src']
    #     print(attrs)
    #     if len(img) != 0:
    #       img = img[0][1].strip()
    #       imglist.append(img)
    #   pass

# url = "http://www.ifeng.com/"
# url = 'http://www.autohome.com.cn/chengdu/'
# url = 'https://avmo.pw/cn/movie/245k'
# url = 'http://cn163.net/archives/3479/'
url = 'http://bbs.ngacn.cc/read.php?tid=11440010/'
# url = 'https://www.chiphell.com/thread-1690478-1-1.html'
# url = 'https://en.wikipedia.org/wiki/Lake_Como'
#解码类型
decodetype = 'gbk'
# decodetype = 'utf-8'
#伪装头部
# req.add_header("User-Agent", 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
# req.add_header("Accept-Language","zh-CN,zh;q=0.8,en;q=0.6")
# req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
# req.add_header("Accept-Encoding","gzip, deflate, sdch")
# req.add_header("Connection","keep-alive")
# req.add_header("Cache-Control","no-cache")
# req.add_header("Pragma","no-cache")
# req.add_header("Proxy-Connection","keep-alive")
# req.add_header("upgrade-insecure-requests","1")
# req.add_header()
# req.add_header("referer", "https://www.chiphell.com/portal.php?mod=list&catid=32&page=2")

headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
}
  # 'Referer':None #注意如果依然不能抓取，这里可以设置抓取网站的host
  # "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
  # "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
  # "Accept-Encoding":"gzip, deflate, sdch",
  # "Connection":"keep-alive",
  # "Cache-Control":"no-cache",
  # "Pragma":"no-cache",
  # "Proxy-Connection":"keep-alive",
  # "upgrade-insecure-requests":"1",
  # "authority": "www.chiphell.com",
  # "method": "GET",
  # "path": "/thread-1690478-1-1.html",
  # "scheme": "htpps"
req = request.Request(url=url,headers=headers)

name = '张明之'
print(name.encode())

with request.urlopen(req) as f:
  data = f.read()
  data = data.decode(decodetype)
  pc = pacong()
  pc.feed(data)
  with open(worddir+"/img.txt", 'w') as txt:
    for k,v in enumerate(imglist):
      txt.write(v+"\n")
      # print(v)
      # downloadImage(v)
  