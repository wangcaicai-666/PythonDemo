#__author: yaomingxi
#__date: 2019-08-04

from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from time import sleep as sl

dr = webdriver.Chrome()
dr.maximize_window()
url = "https://www.baidu.com/"
dr.get(url)




ky = dr.find_element_by_id("kw")
ky.send_keys("selenium")
ky.send_keys(Keys.ENTER)



'''
sl(1)
#删除多输入的一个 m
ky.send_keys(Keys.BACK_SPACE)
sl(1)

#键盘全选操作
dr.find_element_by_id("kw").send_keys(Keys.CONTROL,'A')
sl(2)

#键盘复制操作
dr.find_element_by_id("kw").send_keys(Keys.CONTROL,'C')
sl(2)

bk = dr.find_element_by_id("result_logo")
bk.click()
sl(1)

#键盘剪切操作
dr.find_element_by_id("kw").send_keys(Keys.CONTROL,'V')
sl(2)



ky.send_keys(Keys.CONTROL,'a')
sl(1)
ky.send_keys(Keys.CONTROL,'X')
sl(1)
bk = dr.find_element_by_id("result_logo")
bk.click()
sl(1)
ky.send_keys(Keys.CONTROL,'V')


els = dr.find_elements_by_xpath("//div[@id='u1']/a")
print("元素个数： "+str(len(els)))

for i in els:
    print(i.text)

print("===========================================")
sl(3)
gd = dr.find_elements_by_xpath("//div[@class='bdbriwrapper']/a")
print("元素个数： "+str(len(gd)))

for k in gd:
    print(k.text)

sy = dr.find_elements_by_xpath("//p[@id='lh']/a")

print("元素个数："+str(len(sy)))

for j in sy:

    print(j.text)

print("===========================================")
sl(3)
sy2 = dr.find_elements_by_xpath("//p[@id='cp']/a")
print("元素个数："+str(len(sy2)))

for i1 in sy2:

    print(i1.text)
    
'''
sl(1)
sll = dr.find_elements_by_xpath("//div[@class='f13']/a")
#sll = dr.find_elements_by_xpath("//div[@id='1']/h3/a")
print("元素个数："+str(len(sll)))

for i in sll:

    print(i.text)


sl(3)
dr.quit()