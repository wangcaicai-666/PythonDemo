#__author: yaomingxi
#__date: 2019-08-02

list_1 = [1,2,3,'a','b','c']

print(list_1)

z = 1
for i in list_1:

    print("序号",z,"_",i)
    z = z+1

#取第一个值
print(list_1[0])

#取第四个值
print(list_1[3])

#取最后一个值
print(list_1[-1])

#修改列表值

list_1[4] = 'E'
#list_1[5] = 'c'
print(list_1)

#向列表添加值(末尾)
list_1.append('G')
print(list_1)

#删除列表指定值
list_1.pop(1)
print(list_1)



#tuple

tup1 = ('a','b','t',1,2,9)
print(tup1)

print(tup1[0])
print(tup1[3])
print(tup1[-1])

print(tup1[1:3])
print(tup1[0:1])

#连接元组

tup2 = (9,8,7,2,4,'l','G')

tup3 = tup1 + tup2
print(tup3)


tup4 = 'da nan    '
print(tup4 * 5)


list_1.append('Cc')
tup2.append('KK')

#元组是不可变的
#列表可以编辑

#AttributeError: 'tuple' object has no attribute 'append'




