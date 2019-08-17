#__author: yaomingxi
#__date: 2019-08-02


#判断  if
'''

a = input(str("请输入一个数字 ："))
b = input(str("请输入一个数字 ："))

if a<b:
    print(a,"小于",b)
elif a>b:
    print(a,"大于",b)
else:
    print(a,"等于",b)
 
'''


for i in 'hello':
    print(i)

hello = ['danan','laomao',123456]

for j in hello:
    print(j)
    
t = 10

for k in range(0,t,2):
    print(k)



for ll in range(1,10):
    for rr in range(1,ll+1):
        print(rr,"*",ll,"=",ll*rr,end='     ')
    print()
    




