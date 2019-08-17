#__author: yaomingxi
#__date: 2019-08-12


from selenium_20190727.test_day_08.base import BasePage

from poium import Page,PageElement

'''
class BaiduPage(BasePage):
    """百度Page层，百度页面封装操作到的元素"""
    url = 'https://www.baidu.com/'

    def search_input(self,search_key):
        self.by_id( "kw" ).clear()
        self.by_id("kw").send_keys(search_key)

    def search_button(self):
        self.by_id("su").click()
'''

class BaiduPage(Page):
    """百度Page层，百度页面封装操作到的元素"""
    search_input = PageElement(id_="kw")
    search_button = PageElement(id_="su")


