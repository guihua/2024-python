from email.mime.text import MIMEText
import smtplib

# 邮件正文是纯文本，所以继续使用MIMEText
# 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令，注意口令是口令不是邮箱的登录密码，是授权码，如何获取授权码，请看Email文档
from_addr = input('From:')
password = input('Password:')
# 输入收件人地址
to_addr = input('To:')
# 输入SMTP服务器地址，注意是SMTP协议的地址，不是网页的地址
smtp_server = 'smtp.126.com'

# Create an SMTP object and connect to the server
server = smtplib.SMTP(smtp_server, 25)
server.connect()

# 打印出和SMTP服务器交互的所有信息，包括登录信息
server.set_debuglevel(1)
# 登录SMTP服务器，注意是授权码，不是邮箱的登录密码
server.login(from_addr, password)
# 发送邮件
# sendmail()方法就是发邮件，由于可以一次发给多个人，所以传入一个list，邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
# 关闭连接
# 注意，不关闭连接会导致后面的邮件发送失败
server.quit()
