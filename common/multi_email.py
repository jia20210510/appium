# SMTP:simple mail transfer protocol 属TCP/IP协议簇
# SMTP中email是构建邮件模块，smtplib是发送邮件模块

from email.mime.text import MIMEText  # 定义邮件内容
from email.header import Header       # 定义邮件标题
from email.mime.multipart import MIMEMultipart  #   带附件
import smtplib

# 定义发送邮箱的服务器，邮件设置可查
smtpserver = 'smtp.163.com'
# 邮箱客户端开启授权密码
user= 'xiao'
password= ''

# 发送方
sender = 'yuexiao2019@163.com'
# 邮件接收方
receives = ['yuexiao2019@163.com', 'yuexiao2019@sina.com']

# 邮件主题和内容
subject = '自动化测试'
content = '<html><h1 style= "color:red">自学成才！</h1></html>'

# 邮件正文
msg = MIMEText(content, 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = sender
msg['To'] = ','.join(receives)  # ,号的格式将列表值分开加入

# 带附件
send_file= open('E:\\PycharmProject\\appium\\screenshots\\2019-09-07-18_08_35.png','rb').read()
att= MIMEText(send_file,'base-64','utf-8')
att["content-type"]='application/octet-stream'
att["content-Disposition"]='attachment;filename="log.png"'
# 构建发送与接收
msgRoot= MIMEMultipart()
msgRoot.attach(MIMEText(content,'html','utf-8'))  # 附件正文
msgRoot['Subject']= subject
msgRoot['From']=sender
msgRoot['To']=','.join(receives)
msgRoot.attach(att)


# 使用SSL协议发送，端口号 465/994
smtp= smtplib.SMTP_SSL(smtpserver, 465)
# 向服务器标识用户身份
smtp.helo(smtpserver)
# 服务器返回结果确认
smtp.ehlo(smtpserver)
# 登录用户名和密码
smtp.login(user, password)

print('start sent email ....')
# 发送正文邮件
smtp.sendmail(sender, receives, msg.as_string())
# 发送带附件邮件
# smtp.sendmail(sender,receives,msgRoot.as_string())
smtp.quit()
print('send email end!')

