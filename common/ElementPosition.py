from common.emulator_desired import desired

# by x-path
# 路径表达式：
# / 从根节点选取
# // 从匹配选择的当前节点选择文档中的节点，不考虑它们的位置
# .当前节点   ..当前节点的父节点 @选取属性   nodename选取此节点的所有子节点
driver = desired()
driver.find_element_by_xpath('//android.widget.EditText[@text="请输入用户名"]').send_keys('zxw1234')
driver.find_element_by_xpath('//*[@class="android.widget.EditText" and @index="3"]').send_keys('zxw123456')
# driver.find_element_by_xpath('//android.widget.Button').click()
driver.find_element_by_xpath('//*[@class="android.widget.Button"]').click()


# by class name
driver.find_element_by_class_name('android.widget.EditText').send_keys('2018')
driver.find_element_by_class_name('android.widget.EditText').send_keys('zx2018')
driver.find_element_by_class_name('android.widget.Button').click()

# by relative 相对定位
driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
root_element=driver.find_element_by_id('com.tal.kaoyan:id/activity_register_parentlayout')
root_element.find_element_by_class_name('android.widget.ImageView').click()

# by list
driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
driver.find_elements_by_id('com.tal.kaoyan:id/major_subject_title')[6].click()  # 理学
driver.find_elements_by_id('com.tal.kaoyan:id/major_group_title')[1].click()  # 计算机科学与技术
driver.find_elements_by_id('com.tal.kaoyan:id/major_search_item_name')[2].click()

# by id
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys('a')
driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()

# by uiautomator
# driver.find_element_by_android_uiautomator\ 固定用法，其中\是为了换行，主要有 ID ,CLASS,TEXT 三种定位方式
driver.find_element_by_android_uiautomator\
     ('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys('zxw1234')
driver.find_element_by_android_uiautomator\
     ('new UiSelector().text("请输入用户名")').send_keys('zxw1234')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().className("android.widget.EditText")').send_keys('zxw1234')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_password_edittext")').send_keys('zxw123456')

driver.find_element_by_android_uiautomator\
    ('new UiSelector().resourceId("com.tal.kaoyan:id/login_login_btn")').click()


