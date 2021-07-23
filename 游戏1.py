"""
#用python设计的第一个游戏
"""
import random
b = int(random.randint(0,1000))
while True:
    a = int(input("请猜一下我心中想的数字（0-1000)!："))
    if a > b:
        print("该数字偏大喔！")
    elif a < b:
        print("该数字偏小喔！")
    elif a == b: 
        print("恭喜你答对啦！")
        print("奖励你一口 mua~")
        break
    else:
        print()
print("游戏结束！")  

""" 
用python设计的第一个游戏
加上easygui进行改进
"""
import random
import easygui as g
g.msgbox("欢迎进入游戏！")
title = "猜数字小游戏"
msg = "猜一下我心里现在想的数字："
shuzi = random.randint(1,100)
guess = g.integerbox(msg,title,lowerbound=1,upperbound=100)       #输入框  限定一些数据对象
while True:
    if guess == shuzi:
        g.msgbox("哇，你真厉害这都猜对了")
        g.msgbox("奖励你一口 木啊~")
        break
    else:
        if guess > shuzi:
            g.msgbox("大了喔")
        else:
            g.msgbox("小了喔")
        guess = g.integerbox(msg,title,lowerbound=1,upperbound=100)
g.msgbox("游戏结束")
