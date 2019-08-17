#__author: yaomingxi
#__date: 2019-08-05

#from selenium import webdriver
#from time import sleep,time
from module import Mail


'''
driver = webdriver.Chrome()
driver.maximize_window()
url = "https://mail.qq.com"
driver.get(url)


sleep(3)
driver.find_element_by_id("qqLoginTab").click()
sleep(1)
driver.switch_to.frame("login_frame")
sleep(1)
driver.find_element_by_id("switcher_plogin").click()
sleep(2)
driver.find_element_by_name("u").clear()
driver.find_element_by_name("u").send_keys("546647817@qq.com")
driver.find_element_by_name("p").clear()
driver.find_element_by_name("p").send_keys("3856018ccc")
sleep(2)
driver.find_element_by_id("login_button").click()

sleep(5)
self.driver.find_element_by_link_text("退出").click()



'''

mail = Mail()

mail.login("546647817@qq.com", "3856018ccc")
mail.logout()

