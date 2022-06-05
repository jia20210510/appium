from test_case.multi_appium import appium_start
from test_case.multi_devices import appium_desired
from common.check_port import *
from time import sleep
import multiprocessing


devices_list = ['127.0.0.1:62001', '127.0.0.1:62026']


# 端口是否被占用
def check_server_port(host, port):
    if check_port(host, port):
        return True
    else:
        print('appium %s start fail' % port)
        return False


# 如果appium服务器端口可用就启动服务器和APP,否则关闭占用端口
def start_devices_action(udid, port, sysport):
    host = '127.0.0.1'
    if check_server_port(host, port):
        # 启动服务器
        appium_start(host, port)
        # 执行登录功能
        appium_desired(udid, port, sysport)
    else:
        release_port(port)


# 同时启动多个appium服务
def appium_start_sync():
    print('=====appium_start_sync=====')

    appium_process = []

    for i in range(len(devices_list)):
        host = '127.0.0.1'
        port = 4723 + 2 * i

        appium = multiprocessing.Process(target=check_server_port, args=(host, port))
        appium_process.append(appium)

    for appium in appium_process:
        appium.start()
    for appium in appium_process:
        appium.join()

    sleep(5)


#  同时启动多个设备
def devices_star_sync():

    print('======devices_star_sync===')

    desired_process = []

    for i in range(len(devices_list)):
        port = 4723 + 2 * i
        sysport= 8200+i
        desired = multiprocessing.Process(target=start_devices_action, args=(devices_list[i], port,sysport))
        desired_process.append(desired)

    for desired in desired_process:
        desired.start()
    for desired in desired_process:
        desired.join()


if __name__ == '__main__':
    appium_start_sync()
    devices_star_sync()

