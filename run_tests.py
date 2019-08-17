#__author: yaomingxi
#__date: 2019-08-10

import unittest
from HTMLTestRunner import HTMLTestRunner
from time import time,strftime
import yagmail

#定义测试用例都目录为当前目录中的test_day_06/目录

test_dir = "/Users/yaomingxi/Desktop/test_baidu_csv/test_baidu_data_02/"

suits = unittest.defaultTestLoader.discover(test_dir, pattern='test_baidu_data_02*.py')

def send_mail(html_report):

    yag = yagmail.SMTP( user="huatianxidi14@126.com", password="QpSkCn4.6?8'gun", host='smtp.126.com' )

    contens = [
        'The younger brother wrote a simple code for sending a python email, but it is OK when it is sent to himself, but if it is sent to other mailboxes, there will be problems. Please trouble the big god to see where it is, thank you!']

    yag.send( ['512321751@qq.com', 'huatianxidi14@126.com'], 'subject', contens, html_report )




if __name__ == '__main__':

    # 使用当前添加文件名
    now_time = strftime("%Y-%m-%d %H-%M-%S")
    html_report = '/Users/yaomingxi/Desktop/test_baidu_csv/test_baidu_data_02/baidu_test_'+now_time+'.html'
    fp = open(html_report,'wb')

    #使用时间戳添加文件名
    #fp = open('/Users/yaomingxi/Desktop/baidu_test_'+str(int(time()))+'.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title ="百度搜索_数据驱动_03_测试报告", description="运行环境：MacBook Pro, Chrome 浏览器")
    runner.run(suits)
    fp.close()

    send_mail(html_report)



