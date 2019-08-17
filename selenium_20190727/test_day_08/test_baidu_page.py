#__author: yaomingxi
#__date: 2019-08-12
import time
import unittest
from selenium import webdriver
from selenium_20190727.test_day_08.baidu_page import BaiduPage



class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    '''
    def test_baidu_search_case(self):

        page = BaiduPage(self.driver)
        page.open_page()
        page.search_input("selenium")
        page.search_button()
        time.sleep(2)
        self.assertEqual(page.get_title(),"selenium_百度搜索")
        print(page.get_title())
    '''

    def test_baidu_search_case_02(self):

        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com/")
        page.search_input = "selenium"
        page.search_button.click()


    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)