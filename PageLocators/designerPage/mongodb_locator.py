# -*- coding: utf-8 -*-
# @Time     : 2019/11/816:36
# @Author   : l7
# @File     : mongodb_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By


class MongoLocator:
    # Mongodb数据库，操作相关========================================================================
    # 数据库-Mongodb
    MongoDB = (By.XPATH, ' //span[text()="MongoDB"]')

    # 数据库选择后的确认按钮
    btn_onfirm_type = (By.XPATH, '//a[@id="btn-db-type"]')
    # 数据类型为Mongodb，新增按钮
    add_button_mongo = (By.XPATH, '//button[@id="addSource"]')

    # 连接名称输入框
    conn_name = (By.XPATH, '//input[@id="sourceName"]')
    # conn_name_2 = (By.XPATH, '//input[@id="sourceName"]')

    ip = (By.XPATH, '//input[@id="mongodbip"]')
    port = (By.XPATH, '//input[@id="port"]')

    # 权限
    auth = (By.XPATH, '//select[@name="isAuth"]')
    # 所属系统下拉三角按钮
    select_system = (
    By.XPATH, '//span[@id="select2-belongToSysName-container"]//parent::span//span[@class="select2-selection__arrow"]')
    # 所属系统的select
    select_option = (By.XPATH, '//span[@dir="ltr"]//parent::div//select[@id="belongToSysName"]')

    # 认证数据库
    auth_database = (By.XPATH, '//input[@id="authDatabase"]')
    # 认证模式:SCRAM-SHA-1,MONGODB-CR
    auth_mode = (By.XPATH, '//select[@id="authMechanism"]')
    # 用户名
    user_name = (By.XPATH, '//input[@id="authUserName"]')
    # 密码
    pwd = (By.XPATH, '//input[@id="authPassword"]')
    # 测试连接按钮
    test_connect = (By.XPATH, '//a[text()="测试连接"]')
    # 测试连接的toast:
    test_msg = (By.XPATH, '//span[text()="测试MongoDB连接成功!"]')
    # 下一步按钮
    next_step = (By.XPATH, '//a[text()="下一步"]')
    # 数据库名称
    database = (By.XPATH, '//input[@id="manDatabase"]')
    # 按钮-获取表
    btn_get_tb = (By.XPATH, '//a[text()="获取表"]')
    # 选择表名
    select_tb = (By.XPATH, '//select[@id="tablename"]')
    # 表：city
    tb_city = (By.XPATH, '//li[text()="city"]')
    # 最终确定按钮
    confirm_button = (By.XPATH, '//a[text()="确定"]')


    # 添加后的数据节点：mongodb_source_1
    node_mongodb_source_1 = (By.XPATH, '//span[text()="mongodb_source_1"]')