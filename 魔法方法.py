class  Rectangle:
    def __init__(self,x,y):     #此时需要传入两参数 x,y  所以有需求才会使用__init__   根据需求来使用
        #一但使用Rectangle类会自动调用__init__方法
        self.x = x
        self.y =y
    def getPeri(self):
        return (self.x + self.y) *2
    def getArea(self):
        return self.x *self.y
rect = Rectangle(3,4)
print(rect.getArea())
class CapStr(str):
    def __new__(cls,string):
        string = string.upper()
        return str.__new__(cls,string)
a = CapStr("I love you")
print(a)
class New_int(int):
    def __add__(self,other):
        return int.__sub__(self,other)   #前提是+后实际运行为-  
    def __sub__(self, other):
        return int.__add__(self,other)  #前提是-后实际运行为+
b = New_int(3)
c = New_int(5)
print(c+b)