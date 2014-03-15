#!/usr/bin/env python
#coding:utf-8

import smtplib
from email.mime.text import MIMEText

MailDic = {"163.com":"smtp.163.com"}

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
        return False
        
def main(sub,content):
    if SendMail(to, sub, content):
        wx.MessageBox(u"邮件发送成功!", u"消息框",
            wx.OK | wx.ICON_QUESTION)
    else:
        wx.MessageBox(u"发送失败,请重试！", u"消息框",
            wx.OK | wx.ICON_QUESTION)

if __name__ == '__main__':
    main()
