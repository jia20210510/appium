# _*_ coding:utf-8 _*_
"""
@version: python3.8
@project: appium
@file:   emulator_desired.py
@date:   2021/6/16 19:28
@Author: jia
@Desc:   使用模拟器的初始化参数
"""
from appium import webdriver
import yaml


def desired():
    # 读取YAML配置文件
    with open('../config/android_emulator.yaml', 'r', encoding='utf-8') as file:
        data = yaml.full_load(file)  # yaml 5.1新用法

    # 初始化配置数据
    desired_caps = dict()
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion'] = data['platformVersion']
    desired_caps['deviceName'] = data['deviceName']
    # 自动安装APP
    desired_caps['app'] = data['app']
    desired_caps['appPackage'] = data['appPackage']
    desired_caps['appActivity'] = data['appActivity']
    # false,执行的操作会重置，true不重置
    desired_caps['noReset'] = data['noReset']
    # 输入中文需要设置
    desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
    desired_caps['resetKeyboard'] = data['resetKeyboard']
    # 检查toast需要uiautomator2
    desired_caps['automationName'] = data['automationName']
    # 启动APP
    driver = webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub', desired_caps)

    driver.implicitly_wait(8)
    return driver



