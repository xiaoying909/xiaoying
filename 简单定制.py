import time as t
class Mytimer():
    def __init__(self):
        self.unit = ['年','月','天','小时','分钟','秒']
        self.prompt = "未开始计时"
        self.lasted = []
        self.bengin = 0
        self.end = 0
    def __str__(self):
        return self.prompt

    __repr__ = __str__
    def __add__(self,other):
        prompt = "总共运行了"
        result = []
        for index  in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])
        return prompt
    #开始计时
    def start(self):
        self.bengin = t.localtime()
        self.prompt = "提示请先调用stop()停止计时！"
        print("计时开始。。。")
    #计时结束
    def stop(self):
        if not self.bengin:
            print("提示：请先调用start（）进行计时！")
        else:
            self.end = t.localtime()
            self._calc()
            print("计时停止!")
    #内部方法，计算运行时间
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.bengin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index]) + self.unit[index])
    #为下一轮计时初始化参量
        self.begin = 0
        self.end = 0
t1 = Mytimer()
t1.start()
t1.stop()
print(t1)
t2 = Mytimer()
t2.start()
t2.stop()
print(t2)
print(t1+t2)