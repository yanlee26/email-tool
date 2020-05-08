#coding: utf-8    
import os
import smtplib    
from email.mime.multipart import MIMEMultipart   
from email.mime.text import MIMEText    
from email.header import Header   

from utils import read_template, get_contacts

#设置smtplib所需的参数
#下面的发件人，收件人是用于邮件传输的。
smtpserver = 'smtp.163.com'
password=os.environ['pwd']
sender='elliot29@163.com'
username = 'elliot29'
#receiver='XXX@126.com'
#收件人为多个收件人

# subject
# subject = 'Python email test'
#通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
subject = '你好，世界！'
#subject=Header(subject, 'utf-8').encode()
    
#构造邮件对象MIMEMultipart对象
#下面的主题，发件人，收件人，日期是显示在邮件页面上的。

#msg['To'] = 'XXX@126.com'
#收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
# msg['To'] = ";".join(receiver) 
#msg['Date']='2012-3-16'

#构造图片链接
# sendimagefile=open(r'D:\pythontest\testimage.png','rb').read()
# image = MIMEImage(sendimagefile)
# image.add_header('Content-ID','<image1>')
# image["Content-Disposition"] = 'attachment; filename="testimage.png"'
# msg.attach(image)

#构造html
#发送正文中的图片:由于包含未被许可的信息，网易邮箱定义为垃圾邮件，报554 DT:SPM ：<p><img src="cid:image1"></p>
# html = """
# <html>  
#   <head></head>  
#   <body>  
#     <p>Hi!<br>  
#        How are you?<br>  
#        Here is the <a href="http://www.baidu.com">link</a> you wanted.<br> 
#     </p> 
#   </body>  
# </html>  
# """    
# text_html = MIMEText(html,'html', 'utf-8')
# text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'   
# msg.attach(text_html)    


#构造附件
# sendfile=open(r'D:\pythontest\1111.txt','rb').read()
# text_att = MIMEText(sendfile, 'base64', 'utf-8') 
# text_att["Content-Type"] = 'application/octet-stream'  
# #以下附件可以重命名成aaa.txt  
# #text_att["Content-Disposition"] = 'attachment; filename="aaa.txt"'
# #另一种实现方式
# text_att.add_header('Content-Disposition', 'attachment', filename='aaa.txt')
# #以下中文测试不ok
# #text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
# msg.attach(text_att)    


#发送邮件
def main(contactsFile, tplFile):
    names, emails, ccs = get_contacts(contactsFile)
    for name, email, cc in zip(names, emails, ccs):
        msg = MIMEMultipart('mixed') 
        msg['Subject'] = subject
        msg['From'] = sender
        msg['Cc'] = cc
        print('sending to ...', name)
        message_template = read_template(tplFile)
        message = message_template.substitute(PERSON_NAME=name.title())
        msg.attach(MIMEText(message, 'plain'))
        # print(message)
        smtp = smtplib.SMTP()    
        smtp.connect('smtp.163.com')
        #我们用set_debuglevel(1)就可以打印出和SMTP服务器交互的所有信息。
        # smtp.set_debuglevel(1)  
        smtp.login(username, password)    
        smtp.sendmail(sender, email, msg.as_string())   
        del msg 
    # Terminate the SMTP session and close the connection
    smtp.quit()

main('./contacts/contacts.txt', './templates/message.txt')

