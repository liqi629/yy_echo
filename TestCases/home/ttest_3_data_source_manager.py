# -*- coding: utf-8 -*-
# @Time     : 2019/10/319:34
# @Author   : l7
# @File     : ttest_3_data_source_manager.py
import pytest

from PageObjects.home_page import HomePage as hp


@pytest.mark.usefixtures("class_home_3")
@pytest.mark.usefixtures("case_home")
class TestDataSourceManager:

    # 筛选查看数据库，判断列表是否展示
    def test_1_show_data_source(self, class_home_3):
        hp(class_home_3[0]).select_unit_type("数据库")
        msg = hp(class_home_3[0]).is_at_source_1()
        assert msg == True

    # 查看详情
    def test_2_look_data_source(self, class_home_3):
        # 操作步骤：选择数据库，点击查看详情。断言：dialog弹窗标题
        hp(class_home_3[0]).look_data_source_at_source_1()
        msg = hp(class_home_3[0]).is_look_data_source()
        assert msg ==True

    # 时间筛选
    def test_3_search_up_datetime(self, class_home_3):
        # 操作步骤：选择数据库，输入开始时间和结束时间，点击查询。断言：显示添加的数据库：at_source_1
        hp(class_home_3[0]).search_up_datetime(class_home_3[1], class_home_3[2])
        msg = hp(class_home_3[0]).is_at_source_1()
        assert msg == True

    # 删除数据源

    def test_4_del_data_source(self, class_home_3):
        hp(class_home_3[0]).del_data_source_at_source_1()
        msg = hp(class_home_3[0]).is_at_source_1()
        assert msg == False