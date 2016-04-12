#!/usr/bin
#coding:utf-8

import smtplib
from email.mime.text import MIMEText

#邮箱基本信息
smtpserver = 'smtp.mxhichina.com'
username = 'ci@synitalent.com'
password= 'q1w2E#R$'
from_addr = username
to_addr = 'huang.xiaokun@synitalent.com'

msg = MIMEText('<html><h1>你好,发送邮件了，请注意查收</h1></html>','html','utf-8')
msg['From'] = from_addr
msg['To'] = to_addr
subject = 'html形式的邮件'
msg['Subject'] = subject

try:
    smtp = smtplib.SMTP(smtpserver,port=587,timeout=20)
    smtp.login(username,password)
    smtp.sendmail(from_addr,to_addr,msg.as_string())
    smtp.quit()
    print 'send successful'
except smtplib.SMTPException:
    print 'send failed'
