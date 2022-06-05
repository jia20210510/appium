from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='5.1.1'
desired_caps['deviceName']='127.0.0.1:21503'

#desired_caps['app']=r'C:\Users\Shuqing\Desktop\dr.fone3.2.0.apk'
# 夜神模拟器android system webview 74.0.3729
desired_caps['chromedriverExecutable']= 'C:\\Users\\Administrator\\AppData\\Roaming\\npm\\node_modules\\appium' \
                                        '\\node_modules\\_appium-chromedriver@4.16.0@appium-chromedriver\\chromedriver' \
                                        '\\win74\\chromedriver.exe'

'''
# 逍遥模拟器android system webview 39.0.0
desired_caps['chromedriverExecutable']= 'C:\\Users\\Administrator\\AppData\\Roaming\\npm\\node_modules\\appium' \
                                        '\\node_modules\\_appium-chromedriver@4.16.0@appium-chromedriver\\chromedriver' \
                                        '\\win39\\chromedriver.exe'
'''
desired_caps['appPackage']='com.wondershare.drfone'
desired_caps['appActivity']='com.wondershare.drfone.ui.activity.WelcomeActivity'

driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.implicitly_wait(3)

driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()

WebDriverWait(driver,8).until(lambda x:x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()
#等待webview页面的加载
WebDriverWait(driver,8).until(lambda x:x.find_element_by_class_name('android.webkit.WebView'))
# 打印contexts输出webview
contexts=driver.contexts
print(contexts)
# 从android的activity切换到H5对应的webview页面
driver.switch_to.context('WEBVIEW_com.wondershare.drfone')
driver.find_element_by_id('email').send_keys('shuqing2018@163.com')
driver.find_element_by_class_name('btn_send').click()

driver.switch_to.context('NATIVE_APP')
driver.find_element_by_class_name('android.widget.ImageButton').click()