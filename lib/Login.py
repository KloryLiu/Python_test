import time
from selenium import webdriver

# 调用谷歌浏览器
wd = webdriver.Chrome(r'e:\Klory\03.Tool\08.driver\chromedriver.exe')
# 隐形等待300毫秒 （规定时间内等待浏览器打开加载完毕后，执行下一步
wd.implicitly_wait(300)
# 跳转路径
wd.get('http://120.79.5.120/login?tid=2288')
# 窗口最大化
wd.maximize_window()
# 强制等待一秒
time.sleep(1)


def login():
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








