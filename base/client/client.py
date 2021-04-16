from lib.Login import *
#点击基础数据
def base():
    wd.find_element_by_class_name('fa-align-justify').click()
base()

#点击客户管理
def client():
    wd.find_elements_by_class_name('el-menu-item')[1].click()
client()

#切换frame
def f1():
    time.sleep(5)
    wd.switch_to.frame(1)
    print('切换成功')
f1()
