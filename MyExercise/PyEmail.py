#!/usr/bin/env python
#coding:utf-8

import smtplib
from email.mime.text import MIMEText

#list of mail address you wana to send
to = ["123456@qq.com", "test@163.com","wpf420@gmail.com"]

#user and password of your mail
MailHost = "smtp.163.com"
MailUser = "用户名"
MailPswd = "密码"
MailPostfix = "163.com"

def SendMail(to, sub, content):
    
    Me = MailUser + "<" + MailUser + "@" + MailPostfix + ">"
    Msg = MIMEText(content)
    Msg['Subject'] = sub
    Msg['From'] = Me
    Msg['To'] = ";".join(to)
    
    try:
        s = smtplib.SMTP()
        s.connect(MailHost)
        s.login(MailUser, MailPswd)
        s.sendmail(Me, to, Msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False
        
def main():
    
    sub = "email title"
    content = "这是一封测试邮件"
    if SendMail(to, sub, content):
        print 'send successful'
    else:
        print 'send failed'
    return 0

if __name__ == '__main__':
    main()