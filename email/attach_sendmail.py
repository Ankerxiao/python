#!/usr/bin
#coding:utf-8

import os
import smtplib
import time
import re

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

import sys
reload(sys)
sys.setdefaultencoding('utf8')

#邮箱基本信息
smtpserver = 'smtp.mxhichina.com'
username = 'ci@synitalent.com'
password= 'q1w2E#R$'
from_addr = username
to_addr = 'huang.xiaokun@synitalent.com'

msg = MIMEMultipart()
msg['Subject'] = u"附件测试邮件,heheda"
msg['From'] = from_addr
msg['To'] = to_addr

mail_body = "hello,拜托啊，有邮件正文了,中文已经不乱码喽"
body = MIMEText(mail_body,"text","utf-8")
msg.attach(body)

att = MIMEText(open('html_sendmail.py','rb').read(),'base64','utf-8')
att['Content-Type'] = 'application/octet-stream'
att['Content-Disposition'] = 'attachment;filename="text_sendmail.py"'
msg.attach(att)

try:
    sm = smtplib.SMTP(smtpserver,port=587,timeout=20)
    sm.login(username,password)
    sm.sendmail(from_addr,to_addr,msg.as_string())
    sm.quit()
    print '邮件发送成功'
except smtplib.SMTPException:
    print "Error:无法发送邮件"
