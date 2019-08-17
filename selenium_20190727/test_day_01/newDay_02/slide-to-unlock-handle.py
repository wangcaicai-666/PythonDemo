#__author: yaomingxi
#__date: 2019-08-04

from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
import pyautogui

dr = webdriver.Chrome()
dr.get("https://www.helloweba.com/demo/2017/unlock/")
dr.maximize_window()

#定位滑动块
slider = dr.find_element_by_class_name("slide-to-unlock-handle")
action = ActionChains(dr)
action.click_and_hold(slider).perform()

for index in range(200):
    try:
        action.move_by_offset(2,0).perform()
    except UnexpectedAlertPresentException:
        break
    sleep(1)
    action.reset_actions()
    sleep(0.1)

#打印警告框提示
success_text = dr.switch_to.alert.text
print(success_text)
pyautogui.keyDown('enter')


sleep(3)
dr.quit()