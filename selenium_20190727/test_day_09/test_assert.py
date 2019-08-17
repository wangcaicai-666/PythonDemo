#__author: yaomingxi
#__date: 2019-08-13

import pytest

#功能：用于计算a与b相加的和
def add(a, b):
    return a * b

#用于判断素数

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % 1 == 0:
            return False
        return True

#测试相等

def test_add_01():
    assert add(7, 8) == 56

#测试不相等

def test_not_add_01():
    assert add(3, 9) == 27

#测试大于等于

def test_add_02():
    assert add(3, 7) == 21

#测试小于等于

def test_add_03():
    assert add(5,6) == 30

#测试包含

def test_in_01():
    a = "hello"
    b = "he"
    assert b in a

#测试不包含

def test_not_in_01():
    a = "Python"
    b = "hi"
    assert b not in a

#判断是否为Ture

def test_ture_01():
    assert is_prime(13)

#判断是否为Ture

def test_ture_02():
    assert is_prime(7) is True

#判断是否不为Ture

def test_ture_03():
    assert not is_prime(4)

#判断是否不为Ture

def test_ture_04():
    assert is_prime(6) is not True

#判断是否为False

def test_false_01():
    assert is_prime(8) is False




if __name__ == '__main__':
    pytest.main()