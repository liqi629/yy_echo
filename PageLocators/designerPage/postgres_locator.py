# -*- coding: utf-8 -*-
# @Time     : 2019/11/2810:41
# @Author   : l7
# @File     : postgres_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By
from PageLocators.designerPage.mysql_locator import MysqlLocator

# form表单，name="sameTOMysqlDriver"，与mysql窗口一样，继承mysql的元素定位
class PostgresLocator(MysqlLocator):
    # Postgres数据库，操作相关========================================================================
    # 数据库-Postgres
    DB2 = (By.XPATH, ' //span[text()="POSTGRESQL"]')

    # # 数据库选择后的确认按钮
    # db_button = (By.XPATH, '//a[@id="btn-db-type"]')
    # # 数据类型为Postgres，新增按钮
    # add_button_oracle = (By.XPATH, '//form[@name="com.kingbase.Driver"]//button[@id="addSource"]')
    #
    # # 连接名称输入框
    # source_name = (By.XPATH, '//form[@name="com.kingbase.Driver"]//input[@id="sourceName"]')