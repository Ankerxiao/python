#!/usr/bin
#coding:utf-8

import os
import smtplib
import time

from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

#邮箱基本信息
smtpserver = 'smtp.mxhichina.com'
username = 'ci@synitalent.com'
password= 'q1w2E#R$'
from_addr = username
to_addr = 'huang.xiaokun@synitalent.com'

msg = MIMEMultipart('related')
msg['Subject'] = '附件测试邮件'
msg['From'] = from_addr
msg['To'] = to_addr

message = "hello,有邮件正文了"
body = MIMEText('hello,有邮件正文了','text','utf-8')
msg.attach(body)

att = MIMEText(open('text_sendmail.py','rb').read(),'base64','utf-8')
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
