#coding:utf-8
'''编码问题.py'''

u = u'中文' #显示指定unicode类型对象u
str0 = u.encode('gb2312') #以gb2312编码对unicode对像进行编码
str1 = u.encode('gbk') #以gbk编码对unicode对像进行编码
str2 = u.encode('utf-8') #以utf-8编码对unicode对像进行编码
u1 = str0.decode('gb2312')#以gb2312编码对字符串str进行解码，以获取unicode
u2 = str2.decode('utf-8')#如果以utf-8的编码对str进行解码得到的结果，将无法还原原来的unicode类型
u3 = str1.decode('gbk')#以gbk进行解码

print str0,type(str0)
print str1,type(str1)
print str2,type(str2)
print u1,type(u1)
print u2,type(u2)
print u3,type(u3)

'''
>>> 
中文 <type 'str'>
中文 <type 'str'>
中文 <type 'str'>
中文 <type 'unicode'>
中文 <type 'unicode'>
中文 <type 'unicode'>
>>> 
'''
