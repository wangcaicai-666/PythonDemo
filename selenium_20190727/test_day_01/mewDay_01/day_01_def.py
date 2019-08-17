#__author: yaomingxi
#__date: 2019-08-02

def add(a,b):

    c = a+b

    return c


z = add(2,7)
print(z)

def add_1(a=200,b=400):

    c =  a+b
    return c

z1 = add_1()
print(z1)



def add_2(a=200,b=400):

    c =  a+b
    return c

z2 = add_2()
z3 = add_2(9,8)
print(z2)
print(z3)

