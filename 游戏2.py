import easygui as g
import sys

from easygui.boxes.choice_box import choicebox
while 1:
    g.msgbox("嗨！欢迎进入第一个界面小游戏QAQ")   #提示输出框
    msg = "请问你希望在小影工作室学到什么？"     #
    title = "小游戏互动"                         #标题框
    choice = ["谈恋爱","赚钱","搬砖","读书"]    #选择对话框
    choice = g.choicebox(msg,title,choice)
    g.msgbox("你的选择是："+str(choice),"结果")
    msg = "你希望重新开始小游戏吗？"
    title = "请选择"
    if g.ccbox(msg,title):               #选择按钮
        pass
    else:
        sys.exit(0)