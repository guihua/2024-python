# MIMEText 构造一个邮件对象
# 邮件对象可以视为邮件的抽象，或者可以认为是一个dict，要把邮件内容写进去，用set_content()方法
# 邮件主题、发件人、收件人等信息并不是通过MIMEText直接添加到MIMEText对象中的，而是添加到邮件头中的
# 邮件头是一个dict对象，可以直接把邮件头添加进去，也可以用set_from()、set_to()等方法来添加
# 邮件对象本身就可以看作邮件头和邮件正文的组合
from email.mime.text import MIMEText
# smtplib 发送邮件
# 发送邮件就是发送MIMEText对象
# 标准的SMTP协议的默认端口是25，但是如果是80端口，那就不叫SMTP协议，而是叫HTTP协议
# 要发送邮件，就必须知道邮件的发送者和接受者
# 邮件发送者就是from，接受者就是to
import smtplib

# 构造一个最简单的邮件对象
# 邮件正文是纯文本，所以继续使用MIMEText
# 注意到构造MIMEText对象时，第一个参数就是邮件正文，第二个参数是MIME的subtype，传入'plain'表示纯文本，最终的MIME就是'text/plain'，最后一定要用utf-8编码保证多语言兼容性
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

# 输入Email地址和口令，注意口令是口令不是邮箱的登录密码，是授权码，如何获取授权码，请看Email文档
from_addr = input('From: guihuapeng@126.com')
password = input('Password: VSdDjyDTguu2aL3g')
# 输入收件人地址
to_addr = input('To: guihuapeng@126.com')
# 输入SMTP服务器地址，注意是SMTP协议的地址，不是网页的地址
smtp_server = input('smtp.126.com')

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
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