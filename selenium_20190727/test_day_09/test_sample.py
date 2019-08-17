#__author: yaomingxi
#__date: 2019-08-13

import pytest

def inc(x):
    return x + 1
def test_answer():
    assert inc(3) == 5

if __name__ == '__main__':
    pytest.main()