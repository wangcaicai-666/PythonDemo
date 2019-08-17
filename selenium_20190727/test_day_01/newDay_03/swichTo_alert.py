#__author: yaomingxi
#__date: 2019-08-04


# 多窗口切换
# 获取当前窗口handle
#current_window_handle
# 获取所有窗口handles
#window_handles
# 切换窗口
#switch_to.window()

# 警告框处理
# 返回 alert confirm  prompt 中的文字信息
#switch_to.alert.text
# 接受现有警告框
#switch_to.alert.accept()
# 解算现有警告框
#switch_to.alert.dismiss()
# 在警告框中输入文本
#switch_to.alert.send_keys()



from selenium import webdriver as dr
from time import sleep as sl

dr =dr.Chrome()
url = 'https://www.baidu.com/'
dr.get(url)

sl(2)
st = dr.find_element_by_link_text("设置")
st.click()
ss = dr.find_element_by_link_text("搜索设置")
ss.click()
sl(2)

hp = dr.find_element_by_id("sh_2")
hp.click()
sl(2)

#bc = dr.find_element_by_link_text("保存设置")
bc = dr.find_element_by_xpath("//div[@id='gxszButton']/a[1]")
bc.click()
sl(2)

#切换到ALTER弹窗
alt = dr.switch_to.alert
#获取弹窗文本
tx = alt.text
print("获取弹窗文本： "+str(tx))
#确认
#alt.accept()
#取消
alt.dismiss()


sl(3)
dr.quit()