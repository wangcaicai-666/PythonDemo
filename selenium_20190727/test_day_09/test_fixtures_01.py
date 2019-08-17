#__author: yaomingxi
#__date: 2019-08-13

#功能函数

import pytest

def multiply(a, b):
    return a * b


# ============== Fixtures =================

def setup_module(module):
    print("setup_module  --------------->")

def teardown_module(module):
    print("teardown_module  --------------->")

def setup_function(function):
    print("setup_function  --------------------->")

def teardown_function(function):
    print("teardown_function")

def setup():
    print("setup  ----------------->")

def teardown():
    print("teardown  ---------------->")


# ============  测试用例  ===============

def test_multiply_3_4():

    print("test_multiply_3_4")
    assert multiply(3, 4) == 12

def test_multiply_a_3():

    print("test_multiply_a_3")
    assert multiply('a', 3) == 'aaa'



    '''
        ======================================================================================== test session starts ========================================================================================
    platform darwin -- Python 3.7.3, pytest-5.0.1, py-1.8.0, pluggy-0.12.0
    rootdir: /Users/yaomingxi/PycharmProjects/untitled/selenium_20190727/test_day_09
    plugins: parallel-0.0.9, html-1.22.0, rerunfailures-7.0, metadata-1.8.0
    collected 2 items                                                                                                                                                                                   
    
    test_fixtures_01.py setup_module  --------------->
    setup_function  --------------------->
    setup  ----------------->
    test_multiply_3_4
    .teardown  ---------------->
    teardown_function
    setup_function  --------------------->
    setup  ----------------->
    test_multiply_a_3
    .teardown  ---------------->
    teardown_function
    teardown_module  --------------->
    
    
    ===================================================================================== 2 passed in 0.01 seconds ======================================================================================
        
    '''