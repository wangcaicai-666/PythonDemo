#__author: yaomingxi
#__date: 2019-08-03

from selenium import webdriver as dr
from time import sleep as sl

from selenium.webdriver.common.by import By


dr = dr.Safari()
dr.maximize_window()

url = 'https://www.baidu.com/'
dr.get(url)

#wb = dr.find_element_by_xpath('/html/body/div/div/div/div/div/form/span/input')
#wb.send_keys('selenium webdriver')

sl(1)
#cl = dr.find_element_by_link_text('新闻')

#cl = dr.find_element_by_xpath('/html/body/div/div/div/div[3]/a[1]')
#cl.click()
#利用元素属性定位
#cl1 = dr.find_element_by_xpath("//input[@id='kw']")
#cl1.send_keys('selenium webdriver')

#不指定标签名，可以用*号代替
#cl2 = dr.find_element_by_xpath("//*[@name='tj_trnews']")
#cl2.click()

#层级于属性组合
#cl3 = dr.find_element_by_xpath("//div[@id='u1']/a[1]")
#cl3.click()

#逻辑运算符
#cl4 = dr.find_element_by_xpath("//a[@class='mnav' and @name='tj_trnews']")
#cl4.click()

#contains用于匹配一个属性中包含的字符串
#cl5 = dr.find_element_by_xpath("//span[contains(@class='bg s_ipt_wr quickdelete-wrap')]/input")
#cl5.send_keys('京东商城')


#使用text()方法
#cl6 = dr.find_element_by_xpath("//a[cintains(text(),'新闻')]")
#cl6.click()



#通过css定位元素，,代表使用class定位
#cl7 = dr.find_element_by_css_selector(".s_ipt")
#cl7.send_keys("京东商城")
#cl8 = dr.find_element_by_css_selector(".s_btn")
#cl8.click()


#通过css定位元素，#代表使用ID定位
#cl9 = dr.find_element_by_css_selector("#kw")
#cl9.send_keys("京东商城")
#cl10 = dr.find_element_by_css_selector("#su")
#cl10.click()

#使用标签定位，input代表使用标签定位，span代表父级下的所有标签
#cl11 = dr.find_element_by_css_selector("span > input")
#cl11.send_keys("京东商城")
#cl12 = dr.find_element_by_css_selector("span > input")
#cl12.click()


#通过属性定位
#cl13 = dr.find_element_by_css_selector("[autocomplete=off]")
#cl13.send_keys("京东商城")
#cl14 = dr.find_element_by_css_selector("[value=百度一下]")
#cl14.click()

#组合定位
#cl15 = dr.find_element_by_css_selector("form.fm > span > input.s_ipt")
#cl15.send_keys("selenium webdriver")
#cl16 = dr.find_element_by_css_selector("form.fm > span > input.s_btn")
#cl16.click()


'''
#用By定位元素
cl17 = dr.find_element(By.ID,"kw")
#获取输入框尺寸
print(cl17.size)
cl17.send_keys("京东商城")
sl(1)
#清空输入框
cl17.clear()
cl17.send_keys("京东")
cl18 = dr.find_element(By.CLASS_NAME,"s_btn")
#点击百度一下
cl18.click()
#获取当前页面的handle
dangqianhandle = dr.current_window_handle
sl(3)
#点击京东商城
cl19 = dr.find_element(By.PARTIAL_LINK_TEXT,"官网 多快好省 只为品质生活")
cl19.click()

#获取所有页面handle
sl(3)
all_handles = dr.window_handles

for handle in all_handles:

    if handle != dangqianhandle:
        dr.switch_to.window(handle)  #控制权转交

        dr.implicitly_wait(3)

        tl = dr.find_element_by_class_name("user_tip")
        #t2 = dr.find_element_by_link_text('Hi~欢迎逛京东！')
        print("result: "+tl.text)   #获取元素文本
        #print("result:"+t2.text)
        print("result: "+tl.get_attribute('class'))  #获取元素的属性
        #print("result: "+tl.is_displayed())  #判断元素是否可见     失败
        print("result: "+dr.title)   #获取页面title
        print("result: "+dr.current_url)   #获取页面地址

'''

sl(2)
dr.quit()