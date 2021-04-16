from base.client.client import *


#新增客户_01
time.sleep(3)
def new_client1():
    wd.find_element_by_id('activeid_1').click()
    wd.find_elements_by_class_name('FieldEdit')[2].send_keys('test_01')
    wd.find_elements_by_class_name('FieldEdit')[3].send_keys('广东省惠州市惠城区马安镇利元亨')
    wd.find_elements_by_class_name('FieldEdit')[4].send_keys('小利')
    wd.find_elements_by_class_name('FieldEdit')[5].send_keys('13012341234')
    wd.find_element_by_id('activeid_7').click()
new_client1()

# 新增客户_02
# time.sleep(3)
# def new_client2():
#     wd.find_element_by_id('activeid_1').click()
#     wd.find_elements_by_class_name('FieldEdit')[2].send_keys('test_02')
#     wd.find_elements_by_class_name('FieldEdit')[3].send_keys('广东省惠州市惠城区马安镇利元亨')
#     wd.find_elements_by_class_name('FieldEdit')[4].send_keys('小利')
#     wd.find_elements_by_class_name('FieldEdit')[5].send_keys('13012341234')
#     wd.find_element_by_id('activeid_7').click()
# new_client2()
# print('新增成功')


#修改客户_01
time.sleep(3)
def change_client1():
    # 勾选checkbox
    wd.find_element_by_id('jqg_main-table_1').click()
    # 点击修改
    wd.find_element_by_id('activeid_2').click()
    #清除文本
    wd.find_elements_by_class_name('FieldEdit')[2].clear()
    wd.find_elements_by_class_name('FieldEdit')[3].clear()
    #更改文本
    wd.find_elements_by_class_name('FieldEdit')[2].send_keys('test_01_改')
    wd.find_elements_by_class_name('FieldEdit')[3].send_keys('广东省惠州市惠城区马安镇利元亨_改')
    wd.find_element_by_id('activeid_7').click()
change_client1()

#修改客户_02
time.sleep(3)
def change_client2():
    # 勾选checkbox
    wd.find_element_by_id('jqg_main-table_2').click()
    # 点击修改
    wd.find_element_by_id('activeid_2').click()
    #清除文本
    wd.find_elements_by_class_name('FieldEdit')[2].clear()
    wd.find_elements_by_class_name('FieldEdit')[3].clear()
    #更改文本
    wd.find_elements_by_class_name('FieldEdit')[2].send_keys('test_02_改')
    wd.find_elements_by_class_name('FieldEdit')[3].send_keys('广东省惠州市惠城区马安镇利元亨_改')
    wd.find_element_by_id('activeid_7').click()
change_client2()

#选择删除
time.sleep(3)
def del_client():
    #勾选checkbox
    wd.find_element_by_id('jqg_main-table_1').click()
    wd.find_element_by_id('jqg_main-table_2').click()

    #点击删除按钮
    wd.find_element_by_id('activeid_3').click()
    #alert确定
    wd.switch_to.alert.accept()
    time.sleep(2)
    wd.find_element_by_id('AlertConfirmButton').click()
    print('删除成功')
del_client()
