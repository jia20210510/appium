from common.emulator_desired import desired
from time import sleep

driver = desired()

# 隐式等待，针对全部元素设置的等待时间,智能等待
driver.implicitly_wait(5)

# 强制等待 X秒，线程休眠
sleep(2)

from selenium.webdriver.support.ui import WebDriverWait
# 显示等待，针对某个特定元素等待
# (self, driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None):
# poll_frequency:每隔一段时间检测一次，默认0.5秒
# ignored:超时报错信息
WebDriverWait(driver, 3).until(lambda x:x.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum'))

# lambda 匿名函数 没有名字
# lambda arg_list:expression
add = lambda x, y: x+y
add(1, 2)
