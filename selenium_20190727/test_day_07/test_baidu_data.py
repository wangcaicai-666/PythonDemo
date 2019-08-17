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

    def baidu_search(self, search_key):

        self.dr.get(self.bd_url)
        self.dr.find_element_by_id("kw").clear()
        self.dr.find_element_by_id("kw").send_keys(search_key)
        self.dr.find_element_by_id("su").click()
        sleep(3)

    def test_search_01(self):
        with codecs.open('/Users/yaomingxi/Desktop/baidu_data.csv','r','utf_8_sig') as f:
            data = csv.reader(f)
            for line in islice(data,1,None):
                search_key = line[1]
                self.baidu_search(search_key)

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.dr.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)