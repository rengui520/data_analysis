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

# 给指定某条微博添加内容
def add_comment(weibo_url, content):
     browser.get(weibo_url)
     browser.implicitly_wait(5)
     content_textarea = browser.find_element_by_css_selector("textarea.W_input").clear()
     content_textarea = browser.find_element_by_css_selector("textarea.W_input").send_keys(content)
     time.sleep(2)
     # comment_button = browser.find_element_by_css_selector("a.W_btn_a").click()
     comment_button = browser.find_element_by_xpath('//*[@id="Pl_Official_WeiboDetail__73"]/div/div/div/div[4]/div/div[2]/div[2]/div[2]/div[1]/a/em').click()
     time.sleep(1)
content = '每天学点心理学'
weibo_url = 'https://weibo.com/1890826225/HjjqSahwl'
add_comment(weibo_url, content)