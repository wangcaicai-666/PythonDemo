#__author: yaomingxi
#__date: 2019-07-28

from selenium import webdriver as wd

#import tesseract
import tesserocr
#import PIL

import time

dr = wd.Safari()
dr.maximize_window()

url2 = "https://mail.163.com"
dr.get(url2)
search_window = dr.current_window_handle

time.sleep(1)
dc = dr.find_element_by_link_text("注册新帐号")
dc.click()

all_handles = dr.window_handles
time.sleep(1)

for handle in all_handles:
    if handle != search_window:
        dr.switch_to.window(handle)
        print(dr.title)

        time.sleep(1)
        us = dr.find_element_by_id("nameIpt")
        us.send_keys("seleniumTestNo01")

        time.sleep(1)
        pw = dr.find_element_by_id("mainPwdIpt")
        pw.send_keys("9988521666")

        time.sleep(1)
        pw2 = dr.find_element_by_id("mainCfmPwdIpt")
        pw2.send_keys("9988521666")


        time.sleep(2)
        yzm = dr.find_element_by_id("vcodeImg")

        sb = tesserocr.image_to_text(yzm)
        print(sb)

        time.sleep(1)
        ym = dr.find_element_by_id("vcodeIpt")
        ym.send_keys(sb)

        time.sleep(1)
        mb = dr.find_element_by_id("mainMobileIpt")
        mb.send_keys("13918962788")

        time.sleep(1)
        ty = dr.find_element_by_id("mainAcceptIpt")
        ty.click()

        time.sleep(1)
        go = dr.find_element_by_id("mainRegA")
        go.click()

        time.sleep(3)
        cs = dr.find_element_by_class_name("txt-err")
        tx = cs.text

        if tx == "  验证码不正确，请重新填写":
            print("pass" + tx)
        else:
            print("false")


dr.quit()





