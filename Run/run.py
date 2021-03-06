#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: appium
@File: run.PY
@Date: 2022/5/28 21:22
@Author: jia
@Description:

 # -vs 详细输出；--reruns=2 失败重跑2次；-x 失败停止执行；-maxfail=2 失败2个就停止
 # -k 'xi and test' 只执行用例名包含字符xi和test的用例; -n 2 多线程运行
 # -m=smoke or retest 执行两种自定义标记的用例
 # pytest.main(['-vs', '-m=smoke or retest', '--reruns=2'])
 # pytest.main(['-s', '../Case', '--html=../Report/Report.html'])

 # pytest --alluredir ../Temp  先执行命令在此目录收集测试结果

 # https://github.com/allure-framework/allure2/releases,下载后将bin地址放在path
 # os.system('allure generate ../Temp -o ../Report --clean')
 # ../temp临时json文件目录， ../report最终输出报告的目录
 # 经测试temp不在根目录时，OS.SYSTEM操作时找不到文件

 # [0x7FFDA42FE0A4] ANOMALY: use of REX.w is meaningless (default operand size is 64)
 # 命令行报以上错误时打开注册表“regedit”
 # HKEY_LOCAL_MACHINE/SOFTWARE/TEC/Ocular.3/agent/config.yaml.yml 添加二进制数值
 # hookapi_disins,数值数据: 1
 """

import pytest
import os
if __name__ == '__main__':

    #  控制台生成测试报告
    pytest.main(['-s', '../test_case/test_HomeLinking.py'])
    os.system('allure generate ../Report/temp -o ../Report/allure_report --clean')

    # Terminal下执行
    # pytest -s Case/test/test_case1.py  --alluredir=Report/temp
    # allure generate Report/temp -o Report/allure_report --clean
