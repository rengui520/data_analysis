from selenium import webdriver
import time

browser = webdriver.Chrome()

# 登录微博
def weibo_login(username, password):
     # 打开微博登录页
     browser.get('https://passport.weibo.cn/signin/login')
     browser.implicitly_wait(5)
     time.sleep(1)
     # 填写登录信息：用户名、密码
     browser.find_element_by_id("loginName").send_keys(username)
     browser.find_element_by_id("loginPassword").send_keys(password)
     time.sleep(1)
     # 点击登录
     browser.find_element_by_id("loginAction").click()
     time.sleep(1)
# 设置用户名、密码
username = '16607730939'
password = "ljwb7313520"
weibo_login(username, password)

# 添加指定的用户
def add_follow(uid):
     browser.get('https://m.weibo.com/u/'+str(uid))
     time.sleep(1)
     #browser.find_element_by_id("follow").click()

     follow_button = browser.find_element_by_xpath('//div[@class="m-add-box m-followBtn"]')
     follow_button.click()
     time.sleep(1)
     # 选择分组

     group_button = browser.find_element_by_xpath('//div/a[@class="m-btn m-btn-white m-btn-text-black"]')
     group_button.click()
     time.sleep(1)
# 每天学点心理学 UID
uid = '1890826225'
add_follow(uid)