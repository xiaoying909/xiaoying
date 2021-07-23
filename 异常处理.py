# flie_name = input("请输入需要打开的文件:")
# f = open(flie_name)
# print("文件的内容是：")
# for each_line in f:
#     print(each_line)
#try 语句的应用
try:
    f = open("我为什么是一个文件.txt")
    print(f.read())
    f.close()
except OSError:
     print("文件出错了T_T")
#丰富的else语句  with语句使用则不用手动关闭文件
