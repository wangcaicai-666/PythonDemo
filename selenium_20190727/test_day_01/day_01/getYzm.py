#__author: yaomingxi
#__date: 2019-08-01



from selenium import webdriver
import time
import tesserocr,requests
from PIL import Image,ImageDraw



dr = webdriver.Chrome()
dr.maximize_window()
url3 = "http://www.cnki.net"
dr.get(url3)

handle1 = dr.current_window_handle

#点击注册

zc = dr.find_element_by_link_text("注册")
zc.click()
time.sleep(1)

handles = dr.window_handles

for handle in handles:
    if handle != handle1:
        dr.switch_to.window(handle)
        print(dr.title)


        '''

        us = dr.find_element_by_id("username")
        us.send_keys("Myzhonggzhiwang_001")

        pw = dr.find_element_by_id("txtPassword")
        pw.send_keys("password001")

        em = dr.find_element_by_id("txtEmail")
        em.send_keys("546647817@qq.com")
        time.sleep(3)
        
        '''
        # http://my.cnki.net/elibregister/CheckCode.aspx

        #获取验证码属性ID

        image_url = "http://my.cnki.net/elibregister/CheckCode.aspx"
        time.sleep(1)

        image_path = "/Users/yaomingxi/Desktop/CheckCode123.jpeg"

        response = requests.get(image_url)
        with open(image_path, 'wb') as f:
            f.write(response.content)


        #打开本地图片
        pilImg = Image.open(image_path)

        #将图片转化为灰度图像
        pilImg = pilImg.convert('L')
        #传入1即可将图片进行二值化处理
        pilImg = pilImg.convert('1')
        #指定二值化的阈值
        threshold = 223
        table = []
        for i in range(256):
            if i < threshold:
                table.append(0)
            else:
                table.append(1)
        pilImg = pilImg.point(table, '1')

        # 识别图片
        image1 = tesserocr.image_to_text(pilImg)

        #将识别的文字输入文本框

        time.sleep(2)
        yzmsr = dr.find_element_by_id("txtOldCheckCode")
        yzmsr.send_keys(image1)
        print(image1)

        '''


        time.sleep(3)
        tk = dr.find_element_by_id("protocolFlag")
        tk.click()

        time.sleep(1)
        go = dr.find_element_by_id("ButtonRegister")
        go.click()

#dr.quit()

'''


