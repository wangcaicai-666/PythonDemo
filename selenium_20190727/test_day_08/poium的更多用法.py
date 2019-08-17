#__author: yaomingxi
#__date: 2019-08-12

from poium import Page,PageElement


#poium支持8种定位方式
class SomePage(Page):

    elm_id = PageElement(id_='id')
    elm_name = PageElement(name='name')
    elm_class = PageElement(class_name='class')
    elm_tag = PageElement(tag='inpurt')
    elm_link_text = PageElement(link_text='link')
    elm_partial = PageElement(partial_linl_text='par_link')
    elm_xpath = PageElement(xpath='//*[@id="kw"]')
    elm_css = PageElement(css='#id')

#通过timeout参数可设置元素超时时间，默认为10s
class BaiduPage(Page):
    search_input = PageElement(id_='kw', timeout=5)
    search_button = PageElement(id_='su',timeout=30)


#设置元素描述  注释定义的元素  describe参数

class Login(Page):
    """
    登录
    """
    username = PageElement(css='#loginAccount',describe="用户名")
    password = PageElement(css='#loginPwd',describe="密码")


#定位一组元素

class ResultPage(Page):
    search_result = PageElements(xpath="//div/h3/a")



