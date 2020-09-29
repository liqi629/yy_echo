# -*- coding: utf-8 -*-
# @Time     : 2019/11/513:51
# @Author   : l7
# @File     : script_manager_page.py
# @Software : PyCharm

import time

from Common.BasePage import BasePage
from PageObjects.home_page import HomePage
from PageLocators.scriptManagerPage_locator import ScriptManagerPageLocator as loc


class ScriptManagerPage(HomePage):

    # dbType select操作
    def select_dbType(self, text):
        s = self.select(loc.select_dbType)
        s.select_by_visible_text(text)

    # select_scriptType select操作
    def select_scriptType(self, text):
        s = self.select(loc.select_scriptType)
        s.select_by_visible_text(text)
        # s.select_by_value(11)
        # 1、下标
        # s.deselect_by_index()
        # # 2、value属性
        # s.deselect_by_value(11)
        # # 3、文本内容
        # s.deselect_by_visible_text("其他")

    # 添加脚本
    def add_script(self, name, content, mark):
        """

        :param name: 脚本名称
        :param content: 内容
        :param mark: 备注
        :return:
        """
        self.into_script_manager()

        # 点击添加按钮
        self.wait_eleVisible(loc.btn_add_script)
        self.click_element(loc.btn_add_script)
        # 输入脚本名字
        self.wait_eleVisible(loc.script_name)
        self.input_text(loc.script_name, name)
        time.sleep(2)

        # self.wait_eleVisible(loc.script_name)
        # self.keyboard_tab(loc.script_name)

        elem = self.driver.find_element_by_xpath('//div[@class="CodeMirror cm-s-default CodeMirror-wrap"]')

        self.driver.execute_script("arguments[0].CodeMirror.setValue(arguments[1]);", elem,content)
        # self.click_element(loc.sss)
        # time.sleep(3)
        # 输入脚本内容
        # self.input_text(loc.sss, content)
        # time.sleep(3)
        self.input_text(loc.mark, mark)
        self.click_element(loc.btn_sub)

    # 判断脚本是否添加成功
    def is_addScript(self, loc_scriptText=loc.script_gbase_loader_1):
        try:
            self.wait_eleVisible(loc_scriptText, timeout=3)
            return True
        except:
            return False

    # 查看脚本
    def look_script(self):
        self.into_script_manager()
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.btn_look_gbase_loader_1)
        self.click_element(loc.btn_look_gbase_loader_1)

    # 判断查看窗口是否打开
    def is_look_script(self):
        try:
            self.wait_eleVisible(loc.modal_title_look, timeout=3)
            return True
        except:
            return False

    # 编辑脚本：编辑名称
    def edit_script(self, name):
        self.into_script_manager()
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.btn_edit_gbase_loader_1)
        self.click_element(loc.btn_edit_gbase_loader_1)
        self.wait_eleVisible(loc.modal_title_edit)
        self.input_text(loc.edit_name, name)
        self.click_element(loc.btn_edit_sub)

    # 判断脚本名称是否修改成功
    def is_edit_script(self, loc_scriptText=loc.script_gbase_loader_2):
        try:
            self.wait_eleVisible(loc_scriptText, timeout=3)
            return True
        except:
            return False

    # 启用脚本
    def start_script(self):
        self.into_script_manager()
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.script_gbase_loader_2)
        self.click_element(loc.btn_status_gbase_loader_2)

    #  判断脚本状态是否启用
    def is_start_script(self, loc_script_status=loc.status_1_gbase_loader_2):
        try:
            self.wait_eleVisible(loc_script_status, timeout=3)
            return True
        except:
            return False

    # 筛选-脚本状态
    def search__status(self, text):
        self.into_script_manager()
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.search_select_script_status)
        self.select(loc.search_select_script_status).select_by_visible_text(text)
        self.click_element(loc.btn_search_script)

    # 筛选-脚本名称
    def search_name(self, text):
        self.into_script_manager()
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.search_script_name)
        self.input_text(loc.search_script_name, text)
        self.click_element(loc.btn_search_script)

    # 筛选-脚本操作类型
    def search_type(self, text):
        self.into_script_manager()
        self.switch_iframe(loc.main_frame)
        self.select(loc.search_select_script_type).select_by_visible_text(text)
        self.click_element(loc.btn_search_script)


    # 筛选-数据库类型
    def search_db(self, text):
        self.into_script_manager()
        self.switch_iframe(loc.main_frame)
        self.select(loc.search_select_dbtypt).select_by_visible_text(text)
        self.click_element(loc.btn_search_script)

    # 筛选-时间
    def search_up_datetime(self, start_time, end_time):
        self.into_script_manager()
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.search_start_time)
        self.input_text(loc.search_start_time, start_time)
        self.input_text(loc.search_end_time, end_time)
        self.click_element(loc.btn_search_script)

    # 筛选-数据为空
    def is_search_empty(self):
        try:
            self.wait_eleVisible(loc.search_empty)
            return True
        except:
            return False

    # 删除脚本:demo_1
    def delScript(self, loc_delscript=loc.btn_del_gbase_loader_2):
        self.into_script_manager()
        # 切入iframe页面进行操作
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc_delscript)
        self.click_element(loc_delscript)
        self.wait_eleVisible(loc.btnConfirm)
        self.click_element(loc.btnConfirm)

    # 判断是否删除成功
    def is_delScript(self, loc_scriptname=loc.script_gbase_loader_1):
        time.sleep(1)
        try:
            self.wait_eleVisible(loc_scriptname, timeout=3)
            return True
        except:
            return False
