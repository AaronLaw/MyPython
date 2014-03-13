#coding:utf-8
coins = [25,10,5,1]
try:
    money = int(input(u"请输入金额："))
    if money < 300:
        for i in coins:
            if money >= i:
                print("可兑换%s枚%s美分硬币。"%((money//i),i))
                money %= i
    else:
        print u"输入错误，请输入小于100的整数。"
except:
    print u"输入错误，请输入小于100的整数。"
