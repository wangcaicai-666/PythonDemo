#__author: yaomingxi
#__date: 2019-08-10

import unittest

class TestAssert(unittest.TestCase):

    def setUp(self):
        print("start...")

    def tearDown(self):
        print("end...")

    def test_equal(self):
        self.assertEqual(2+2, 4)
        self.assertEqual('python','python')
        self.assertNotEqual('pycharam','pychram')

    def test_in(self):
        self.assertIn('hello','hello world')
        self.assertNotIn('hl', 'hello')
        self.assertNotIn('123','456')
        self.assertIn('123','123')

    def test_true(self):
        self.assertTrue(1+1, 2)
        self.assertFalse(False)

    def test_none(self):
        self.assertIsNone()
        self.assertIsNotNone(123)


if __name__ == '__main__':

    unittest.main()