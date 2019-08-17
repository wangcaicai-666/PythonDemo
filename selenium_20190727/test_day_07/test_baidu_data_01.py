#__author: yaomingxi
#__date: 2019-08-11

import csv
import codecs
import unittest
from time import time,sleep
from itertools import islice
from selenium import webdriver

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.dr = webdriver.Chrome()
        cls.dr.implicitly_wait(10)
        cls.bd_url = "https://www.baidu.com/"
        cls.dr.get(cls.bd_url)
        cls.dr.maximize_window()

        #打开csv文件
        cls.test_data_list = []
        with codecs.open('/Users/yaomingxi/Desktop/test_baidu_csv/test_baidu_data_02/baidu_data.csv','r','utf_8_sig') as f:
            data = csv.reader(f)
            for line in islice(data,1,None):
                cls.test_data_list.append(line)
                #search_key = line[1]
                #self.baidu_search(search_key)

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.dr.quit()

    def baidu_search(self, search_key):

        self.dr.get(self.bd_url)
        self.dr.find_element_by_id("kw").clear()
        self.dr.find_element_by_id("kw").send_keys(search_key)
        self.dr.find_element_by_id("su").click()
        sleep(3)

    def test_search_01_selenium(self):
        """ 百度搜索：selenium """
        self.baidu_search(self.test_data_list[0][1])

    def test_search_02_unittest(self):
        """ 百度搜索：uunittest """
        self.baidu_search(self.test_data_list[1][1])

    def test_search_03_parameterized(self):
        """ 百度搜索： parameterized """
        self.baidu_search(self.test_data_list[2][1])



if __name__ == '__main__':
    unittest.main(verbosity=2)