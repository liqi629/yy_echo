# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 10:11
# @Author   : l7
# @File     : loginPage_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By


class LoginPageLocator:
    # 用户名输入框
    user_input = (By.XPATH, '//input[@name="username"]')
    # 密码输入框
    passwd_input = (By.XPATH, '//input[@name="password"]')
    # 登陆按钮
    login_button = (By.XPATH, '//span[text()="登 录"]')

    erro_msg = (By.XPATH, '//*[text()="用户名或密码错误!"]')
