#__author: yaomingxi
#__date: 2019-08-04

from selenium import webdriver
from time import sleep as sl
from selenium.webdriver.support.select import Select

dr = webdriver.Chrome()
url = 'https://www.baidu.com/'
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

sl(2)
dr.quit()