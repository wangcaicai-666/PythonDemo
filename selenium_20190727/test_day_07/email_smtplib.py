#__author: yaomingxi
#__date: 2019-08-11

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time


subject = '利奇马将登陆山东'

#编写HTML类型的邮件正文
msg = MIMEText('<html><h1>冲锋舟和救援力量赶赴现场紧急救援</h1></html>','html','utf-8')
msg['Subject'] = Header(subject,'utf-8')

#发送邮件
stmp = smtplib.SMTP()
stmp.connect('smtp.126.com',25)
time.sleep(1)
stmp.login("huatianxidi14@126.com","QpSkCn4.6?8'gun")  # 126:  "huatianxidi14@126.com","QpSkCn4.6?8'gun"   #qq: "546647817@qq.com","3856018ccc"
time.sleep(1)
stmp.sendmail("huatianxidi14@126.com", ["512321751@qq.com","huatianxidi14@126.com"], msg.as_string())
time.sleep(1)
stmp.quit()




