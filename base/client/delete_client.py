from base.client.new_client import  *

#选择删除
time.sleep(3)
def del_client():
    wd.find_element_by_id('jqg_main-table_1').click()
    # wd.find_element_by_id('jqg_main-table_2').click()
    wd.find_element_by_id('activeid_3').click()
    wd.switch_to.alert.accept()
    time.sleep(3)
    wd.find_element_by_id('AlertConfirmButton').click()
    print('删除成功')
del_client()