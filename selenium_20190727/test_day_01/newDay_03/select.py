#__author: yaomingxi
#__date: 2019-08-04
'''
from selenium import webdriver
from time import sleep as sl
#from selenium.webdriver.support.select import Select

#from selenium_20190727.test_day_01.newDay_02.newDay_03.openBaidu import dr


Select类用于定位<select>标签
select_by_value()通过value值定位下拉选项
select_by_visible_text()通过text值定位下拉选项
select_by_index()根据下拉选项进行索引

dr = webdriver.Chrome()
url = 'https://www.baidu.com'
dr.get(url)

sl(2)
st = dr.find_element_by_link_text("设置")
st.click()
sl(2)
ss = dr.find_element_by_link_text("搜索设置")
ss.click()
sl(2)
xl = dr.find_element_by_id("nr")
Select(xl).select_by_value('20')
sl(2)
Select(xl).select_by_index(0)
sl(2)
Select(xl).select_by_visible_text("每页显示50条")




from selenium import webdriver as dr
from time import sleep as sl

from selenium.webdriver.common.by import By


dr = dr.Safari()
dr.maximize_window()

url = 'https://www.baidu.com/'
dr.get(url)

'''

import time
tt = time.time()
print(int(tt))

#t2 = int(time.mktime(time.strptime('YYYY-MM-DD HH:MM:SS', '%Y-%m-%d %H:%M:%S')))
#print("t2:  "+t2)

t = time.ctime()
print(t)

#time.sleep(3)
#dr.quit()


