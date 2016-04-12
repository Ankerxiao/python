#!/usr/bin

import os
import smtplib
import time

smtpserver = 'smtp.mxhichina.com'
username = 'ci@synitalent.com'
pasword= 'q1w2E#R$'

from_addr = username
to_addr = 'huang.xiaokun@synitalent.com'




sm = smtplib.SMTP(smtpserver,port=587,timeout=20)
sm.login(username,password)
sleep(5)
sm.quit()
