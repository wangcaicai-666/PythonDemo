#__author: yaomingxi
#__date: 2019-08-03

def say_hello(name = None):
    if name is None:
        raise NameError('"name" cannot be empty')
    else:
        print("hello, %s" %name)


#传name参数
say_hello('lao mao')

#不传参数
say_hello()#抛出异常

'''

Traceback (most recent call last):
  File "/Users/yaomingxi/PycharmProjects/untitled/selenium_20190727/test_day_01/newDay_02/raiseError.py", line 15, in <module>
    say_hello()#抛出异常
  File "/Users/yaomingxi/PycharmProjects/untitled/selenium_20190727/test_day_01/newDay_02/raiseError.py", line 6, in say_hello
    raise NameError('"name" cannot be empty')
NameError: "name" cannot be empty


'''