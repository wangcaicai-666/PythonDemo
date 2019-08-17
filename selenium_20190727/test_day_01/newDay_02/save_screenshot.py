#__author: yaomingxi
#__date: 2019-08-04

from selenium import webdriver
from time import sleep,time

a = str(int(time()))

dr = webdriver.Chrome()
dr.get('https://www.baidu.com')
dr.maximize_window()

sleep(1)
kw = dr.find_element_by_id("kw").send_keys("selenium 京东商城")
su = dr.find_element_by_id("su").click()

sleep(3)
dr.save_screenshot("/Users/yaomingxi/Desktop/"+a+".png")


sleep(3)
dr.quit()

