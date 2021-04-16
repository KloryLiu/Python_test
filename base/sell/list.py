
from base.sell.new_order import *

from selenium.webdriver.common.action_chains import ActionChains
import os



mainWindow = wd.current_window_handle
handles = wd.window_handles
print(handles)
# 销售订单列表
def sell():
    wd.find_element_by_xpath('//div//li//i[@class="fa fa-desktop"]').click()
    wd.implicitly_wait(300)
    wd.find_element_by_xpath('//div//li//li//i[@class="fa fa-leanpub"]').click()
    # 切换frame
    wd.switch_to.frame(2)
    print('切换成功')
sell()

time.sleep(3)
#
# #打印图纸
def print_paper():
    # 勾选checkbox
    gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    gx.click()

    #点击批量接收
    wd.find_elements_by_xpath('//div//button[@class="el-button el-button--default el-button--small"]')[0].click()
    time.sleep(3)
    wd.switch_to.window(wd.window_handles[2])
    wd.close()
    wd.switch_to.window(wd.window_handles[1])

    print('打印成功')
print_paper()

wd.refresh()
def sell():
    wd.find_element_by_xpath('//div//li//i[@class="fa fa-desktop"]').click()
    wd.implicitly_wait(300)
    wd.find_element_by_xpath('//div//li//li//i[@class="fa fa-leanpub"]').click()
    # 切换frame
    wd.switch_to.frame(2)
    print('切换成功')

sell()
#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#
#修改订单信息
def change_order():

    # 勾选checkbox
    time.sleep(3)
    gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    gx.click()
    # 点击修改订单
    wd.implicitly_wait(300)
    change = wd.find_elements_by_xpath('//div//button[@class="el-button el-button--default el-button--small"]')[1]
    change.click()
    wd.find_elements_by_xpath('//div//input[@class="el-input__inner"]')[18].send_keys('_改')
    # save = wd.find_element_by_xpath('//div/button/span[text()="保存"]')
    save = wd.find_elements_by_xpath('//div/button[@class="el-button el-button--success el-button--small"]')[0]
    save.click()
    wd.find_element_by_xpath('//div/button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
    print('修改订单成功')
change_order()


#---------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------#


# 导出订单
def export_order():
    # 勾选checkbox
    gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    gx.click()

    export = wd.find_elements_by_xpath('//div//button[@class="el-button el-button--default el-button--small"]')[2]
    export.click()
    # 调用exe上传程序
    save_excel = (r"E:\Klory\01.Work\07.JJ\save_excel.exe")
    os.system(save_excel)
    print('导出成功')

export_order()
#
# 图纸变更
def change_paper ():
    # 勾选checkbox
    gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    gx.click()
    gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    gx.click()
    time.sleep(5)
    change_paper = wd.find_element_by_xpath('//div//button[@class="el-button el-button--default el-button--small el-dropdown-selfdefine"]')
    ActionChains(wd).move_to_element(change_paper).perform()
    time.sleep(5)
    change_paper = wd.find_element_by_xpath('//ul//li[text()="图纸变更"]')
    time.sleep(5)
    change_paper.click()
    # 点击打开上传窗口
    time.sleep(4)
    wd.find_elements_by_xpath('//div/button[@class="el-button el-button--primary el-button--small"]')[2].click()
    wd.implicitly_wait(500)
    # 调用exe上传程序
    a = (r"E:\Klory\01.Work\07.JJ\upl.exe")
    os.system(a)
    # 确认上传图纸
    time.sleep(4)
    js_6 = 'document.getElementsByClassName("el-button el-button--success el-button--small")[2].click()'
    wd.execute_script(js_6)
    print('图纸变更成功')
change_paper ()

# 图纸变更记录
def change_paper_log():
    # 勾选checkbox
    time.sleep(4)
    gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    gx.click()

    change_paper = wd.find_element_by_xpath('//div//button[@class="el-button el-button--default el-button--small el-dropdown-selfdefine"]')
    ActionChains(wd).move_to_element(change_paper).perform()
    time.sleep(4)

    change_paper_log = wd.find_element_by_xpath('//ul//li[text()="图纸变更记录"]')
    time.sleep(4)
    change_paper_log.click()

    wd.find_elements_by_xpath('//div//button[@class="el-button el-button--primary el-button--mini"]')[61].click()
    wd.find_element_by_xpath('//div//button[@class="el-button el-button--success el-button--mini"]').click()
    time.sleep(4)
    wd.switch_to.window(wd.window_handles[2])
    wd.close()
    time.sleep(4)
    wd.switch_to.window(wd.window_handles[1])
    wd.switch_to.frame(2)
    js_5 = 'document.getElementsByClassName("el-dialog__close el-icon el-icon-close")[5].click()'
    wd.execute_script(js_5)
    print('图纸变更记录成功')
change_paper_log()
time.sleep(5)


# 图纸调整
def adjust_paper():
    # 勾选checkbox
    time.sleep(3)
    # gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    # gx.click()
    #
    # gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    # gx.click()

    time.sleep(4)
    adjust_paper = wd.find_element_by_xpath('//div//button[@class="el-button el-button--default el-button--small el-dropdown-selfdefine"]')
    ActionChains(wd).move_to_element(adjust_paper).perform()
    time.sleep(4)

    adjust_paper = wd.find_element_by_xpath('//ul//li[text()="图纸调整"]')
    adjust_paper.click()
    time.sleep(5)
    wd.find_elements_by_xpath('//div//input[@class="el-input__inner"]')[56].send_keys('50')
    # wd.find_elements_by_xpath('//div[@class="el-tooltip item el-input-number el-input-number--mini"]//div[@class="el-input el-input--mini"]//input[@class="el-input__inner"]')[10].send_keys('50')
    wd.implicitly_wait(300)
    wd.find_element_by_xpath('//div//button//span[text()="预览"]').click()

    wd.switch_to.window(wd.window_handles[2])
    wd.close()
    wd.switch_to.window(wd.window_handles[1])
    time.sleep(3)
    wd.switch_to.frame(2)
    wd.implicitly_wait(300)
    wd.find_elements_by_xpath('//div//button[@class="el-button el-button--success el-button--small"]')[3].click()
    print('图纸调整成功')
adjust_paper()

# 批量调整坐标
def batch_adjustment():
    # 勾选checkbox
    time.sleep(3)
    gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    gx.click()
    batch_adjustment = wd.find_elements_by_xpath('//div//button[@class="el-button el-button--default el-button--small el-dropdown-selfdefine"]')[0]
    ActionChains(wd).move_to_element(batch_adjustment).perform()
    time.sleep(3)
    batch = wd.find_element_by_xpath('//ul/li[text()="批量调整坐标"]')
    time.sleep(3)
    batch.click()
    time.sleep(3)
    wd.find_elements_by_xpath('//div//input[@class="el-input__inner"]')[72].send_keys('50')
    # wd.find_elements_by_xpath('//div//div//div[@class="el-tooltip item el-input-number el-input-number--mini"]//div//input')[15].send_keys('50')
    wd.find_elements_by_xpath('//div//button//span[text()="预览"]')[1].click()
    wd.switch_to.window(wd.window_handles[2])
    wd.close()
    wd.switch_to.window(wd.window_handles[1])
    wd.switch_to.frame(2)
    wd.implicitly_wait(300)
    wd.find_elements_by_xpath('//div/button[@class="el-button el-button--success el-button--small"]')[4].click()
    wd.find_element_by_xpath('//div/button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
    print('批量调整坐标成功')
batch_adjustment()

# 接收图纸
def accept_paper():
    # 勾选checkbox
    gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    gx.click()
    time.sleep(3)
    accept_paper = wd.find_elements_by_xpath('//div//button[@class="el-button el-button--default el-button--small el-dropdown-selfdefine"]')[1]
    ActionChains(wd).move_to_element(accept_paper).perform()
    time.sleep(3)
    accept = wd.find_element_by_xpath('//ul/li[text()="接收图纸"]')
    time.sleep(3)
    accept.click()
    wd.find_element_by_xpath('//div/button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
    print('接收图纸成功')
accept_paper()


# 下载图纸
def download_paper():
    # 勾选checkbox
    gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    gx.click()
    time.sleep(3)
    download_paper = wd.find_elements_by_xpath(
        '//div//button[@class="el-button el-button--default el-button--small el-dropdown-selfdefine"]')[1]
    ActionChains(wd).move_to_element(download_paper).perform()
    time.sleep(3)
    download = wd.find_element_by_xpath('//ul/li[text()="下载图纸"]')
    time.sleep(3)
    download.click()
    print('下载图纸成功')
download_paper()


# # 批量发货
# def batch_deliver():
#     # 勾选checkbox
#     gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
#     gx.click()
#     time.sleep(3)
#     batch_deliver = wd.find_elements_by_xpath(
#         '//div//button[@class="el-button el-button--default el-button--small el-dropdown-selfdefine"]')[1]
#     ActionChains(wd).move_to_element(batch_deliver).perform()
#     time.sleep(2)
#     deliver = wd.find_element_by_xpath('//ul/li[text()="批量发货"]')
#     time.sleep(2)
#     deliver.click()
#     print('批量发货')
# batch_deliver()



# 停止生产
def stop_produce():
    # 勾选checkbox
    # gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    # gx.click()
    time.sleep(3)
    stop_produce = wd.find_elements_by_xpath(
        '//div//button[@class="el-button el-button--default el-button--small el-dropdown-selfdefine"]')[1]
    ActionChains(wd).move_to_element(stop_produce).perform()
    time.sleep(3)
    stop = wd.find_element_by_xpath('//ul/li[text()="停止生产"]')
    time.sleep(3)
    stop.click()
    wd.find_element_by_xpath(
        '//div/button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
    print('停止生产成功')
stop_produce()


# 恢复生产
def recover_produce():
    # 勾选checkbox
    gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    gx.click()
    time.sleep(4)
    recover_produce = wd.find_elements_by_xpath(
        '//div//button[@class="el-button el-button--default el-button--small el-dropdown-selfdefine"]')[1]
    ActionChains(wd).move_to_element(recover_produce).perform()
    time.sleep(4)
    recover = wd.find_element_by_xpath('//ul/li[text()="恢复生产"]')
    time.sleep(4)
    recover.click()
    wd.find_element_by_xpath(
        '//div/button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
    print('恢复生产成功')
recover_produce()


# 数据补录
def data_supplemental():
    # 勾选checkbox
    gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    gx.click()
    time.sleep(3)
    data_supplemental = wd.find_elements_by_xpath(
        '//div//button[@class="el-button el-button--default el-button--small el-dropdown-selfdefine"]')[1]
    ActionChains(wd).move_to_element(data_supplemental).perform()
    time.sleep(2)
    supplemental = wd.find_element_by_xpath('//ul/li[text()="数据补录"]')
    time.sleep(2)
    supplemental.click()
    wd.find_element_by_xpath(
        '//div/button[@class="el-button el-tooltip item el-button--default el-button--mini"]/span[text()="确认"]').click()

data_supplemental()



#删除订单
def delete_order():
    time.sleep(2)
    # 勾选checkbox
    gx = wd.find_elements_by_xpath('//div//label//span//span[@class="el-checkbox__inner"]')[69]
    gx.click()

    wd.implicitly_wait(300)
    delete = wd.find_elements_by_xpath('//div//button[@class="el-button el-button--default el-button--small"]')[4]
    delete.click()
    wd.find_element_by_xpath('//div/button[@class="el-button el-button--default el-button--small el-button--primary "]').click()
    print('删除成功')
delete_order()