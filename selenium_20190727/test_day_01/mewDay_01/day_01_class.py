#__author: yaomingxi
#__date: 2019-08-02

#定义类Class

class MyClass:

    def __init__(self,a,b):

        self.a = int(a)
        self.b = int(b)


    def sub(self):

        return self.a - self.b

k = MyClass(9,7)
y = k.sub()
#print(y)

