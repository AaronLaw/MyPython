#coding:utf-8
#!/usr/bin/env python
'''
@author:  kolaman
@version:   0.1
@email:   wpf420@gmail.com
@date:  20140316
@desc:  用wxpython写的一个能够批量改写文件名称的小脚本，可批量更改中文名称
'''
import wx
import os
import wx.lib.buttons as buttons

import sys 
reload(sys)
sys.setdefaultencoding('utf-8')

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,u"批量修改文件名称",
            style=wx.DEFAULT_FRAME_STYLE^(wx.RESIZE_BORDER))
        panel = wx.Panel(self,-1)
        panel.SetBackgroundColour('white')
        self.CreateStatusBar(1, wx.ST_SIZEGRIP)
        self.SetStatusText(u'一个批量修改文件名字的脚本',0)

        self.Open = wx.TextCtrl(panel,-1,size=(250,50),
            style=wx.TE_MULTILINE)
        self.OldName = wx.TextCtrl(panel,-1,size=(250,-1))
        self.NewName = wx.TextCtrl(panel,-1,size=(250,-1))
        
        self.OpenButton = buttons.GenButton(panel,-1,u'打开文件',size=(70,-1))
        self.FindButton = buttons.GenButton(panel,-1,u'查询',size=(70,-1))
        self.ModButton = buttons.GenButton(panel,-1,u'修改',size=(70,-1))
        self.OpenButton.SetUseFocusIndicator(False)
        self.FindButton.SetUseFocusIndicator(False)
        self.ModButton.SetUseFocusIndicator(False)
        self.Bind(wx.EVT_BUTTON,self.OpenFile,self.OpenButton)
        self.Bind(wx.EVT_BUTTON,self.FindFile,self.FindButton)
        self.Bind(wx.EVT_BUTTON,self.ModFile,self.ModButton)

        self.cmd = wx.TextCtrl(panel, -1,
            u'''
            使用步骤：
            1.选择所在文件目录;
            2.输入需要批量修改的文件名并提交;
            3.输入变更后的文件名;
            4.提交进行批量修改。    
            ''',
            size=(330, 200), style=wx.TE_MULTILINE) 
        self.FilePath = ''
        self.OldText = ''
        self.NewText = ''
#########################布局:##############################
        MainSizer = wx.BoxSizer(wx.VERTICAL)
        B1 = wx.StaticBox(panel,-1,u'输入文件夹地址：')
        BOX1 = wx.StaticBoxSizer(B1,wx.VERTICAL)
        OpenSizer = wx.GridBagSizer(hgap=10,vgap=10)
        OpenSizer.Add(self.Open,pos=(0,0))
        OpenSizer.Add(self.OpenButton,pos=(0,1),span=(1,2),flag=wx.EXPAND)
        BOX1.Add(OpenSizer)

        B2 = wx.StaticBox(panel,-1,u'查找和替换')
        BOX2 = wx.StaticBoxSizer(B2,wx.VERTICAL)
        FindSizer = wx.GridBagSizer(hgap=10,vgap=10)
        FindSizer.Add(self.OldName,pos=(0,0))
        FindSizer.Add(self.FindButton,pos=(0,1))
        FindSizer.Add(self.NewName,pos=(1,0))
        FindSizer.Add(self.ModButton,pos=(1,1))
        BOX2.Add(FindSizer)

        MainSizer.Add(BOX1,flag=wx.ALIGN_CENTER)
        MainSizer.Add(BOX2,flag=wx.ALIGN_CENTER)
        MainSizer.Add(self.cmd,flag=wx.ALIGN_CENTER|wx.SHAPED)
        panel.SetSizer(MainSizer)
        MainSizer.Fit(self)
############################################################

    def OpenFile(self,evt):
        #取得所在文件目录
        dialog = wx.DirDialog(None, u'选择所在文件目录',
          style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.FilePath = dialog.GetPath()
            self.Open.SetValue(self.FilePath)
            self.cmd.SetValue(u'您所选择的文件夹目录是：'+self.FilePath)
        dialog.Destroy()
    
    def FindFile(self,evt): 
        #查询文件
        self.OldText = self.OldName.GetValue().decode('utf-8')
        if self.OldText:
            self.cmd.SetValue(u'您所希望更改的文件名称是：'+self.OldText)
        else:
            self.cmd.SetValue(u'请输入您所希望修改的文件名')
    
    def ModFile(self,evt):
        #替换文件
        if self.OldText and self.FilePath:
            self.NewText = self.NewName.GetValue().decode('utf-8')
            self.run(self.FilePath,self.OldText,self.NewText)
            self.cmd.SetValue(u"修改完毕,已经将文件名称中的 \""+self.OldText+"\" 部分修改为 \""+self.NewText+"\"")
        else:
            self.cmd.SetValue(u'请先选择文件夹目录\n\r并且输入您所希望修改的文件名\n\r后再提交修改')
    
    def run(self,filepath,oldname,newname):
        #查询和替换的方法
        try:
            l = os.listdir(filepath)
            for i in l:
                name = os.path.splitext(i)[0]
                if name.find(oldname) > -1:
                    length = len(oldname)
                    inx = name.index(oldname)
                    theoldname = filepath+'\\'+i
                    thenewname = filepath+'\\'+name[:inx]+newname+name[inx+length:]+os.path.splitext(i)[1]
                    os.rename(theoldname,thenewname)
        except Exception:
            self.cmd.SetValue(u"修改失败")
            
app = wx.App()
Frame().Show()
app.MainLoop()
