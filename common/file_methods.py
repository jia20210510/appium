# _*_ coding:utf-8 _*_
"""
@Coding: utf-8
@Version: python3.8
@Project: appium
@File: file_method.PY
@Date: 2022/5/28 21:03
@Author: jia
@Description:
"""
import os
import shutil
import yaml


class FileMethod:

    # 清除文件夹
    @classmethod
    def clean_dir(cls, dir_path):
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        else:
            shutil.rmtree(dir_path)
            os.mkdir(dir_path)

    # 取项目根目录
    @classmethod
    def get_project_path(cls, project_name):
        base_dir = os.getcwd()
        root_path = base_dir[:base_dir.find(project_name + "\\") + len(project_name + "\\")]
        project_path = root_path.replace("\\", '/')
        print('project_path:', project_path)
        return project_path

    # 向文件写入
    @classmethod
    def write_file(cls, file_path, write_text):
        with open(file_path, 'w', encoding='utf-8') as wf:
            wf.write(write_text)

    # 读取yaml文件数据
    @classmethod
    def read_yaml(cls, f_path):
        with open(f_path, encoding='utf-8', mode='r') as f:
            ff = yaml.load(f, Loader=yaml.FullLoader)
            return ff

    # 向YAML文件写入数据
    @classmethod
    def write_yaml(cls, f_path, f_data):
        with open(f_path, encoding='utf-8', mode='w') as wf:
            yaml.dump(f_data, stream=wf)

    # 将yaml文件内容清除
    @classmethod
    def clear_yaml(cls, f_path):
        with open(f_path, encoding='utf-8', mode='r+') as cf:
            cf.truncate()

    # 取根目录中extract文件的值
    @classmethod
    def read_extract_yaml(cls, project_name, one_name):
        with open(str(cls.get_project_path(project_name) + 'extract.yaml.yaml.yml'), mode='r', encoding='utf-8') as rf:
            extract = yaml.load(rf.read(), Loader=yaml.FullLoader)
            return extract[one_name]

    # 修改yaml数据
    @classmethod
    def test_modify(cls, f_path, in_para, one_name, two_name):
        """
        修改YAML文件参数
        f_path: 打开文件的路径
        in_para: 输入的参数
        one_name: 字典第一个key
        two_name: 字典第二个kdy
        """
        with open(f_path) as f:
            doc = yaml.safe_load(f)
            doc[one_name][two_name] = in_para
        with open(f_path, 'w') as wf:
            yaml.safe_dump(doc, wf, allow_unicode=True)