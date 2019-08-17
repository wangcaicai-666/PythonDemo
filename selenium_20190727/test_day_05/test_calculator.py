#__author: yaomingxi
#__date: 2019-08-08

from calculator import Calculator

def test_add():

    c = Calculator(3,8)
    result = c.add()
    print('运算结果为：'+str(result))
    assert result == 11, '加法运算失败！'

def test_sub():

    c = Calculator(17, 9)
    result = c.sub()
    print('运算结果为：'+str(result))
    assert result == 8, '减法运算失败！'


if __name__ == '__main__':
    test_sub()
    test_add()