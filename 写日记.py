import time
now = time.strftime("%Y-%m-%d %H:%M:%S")
text = input("请输入今天的心情：")
with open("日记.txt","a",encoding="utf8") as f:# w   是写入，并清空   a  追加
    f.write(now+"\n")
    f.write(text+"\n")
    f.write("--------------------------\n")
    
