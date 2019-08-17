#__author: yaomingxi
#__date: 2019-08-11

import yagmail
yag = yagmail.SMTP(user="huatianxidi14@126.com",password="QpSkCn4.6?8'gun",host='smtp.126.com')

contens = ['The younger brother wrote a simple code for sending a python email, but it is OK when it is sent to himself, but if it is sent to other mailboxes, there will be problems. Please trouble the big god to see where it is, thank you!']

yag.send(['512321751@qq.com','huatianxidi14@126.com'],'subject',contens,['//Users//yaomingxi//Desktop//test_baidu_csv//test_baidu_data_02//baidu_data.csv'])
