# -*- coding: utf-8 -*-
# @Time     : 2019/6/25 15:24
# @Author   : l7
# @File     : 1conftest.py
# @Software : PyCharm
import pytest
import time
import datetime

from PageObjects.home_page import HomePage
from PageObjects.login_page import LoginPage
from PageObjects.designer_page import DesignerPage
from TestDatas import Common_Datas as CD
from TestDatas.home_datas import operation_system_2 as os_2
from TestDatas import login_datas as ld
from TestDatas import designer_datas as dd
from TestDatas.designer_datas import DesignerDatas
from PageLocators.homePage_locator import HomePageLocator as hp_loc

from PageLocators.designerPage_locator import DesignerPageLocator as dp_loc
# from config import RunConfig

# #
#
# @pytest.fixture(scope="class")
# def login_class():
#     print("============整个测试类只执行一次的前置======================")
#     driver =browser()
#     driver.get("www.baidu.com")
#
#
#
#     print("============整个测试类只执行一次的后置======================")
from config import RunConfig
@pytest.fixture(scope="class")
def login_class():
    print("============整个测试类只执行一次的前置======================")
    global driver
    driver = RunConfig.driver
    yield

    print("============整个测试类只执行一次的后置======================")

@pytest.fixture()
def login_case():
    print("============函数的前置======================")
    driver = RunConfig.driver
    time.sleep(5)
    driver.get(CD.login_url)
    yield
    driver.refresh()

    print("============函数的后置======================")


    #
    #
    # print("============整个测试类只执行一次的后置======================")

