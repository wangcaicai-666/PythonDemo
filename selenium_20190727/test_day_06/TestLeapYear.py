#__author: yaomingxi
#__date: 2019-08-10

from leap_year import Leapyear
import unittest

class TestLeapYear(unittest.TestCase):

    def setUp(self):
        print("start...")

    def tearDown(self):
        print("end...")

    def test_2000(self):
        ly = Leapyear(2000)
        self.assertEqual(ly.answer(), '2000是闰年！')

    def test_2004(self):
        lp = Leapyear(2004)
        self.assertEqual(lp.answer(),'2004是闰年！')

    def test_2017(self):
        lp = Leapyear(2017)
        self.assertEqual(lp.answer(),'2017不是闰年！')

    def test_2100(self):
        lp = Leapyear(2100)
        self.assertEqual(lp.answer(),'2100不是闰年！')


if  __name__ == '__main__':
    unittest.main()