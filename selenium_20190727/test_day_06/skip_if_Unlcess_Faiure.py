#__author: yaomingxi
#__date: 2019-08-10

import unittest


@unittest.skip("直接跳过，不测试该测试类")
class MyTest(unittest.TestCase):

    @unittest.skip("直接跳过测试")
    def test_skip(self):
        print("test aaa")

    @unittest.skipIf(4 > 2, "当条件为真时跳过测试")
    def test_skip_if(self):
        print("test bbb")

    @unittest.skipUnless(4 > 2, "当条件为真时执行测试")
    def test_skipUnless(self):
        print("test ccc")

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(2,3)

if __name__ == '__main__':
    unittest.main()