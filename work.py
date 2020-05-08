#!/usr/bin/env python3

#- * -coding: utf - 8 - * -
import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from utils import read_template

# 发件人邮箱账号
my_sender = 'yanli@xiaoheiban.cn'
# user登录邮箱的用户名， password登录邮箱的密码（ 授权码， 即客户端密码， 非网页版登录密码）， 但用腾讯邮箱的登录密码也能登录成功# 收件人邮箱账号
my_user = '1393273899@qq.com'
my_pass = os.environ['pwd']
username = 'elliot29'
cc = 'xx <yanli@xiaoheiban.cn>; yy <1393273899@qq.com>'

CURRENT = '''
1. sentry 配置
2. electron sentry 配置
'''

LEARNED = '''
1. LEARNED sentry 配置
2. LEARNED electron 配置
'''

QUESTION = '''
1. electron 自动升级各种坑点， electron 基础包本兼容问题踩坑

'''

NEXT = '''
1. electron 升级各种坑点规避及总结
'''

# def read_template(filename):
#     """
#     Returns a Template object comprising the contents of the 
#     file specified by filename.
#     """
    
#     with open(filename, 'r', encoding='utf-8') as template_file:
#         template_file_content = template_file.read()
#     return Template(template_file_content)

def mail():
    ret = True
    try:
        message_template = read_template('./templates/work.txt')
        message = message_template.substitute(PERSON_NAME = 'All', CURRENT = CURRENT, LEARNED = LEARNED, QUESTION = QUESTION, NEXT = NEXT)

        # 邮件内容
        msg = MIMEText(message, 'plain', 'utf-8')# 括号里的对应发件人邮箱昵称、 发件人邮箱账号
        msg['From'] = formataddr([username, my_sender])# 括号里的对应收件人邮箱昵称、 收件人邮箱账号

        msg['To'] = formataddr(['收件人', my_user])# 邮件的主题
        msg['Subject'] = "12周周报"
        msg['Cc'] = cc

        # SMTP服务器， 腾讯企业邮箱端口是465， 腾讯邮箱支持SSL(不强制)， 不支持TLS# qq邮箱smtp服务器地址: smtp.qq.com, 端口号： 456# 163 邮箱smtp服务器地址： smtp .163.com， 端口号： 25
        server = smtplib.SMTP_SSL("smtp.exmail.qq.com", 465)# 登录服务器， 括号中对应的是发件人邮箱账号、 邮箱密码
        server.login(my_sender, my_pass)# 发送邮件， 括号中对应的是发件人邮箱账号、 收件人邮箱账号、 发送邮件
        server.sendmail(my_sender, [my_user, ], msg.as_string())# 关闭连接
        server.quit()
        # 如果 try 中的语句没有执行， 则会执行下面的 ret = False
    except Exception:
        ret = False
    return ret

ret = mail()
if ret:
  print("邮件发送成功")
else :
  print("邮件发送失败")