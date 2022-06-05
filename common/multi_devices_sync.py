from common.emulator_desired import desired
import multiprocessing

driver = desired()
devices_list = ['127.0.0.1:62027', '127.0.0.1:62028']

# 构建desired进程组
desired_process = []

for i in range(len(devices_list)):
    port = 4723+2*i
    # 加载进程，target:可执行的函数，args有两个参数：UDID和port
    desired=multiprocessing.Process(target=desired, args=(devices_list[i], port))

    # 添加进程
    desired_process.append(desired)


if __name__ == '__main__':
    # 并发执行
    for desired in desired_process:
        desired.start()

    # 等子进程全部运行完再关闭
    for desired in desired_process:
        desired.join(1)


