#__author: yaomingxi
#__date: 2019-07-30


import tesserocr
from PIL import Image

'''
image = Image.open("/Users/yaomingxi/Desktop/image.png")
#print(tesserocr.image_to_text(image))
result = tesserocr.image_to_text(image)
print(result)

im = Image.open("/Users/yaomingxi/Desktop/CheckCode.jpg")
rs = tesserocr.image_to_text(im)
print(rs)

im2 = Image.open("/Users/yaomingxi/Desktop/CheckCode.png")
rs2 = tesserocr.image_to_text(im2)
print(rs2)
'''

im2 = Image.open("/Users/yaomingxi/Desktop/CheckCode.jpeg")
im2 = im2.convert('L')
im2 = im2.convert('1')
rs2 = tesserocr.image_to_text(im2)