from appium import webdriver
import yaml
from time import ctime
from homelinking.loginView import LoginView


with open('../config/android_emulator.yaml','r') as file:
    data = yaml.full_load(file)

devices_list=['127.0.0.1:62001', '127.0.0.1:62026']


def appium_desired(udid, port, sysport):
    desired_caps = dict()
    desired_caps['platformName'] = data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']
    desired_caps['automationName']=data['automationName']
    desired_caps['systemPort'] =sysport
    desired_caps['udid']=udid

    # desired_caps['app']=Data['app']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']
    desired_caps['noReset']=data['noReset']

    print('appium port:%s start run %s at %s' %(port,udid,ctime()))
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(port)+'/wd/hub',desired_caps)
    driver.implicitly_wait(5)

    l = LoginView()
    l.check_authority()
    l.login_action()
    l.logout_action()
    return driver


if __name__ == '__main__':
    appium_desired(devices_list[0],4723)
    appium_desired(devices_list[1],4725)