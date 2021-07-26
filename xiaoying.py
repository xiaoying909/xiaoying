"""
输入“好大鹅”之后进行“笨比”的200次循环
并且判断输入其他则为“清重新输入”
"""
name=input("请输入：")
while True:
    if  name == "好大鹅":
        print("笨比",end="  ")  
        break
    else:
        print("请重新输入")
        break
    
print=(name)