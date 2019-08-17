#__author: yaomingxi
#__date: 2019-08-10
import json

with open('/Users/yaomingxi/Desktop/user_info.json') as f :
    data = f.read()

#u = json.loads(data)
u1 = json.load(data)
print(json.load(u1))




