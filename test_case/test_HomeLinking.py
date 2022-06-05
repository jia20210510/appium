# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: Appium
@File: test_HomeLinking.PY
@Date: 2022/5/28 20:12
@Author: jia
@Description:
测试登录 退出
"""
import allure
import pytest
from time import sleep
from common.Func import *
from common import file_methods


class TestHomeLinking:
    root_dir = file_methods.FileMethod.get_project_path('appium')

    def setup_class(self):
        """
        配置allure报告中的环境变量
        :return:
        """
        #
        en_text = 'System.version = win10\nauthor = jia\npython = 3.8.0\n' \
                  'pyTest = 6.2.4\nallure = 2.9.43\nflask = 2.0.1\nhtml = 3.1.1'

        # 先清除后写入
        file_methods.FileMethod.clean_dir(self.root_dir+"Report/temp")
        file_methods.FileMethod.write_file(self.root_dir+"Report/temp/environment.properties", en_text)

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('用户登录')
    def test_login(self):
        logger.info('============login==============')

        # 清除应用数据，相当于卸载
        driver.reset()

        # 检查权限弹窗
        check_uiautomator('new UiSelector().text("同意")', '隐私政策弹窗')
        check_uiautomator('new UiSelector().text("允许")', '存储权限弹窗')

        # from selenium.webdriver.common.by import By 导入才可使用这种写法
        check_element('com.hle.lhzm:id/rb_user_center', note='我的')

        login_tag = driver.find_element_by_id("com.hle.lhzm:id/login_immediately").get_attribute('name')
        if login_tag == '立即登录':
            driver.find_element_by_id("com.hle.lhzm:id/login_immediately").click()
        sleep(5)

        # 允许获取位置权限
        check_element('com.hle.lhzm:id/confirm_but', note='位置权限弹窗')

        country = driver.find_element_by_id('com.hle.lhzm:id/time_zone').get_attribute('name')
        logger.info('账号区域是：'+country)
        # 输入账号密码
        driver.find_element_by_id('com.hle.lhzm:id/et_account').clear()
        driver.find_element_by_id('com.hle.lhzm:id/et_account').send_keys('18800000018')
        driver.find_element_by_id('com.hle.lhzm:id/et_password').clear()
        driver.find_element_by_id('com.hle.lhzm:id/et_password').send_keys('888888')
        check_box = driver.find_element_by_id('com.hle.lhzm:id/cb_rule').get_attribute('checked')
        if check_box == 'false':
            driver.find_element_by_id('com.hle.lhzm:id/cb_rule').click()
        logger.info('点击登录')
        driver.find_element_by_id('com.hle.lhzm:id/btn_login').click()
        sleep(6)

    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_check_status(self):
        logger.debug('=====check_logon_status======')

        element = check_exist('com.hle.lhzm:id/tv_home_family_but')
        if element:
            text = driver.find_element_by_id('com.hle.lhzm:id/tv_home_family_but').text
            if text == '18800000018的家庭':
                logger.debug('用户已登录')
            screenshots(r'E:\\PycharmProject\\appium\\screenshots\\')
        else:
            logger.debug('用户未登录')
            screenshots(r'E:\\PycharmProject\\appium\\screenshots\\')

    @allure.severity(allure.severity_level.NORMAL)
    @allure.step('退出登录')
    def test_logout(self):
        logger.info('=====logout======')
        # 点击 “我的”
        check_element('com.hle.lhzm:id/rb_user_center', note='我的')
        # 点击 设置
        driver.find_element_by_id('com.hle.lhzm:id/setting_btn').click()
        # 点击退出账号
        driver.find_element_by_id('com.hle.lhzm:id/outlogin').click()
        login_but = check_exist('com.hle.lhzm:id/btn_login')
        if login_but:
            logger.debug('账号已退出')
            screenshots(r'E:\\PycharmProject\\appium\\screenshots\\')
        else:
            logger.debug('账号未退出')
            screenshots(r'E:\\PycharmProject\\appium\\screenshots\\')

    @staticmethod
    def teardown_class():
        # 关闭APP
        driver.close_app()
        # 结束驱动连接
        driver.quit()
