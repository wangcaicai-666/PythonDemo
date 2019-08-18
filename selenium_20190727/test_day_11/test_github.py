#__author: yaomingxi
#__date: 2019-08-18


from selenium import webdriver
import time
import unittest
import pytest


class TestGitHub(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Chrome()
        cls.bd_url = 'https:www.baidu.com/'
        cls.dr.maximize_window()
        cls.dr.get(cls.bd_url)

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.dr.quit()


    def search_baidu(self,search_key):

        self.dr.get(self.bd_url)
        self.dr.find_element_by_id("kw").clear()
        self.dr.find_element_by_id("kw").send_keys(search_key)
        self.dr.find_element_by_id("su").click()
        time.sleep(1)

    def test_open_baidu(self):

        search_key = 'selenium'
        self.search_baidu(search_key)
        time.sleep(2)
        title = self.dr.title
        self.assertEqual(title,search_key+"_百度搜索")
        print("获取到title ："+title)


if __name__ == '__main__':
    unittest.main(verbosity=2)