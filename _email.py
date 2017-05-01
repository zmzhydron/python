# -*- coding: utf-8 -*-
import sys
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = '373027385@qq.com' #发送账号
password = 'acikovpowakgbjgh'   #发送账号密码
to_addr = 'zmzhydron@163.com'   #送达账号

smtp_server = 'smtp.qq.com' #使用是qq SMTP服务器
# smtp_server = 'smtp-mail.outlook.com'
mystring = """
    <a href="http://www.baidu.com">不信你点点看</a>
    <img src="cid:imageOne">
"""

#添加附件的情况下需要增加multipart，并往multipart添加MIMEText

contents = MIMEText(mystring, 'html', 'utf-8')

msg = MIMEMultipart() #申明这个邮件的格式内容为类型的，包含了html、附件、和图片；
msg['From'] = _format_addr(' me <%s>' % from_addr) #添加基本信息
msg['To'] = _format_addr(' bitch <%s>' % to_addr) 
msg['Subject'] = Header('yo watup???', 'utf-8').encode() #标题

#添加邮件正文
msg.attach(contents);
#添加附件1
att1 = MIMEText(open('daytwo.txt','rb').read(), "base64", 'utf-8')
att1['Content-Type'] = 'application/octet-stream'
att1['Content-Disposition'] = 'attachment; filename="xixi.txt"'
msg.attach(att1)
#添加图片，使用的是通过html写入img标签来展示图片，地址为相对地址，需要把图片上传到email服务器中来展示。 
#注意<img src="cid:imageOne">中的CID，这个CID估计是为了和msgImages.add_header('Content-ID', '<imageOne>')进行匹配
#来确定展示的图片id来转换成src路径
with open('methods/1.jpg','rb') as imgfp:
    msgImages = MIMEImage(imgfp.read())

# 定义图片 ID，在 HTML 文本中引用
msgImages.add_header('Content-ID', '<imageOne>')
msg.attach(msgImages)


def sendEmail():
    server = smtplib.SMTP()
    server.connect(smtp_server, '587') #使用QQ的SMTP的需要加入SSL加密，SSL的加密端口和普通（25）不一致，加密的为587
    # server.set_debuglevel(1)
    #http://stackoverflow.com/questions/19765073/cant-send-email-via-python-using-gmail-smtplib-smtpexception-smtp-auth-extens
    server.starttls() ##不加上这行会报错
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
try:
    sendEmail()
    print(" 发送 email 成功 ")
except smtplib.SMTPException: 
    print(" 失败 ")
    