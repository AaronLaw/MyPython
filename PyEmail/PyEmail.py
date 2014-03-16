#!/usr/bin/env python
#coding:utf-8
'''
@author:   kolaman
@version:  0.1beta
@email:    wpf420@gmail.com
@date:     20140315
@desc:     使用wxPython写的一个简单的邮件群发工具,测试版暂时只能使用163邮箱进行群发
'''
import wx
import wx.lib.buttons as buttons
import re
import SimpleEmail
import sys  

reload(sys) 
sys.setdefaultencoding('utf-8')   

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,u'邮件群发器')
        panel = wx.Panel(self)
        panel.SetBackgroundColour('white')
        self.CreateStatusBar(1, wx.ST_SIZEGRIP)
        self.SetStatusText(u'一个简单的邮件群发脚本',0)

        self.EmailName = wx.StaticText(panel,-1,u'帐号',
            size=(50,-1),style=wx.ALIGN_CENTER)
        self.EmailPwd = wx.StaticText(panel,-1,u'密码',
            size=(50,-1),style=wx.ALIGN_CENTER)
        self.EmailTitle = wx.StaticText(panel,-1,u'邮件标题：',
            size=(150,20))
        self.EmailContent = wx.StaticText(panel,-1,u'邮件内容：',
            size=(150,20))
        self.EmailNameTC = wx.TextCtrl(panel,-1,
            size=(180,-1))
        self.EmailPwdTC = wx.TextCtrl(panel,-1,
            size=(180,-1),style=wx.TE_PASSWORD)
        self.EmailTitleTC = wx.TextCtrl(panel,-1,'test',
            size=(600,50),style=wx.TE_MULTILINE)
        self.toEmail = wx.TextCtrl(panel, -1,
            'wpf420@gmail.com',
               size=(250, 400), style=wx.TE_MULTILINE)
        self.EmailContentTC = wx.TextCtrl(panel,-1,'test',
            size=(-1,-1),style=wx.TE_MULTILINE)
        self.EmailTitleTC.SetMaxLength(150)
        self.EmailContentTC.SetMaxLength(100000)

        self.button1 = buttons.GenButton(panel,-1,u"提交",size=(180,-1))
        self.button2 = buttons.GenButton(panel,-1,u'提交',size=(250,-1))
        self.button3 = buttons.GenButton(panel,-1,u'发送邮件',size=(600,50))
        self.button1.SetUseFocusIndicator(False)
        self.button2.SetUseFocusIndicator(False)
        self.button3.SetUseFocusIndicator(False)
        self.Bind(wx.EVT_BUTTON,self.SetMyAccounts,self.button1)
        self.Bind(wx.EVT_BUTTON,self.SetAccounts,self.button2)
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.button3)

##################### 布局  #####################
        mainSizer = wx.BoxSizer(wx.HORIZONTAL)
        Sizer = wx.BoxSizer(wx.VERTICAL)
#+++++++++++++++++++++box1:个人信息栏++++++++++++++++++++++++++++++++++++++++++
        box1 = wx.StaticBox(panel,-1,u'您的邮箱信息')
        box1Sizer = wx.StaticBoxSizer(box1,wx.VERTICAL)
        nameSizer = wx.GridBagSizer(hgap=20,vgap=20)
        nameSizer.Add(self.EmailName,pos=(0,0))
        nameSizer.Add(self.EmailNameTC,pos=(0,1))
        nameSizer.Add(self.EmailPwd,pos=(1,0))
        nameSizer.Add(self.EmailPwdTC,pos=(1,1))
        nameSizer.Add(self.button1,pos=(2,1),flag=wx.ALIGN_RIGHT)
#+++++++++++++++++++++box2：目标邮箱栏++++++++++++++++++++++++++++++++++++++++++
        box2 = wx.StaticBox(panel,-1,u'您要群发的邮箱')
        box2Sizer = wx.StaticBoxSizer(box2,wx.VERTICAL)
#+++++++++++++++++++++box3：内容板块++++++++++++++++++++++++++++++++++++++++++++
        Box3 = wx.StaticBox(panel,-1,u'请输入邮件内容')
        box3 = wx.StaticBoxSizer(Box3,wx.VERTICAL)
        #box3 = wx.BoxSizer(wx.VERTICAL)
        box3.Add(self.EmailTitle,0,wx.TOP)
        box3.Add(self.EmailTitleTC,0,wx.SHAPED,10)
        box3.Add(self.EmailContent)
        box3.Add(self.EmailContentTC,10,wx.EXPAND,10)
        box3.Add(self.button3)

        box2Sizer.Add(self.toEmail)
        box2Sizer.Add(self.button2)
        box1Sizer.Add(nameSizer)
        Sizer.Add(box1Sizer,0,wx.ALL,5)
        Sizer.Add(box2Sizer,5,wx.ALL,5)

        mainSizer.Add(Sizer)
        mainSizer.Add(box3,0,wx.EXPAND,10)
        panel.SetSizer(mainSizer)
        mainSizer.Fit(self)
#####################方法：#####################

    def SetMyAccounts(self,evt):
        account = self.EmailNameTC.GetValue()
        pwd = self.EmailPwdTC.GetValue()
        try:
            n = account.index('@')
            SimpleEmail.MailUser = account[:n]
            SimpleEmail.MailPswd = pwd
            SimpleEmail.MailPostfix = account[n+1:]
            SimpleEmail.MailHost = SimpleEmail.MailDic[SimpleEmail.MailPostfix]
            self.SetStatusText(u'一个简单的邮件群发脚本',0)
        except ValueError,e:
            self.SetStatusText(u'请填写正确的邮箱格式',0)
             
    def SetAccounts(self,evt):
        account = self.toEmail.GetValue()
        try:
            SimpleEmail.to = account.split()
        except:
            self.SetStatusText(u'请填写正确的邮箱格式',0)

    def OnClick(self,evt):
        title = self.EmailTitleTC.GetValue().encode('utf-8')
        content = self.EmailContentTC.GetValue().encode('utf-8')
        try:
            SimpleEmail.main(title,content)
            self.SetStatusText(u'邮件发送成功',0)
        except:
            self.SetStatusText(u'发送失败',0)

app = wx.App()
Frame().Show()
app.MainLoop()
