#__author: yaomingxi
#__date: 2019-08-11

import unittest
from time import time,sleep
from selenium import webdriver
from ddt import ddt,data,file_data,unpack


@ddt
class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.dr.maximize_window()
        #cls.dr.implicitly_wait(10)
        cls.bd_url = 'https://www.baidu.com/'

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()


    def baidu_search(self, search_key):
        self.dr.get(self.bd_url)
        self.dr.find_element_by_id("kw").clear()
        self.dr.find_element_by_id("kw").send_keys(search_key)
        self.dr.find_element_by_id("su").click()

    #参数化使用方式一
    @data(["case1","selenium"],["case2","ddt"],["case3","python"])
    @unpack
    def test_search_01_list(self,case,search_key):
        print("第一组测试用例：",case,search_key)
        self.baidu_search(search_key)
        sleep(0.7)
        self.assertEqual(self.dr.title,search_key+'_百度搜索')


    #参数化使用方式二
    @data(("case1","selenium"),("case2","ddt"),("case3","python"))
    @unpack
    def test_search_02_tup(self,case,search_key):
        print("第二组测试用例：",case,search_key)
        self.baidu_search(search_key)
        sleep(0.7)
        self.assertEqual(self.dr.title,search_key+"_百度搜索")

    @data({"search_key":"selenium"},{"search_key":"ddt"},{"search_key":"python"})
    @unpack
    def test_search_03_dict(self,search_key):
        print("第三组测试用例：",search_key)
        self.baidu_search(search_key)
        sleep(0.7)
        self.assertEqual(self.dr.title,search_key+"_百度搜索")

if __name__ == "__main__":
    unittest.main( verbosity=2)