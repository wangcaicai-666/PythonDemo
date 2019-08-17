#__author: yaomingxi
#__date: 2019-07-27


from selenium import webdriver
import time

driver = webdriver.Safari()
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("mac selenium")
driver.find_element_by_id("su").click()
time.sleep(3)
driver.quit()