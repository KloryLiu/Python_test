import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

# 调用谷歌浏览器
wd = webdriver.Chrome(r'e:\Klory\03.Tool\08.driver\chromedriver.exe')
# 隐形等待300毫秒 （规定时间内等待浏览器打开加载完毕后，执行下一步
wd.implicitly_wait(300)

def login():

    # 跳转路径
    wd.get('http://120.79.5.120/login?tid=2288')
    # 窗口最大化
    wd.maximize_window()
    # 强制等待一秒
    time.sleep(1)
    # 选择账号登录
    wd.find_element_by_id('tab-1').click()
    # 填入账号
    wd.find_elements_by_class_name('el-input__inner')[0].send_keys('04987')
    # 填入密码
    wd.find_elements_by_class_name('el-input__inner')[1].send_keys('123456789')
    # 点击登陆
    wd.find_element_by_class_name('el-button--primary').click()
    # 选择机加
    wd.find_elements_by_class_name('singleLogin-style')[0].click()
    # 切换机加窗口
    wd.switch_to.window(wd.window_handles[1])
    print('登录成功')
login()

# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------
#点击基础数据
# def client():
#     wd.find_element_by_class_name('fa-align-justify').click()
#     wd.find_elements_by_class_name('el-menu-item')[1].click()
#     time.sleep(3)
#     wd.switch_to.frame(1)
#     time.sleep(3)
#
#     def new_client1():
#         wd.find_element_by_id('activeid_1').click()
#         wd.find_elements_by_class_name('FieldEdit')[2].send_keys('test_01')
#         wd.find_elements_by_class_name('FieldEdit')[3].send_keys('广东省惠州市惠城区马安镇利元亨')
#         wd.find_elements_by_class_name('FieldEdit')[4].send_keys('小利')
#         wd.find_elements_by_class_name('FieldEdit')[5].send_keys('13012341234')
#         wd.find_element_by_id('activeid_7').click()
#     new_client1()
#     time.sleep(3)
#     # 修改客户_01
#     def change_client():
#         # 勾选checkbox
#         wd.find_element_by_id('jqg_main-table_1').click()
#         # 点击修改
#         wd.find_element_by_id('activeid_2').click()
#         # 清除文本
#         wd.find_elements_by_class_name('FieldEdit')[2].clear()
#         wd.find_elements_by_class_name('FieldEdit')[3].clear()
#         # 更改文本
#         wd.find_elements_by_class_name('FieldEdit')[2].send_keys('test_01_改')
#         wd.find_elements_by_class_name('FieldEdit')[3].send_keys('广东省惠州市惠城区马安镇利元亨_改')
#         wd.find_element_by_id('activeid_7').click()
#     change_client()
#     # 选择删除
#     time.sleep(3)
#     def del_client():
#         # 勾选checkbox
#         wd.find_element_by_id('jqg_main-table_1').click()
#         # 点击删除按钮
#         wd.find_element_by_id('activeid_3').click()
#         # alert确定
#         wd.switch_to.alert.accept()
#         time.sleep(2)
#         wd.find_element_by_id('AlertConfirmButton').click()
#     del_client()
#     print('客户管理正常')
#     wd.switch_to.default_content()
# client()
#
# # ---------------------------------------------------------------------------------------------------------------------
# # ---------------------------------------------------------------------------------------------------------------------
# # ---------------------------------------------------------------------------------------------------------------------
# # ---------------------------------------------------------------------------------------------------------------------
#
# def pro():
#     wd.find_elements_by_class_name('el-menu-item')[2].click()
#     wd.switch_to.frame(2)
#     time.sleep(3)
#
#     def new_pro():
#         wd.find_element_by_id('activeid_1').click()
#         wd.find_elements_by_class_name('FieldEdit')[2].send_keys('test_01')
#         wd.find_element_by_id('activeid_7').click()
#     new_pro()
#     time.sleep(3)
#     def change_pro():
#         wd.find_element_by_id('jqg_main-table_1').click()
#         # 点击修改
#         wd.find_element_by_id('activeid_2').click()
#         #清除文本
#         wd.find_elements_by_class_name('FieldEdit')[2].clear()
#         #更改文本
#         wd.find_elements_by_class_name('FieldEdit')[2].send_keys('test_01_改')
#         wd.find_element_by_id('activeid_7').click()
#     change_pro()
#     time.sleep(3)
#     def del_pro():
#         # 勾选checkbox
#         wd.find_element_by_id('jqg_main-table_1').click()
#         # 点击删除按钮
#         wd.find_element_by_id('activeid_3').click()
#         # alert确定
#         wd.switch_to.alert.accept()
#         time.sleep(2)
#         wd.find_element_by_id('AlertConfirmButton').click()
#     del_pro()
#     print('工序管理正常')
#     wd.switch_to.default_content()
# pro()
#
# def path():
#     wd.find_elements_by_class_name('el-menu-item')[5].click()
#     time.sleep(3)
#     wd.switch_to.frame(3)
#
#     def new_path():
#         wd.find_elements_by_class_name('el-button--primary')[1].click()
#         wd.find_element_by_xpath('//div[@class="cell"]/span/input').send_keys('test_01')
#         # wd.find_elements_by_class_name('el-switch')[0].click()
#         wd.find_elements_by_class_name('button-new-tag')[0].click()
#         # 点击输入框
#         wd.find_elements_by_class_name('el-input__inner')[3].click()
#         time.sleep(2)
#         # 点击路径
#         sz = wd.find_elements_by_css_selector('li.el-select-dropdown__item')
#         for xx in sz:
#             if 'CNC' in xx.text:
#                 xx.click()
#                 break
#         time.sleep(2)
#         # 点击new tag
#         wd.find_elements_by_class_name('button-new-tag')[0].click()
#         # 点击输入框
#         wd.find_elements_by_class_name('el-input__inner')[3].click()
#         # 点击路径
#         time.sleep(2)
#         sz = wd.find_elements_by_css_selector('li.el-select-dropdown__item')
#         for yy in sz:
#             if 'OQC' in yy.text:
#                 # print(yy.text)
#                 yy.click()
#                 break
#         time.sleep(2)
#         wd.find_element_by_xpath('//div/button/span[text()="保存"]').click()
#     new_path()
#
#     # def change_path():
#     #     time.sleep(3)
#     #     # 勾选框
#     #     # cks = wd.find_elements_by_xpath('//span[@class="el-checkbox__inner"]')
#     #     # cks[1].click()
#     #     cks = WebDriverWait(wd, 50).until(EC.visibility_of_element_located((By.XPATH, '//span[@class="el-checkbox__inner"]')))
#     #     print('2')
#     #     cks[1].click()
#     #     print('1')
#     #     # 修改按钮
#     #     wd.find_element_by_xpath('//span[text()="修改"]').click()
#     #     # 修改名称
#     #     # wd.find_element_by_xpath('//div[@class="cell"]/span/input').clear()
#     #     time.sleep(2)
#     #     wd.find_element_by_xpath('//div[@class="cell"]/span/input').send_keys('_改')
#     #     # 改标签
#     #     sz = wd.find_elements_by_css_selector('li.el-select-dropdown__item')
#     #     for yy in sz:
#     #         if '热处理' in yy.text:
#     #             print(yy.text)
#     #             yy.click()
#     #             break
#     #     wd.find_element_by_xpath('//div/button/span[text()="保存"]').click()
#     # change_path()
#
#     # def del_path():
#     #     time.sleep(3)
#     #     cks = wd.find_elements_by_xpath('//span[@class="el-checkbox__inner"]')
#     #     cks[1].click()
#     #     wd.find_element_by_xpath('//span[text()="删除"]').click()
#     #     wd.find_element_by_xpath('//div/button/span[text()="确定"]').click()
#     # del_path()
#     print('工序路径正常')
#     wd.switch_to.default_content()
# path()
#
#
#
def sell():
    time.sleep(3)
    mainWindow = wd.current_window_handle
    handles = wd.window_handles
    # print(handles)
    wd.find_element_by_xpath('//div//li//i[@class="fa fa-desktop"]').click()
    wd.find_element_by_xpath('//div//li//li//i[@class="el-icon-document-copy"]').click()
    wd.implicitly_wait(300)
    wd.switch_to.frame(1)
    # 新建订单
    def new_order():
        # 选择客户
        js_3 = 'document.getElementsByClassName("el-select el-select--mini")[0].click();'
        wd.execute_script(js_3)
        clients = wd.find_elements_by_css_selector('li.el-select-dropdown__item')
        for client in clients:
            if '一加' in client.text:
                client.click()
                break
        time.sleep(3)
        # 紧急程度
        js_4 = 'document.getElementsByClassName("el-select el-select--mini")[1].click();'
        wd.execute_script(js_4)
        urgency = wd.find_elements_by_css_selector('li.el-select-dropdown__item')
        for urgent in urgency:
            if '紧急' in urgent.text:
                # print(urgent.text)
                urgent.click()
                break
        # 订单交期
        time.sleep(2)
        date_1 = wd.find_elements_by_xpath(
            '//div[@class="el-date-editor el-input el-input--mini el-input--prefix el-input--suffix el-date-editor--date"]')[1]
        date_1.click()
        time.sleep(2)
        # 选择日期
        wd.find_element_by_xpath('//td[@class="available today"]//div//span').click()
        # 点击图纸导入
        wd.find_element_by_xpath('//button//span[text()="图纸导入"]').click()
        time.sleep(3)
        # 点击打开上传窗口
        js_5 = 'document.getElementsByClassName("el-button el-button--primary el-button--small")[1].click()'
        wd.execute_script(js_5)
        # 调用exe上传程序
        a = (r"E:\Klory\01.Work\07.JJ\upl.exe")
        os.system(a)
        # 确认上传图纸
        time.sleep(3)
        js_6 = 'document.getElementsByClassName("el-button el-button--success el-button--small")[1].click()'
        wd.execute_script(js_6)

        global number
        number = wd.find_element_by_xpath('//div//td[@class="el-table_1_column_2  "]').get_attribute('textContent')
        print(number)
        # #客户订单号
        time.sleep(2)
        wd.find_elements_by_xpath('//div//input[@placeholder="输入数量"]')[0].clear()
        wd.find_elements_by_xpath('//div//input[@placeholder="输入数量"]')[0].send_keys('50')
        # 确认
        wd.find_element_by_xpath('//button//span[text()="确认"]').click()
        print('新建订单正常')
        wd.switch_to.default_content()
    new_order()
sell()

def PDA():
    js = 'window.open("http://120.79.5.120/mes-mobile/#/login?tid=null");'
    wd.execute_script(js)
    wd.switch_to.window(wd.window_handles[2])
    time.sleep(3)

    # 获取当前窗口句柄
    pda = wd.current_window_handle
    handles = wd.window_handles
    # print(handles)

    time.sleep(3)
    a = wd.find_element_by_xpath('//div[@class="footer"]/div/a/u[text()="账号登录"]')
    # print(a.text)
    a.click()
    time.sleep(3)
    wd.find_elements_by_class_name('van-field__control')[0].send_keys('04987')
    # 填入密码
    wd.find_elements_by_class_name('van-field__control')[1].send_keys('123456789')
    # 显性等待并找到该元素
    b = WebDriverWait(wd, 20).\
        until(EC.visibility_of_element_located((By.XPATH,
            '//div//button[@class="van-button van-button--info van-button--normal van-button--block van-button--round"]')))
    # b = wd.find_element_by_xpath('//div//button//div//span[text()=" 登录 "]')
    # print(b.text)
    b.click()

    # 接收图纸
    time.sleep(3)
    accept_paper = wd.find_elements_by_xpath('//div//button')[1]
    accept_paper.click()
    time.sleep(3)
    wd.find_elements_by_class_name('van-field__control')[0].send_keys(number)
    wd.find_element_by_xpath('//div//button').click()
    wd.find_element_by_xpath('//div[@class="van-nav-bar__left"]').click()
    # 开始工序
    time.sleep(3)
    start_process = wd.find_elements_by_xpath('//div//button')[2]
    start_process.click()
    time.sleep(1)
    wd.find_elements_by_class_name('van-field__control')[0].send_keys(number)
    time.sleep(2)
    wd.find_element_by_xpath('//div//button').click()
    wd.find_element_by_xpath('//div[@class="van-nav-bar__left"]').click()

    # 结束工序
    time.sleep(3)
    end_process = wd.find_elements_by_xpath('//div//button')[4]
    end_process.click()
    time.sleep(1)
    wd.find_elements_by_class_name('van-field__control')[0].send_keys(number)
    time.sleep(2)
    wd.find_element_by_xpath('//div//button').click()
    wd.find_element_by_xpath('//div[@class="van-nav-bar__left"]').click()

    # QC品检
    time.sleep(3)
    QC_process = wd.find_elements_by_xpath('//div//button')[7]
    QC_process.click()
    wd.find_elements_by_xpath('//div//button')[1].click()
    wd.find_elements_by_xpath('//div//button')[0].click()
    wd.find_elements_by_class_name('van-field__control')[0].send_keys(number)
    time.sleep(2)
    wd.find_element_by_xpath('//div//button').click()
    wd.find_element_by_xpath('//div[@class="van-nav-bar__left"]').click()
    wd.find_element_by_xpath('//div[@class="van-nav-bar__left"]').click()
    wd.find_element_by_xpath('//div[@class="van-nav-bar__left"]').click()


    # 发货
    time.sleep(3)
    deliver_goods = wd.find_elements_by_xpath('//div//button')[8]
    deliver_goods.click()
    wd.find_elements_by_class_name('van-field__control')[0].send_keys(number)
    wd.find_elements_by_class_name('van-field__control')[2].send_keys(5)
    time.sleep(2)
    wd.find_element_by_xpath('//div//button').click()
    wd.close()
    wd.switch_to.window(wd.window_handles[1])

    print('PDA正常')
PDA()