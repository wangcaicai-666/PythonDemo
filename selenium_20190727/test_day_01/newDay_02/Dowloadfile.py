#__author: yaomingxi
#__date: 2019-08-04

from selenium import webdriver
from time import sleep,time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui

dr = webdriver.Chrome()
url = 'https://www.baidu.com/'
dr.get(url)
dr.maximize_window()


sleep(1)
pp = dr.find_element_by_id("kw").send_keys("MacBookPro 壁纸")
ss = dr.find_element_by_id("su").click()
dangqianhandle = dr.current_window_handle

sleep(1)
meizhuowang = dr.find_element_by_xpath("//div[@id='2']/h3/a").click()

all_handles = dr.window_handles

for handle in all_handles:
    if handle != dangqianhandle:
        dr.switch_to.window(handle)



        #for li in range():
         #   li = li+1

        sleep(2)
        dl = dr.find_element_by_xpath("//div[@id='imgid']/div/ul/li[9]/div/a/img")
        dl1 = dr.find_elements_by_xpath("//div[@id='imgid']/div/ul/li")
        print(len(dl1))
        ActionChains(dr).context_click(dl).perform()
        sleep(1)

        pyautogui.typewrite(['down','down','down','down','down','down','down','enter'],'0.05')  # 选中右键菜单中第2个选项
        sleep(1)
        t = time()
        #t1 = str(int(t*1000000))
        t1 = str(int(t))

        pyautogui.typewrite(t1)
        sleep(1)
        pyautogui.keyDown('enter')
        sleep(1)




sleep(5)
dr.quit()