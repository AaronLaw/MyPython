#coding:utf-8
'''
用wxpython写的一份简历模板
@author:  kolaman
@version:   0.1
@email:   wpf420@gmail.com
'''
import wx

class ResumeFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,u"个人简历")
        self.Center(direction=wx.BOTH)
        self.SetBackgroundColour('white')
        self.scroll = wx.ScrolledWindow(self, -1)
        self.scroll.SetScrollbars(1, 1, -1, 800)

        img = wx.Image('im.jpg', type=wx.BITMAP_TYPE_ANY, index=-1)
        imgsb = wx.StaticBitmap(self.scroll, -1, wx.BitmapFromImage(img))

        title = wx.StaticText(self.scroll,-1,u"我的wxPython简历")
        title.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        name = wx.StaticText(self.scroll,-1,u'姓名:')
        tel = wx.StaticText(self.scroll,-1,u'电话:')
        email = wx.StaticText(self.scroll,-1,'E-mail:')
        university = wx.StaticText(self.scroll,-1,u'毕业学校：')
        edu = wx.StaticText(self.scroll,-1,u'学历：')
        major = wx.StaticText(self.scroll,-1,u'专业：')
    
        intro = wx.StaticText(self.scroll,-1,u'自我介绍：')
        experience = wx.StaticText(self.scroll,-1,u'工作经验：')
        skill = wx.StaticText(self.scroll,-1,u'技能：')
        sns = wx.StaticText(self.scroll,-1,u'社交网络&github：')

        self.nameTC = wx.TextCtrl(self.scroll,-1,u'your name',size=(150,-1))
        self.telTC = wx.TextCtrl(self.scroll,-1,u'186***********',size=(150,-1))
        self.emailTC = wx.TextCtrl(self.scroll,-1,u'wpf420@gmail.com',size=(150,-1))
        self.eduTC = wx.TextCtrl(self.scroll,-1,u'大学本科',size=(150,-1))
        self.universityTC = wx.TextCtrl(self.scroll,-1,'xxx university',size=(150,-1))
        self.majorTC = wx.TextCtrl(self.scroll,-1,'xxxxx',size=(150,-1))

        self.introTC = wx.TextCtrl(self.scroll,-1,u'',size=(500,50),style=wx.TE_MULTILINE)
        self.experienceTC = wx.TextCtrl(self.scroll,-1,u'',size=(500,50),style=wx.TE_MULTILINE)
        self.skillTC = wx.TextCtrl(self.scroll,-1,u'',size=(500,50),style=wx.TE_MULTILINE)
        self.snsTC = wx.TextCtrl(self.scroll,-1,u'',size=(500,50),style=wx.TE_MULTILINE)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        Sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        Sizer2 = wx.BoxSizer(wx.VERTICAL)
        B1 = wx.StaticBox(self.scroll,-1,u'个人信息：')
        Box1 = wx.StaticBoxSizer(B1,wx.VERTICAL)
        Box2 = wx.BoxSizer(wx.VERTICAL)

        mainSizer.Add(title,0,wx.ALL|wx.ALIGN_CENTER_HORIZONTAL,5)
        mainSizer.Add(wx.StaticLine(self.scroll), 0,
                wx.EXPAND|wx.TOP|wx.BOTTOM, 5)

        Sizer1GB = wx.GridBagSizer(hgap=20, vgap=10)
        Sizer1GB.Add(name,pos=(0,0))
        Sizer1GB.Add(self.nameTC,pos=(0,1))
        Sizer1GB.Add(tel,pos=(1,0))
        Sizer1GB.Add(self.telTC,pos=(1,1))
        Sizer1GB.Add(email,pos=(2,0))
        Sizer1GB.Add(self.emailTC,pos=(2,1))
        Sizer1GB.Add(university,pos=(3,0))
        Sizer1GB.Add(self.universityTC,pos=(3,1))
        Sizer1GB.Add(edu,pos=(4,0))
        Sizer1GB.Add(self.eduTC,pos=(4,1))
        Sizer1GB.Add(major,pos=(5,0))
        Sizer1GB.Add(self.majorTC,pos=(5,1))
        Box1.Add(Sizer1GB,0,wx.ALL,20)
        Box2.Add(imgsb,0,wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT|wx.LEFT,30)
        Sizer1.Add(Box1,0,wx.ALL,5)
        Sizer1.Add(Box2,0,wx.ALL,15)

        Sizer2.Add(intro,0,wx.ALL,5)
        Sizer2.Add(self.introTC,1,wx.ALL,5)
        Sizer2.Add(experience,0,wx.ALL,5)
        Sizer2.Add(self.experienceTC,1,wx.ALL,5)
        Sizer2.Add(skill,0,wx.ALL,5)
        Sizer2.Add(self.skillTC,1,wx.ALL,5)
        Sizer2.Add(sns,0,wx.ALL,5)
        Sizer2.Add(self.snsTC,1,wx.ALL,5)

        mainSizer.Add(Sizer1,0,wx.ALL,5)
        mainSizer.Add(Sizer2,0,wx.ALL,5)
        self.scroll.SetSizer(mainSizer)
        mainSizer.Fit(self)
        #mainSizer.SetSizeHints(self)

app = wx.App()
ResumeFrame().Show()
app.MainLoop()
