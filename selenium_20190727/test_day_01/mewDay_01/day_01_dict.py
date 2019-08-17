#__author: yaomingxi
#__date: 2019-08-02


dicts = {"danan":"25","laomao":"0.5","macbookpro":"0.5"}
print(dicts.keys())
print(dicts.values())

#向字典中添加键值对

dicts['book'] = 'python'
print(dicts)

for k,v in dicts.items():
    print("dicts keys is %r"%k)
    print("dicts valuesis %r"%v)

dicts.pop('book')
print(dicts)

print(dicts.items())