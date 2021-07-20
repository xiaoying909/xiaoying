import abc


def hanshu():
    print("123546")
def he(a,b):  
    '计算a+b的方法'              #定义   he()为一个加法函数
    return a+b
print(he(3,4))
def power(x=3,y=2):
    '这个计算x的y次幂的方法 '
    a=x**y
    return a 
print(power(3,9))
# 在方法中可以导入默认参数，当输出无值时便是由默认参数代替
def text(*params):   #   *变量名，则变为了一个收集参数
     print("参数的长度是：",len(params))
     print("第二个参数是：",params[1])
text(1,'小影',5,'abc',6,8.7)    # 此时不是用return返回则无需使用 print 直接text（）
def Narcissus():
    '定义一个寻找水仙花数的方法'
    for each in range(100, 1000):
        temp = each
        sum = 0
        while temp:
            sum = sum + (temp%10) ** 3
            temp = temp // 10  # 注意这里用地板除

        if sum == each:
            print(each, end='\t')

def hello():
    return("hello world!")                #这里用print则是直接输出hello world  当a=hello（）这个方法时则会直接输出，用print（a）
                                         #则不会输出值，但是用return给予返回值后，使用到print（a）即可以输出hello world
a=hello()
print(a)
def back():
    return 1,"xiaoy",2

print(back())
def discounts(price,rate):
    '定义一个打折的方法'
    final_price = price*rate        #在函数里定义的参数，称之为局部变量   在全局中是找不到的。
    return final_price
old_price = float(input("请输入价格："))
rate = float(input("请输入折扣："))
new_price=discounts(old_price,rate)
print("打折后的价格是",new_price)


