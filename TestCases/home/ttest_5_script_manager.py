# -*- coding: utf-8 -*-
# @Time     : 2019/11/414:53
# @Author   : l7
# @File     : ttest_5_script_manager.py
# @Software : PyCharm

import pytest

from PageObjects.script_manager_page import ScriptManagerPage as SMP
from TestDatas.designer_datas import script
from TestDatas.designer_datas import search
from TestDatas.designer_datas import DesignerDatas


@pytest.mark.usefixtures("d_class")
@pytest.mark.usefixtures("case_designer_5")
class TestScriptManager:

    # 添加脚本:gbase_loader_1
    def test_1_add_script(self, d_class):
        SMP(d_class[0]).add_script(script["name"], script["AP"], script["content"],
                                   script["ip"], script["scriptType"], script["dbType"])
        assert SMP(d_class[0]).is_addScript() == True

    # 查看脚本:gbase_loader_1
    def test_2_look_script(self, d_class):
        SMP(d_class[0]).look_script()
        msg = SMP(d_class[0]).is_look_script()
        assert msg == True

    # 编辑脚本:名称修改为gbase_loader_2
    @pytest.mark.usefixtures("case_designer_5_3")
    def test_3_edit_script(self, d_class):
        SMP(d_class[0]).edit_script(script["new_name"])
        msg = SMP(d_class[0]).is_edit_script()
        assert msg == True

    # 启用脚本
    def test_4_start_script(self, d_class):
        SMP(d_class[0]).start_script()
        msg = SMP(d_class[0]).is_start_script()
        assert msg == True

    # 筛选-脚本状态：启用
    def test_5_search_status_1(self, d_class):
        SMP(d_class[0]).search__status(search["status_1"])
        msg = SMP(d_class[0]).is_edit_script()
        assert msg == True

    # 筛选-脚本状态：禁用
    def test_5_search_status_2(self, d_class):
        SMP(d_class[0]).search__status(search["status_0"])
        msg = SMP(d_class[0]).is_search_empty()
        assert msg == True

    # 筛选-脚本名称:存在
    def test_6_search_name_1(self, d_class):
        SMP(d_class[0]).search_name(script["new_name"])
        msg = SMP(d_class[0]).is_edit_script()
        assert msg == True

    # 筛选-脚本名称:不存在
    def test_6_search_name_2(self, d_class):
        SMP(d_class[0]).search_name(script["name"])
        msg = SMP(d_class[0]).is_search_empty()
        assert msg == True

    # 筛选-脚本操作类型：客户端命令
    def test_7_search_type_1(self, d_class):
        SMP(d_class[0]).search_type(search["type_2"])
        msg = SMP(d_class[0]).is_edit_script()
        assert msg == True

    # 筛选-脚本操作类型：导入
    def test_7_search_type_2(self, d_class):
        SMP(d_class[0]).search_type(search["type_0"])
        msg = SMP(d_class[0]).is_search_empty()
        assert msg == True

    # 筛选-数据库类型:GBASE
    def test_8_search_db_1(self, d_class):
        SMP(d_class[0]).search_db(search["db_7"])
        msg = SMP(d_class[0]).is_edit_script()
        assert msg == True
    # 筛选-数据库类型:MYSQL
    def test_8_search_db_2(self, d_class):
        SMP(d_class[0]).search_db(search["db_0"])
        msg = SMP(d_class[0]).is_search_empty()
        assert msg == True

    # 筛选-时间
    def test_9_search__up_datetime(self, d_class):
        SMP(d_class[0]).search_up_datetime(getattr(DesignerDatas, "app_manager_start_time"), getattr(DesignerDatas, "app_manager_end_time"))
        msg = SMP(d_class[0]).is_edit_script()
        assert msg == True

    # 删除脚本
    def test_10_del_script(self, d_class):
        SMP(d_class[0]).delScript()
        assert SMP(d_class[0]).is_delScript() == False
