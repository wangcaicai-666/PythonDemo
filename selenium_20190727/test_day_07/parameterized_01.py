#__author: yaomingxi
#__date: 2019-08-11

import unittest
from time import time,sleep
from selenium import webdriver
from parameterized import parameterized

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.dr.maximize_window()
        cls.dr.implicitly_wait(10)
        cls.bd_url = 'https://www.baidu.com/'

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        cls.dr.quit()

    def baidu_search(self,search_key):
        self.dr.get(self.bd_url)
        self.dr.find_element_by_id("kw").clear()
        self.dr.find_element_by_id("kw").send_keys(search_key)
        self.dr.find_element_by_id("su").click()
        sleep(3)
        
    #
    @parameterized.expand([("cse1","selenium"),("case2","unittest"),("case3","parameterized")])

    def test_search(self,name,search_key):
        self.baidu_search(search_key)
        sleep(3)
        self.assertEqual(self.dr.title, search_key+'_百度搜索')


if __name__ == '__main__':
    unittest.main(verbosity=2)