#coding:utf-8
'''
一个wxpython写的简单的笔记本
'''
import wx
import os
import sys
from datetime import datetime

reload(sys) javascript:void(0);
sys.setdefaultencoding('utf-8')  

dt = datetime.now()
d = dt.strftime('%Y-%m-%d %H.%M') 

class Frame(wx.Frame):
    
    def __init__(self):
        wx.Frame.__init__(self,None,-1,u'记事本')
        panel = wx.Panel(self)

        self.title = wx.StaticText(panel,-1,u'  标题:')
        self.content = wx.StaticText(panel,-1,u'  内容:')
        self.titleTC = wx.TextCtrl(panel,-1,size=(400,-1))
        self.contentTC = wx.TextCtrl(panel, -1,
            size=(400, 400), style=wx.TE_MULTILINE)
        self.titleTC.SetMaxLength(20)
        self.contentTC.SetMaxLength(99999)

        self.button = wx.Button(panel,-1,u'保存') 
        self.Bind(wx.EVT_BUTTON,self.OnClick,self.button)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(self.title,0, wx.ALL,5)        
        Sizer.Add(self.titleTC,0, wx.ALL,5)        
        Sizer.Add(self.content,0, wx.ALL,5)        
        Sizer.Add(self.contentTC,0, wx.ALL|wx.EXPAND,5)
        Sizer.Add(self.button,0,wx.ALL|wx.EXPAND,5)        

        panel.SetSizer(Sizer)
        Sizer.Fit(self)

    def OnClick(self,evt):
        name = self.titleTC.GetValue() + d + '.txt'
        txt = self.contentTC.GetValue()
        try:
            fil = open(name,'wt')
            fil.write(txt)
            fil.close()
            wx.MessageBox(u"笔记\"%s\"保存成功"%name, u"提示", wx.OK)
        except:
            wx.MessageBox(u"保存失败", u"警告", wx.OK)

app = wx.App()
Frame().Show()
app.MainLoop()
