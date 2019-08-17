#__author: yaomingxi
#__date: 2019-08-04

from selenium import webdriver
import time

dr= webdriver.Chrome()
url = 'https://www.baidu.com/'
dr.get(url)

dr.set_window_size(700,800)

kw = dr.find_element_by_id("kw").send_keys("selenium")
su = dr.find_element_by_id("su").click()
time.sleep(3)
js = "window.scrollTo(700,750);"
dr.execute_script(js)


time.sleep(3)







getcookie = dr.get_cookies()
#print(getcookie)

print("=============================================================")

for ck in getcookie:
    print(ck)

print("=============================================================")

dr.add_cookie({'name': 'key-lao', 'value': 'value-mao'})

for ck1 in dr.get_cookies():
#for ck1 in getcookie:
    print("%s --> %s" % (ck1['name'], ck1['value']))

time.sleep(3)
dr.quit()