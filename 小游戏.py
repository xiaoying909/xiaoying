# 小鸡啄米
import random
# 分数
score = 0
# 游戏提示
print("WASD魏翊东方式'+'代表你当前的位置；'*'代表目标位置；'+'quit退出游戏！")
print("游戏开始！！！！")
userX = 0
userY = 0
targetX = random.randint(0,9)
targetY = random.randint(0,9)
while True:
    for one in range(0,10):
        xz=""
        outStr=""
        for two in range(0,10):
            if userX == targetX and userY == targetY:
                targetX = random.randint(0,9)
                targetY = random.randint(0,9)
                score += 1
                print("当前分数:%d"%(score))
                if userX == one and targetY == two:
                    xz="+"
                elif targetX == one and targetY == two:
                    xz="*"
                else :
                    xz = "-"
                    outStr += xz
                    print(outStr)
                    move = input("请移动或者退出：").upper()
                    if move == "OUIT":
                        break
                    elif move == "S" and userX < 9:
                        userX += 1
                    elif move == "W" and userX > 0:
                        userX -= 1
                    elif move == "D" and userY < 9:
                        userY += 1
                    elif move == "A" and userY > 0:
                        userY -= 1
                        print("游戏结束，最终得分:{}".format(score))

