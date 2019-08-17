#__author: yaomingxi
#__date: 2019-08-10
import unittest


#在模块开始时执行
def setUpModule():
    print("test module start  >>>>>>>>>>>>>>>>>>>")

#在模块结束时执行
def tearDownModule():
    print("test module end >>>>>>>>>>>>>>>>>>>>")


class MyTest(unittest.TestCase):

    # 在类开始时执行
    @classmethod
    def setUpClass(cls): #cls于self没有本质区别，都表示方法都第一个参数
        print("test class start >>>>>>>>>>>")

    # 在类结束时执行
    @classmethod
    def tearDownClass(cls): #cls于self没有本质区别，都表示方法都第一个参数
        print("test class end  >>>>>>>>>>>>")

    #在测试用例开始时执行
    def setUp(self):
        print("test case start >>>>>>>>>>>>")

    #在测试用例结束时执行
    def tearDown(self):
        print("test case end >>>>>>>>>>>>>>")

    def test_case1(self):
        print("test case1")

    def test_case2(self):
        print("test case2")


if __name__ == '__main__':
    unittest.main()





'''
test module start  >>>>>>>>>>>>>>>>>>>
test class start >>>>>>>>>>>
test case start >>>>>>>>>>>>
test case1
test case end >>>>>>>>>>>>>>
.test case start >>>>>>>>>>>>
test case2
test case end >>>>>>>>>>>>>>
.test class end  >>>>>>>>>>>>
test module end >>>>>>>>>>>>>>>>>>>>
    
'''