import subprocess
from time import ctime
import multiprocessing


def app_start(host_addr, port_num):
    # appium与设备通信的端口
    bootstrap_port = str(port_num + 1)
    # 启动appium服务器命令，/b指后台运行
    cmd = 'start /b appium -a ' + host_addr + ' -p ' + str(port_num) + ' -bp ' + str(bootstrap_port)

    print('%s at %s' % (cmd, ctime()))
    # 开启一个子进程
    subprocess.Popen(cmd, shell=True, stdout=open('../Log/'+str(port_num)+'.log', 'a'),
                     stderr=subprocess.STDOUT)


appium_process = []

for i in range(2):
    host = '127.0.0.1'
    port = 4723+2*i
    # 载入进程
    appium=multiprocessing.Process(target=app_start, args=(host, port))
    # 添加进程
    appium_process.append(appium)

if __name__ == '__main__':
    for appium in appium_process:
        appium.start()
    for appium in appium_process:
        appium.join()