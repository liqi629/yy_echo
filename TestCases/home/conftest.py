# -*- coding: utf-8 -*-
# @Time     : 2019/6/25 15:24
# @Author   : l7
# @File     : 1conftest.py
# @Software : PyCharm
import pytest
import time
import datetime

from PageObjects.login_page import LoginPage
from PageObjects.designer_page import DesignerPage
from TestDatas import login_datas as ld
from TestDatas import Common_Datas as CD
from PageObjects.home_page import HomePage
from PageLocators.designerPage_locator import DesignerPageLocator as dp_loc
from PageLocators.homePage_locator import HomePageLocator as hp_loc
from TestDatas.designer_datas import sucess_source as ss
from TestDatas.home_datas import operation_system_2 as os_2
from TestDatas import designer_datas as dd
from TestDatas.home_datas import HomeDatas
from config import RunConfig


@pytest.fixture(scope="class")
def class_home():
    print("============整个测试类只执行一次的前置======================")
    global driver
    driver = RunConfig.driver
    driver.get(CD.login_url)
    LoginPage(driver).login(ld.ID_2['user'], ld.ID_2['pwd'])
    yield [driver]
    print("============整个测试类只执行一次的后置======================")
@pytest.fixture()
def case_home():
    global driver
    print("============测试类中每个测试用例都执行一次的前置============")
    time.sleep(1)
    driver.refresh()
    yield
    time.sleep(1)
    print("============测试类中每个测试用例都执行一次的后置============")


@pytest.fixture(scope="class")
def class_home_3():
    print("============整个测试类只执行一次的前置======================")
    global driver
    driver.get(CD.login_url)
    LoginPage(driver).login(ld.ID_2['user'], ld.ID_2['pwd'])
    HomePage(driver).into_operation_system()
    HomePage(driver).switch_iframe(hp_loc.main_frame)
    if HomePage(driver).is_add_operation_system() == True:
        driver.get(CD.designer_url)
    else:
        driver.get(CD.home_url)
        HomePage(driver).add_operation_system(os_2["zh_name"], os_2["code"], os_2["short_zn_name"],
                                              os_2["en_name"], os_2["short_en_name"], os_2["sys_remark"],
                                              os_2["sys_version"], os_2["dept"], os_2["contacter"],
                                              os_2["mobile"], os_2["email"])
        driver.get(CD.designer_url)

    DesignerPage(driver).add_job(dd.job_at_01)
    time.sleep(2)
    driver.refresh()
    # 开始时间
    start_time = (datetime.datetime.now() + datetime.timedelta(minutes=-2)).strftime('%Y-%m-%d %H:%M')
    DesignerPage(driver).add_data_node_mysql("source", dp_loc.job_at_01, ss["source_name_2"], ss["ip"],
                                             ss["port"],
                                             ss["user_name"], ss["pass_word"], ss["sys_name"], ss["db_name"],
                                             dp_loc.mysql_common)
    DesignerPage(driver).switch_alert()
    time.sleep(1)
    # 结束时间
    end_time = (datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime('%Y-%m-%d %H:%M')
    driver.get(CD.home_url)
    yield [driver, start_time, end_time]
    driver.get(CD.designer_url)
    time.sleep(1)
    DesignerPage(driver).delete_job(dp_loc.job_at_01)
    driver.get(CD.home_url)
    HomePage(driver).delete_operation_system(hp_loc.btn_del_at_2)
    driver.quit()
    print("============整个测试类只执行一次的后置======================")

@pytest.fixture()
def case_4():
    global driver

    print("============测试类中每个测试用例都执行一次的前置============")
    yield
    print("============测试类中每个测试用例都执行一次的后置============")

@pytest.fixture()
def case_4_3():


    print("============测试类中每个测试用例都执行一次的前置============")
    # 开始时间
    start_time = (datetime.datetime.now() + datetime.timedelta(minutes=-1)).strftime('%Y-%m-%d %H:%M')
    setattr(HomeDatas, "app_manager_start_time", start_time)
    yield
    # 结束时间
    end_time = (datetime.datetime.now() + datetime.timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M')
    setattr(HomeDatas, "app_manager_end_time", end_time)
    print("============测试类中每个测试用例都执行一次的后置============")

