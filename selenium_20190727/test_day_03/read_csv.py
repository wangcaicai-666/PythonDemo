# __author: yaomingxi
# __date: 2019-08-06

import csv
import codecs
from itertools import islice
from time import sleep
from selenium_20190727.test_day_02.module import Mail

data = csv.reader(codecs.open("/Users/yaomingxi/Desktop/user_info.csv", "r", "utf_8_sig"))
# users = []

for line in islice(data, 1, None):
    # users.append(line)
    print(line)
    print(line[0])
    print(line[1])
# print(users)


mail = Mail()

mail.login(line[0], line[1])
mail.logout()
