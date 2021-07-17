"""
输入“好大鹅”之后进行“笨比”的200次循环
并且判断输入其他则为“清重新输入”
"""
name=input("请输入：")
a=1
while a<=200:
    if  name == "好大鹅":
        print("笨比",end="  ")  
        a=a+1 
    else:
        a=201
        print("请重新输入")
    
print=(name)