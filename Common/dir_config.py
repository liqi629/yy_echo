# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 10:06
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : dir_config.py
# @Software : PyCharm
import os

'''
路径切分，base_dir为根目录即项目目录
其他文件目录，使用时，拼接上根目录
'''

base_dir=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

#配置文件路径

case_config_path=os.path.join(base_dir, 'Config', 'case.Config')


#html报告的路径
report_path=os.path.join(base_dir, 'TestResult', 'reports', 'report.html')

#日志文件路径
logs_dir=os.path.join(base_dir, 'TestResult', 'logs')
#截图文件路径
screenshot_dir=os.path.join(base_dir, 'TestResult', 'imgs')

#数据库配置文件路径
db_config_path=os.path.join(base_dir, 'Config', 'db.config')
#浏览器运行模式配置/无头/正常
browser_config_path=os.path.join(base_dir, 'Config', 'browser.config')
#从远程服务器下载文件存储路径
ftp_auto_text_01 = os.path.join(base_dir, 'TestDatas', 'local_auto_text_01')

if __name__ == '__main__':
    # print(case_config_path)
    # print(report_path)
    # print(logs_dir)
    print(db_config_path)