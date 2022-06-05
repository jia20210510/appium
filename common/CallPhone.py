
# coding:utf-8
from twilio.rest import Client
 
# sid和token都是在twilio网站的个人设置中看到的
account_sid = 'AC4d79e18fd3a75ab644598348e510375e'
auth_token = '6893b0ce47570760803ad5db4cc210ac'
# 实例化
client = Client(account_sid, auth_token)


# 开始发短信
def send_msg(message):
    '自定义短信内容message'
    msg = client.messages.create(
        to='+8615651797525',  # 要给谁发短信, 必须带区号, 中国要加上+86
        from_='+12013351008', # 你自己twilio网站申请的手机号码, 必须带上+号
        body=message  # 你的短信内容
    )


# 开始打电话
def call_num(number):
    u'自定义打电话的号码'
    call = client.calls.create(
        to='+86'+number,  # 要给谁打电话, 必须带区号, 中国要加上+86
        from_='+12013351008', # 你自己twilio网站申请的手机号码, 必须带上+号
        url="http://demo.twilio.com/docs/voice.xml" # 要播放的mp3
    )


if __name__ == '__main__':
    send_msg('伤心')
'''

第一步：安装twilio库

cmd输入命令 pip install twilio

第二步：

申请获得twilio的API Credentials

打开twilio网站：https://www.twilio.com/

1.先注册后登录进去

2.验证手机, 点击右上角, 个人设置, Phone Number

3. 创建项目, sms或voice都可以

4.获取一个手机号

5.setting中还可以看到编码需要的ACCOUNT SID和auth_token

'''