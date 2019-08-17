#__author: yaomingxi
#__date: 2019-08-03
from selenium_20190727.test_day_01.mewDay_01.day_01_class import MyClass



class MyClass2(MyClass):

    def add2(self):
        return self.b + self.a


print(MyClass2(8,6).add2())


import time

print(time.ctime())

from time import ctime

print(ctime())

from time import *

#当前时间
print(ctime())
#睡眠3秒
#sleep(3)

from time import sleep as s
print("开始休眠了，狗狗狗！！！")
#睡眠3秒
s(3)
print("睡眠了3秒钟。呼呼呼。。。")

help(time)


