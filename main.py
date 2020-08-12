# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 11:25
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : main.py
# @Software : PyCharm
import pytest
import allure

'''
测试使用非admin账号进行，如果数据库用户账户被清除，需要测试之前新建用户
'''


# 全部测试
pytest.main(["--html=TestResult/reports/report.html","--self-contained-html","--junitxml=TestResult/reports/report.xml"])

# 冒烟测试
# pytest.main(["-m=smoke","--html=TestResult/reports/report.html","--junitxml=TestResult/reports/report.xml"])
# pytest.main(["-m=demotest", "--html=TestResult/reports/report.html"])
# pytest.main(["-m=smoke",'-s', '-q', '--alluredir', './TestResult'])


# pytest.main(["-m=smoke","--html=TestResult/reports/report.html","--self-contained-html","--junitxml=TestResult/reports/report.xml"])

#执行完毕之后，发送测试报告
# sendEmail().send_email('liqi_629@163.com',dir_config.report_path)