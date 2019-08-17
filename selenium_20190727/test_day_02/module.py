# __author: yaomingxi
# __date: 2019-08-05

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
url = "https://mail.qq.com"
driver.get(url)

class Mail:

    '''
    def __int__(self, driver):
        self.driver = driver
    '''

    def login(self, username, password):
        """登录"""
        sleep(2)
        driver.find_element_by_id("qqLoginTab").click()
        sleep(1)
        driver.switch_to.frame("login_frame")
        sleep(1)
        driver.find_element_by_id("switcher_plogin").click()
        sleep(1)
        driver.find_element_by_name("u").clear()
        driver.find_element_by_name("u").send_keys(username)  #546647817@qq.com
        driver.find_element_by_name("p").clear()
        driver.find_element_by_name("p").send_keys(password)  #3856018ccc
        sleep(2)
        driver.find_element_by_id("login_button").click()

        sleep(3)

    def logout(self):
        """退出"""

        sleep(3)
        driver.find_element_by_link_text("退出").click()
        sleep(2)
        driver.quit()
