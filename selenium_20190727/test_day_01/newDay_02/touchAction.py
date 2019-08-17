#__author: yaomingxi
#__date: 2019-08-04

from time import sleep as sl
from selenium import webdriver

dr = webdriver.Chrome()
dr.get('http://www.jq22.com/yanshi4976')
sl(2)
dr.switch_to.frame("iframe")
dr.find_element_by_id("appDate").click()

sl(3)
dwwos = dr.find_element_by_class_name("dwwo")
year = dwwos[0]
month = dwwos[1]
day = dwwos[2]


action = webdriver.TouchActions(dr)
action.scroll_from_element(year, 0, 5).perform()
action.scroll_from_element(month, 0, 30).perform()
action.scroll_from_element(day, 0, 30).perform()


sl(5)
dr.quit()