#__author: yaomingxi
#__date: 2019-08-08

#计算器类
class Calculator:

    #初始化两个数
    def __init__(self,a, b):
        self.a = int(a)
        self.b = int(b)

    #加法
    def add(self):
        return self.a + self.b

    #减法
    def sub(self):
        return self.a - self.b

    #乘法
    def mul(self):
        return self.a * self.b

    #除法
    def div(self):
        return self.a / self.b
