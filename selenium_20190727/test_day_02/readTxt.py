#__author: yaomingxi
#__date: 2019-08-05

#读取文件

with(open("/Users/yaomingxi/Desktop/user_info.rtf", "r")) as user_file:
    data = user_file.readlines()

#格式化处理

users = []
for line in data:
    user = line[:-1].split(":")
    users.append(user)


#打印users二维数组
print(users)

from module import Mail

mail = Mail()

mail.login(users[7], users[7])
mail.logout()

