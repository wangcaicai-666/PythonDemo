#__author: yaomingxi
#__date: 2019-08-04


from selenium import webdriver
from selenium.webdriver import ActionChains
import time


dr = webdriver.Chrome()
dr.maximize_window()
dr.get("https://www.baidu.com/")
time.sleep(2)

#定位到要悬停的元素
#st = dr.find_element_by_link_text("设置")
#time.sleep(2)
#对元素执行悬停操作
#ActionChains(dr)  把浏览器驱动作为参数传入
#ActionChains(dr).move_to_element(st).perform()  #perform提交所有ActionChains类中存储对行为

#鼠标右点击
kw = dr.find_element_by_id("kw")
ActionChains(dr).context_click(kw) .perform()

#鼠标拖动
#ActionChains(dr).drag_and_drop(kw) .perform()
time.sleep(3)

dr.quit()


