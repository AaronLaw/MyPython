#coding:utf-8
'''
五局三胜制石头剪刀布
'''
from random import choice
a="stone"
b="scissor"
c="cloth"

option = [a,b,c,a]

flag = True
count1 = 0
count2 = 0

while flag:
    computer = choice(option[0:3])
    print u"现在比分 %d：%d"%(count1,count2)
    people = raw_input("请输入：stone(石头)、scissor(剪刀)、cloth(布)！\n").strip()
    print people
    if not people in option:
        print u"输入错误请重新输入"
        continue
    print u"电脑输入：%s"%computer
    if computer == people:
        print u"平手，再来一回合。"
    elif option[option.index(people)+1] == computer:
        count1 += 1
        if count1 == 3:
            print u"玩家获胜。"
            break
        print u'玩家加1分！玩家现在已经获得%d分！'%count1

    else:
        count2 += 1
        if count2 == 3:
            print u"电脑获胜。"
            break
        print u'电脑加1分！电脑现在已经获得%d分！'%(count2)
