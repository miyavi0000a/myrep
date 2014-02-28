#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 发送邮箱
sender='huwei382@126.com'

# 接收邮箱
receiver='huwei.sz@mopon.cn'

# 邮件主题
subject ='Python email test'

#发送邮箱服务器
smtpserver='smtp.126.com'

# 发送帐号密码
username = 'huwei382@126.com'
password = '***********'

# 中文需要参数‘utf-8’,单字节字符不需要
msg = MIMEText('你好！兲上兲下','text','utf-8')
msg['Subject'] =Header(subject,'utf-8')

try:
	smtp=smtplib.SMTP()
	smtp.connect(smtpserver)
	smtp.login(username,password)
	smtp.sendmail(sender,receiver,msg.as_string())
	smtp.quit()

except Exception,e:
	print e