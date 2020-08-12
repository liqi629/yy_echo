# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 17:13
# @Author   : l7
# @File     : test_2_story_1.py
# @Software : PyCharm
import pytest
import time

from PageObjects.home_page import HomePage as hp
from PageObjects.designer_page import DesignerPage as dp

from PageLocators.homePage_locator import HomePageLocator as hp_loc
from PageLocators.designerPage_locator import DesignerPageLocator as dp_loc

from TestDatas import story_datas as sd
from TestDatas.story_datas import mysql_node_info, map_name, operation_system_1



@pytest.mark.smoke
@pytest.mark.usefixtures("class_home")
@pytest.mark.usefixtures("case_home")
class TestUserStoryOne():
    """
    用户故事一：基础功能，没有涉及特殊的操作，比如系统变量、数据源和系统依赖验证
    内容：添加应用-目录-映射-工作流--试运行-删除工作流-删除工作流涉及-删除映射-删除数据源-删除应用-删除工作目录
    数据：自动化测试目录，映射_mysql_city，mysql_qc_city，自动化测试一
"""

    @pytest.mark.parametrize("data", operation_system_1)
    def test_add_operation_system(self, browser, data):
        """
        名称：添加应用
        前置：登录系统
        步骤：
        1、点击资源管理展开菜单
        2、点击应用管理
        3、点击添加，输入应用信息
        4、点击确定
        检查点：
        * 检查页面弹出的提示信息。
        """

        hp(browser).add_operation_system(data["zh_name"], data["code"], data["short_zn_name"],
                                         data["en_name"], data["short_en_name"], data["sys_remark"],
                                         data["sys_version"], data["dept"], data["contacter"],
                                         data["mobile"], data["email"])
        msg = hp(browser).get_text(hp_loc.toast_msg)
        assert msg == '保存成功!'

    def test_add_work_dir(self, browser):
        """
        名称：添加工作目录
        步骤：
        1、点击工作目录管理
        2、点击添加，输入信息:目录名字和描述
        3、点击确定
        检查点：
        * 检查页面弹出的提示信息。
        """
        hp(browser).add_work_dir(sd.work_dir_name, remark="这是自动化测试运行时添加的工作目录")
        msg = hp(browser).get_text(hp_loc.toast_msg)
        assert msg == '添加工作目录成功!'

    def test_add_map(self, browser):
        """
        名称：添加映射
        步骤：
        1、点击工作目录的进入按钮-映射设计器
        2、切换到新的页面，点击创建映射的+
        3、输入映射名称
        4、点击确定
        检查点：
        * 检查页面弹出的提示信息。添加映射成功!
        """
        dp(browser).add_map(sd.work_dir_name)
        dp(browser).add_job(job_name=sd.map_name)
        msg = dp(browser).get_text(dp_loc.toast_msg)
        assert msg == '添加映射成功'

    @pytest.mark.parametrize("data", mysql_node_info)
    def test_add_datanode(self, browser, data):
        """
        名称：添加数据节点,通过参数化的方式添加源和目标，共2个
        步骤：
        1、点击数据源-添加
        2、选择数据源类型，点击确定
        3、在弹出窗口，点击新增按钮
        4、输入数据信息，点击测试连接
        5、点击下一步-下一步-下一步-确定
        6、点击保存
        检查点：
        * 检查页面弹出的提示信息。
        * 检查页面是否有数据节点。
        """
        dp(browser).add_data_node_mysql(data["data_type"], data["job"], data["source_name"],data["ip"],
                                        data["port"], data["user_name"],data["pass_word"], data["db_name"],
                                        data["table"], data["sys_name"])
        msg = dp(browser).get_text(dp_loc.toast_msg)
        assert msg == '更新映射成功'

    def test_pub_map(self, browser):
        """
        名称：发布映射
        步骤：
        1、选择作业，批量连线
        2、保存-发布
        检查点：
        * 检查页面弹出的提示信息。
        """
        dp(browser).on_line(map_name)
        msg = dp(browser).get_text(dp_loc.toast_msg)
        assert msg == '映射发布成功\n更新映射成功' or msg == '映射发布成功'
    def test_create_work_flow(self, browser):
        """
        名称：快速生成工作流
        步骤：
        1、选择作业，点击快速生成工作流
        2、输入名称和描述信息
        3、点击确定
        4、切换到设计器页面，刷新
        检查点：
        * 检查页面是否有作业。
        * 检查页面是否有工作流。
        """
        dp(browser).cre_work_flow(sd.work_flow_name, "自动化测试：工作流的描述")

        msg = dp(browser).get_text(dp_loc.text_to_loc(sd.work_flow_name))
        msg_1 = dp(browser).get_text(dp_loc.text_to_loc(sd.map_name))

        assert msg == sd.work_flow_name
        assert msg_1 == sd.map_name

    def test_pilt_run(self, browser):
        """
        名称：试运行
        步骤：
        1、点击数据源-添加
        2、选择数据源类型，点击确定
        3、在弹出窗口，点击新增按钮
        4、输入数据信息，点击测试连接
        5、点击下一步-下一步-下一步-确定
        6、点击保存
        检查点：
        * 检查页面运行状态信息。
        """
        dp(browser).pilt_run(sd.work_flow_name)
        time.sleep(10)
        msg = dp(browser).is_run_status()
        assert msg == True

    def test_del_work_flow(self, browser):
        """
        名称：删除工作流
        步骤：
        1、选择工作流，点击删除图标
        2、在弹出的确认窗口点击确认
        检查点：
        * 检查页面弹出信息，删除成功!
        """
        dp(browser).del_work_flow(sd.work_flow_name)
        time.sleep(1)
        msg = dp(browser).is_loc_show(loc=dp_loc.text_to_loc(sd.work_flow_name))
        assert msg ==False

    def test_del_job(self, browser):
        """
        名称：删除作业
        步骤：
        1、选择作业，点击删除图标
        2、在弹出的确认窗口点击确认
        检查点：
        * 检查页面弹出信息，删除成功!
        """
        dp(browser).del_job(sd.map_name)
        time.sleep(1)
        msg = dp(browser).is_loc_show(loc=dp_loc.text_to_loc(sd.map_name))
        assert msg ==False

    def test_del_map(self, browser):
        """
        名称：删除映射
        步骤：
        1、进入映射设计器，选择映射，点击删除图标
        2、在弹出的确认窗口点击确认
        检查点：
        * 检查页面弹出信息，删除成功!
        """
        current_handles = dp(browser).current_handles()
        dp(browser).switch_window(current_handles[-1])
        dp(browser).del_map(sd.map_name)
        time.sleep(1)
        msg = dp(browser).is_loc_show(loc=dp_loc.text_to_loc(sd.map_name))
        assert msg ==False

    def test_del_work_dir(self, browser):
        """
        名称：删除工作目录
        步骤：
        1、进入工作目录，选择工作目录，点击删除图标
        2、在弹出的确认窗口点击确认
        检查点：
        * 检查页面弹出信息，删除成功!
        """
        # current_handles = dp(browser).current_handles()
        hp(browser).switch_window("default")
        hp(browser).del_work_dir(sd.work_dir_name)
        msg = hp(browser).get_text(hp_loc.toast_msg)
        assert msg == '删除工作目录成功,删除行数[1]'


    def test_delete_operation_system(self, browser):
        """
        名称：删除应用
        步骤：
        1、进入应用管理，选择应用，点击删除
        2、在弹出的确认窗口点击确认
        检查点：
        * 检查页面弹出的提示信息。
        """
        hp(browser).refresh()
        hp(browser).delete_operation_system("自动化测试一")
        msg = hp(browser).get_text(hp_loc.toast_msg)
        assert msg == '删除成功!'


