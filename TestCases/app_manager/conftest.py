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
from TestDatas import login_datas as ld
from config import RunConfig


@pytest.fixture(scope="class")
def class_home():
    print("============整个测试类只执行一次的前置======================")
    global driver
    driver = RunConfig.driver
    driver.get(RunConfig.url)
    LoginPage(driver).login(ld.ID_2['user'], ld.ID_2['pwd'])
    yield [driver]
    print("============整个测试类只执行一次的后置======================")
    # HomePage(driver).logout()
@pytest.fixture()
def case_home():
    global driver
    print("============测试类中每个测试用例都执行一次的前置============")
    driver.refresh()
    time.sleep(2)
    yield

    print("============测试类中每个测试用例都执行一次的后置============")

