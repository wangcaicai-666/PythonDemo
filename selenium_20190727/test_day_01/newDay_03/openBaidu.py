#__author: yaomingxi
#__date: 2019-08-04



from selenium import webdriver as dr
from time import sleep as sl

dr =dr.Chrome()
url = 'https://www.baidu.com/'
dr.get(url)