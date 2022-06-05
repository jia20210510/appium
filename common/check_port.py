import socket
import os


# 尝试连接一个端口，连接失败表示此端口未打开未占用
def check_port(host, port):
    # 创建一个socket对象，
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect((host, port))
        s.shutdown(2)
    except OSError as msg:
        print('port %s is available!' % port)
        print(msg)
        return True
    else:
        print('port %s already be in use! ' % port)
        return False


# 找到占用此端口的PID进程，然后关闭它
def release_port(port):
    cmd_find = 'netstat -ano |findstr %s' % port
    print(cmd_find)
    # 读取命令执行后的结果
    result = os.popen(cmd_find).read()
    print(result)
    # 如果端口号和listening都存在说明有进程打开
    if str(port) and 'LISTENING' in result:
        # 得到listening的下标值
        i = result.index('LISTENING')
        # 加上7个空格得到pid的起始下标值
        start = i+len('LISTENING')+7
        # 获取换行符做为PID的末位下标值
        end = result.index('\n')
        # 截取字符串得到PID
        pid = result[start:end]

        cmd_kill = 'taskkill -f -pid %s' % pid
        print(cmd_kill)
        os.popen(cmd_kill)
    else:
        print('port %s is available' % port)


if __name__ == '__main__':
    h = '127.0.0.1'
    p = 4725
    check_port(h, p)
    # release_port(port)


