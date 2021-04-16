from lib.Login import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os
# 选择销售台账
mainWindow = wd.current_window_handle
handles = wd.window_handles
print(handles)

def sell():
    wd.find_element_by_xpath('//div//li//i[@class="fa fa-desktop"]').click()
    wd.find_element_by_xpath('//div//li//li//i[@class="el-icon-document-copy"]').click()
    wd.implicitly_wait(300)
    wd.switch_to.frame(1)

sell()



#新建订单
def new_order():
    # #点击新建订单
    # js_1 = 'document.getElementsByClassName("el-button el-button--primary el-button--mini")[1].click();'
    # wd.execute_script(js_1)

    # #点击确认
    # js_2 = 'document.getElementsByClassName("el-button el-button--default el-button--small el-button--primary")[0].click();'
    # wd.execute_script(js_2)
    # # wd.find_element_by_xpath('//div//button//span[text()="确定"]').click()

    #选择客户
    js_3 = 'document.getElementsByClassName("el-select el-select--mini")[0].click();'
    wd.execute_script(js_3)
    clients = wd.find_elements_by_css_selector('li.el-select-dropdown__item')
    for client in clients:
        if '一加' in client.text:
            client.click()
            break
    time.sleep(3)
    #紧急程度
    js_4 = 'document.getElementsByClassName("el-select el-select--mini")[1].click();'
    wd.execute_script(js_4)
    urgency = wd.find_elements_by_css_selector('li.el-select-dropdown__item')
    for urgent in urgency:
        if '紧急' in urgent.text:
            print(urgent.text)
            urgent.click()
            break

    #订单交期
    time.sleep(2)
    date_1 = wd.find_elements_by_xpath('//div[@class="el-date-editor el-input el-input--mini el-input--prefix el-input--suffix el-date-editor--date"]')[1]
    date_1.click()
    time.sleep(2)

    #选择日期
    wd.find_element_by_xpath('//td[@class="available today"]//div//span').click()

    #点击图纸导入
    wd.find_element_by_xpath('//button//span[text()="图纸导入"]').click()
    time.sleep(3)

    #点击打开上传窗口
    js_5 = 'document.getElementsByClassName("el-button el-button--primary el-button--small")[1].click()'
    wd.execute_script(js_5)

    # 调用exe上传程序
    a = (r"E:\Klory\01.Work\07.JJ\upl.exe")
    os.system(a)

    #确认上传图纸
    time.sleep(3)
    js_6 = 'document.getElementsByClassName("el-button el-button--success el-button--small")[1].click()'
    wd.execute_script(js_6)


    global number
    number = wd.find_element_by_xpath('//div//td[@class="el-table_1_column_2  "]').get_attribute('textContent')
    print(number)




    # #客户订单号
    time.sleep(2)
    wd.find_elements_by_xpath('//div//input[@placeholder="输入数量"]')[0].clear()
    wd.find_elements_by_xpath('//div//input[@placeholder="输入数量"]')[0].send_keys('2')

    #确认
    wd.find_element_by_xpath('//button//span[text()="确认"]').click()
    print('新建订单成功')
new_order()

# js打开新窗口 PDA
js = 'window.open("http://120.79.5.120/mes-mobile/#/login?tid=null");'
wd.execute_script(js)
wd.switch_to.window(wd.window_handles[2])
time.sleep(3)

# 获取当前窗口句柄
pda = wd.current_window_handle
handles = wd.window_handles
print(handles)

def login_1():
    # 选择账号登录
    time.sleep(3)
    a = wd.find_element_by_xpath('//div[@class="footer"]/div/a/u[text()="账号登录"]')
    print(a.text)
    a.click()
    time.sleep(3)
    wd.find_elements_by_class_name('van-field__control')[0].send_keys('04987')
    # 填入密码
    wd.find_elements_by_class_name('van-field__control')[1].send_keys('123456789')

    # 显性等待并找到该元素
    b = WebDriverWait(wd, 20).until(EC.visibility_of_element_located((By.XPATH, '//div//button[@class="van-button van-button--info van-button--normal van-button--block van-button--round"]')))
    # b = wd.find_element_by_xpath('//div//button//div//span[text()=" 登录 "]')
    print(b.text)
    b.click()
    # b.send_keys(Keys.ENTER)
login_1()
# print(number)
# # 切换回主窗口
# time.sleep(3)
# wd.switch_to.default_content()
# time.sleep(3)
# wd.refresh()



