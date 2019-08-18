import pytest


#add()函数
def add(a, b):
	return a + b

#测试add函数
def test_add():
	assert add(2, 5) == 8



#本地仓库
#git init  初始化本地仓库本地代码  字体变红
#git add */文件名  提交到本地仓库  字体变绿

#缓存仓库
#git commit -m "first commit"    #提交到缓存仓库  字体变黑


#远程仓库
#git remote add origin https://github.com/wangcaicai-666/PythonDemo.git

#用户名/密码


#提交至远程仓库
#push -u origin master


