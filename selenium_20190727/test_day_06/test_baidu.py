#__author: yaomingxi
#__date: 2019-08-10

import unittest
from time import sleep
from selenium import webdriver

class TestBaidu(unittest.TestCase):
    """  百度搜索测试  """

    #在类开始时执行
    @classmethod
    def setUpClass(cls): # cls为第一个参数

        cls.dr = webdriver.Chrome()
        cls.dr.implicitly_wait(10)
        cls.bd_url = 'https://www.baidu.com/'
        cls.dr.maximize_window()

    #封装搜索关键字方法
    def bd_search_key(self,search_key):

        self.dr.implicitly_wait(10)
        self.dr.get(self.bd_url)
        self.dr.find_element_by_id("kw").clear()
        self.dr.find_element_by_id("kw").send_keys(search_key)
        self.dr.find_element_by_id("su").click()

    #输入关键字，获取title并验证
    def test_bd_search_keys_01(self):
        """  搜索关键字: selenium """

        search_key = "selenium"
        self.bd_search_key(search_key)
        sleep(2)
        title = self.dr.title
        print("获取title为 ："+title)
        self.assertEqual(title, search_key+"_百度搜索")

    # 输入关键字，获取title并验证
    def test_bd_search_keys_02(self):
        """  搜索关键字：unittest """

        search_key = "unittest"
        self.bd_search_key(search_key)
        sleep(2)
        title = self.dr.title
        print("获取title为 ："+title)
        self.assertEqual(title, search_key+"_百度搜索")

    #在类结束时执行
    @classmethod
    def tearDownClass(cls): # cls为第一个参数
        sleep(2)
        cls.dr.quit()



if __name__ == '__main__':
    unittest.main()