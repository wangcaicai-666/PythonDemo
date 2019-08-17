#__author: yaomingxi
#__date: 2019-08-10


from xml.dom.minidom import parse
import xml.dom.minidom





#打开xml文件
dom = parse('/Users/yaomingxi/Desktop/config_01.xml')
#得到文档元素对象
root = dom.documentElement
#获取（一组）标签
tag_name = root.getElementsByTagName('os')


print(tag_name[0].fristChild.data)
print(tag_name[1].fristChild.data)
print(tag_name[2].fristChild.data)
