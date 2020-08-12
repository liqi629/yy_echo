# -*- coding: utf-8 -*-
# @Time     : 2019/11/110:38
# @Author   : l7
# @File     : ttest_4_app_manager.py
# @Software : PyCharm
import pytest

from PageObjects.home_page import HomePage as HP
from PageLocators.homePage_locator import HomePageLocator as hp_loc
from TestDatas.home_datas import operation_system_1 as os
from TestDatas.home_datas import operation_system_2 as os_2
from TestDatas.home_datas import HomeDatas

@pytest.mark.usefixtures("class_home")
@pytest.mark.usefixtures("case_home")
class TestAppManager:

    # 添加一个业务系统:功能自动化测试一
    def test_1_add_operation_system(self, class_home):
        HP(class_home[0]).add_operation_system(os["zh_name"], os["code"], os["short_zn_name"],
                                               os["en_name"], os["short_en_name"], os["sys_remark"],
                                               os["sys_version"], os["dept"], os["contacter"],
                                               os["mobile"], os["email"])
        msg = HP(class_home[0]).is_add_operation_system()
        assert msg == True

    # 查看业务系统详情：功能自动化测试一
    def test_2show_operation_system(self, class_home):
        HP(class_home[0]).look_operation_system_sys_1()
        msg =  HP(class_home[0]).is_look_operation_system()
        assert msg == True

    # 编辑业务系统：功能自动化测试二
    @pytest.mark.usefixtures("case_4_3")
    def test_3_edit_operation_system(self, class_home):
        # 操作步骤：选择业务系统：功能自动化测试一，点击编辑，输入新的业务系统信息：功能自动化测试二，点击确定
        HP(class_home[0]).edit_operation_system_sys_1(os_2["zh_name"], os_2["code"], os_2["short_zn_name"],
                                                      os_2["en_name"], os_2["short_en_name"], os_2["sys_remark"],
                                                      os_2["sys_version"], os_2["dept"], os_2["contacter"],
                                                      os_2["mobile"], os_2["email"])
        msg = HP(class_home[0]).is_add_operation_system(hp_loc.sys_name_at_2)
        assert msg == True

    # 中文简称搜索：自动化测试二
    def test_4_search_short_zn_name_1(self, class_home):
        # 操作步骤:输入中文简称,点击搜索.预期:搜索有结果
        HP(class_home[0]).search__short_zn_name(os_2["short_zn_name"])
        msg = HP(class_home[0]).is_add_operation_system(hp_loc.sys_name_at_2)
        assert msg == True

    # 中文简称搜索：自动化测试一
    def test_5_search_short_zn_name_2(self, class_home):
        # 操作步骤:输入中文简称,点击搜索.预期:搜索没有结果
        HP(class_home[0]).search__short_zn_name(os["short_zn_name"])
        msg = HP(class_home[0]).is_search_empty()
        assert msg == True

    # 英文简称搜索：autoTestTwo
    def test_6_search_short_en_name_1(self, class_home):
        # 操作步骤:输入英文简称,点击搜索.预期:搜索有结果
        HP(class_home[0]).search__short_en_name(os_2["short_en_name"])
        msg = HP(class_home[0]).is_add_operation_system(hp_loc.sys_name_at_2)
        assert msg == True

    # 英文简称搜索：autoTestOne
    def test_7_search_short_en_name_2(self, class_home):
        # 操作步骤:输入英文简称,点击搜索.预期:搜索没有结果
        HP(class_home[0]).search__short_en_name(os["short_en_name"])
        msg = HP(class_home[0]).is_search_empty()
        assert msg == True

    # 部门搜索：产品质量保障二部
    def test_8_search_dept_1(self, class_home):
        # 操作步骤:输入部门,点击搜索.预期:搜索有结果
        HP(class_home[0]).search_dept(os_2["dept"])
        msg = HP(class_home[0]).is_add_operation_system(hp_loc.sys_name_at_2)
        assert msg == True

    # 部门搜索：产品质量保障一部
    def test_9_search_dept_2(self, class_home):
        # 操作步骤:输入部门,点击搜索.预期:搜索没有结果
        HP(class_home[0]).search_dept(os["dept"])
        msg = HP(class_home[0]).is_search_empty()
        assert msg == True

    # 系统状态搜索：正常
    def test_10_search_sys_status(self, class_home):
        # 操作步骤:输入正常,点击搜索.预期:搜索有结果
        HP(class_home[0]).search_sys_status(os_2["sys_status"])
        msg = HP(class_home[0]).is_add_operation_system(hp_loc.sys_name_at_2)
        assert msg == True

    # 系统状态搜索：异常
    def test_11_search_sys_status(self, class_home):
        # 操作步骤:输入异常,点击搜索.预期:搜索没有结果
        HP(class_home[0]).search_sys_status(os_2["sys_status_e"])
        msg = HP(class_home[0]).is_search_empty()
        assert msg == True

    # 时间搜索：
    def test_12_search_up_datetime(self, class_home):
        # 操作步骤:输入部门,点击搜索.预期:搜索有结果
        HP(class_home[0]).search_app_time(getattr(HomeDatas, "app_manager_start_time"), getattr(HomeDatas, "app_manager_end_time"))
        msg = HP(class_home[0]).is_add_operation_system(hp_loc.sys_name_at_2)
        assert msg == True


    # 删除一个业务系统：功能自动化测试二
    @pytest.mark.flaky(reruns=1, reruns_delay=5)
    def test_delete_operation_system(self, class_home):
        HP(class_home[0]).delete_operation_system()
        msg = HP(class_home[0]).is_add_operation_system(hp_loc.sys_name_at_2)
        assert msg == False