from base.process.process import *


#新增工序_01
time.sleep(3)
def new_pro1():
    wd.find_element_by_id('activeid_1').click()
    wd.find_elements_by_class_name('FieldEdit')[2].send_keys('test_01')
    wd.find_element_by_id('activeid_7').click()
new_pro1()
#修改客户_01
time.sleep(3)
def change_pro1():
    # 勾选checkbox
    wd.find_element_by_id('jqg_main-table_1').click()
    # 点击修改
    wd.find_element_by_id('activeid_2').click()
    #清除文本
    wd.find_elements_by_class_name('FieldEdit')[2].clear()
    #更改文本
    wd.find_elements_by_class_name('FieldEdit')[2].send_keys('test_01_改')
    wd.find_element_by_id('activeid_7').click()
change_pro1()


#选择删除
time.sleep(3)
def del_pro():
    #勾选checkbox
    wd.find_element_by_id('jqg_main-table_1').click()
    #点击删除按钮
    wd.find_element_by_id('activeid_3').click()
    #alert确定
    wd.switch_to.alert.accept()
    time.sleep(2)
    wd.find_element_by_id('AlertConfirmButton').click()
    print('删除成功')
del_pro()
