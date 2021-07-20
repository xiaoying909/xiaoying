""" 
用python设计的第一个游戏
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