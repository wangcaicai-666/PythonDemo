#__author: yaomingxi
#__date: 2019-08-04

from selenium import webdriver
from time import sleep as sl


dr = webdriver.Chrome()
url = 'http://videojs.com/'
dr.get(url)
sl(1)

vd = dr.find_element_by_id("preview-player_html5_api")

#返回播放文件地址
url2 = dr.execute_script("return arguments[0].currentSrc;", vd)
print(url2)

#播放视频
print("start")
dr.execute_script("arguments[0].play()", vd)

#播放15s
sl(15)

#暂停播放
print("stop")
dr.execute_script("arguments[0].pause()", vd)





sl(5)
dr.quit()
