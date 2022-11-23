# APP 自动化项目

## 项目介绍：

使用APPIUM对APP界面功能进行验证，技术框架appium+pytest+allure

## 技术特点：
1,关键字驱动

2，使用yaml、excel.csv编辑测试用例

3,allure自动生成测试报告

4,使用pytest库插件可实现测试用例失败生跑，跳过不需要执行的测试用例，执行指定标记的测试用例

5,使用pytest库后，_init_初始化方法将不可用

6,模块名以test_开头或_test结尾；类名以Test开头；方法名以test开头，可在pytest.ini中自定义

## 页面展示：
![image](https://user-images.githubusercontent.com/83941545/203574262-9bcbbcb9-db37-4aee-b01a-6e59419e670a.png)
![image](https://user-images.githubusercontent.com/83941545/203574477-a0efa1f5-f0b3-4edd-87b7-d76289ae4fd8.png)

## 安装环境：
win 10

python 3.8

pytest 6.2.4

allure 2.9.43

flask 2.0.1

html 3.1.1

## 如何安装：
pip install -r requirement_plugin.txt 安装所有使用插件

插件介绍：

pytest-ordering      安装插件后可指定执行顺序

pytest-xdist         安装插件用于多线程运行用例

pytest-rerunfailures 安装插件用于失败重跑

pytest-html          安装插件用于输出报告

allure_report-pytest  安装插件美化报告

fixture              安装插件做用例的前置和后置
