# x = "12321"
# print("是回文数" )if x == x[::-1] else print("不是回文数")
# if x == x[::-1]:
#     print()
# else:
#     print()
               #    打印的值   if    条件     else 或elif    打印的值
x = "i love you"
x = x.title()
# print(x)
a="有内鬼，停止交易"
a = a.center(20,"爬")
print(a)
b = "上海自来水来自海上"
b = b.count("海",0,5)          #count(sub,[,start[,end]])     后两个数值用来指定开始和结束的位置
print(b)
import keyword
d=keyword.iskeyword("py")             #   调用keywoed判断 字符是否为系统的可调字符串      判定  py   fals
print(d)
words = "www.iloveyou.com"
o=words.partition(".")              #  使用pratition的分割符 将其从左到右找到分割符后分割为二 则变为 www  .    iloveyou.com   
l=words.rpartition(".")     #  rpartition则是从右到左去寻找分割符从而分割
print(o)
print(l)
fenge = "小影是笨蛋,大鹅是笨蛋,好多笨蛋,笨蛋,有人喜欢笨蛋嘛"
c=fenge.split(",")      #  split() 可以定义切多少次,从而分割  这里面的逗号可以是任意标点符号数字文字
e = fenge.split(",",1)   #例子
print(e)
z = fenge.splitlines(True)   # splitlines()    直接将里面的换行符归一，并不代表具备分割功能
print(z)
f="22"
f=f.join(("c","b231"))    #   join(a,b)   是a和b的拼接    原本有值的话则是拼成   a + 值 +b
print(f)
yaer = 2010
A = "小影 {}"
B = "1+2={},2的平方是{},3的立方是{}"
A=A.format(yaer)        #   format  格式化字符串      使其可以识别，使用{}替换
B=B.format(1+2,2*2,3**3)    #format   的基本用法   在  {}里可以写上数字，对应想要输出的值
#   format(name=xxx,age=18)  可在{name}，{age}s实现，对应所应的元素和参数
print(B)
C = "{:*>10}{:*<10}"       #这里的*可以替换为任意字符！
C=C.format("好大鹅","好大鹅")    
print(C)
