# -*- coding: utf-8 -*-
# @Time     : 2019/11/2717:54
# @Author   : l7
# @File     : db2_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By


class DB2Locator:
    # DB2数据库，操作相关========================================================================
    # 数据库-DB2
    DB2 = (By.XPATH, ' //span[text()="DB2"]')

    # 数据库选择后的确认按钮
    db_button = (By.XPATH, '//a[@id="btn-db-type"]')
    # 数据类型为DB2，新增按钮
    add_button_db2 = (By.XPATH, '//form[@name="com.kingbase.Driver"]//button[@id="addSource"]')

    # 连接名称输入框
    source_name = (By.XPATH, '//form[@name="com.kingbase.Driver"]//input[@id="sourceName"]')
    # ip输入框
    # ip = (By.ID, 'ip')
    ip = (By.XPATH, '//form[@name="com.kingbase.Driver"]//input[@id="ip"]')
    # 端口
    port = (By.XPATH, '//form[@name="com.kingbase.Driver"]//input[@id="port"]')
    # 用户名
    user_name = (By.XPATH, '//form[@name="com.kingbase.Driver"]//input[@id="userName"]')
    # 密码
    pass_word = (By.XPATH, '//form[@name="com.kingbase.Driver"]//input[@id="passWord"]')
    # 所属系统下拉三角按钮
    select_system = (
    By.XPATH, '//span[@id="select2-belongToSysName-container"]//parent::span//span[@class="select2-selection__arrow"]')
    # 所属系统的select
    select_option = (By.XPATH, '//span[@dir="ltr"]//parent::div//select[@id="belongToSysName"]')
    select = (By.XPATH, '//*[@id="form-fieldset"]//span[@class="select2-selection__arrow"]')
    # 数据库名称
    db_name = (By.XPATH, '//form[@name="com.kingbase.Driver"]//input[@id="dbName"]')
    # 环境类型
    environment_type = (By.XPATH, '//form[@name="com.kingbase.Driver"]//select[@id="environmentType"]')
    # 是否跨域
    cross_domain = (By.XPATH, '//form[@name="com.kingbase.Driver"]//select[@id="crossDomain"]')
    # 编码设置
    character_encoding = (By.XPATH, '//form[@name="com.kingbase.Driver"]//select[@id="characterEncoding"]')
    # 备注
    mark = (By.XPATH, '//form[@name="com.kingbase.Driver"]//input[@id="remark"]')
    # 测试连接按钮
    test_connect = (By.XPATH, '//form[@name="com.kingbase.Driver"]//a[@id="test-connect"]')
    # 测试连接的toast:
    test_msg = (By.XPATH, '//span[text()="连接成功"]')
    # 上一步按钮
    last_step = (By.XPATH, '//a[text()="上一步"]')
    # 下一步按钮
    next_step = (By.XPATH, '//a[text()="下一步"]')

    # 数据源表
    db2_tb_city = (By.XPATH, '//input[@data-name="CITY"]')

    # 数据源节点
    node_db2_source_1 = (By.XPATH, '//span[text()="db2_source_1"]')



if __name__ == '__main__':

    a =  '//form[@name="com.kingbase.Driver"]'
    v = (By.XPATH, a+'//input[@id="sourceName"]')
    print(v)
    print(DB2Locator().source_name)