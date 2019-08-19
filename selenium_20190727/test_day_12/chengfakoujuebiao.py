# -*- coding: UTF-8 -*-
#__author: yaomingxi
#__date: 2019-08-19


import pytest

for i in range(1,10):
    for k in range(1,i+1):
        print(k,'*',i,'=',k*i, end='   ')
    print()