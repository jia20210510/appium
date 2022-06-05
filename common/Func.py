# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: appium
@File: Func.PY
@Date: 2022/05/23 22:40
@Author: jia
@Description: 常用函数
"""
from common.emulator_desired import desired
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support.wait import WebDriverWait
from config import log
import csv
import time
import os

logger = log.log_execute('debug_logger')
driver = desired()


def check_exist(element):
    """
    显示等待X秒，检查元素是否存在
    :param element: id ,example:'com.hle.lhzm:id/btn_login'
    :return: 存在返回 true；失败返回 False
    """
    try:
        WebDriverWait(driver, 10).until(
            lambda x: x.find_element_by_id(element), '没有找到%s' % element)
    except NoSuchElementException:
        return False
    else:
        return True


def check_uiautomator(element, note):
    """
    用 by_android_uiautomator 方式来定位元素
    :param element: 如：'new UiSelector().text("同意")'
    :param note: 注明要查找控件的名称、作用，方便调试
    :return:
    """
    try:
        agree = driver.find_element_by_android_uiautomator(element)
    except NoSuchElementException:
        logger.debug('没有出现%s' % note)
    else:
        agree.click()


def check_element(element, note=None):
    """
    显示等待元素X秒，元素出现则点击，不出现则输出控件名
    :param element: 定位元素
    :param note: 备注控件的名称
    :return:
    """
    try:
        element = WebDriverWait(driver, 15).until(
            lambda x: x.find_element_by_id(element))
    except NoSuchElementException:
        logger.debug('no such element,没有出现%s' % note)
    except TimeoutException:
        logger.debug('time out,没有出现%s' % note)
    else:
        element.click()


# 双指滑动
def swipe(start_x, start_y, end_x, end_y, duration):
    return driver.swipe(start_x, start_y, end_x, end_y, duration)


# 获取屏幕尺寸
def get_screen_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return x, y


# 左划
def swipe_left():
    size = get_screen_size()
    x1 = int(size[0] * 0.9)
    y1 = int(size[1] * 0.5)
    x2 = int(size[0] * 0.1)
    driver.swipe(x1, y1, x2, y1, 1000)


# 上划
def swipe_up():
    size = get_screen_size()
    x1 = int(size[0] * 0.5)
    y1 = int(size[1] * 0.95)
    y2 = int(size[1] * 0.35)
    driver.swipe(x1, y1, x1, y2, 1000)


# 下划
def swipe_down():
    size = get_screen_size()
    x1 = int(size[0] * 0.5)
    y1 = int(size[1] * 0.35)
    y2 = int(size[1] * 0.85)
    driver.swipe(x1, y1, x1, y2, 1000)


# 右划
def swipe_right():
    size = get_screen_size()
    y1 = int(size[1] * 0.5)
    x1 = int(size[0] * 0.25)
    x2 = int(size[0] * 0.95)
    driver.swipe(x1, y1, x2, y1, 1000)


# 缩小
def zoom_out():
    x, y = get_screen_size()
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    pinch_action = MultiAction(driver)

    action1.press(x=x*0.2, y=y*0.2).wait(1000).move_to(x=x*0.4, y=y*0.4).wait(1000).release()
    action2.press(x=x*0.8, y=y*0.8).wait(1000).move_to(x=x*0.6, y=y*0.6).wait(1000).release()
    # mutiaction方法，ADD()添加对象，perform()执行
    pinch_action.add(action1, action2)
    pinch_action.perform()
    logger.info('缩小...')


# 放大
def zoom_in():
    x, y = get_screen_size()
    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    action1.press(x=x*0.4, y=y*0.4).wait(1000).move_to(x=x*0.2, y=y*0.2).wait(1000).release()
    action2.press(x=x*0.6, y=y*0.6).wait(1000).move_to(x=x*0.8, y=y*0.8).wait(1000).release()

    zoom_action.add(action1, action2)
    zoom_action.perform()
    logger.info('放大....')


# 获取年-月-日 时：分：秒
def get_now_time():
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    return now


# 保存截图
def screenshots(save_path):
    now_time = get_now_time()
    # 获得当前文件所在目录绝对路径
    # currentPath = os.path.dirname(os.path.abspath(__file__))
    image_file = os.path.join(save_path + '%s.png' % now_time)
    driver.get_screenshot_as_file(image_file)
    logger.info('image_file: %s' % image_file)


# 检测浮窗广告
def check_market_ad():
    logger.info('====check_market_ad====')
    try:
        element = driver.find_element('ele')
    except NoSuchElementException:
        logger.info('no Ad')
        pass
    else:
        logger.info('close market ad')
        element.click()


# 获取CSV文件指定行的数据
def get_csv_data(csv_file, line):
    logger.info('=====get_csv_data======')
    with open(csv_file, 'r', encoding='utf-8-sig') as file:
        reader = csv.reader(file)
        for index, row in enumerate(reader):  # enumerate对一个可迭代对象输出下标和值，默认初始下标值从0开始
            if index == line:
                return row


def close():
    driver.close_app()


if __name__ == '__main__':
    list_data = 'C:\\Users\\Administrator\\Desktop\\new.csv'
    get_csv_data(list_data, 5)
    for i in range(3):
        zoom_in()

    for i in range(3):
        zoom_out()
