# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: apriceium
@File: debug.PY
@Date: 2021/11/6 21:40
@Author: jia
@Description:
"""


# number   # 数字类型 1,3,888
# string   #字符串类型   "姐来了","aaa"，'hello'
# boolean    #   true false


def coffe():
    price = input("请输入单价")
    print("咖啡单价是%s元" % price)
    
    count = input("please input coffee price")
    print("您点了%s杯咖啡" % count)

    print("您需要支付%s 元" % (int(price)*int(count)))


def sum(a, b):
    sum = a+b
    print("求和：%s" % sum)


def subtraction(a, b):
    result = a-b
    print("两数相减等于：", result)

# 求两数之积
def multiplication(a,b,c):
    result=a*b*c
    print("相乘结果是：%s"% result)


def division (*args):
    a,b,c= args
    result=a/b/c
    print("相除结果是：%s" %result)

def tub():
    key = (12, '123')
    print(key[1],type(key[1]))
if __name__ == '__main__':
    #sum(3, 8)
    #subtraction(11, 36)
    # multiplication(989,71,23)
    # division(989,78,56)
    tub()



