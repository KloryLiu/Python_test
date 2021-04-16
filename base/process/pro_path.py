from lib.Login import *
from selenium.webdriver.common.action_chains import ActionChains
ac = ActionChains(wd)
def base():
    wd.find_element_by_class_name('fa-align-justify').click()
base()

#点击路径管理
def promanage():
    wd.find_elements_by_class_name('el-menu-item')[5].click()
promanage()

#切换frame
def f1():
    time.sleep(5)
    wd.switch_to.frame(1)
f1()


#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#


#添加路径
time.sleep(2)
#点击添加路径按钮
wd.find_elements_by_class_name('el-button--primary')[1].click()

#填写路径名称
def path_name():
    wd.find_element_by_xpath('//div[@class="cell"]/span/input').send_keys('test_01')
path_name()

#选择默认按钮
def path_default():
    wd.find_elements_by_class_name('el-switch')[0].click()
path_default()

#选择路径1
def new_path_sel1():
    #点击new tag
    wd.find_elements_by_class_name('button-new-tag')[0].click()
    #点击输入框
    wd.find_elements_by_class_name('el-input__inner')[3].click()
    time.sleep(2)
    #点击路径
    sz = wd.find_elements_by_css_selector('li.el-select-dropdown__item')
    for xx in sz:
        if 'CNC' in xx.text:
            xx.click()
            break
new_path_sel1()

#选择路径2
def new_path_sel2():
    time.sleep(2)
    # 点击new tag
    wd.find_elements_by_class_name('button-new-tag')[0].click()
    # 点击输入框
    wd.find_elements_by_class_name('el-input__inner')[3].click()
    # 点击路径
    time.sleep(2)
    sz = wd.find_elements_by_css_selector('li.el-select-dropdown__item')
    for yy in sz:
        if 'OQC' in yy.text:
            print(yy.text)
            yy.click()
            break
new_path_sel2()

#点击保存
def save_path():
    time.sleep(2)
    wd.find_element_by_xpath('//div/button/span[text()="保存"]').click()
save_path()


#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#


#点击修改
def change_path():
    time.sleep(2)
    #勾选框
    cks = wd.find_elements_by_xpath('//span[@class="el-checkbox__inner"]')
    print('1')
    cks[1].click()
    print('2')
    #修改按钮
    wd.find_element_by_xpath('//span[text()="修改"]').click()
    #修改名称
    # wd.find_element_by_xpath('//div[@class="cell"]/span/input').clear()
    time.sleep(2)
    wd.find_element_by_xpath('//div[@class="cell"]/span/input').send_keys('_改')
    #改标签
    sz = wd.find_elements_by_css_selector('li.el-select-dropdown__item')
    for yy in sz:
        if '热处理' in yy.text:
            print(yy.text)
            yy.click()
            break
    wd.find_element_by_xpath('//div/button/span[text()="保存"]').click()
change_path()


#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#


#删除
def del_path():
    time.sleep(2)
    cks = wd.find_elements_by_xpath('//span[@class="el-checkbox__inner"]')
    cks[1].click()
    wd.find_element_by_xpath('//span[text()="删除"]').click()

    #方法1：加入For循环 才成功点击
    # sc_1 = wd.find_elements_by_xpath(
    #     '//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    # for sc_2 in sc_1:
    #     print(sc_2.text)
    #     sc_2.click()

    #方法2：调用JS 执行点击事件
    js = 'document.getElementsByClassName("el-button el-button--default el-button--small el-button--primary")[0].click();'
    wd.execute_script(js)
del_path()




