#!/usr/bin
#coding:utf-8

import os
import smtplib
import time

from email.mime.text import MIMEText
from email.header import Header

#邮箱基本信息
smtpserver = 'smtp.mxhichina.com'
username = 'ci@synitalent.com'
password= 'q1w2E#R$'
from_addr = username
to_addr = 'huang.xiaokun@synitalent.com'

#内容
msg = MIMEText('Python邮件发送测试...','text','utf-8')
msg['From'] = from_addr
msg['To'] = to_addr

subject = '电子邮件测试'
msg['subject'] = Header(subject,'utf-8')

try:
    sm = smtplib.SMTP(smtpserver,port=587,timeout=20)
    sm.login(username,password)
    sm.sendmail(from_addr,to_addr,msg.as_string())
    sm.quit()
    print '邮件发送成功'
except smtplib.SMTPException:
    print "Error:无法发送邮件"
