#对象 = 属性 ＋ 方法
class Turtle:
    #属性
    color = "green"
    weight = 10
    legs = 4
    shell = True
    mouth = "大嘴"
    #方法
    def climb(self):
        print("我正在努力的向前爬。。。。。")
    def run(self):
        print("我正在飞快的向前爬。。。")
    def bite(self):
        print("咬死你咬死你！")
    def east(self):
        print("有的吃，有的吃W.W")
    def sleep(self):
        print("困了，睡了，晚安zzz")
        
tt = Turtle()
tt.run()
#继承
class MyList(list):
    pass
list2 = MyList()    #继承了列表的一些调用方法
list2.append(1)
list2.append(9)
list2.append(5)
print(list2)
class Ball:     #定义一个ball类
    def setName(self,name):
        self.name = name   #此时self.name  只是一个参数，变量
    def kick(self):         
        print("我叫%s，该死的，谁踢我。。。" % self.name)      #%s   后面则定义的是字符串
a = Ball()
a.setName("球A")
b = Ball()
b.setName("球B")
a.kick()
# class Ball:
#     def __init__(self,name):   默认参数   __init__(self)
#         self.name = name 
import random as r
class Fish:              #定义一个鱼类
    def __init__(self):   
        self.x = r.randint(1,10)        #x的随机坐标
        self.y = r.randint(1,10)        #y的随机坐标
    def move(slef):                     #定义移动的方法
        slef.x -= 1                     #定义移动的方向步数等等
        print("我的位置是：",slef.x,slef.y)    #输出位置
class Goldfish(Fish):                    #继承鱼类
    pass
class Shark(Fish):                       
    def __init__(self):                #   继承父类方法   直接使用super（）函数   简便快捷
        super().__init__()
        self.hungry = True              #定义一个饥饿的参数
    def eat(self):
        if self.hungry:
            print("天天有吃的感觉真好")
            self.hungry = False
        else:
            print("太撑了，吃不下了！")
f = Shark()
f.move()
        
