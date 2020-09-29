# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 14:19
# @Author   : l7
# @File     : home_page.py
# @Software : PyCharm
import selenium

from PageLocators.homePage_locator import HomePageLocator as loc
from PageLocators.designerPage_locator import DesignerPageLocator
from Common.BasePage import BasePage
from selenium.webdriver.support.ui import Select
import time
class HomePage(BasePage):
    #判断用户名是否存在
    def is_user_link_exists(self):
        try:
            self.wait_eleVisible(loc.user_link)
            return True
        except:
            return False
    #退出登录
    def logout(self):
        self.wait_eleVisible(loc.user_link)
        self.click_element(loc.user_link)
        self.click_element(loc.logout_button)

    # 添加工作目录
    def add_work_dir(self, name, remark):
        self.wait_eleVisible(loc.work_dir)
        self.click_element(loc.work_dir)
        time.sleep(1)
        self.wait_eleVisible(loc.btn_add)
        self.click_element(loc.btn_add)
        self.wait_eleVisible(loc.work_dir_name)
        self.input_text(loc.work_dir_name, name)
        self.input_text(loc.remark, remark)
        self.click_element(loc.btn_confirm)

    # 删除工作目录
    def del_work_dir(self, name):
        self.wait_eleVisible(loc.btn_del_work_dir(name))
        self.click_element(loc.btn_del_work_dir(name))
        self.wait_eleVisible(loc.delete_button)
        self.click_element(loc.delete_button)


    # 进入工作目录
    def into_work_dir(self):
        self.wait_eleVisible(loc.into_work_dir)
        self.click_element(loc.into_work_dir)


    # 添加映射
    def add_map(self, work_dir_name):
        # 获取窗口句柄，要放在新窗口出现之前
        current_handles = self.current_handles()
        #进入工作目录-点击工作目录管理-目录的进入按钮
        self.wait_eleVisible(loc.work_dir)
        self.click_element(loc.work_dir)
        time.sleep(1)
        self.wait_eleVisible(loc.btn_into_work_dir(work_dir_name))
        self.click_element(loc.btn_into_work_dir(work_dir_name))
        # 切换到新窗口
        self.switch_window("new", current_handles)
        time.sleep(3)
        self.wait_eleVisible(loc.map_designer)
        current_handles_1 = self.current_handles()
        self.click_element(loc.map_designer)
        # 切换到新窗口
        self.switch_window("new", current_handles_1)
        time.sleep(3)





    #鼠标悬浮作业设计——点击设计器，进入新窗口
    def into_designer(self):
        # 获取窗口句柄，要放在新窗口出现之前
        current_handles = self.current_handles()
        self.wait_eleVisible(loc.job_design)
        self.hover_element(loc.job_design)
        self.wait_eleVisible(loc.designer)
        self.click_element(loc.designer)
        # 切换到新窗口
        self.switch_window("new", current_handles)
        time.sleep(1)  # 加硬等待，增强稳定性
    # 点击数据源管理
    def into_data_source(self):
        #等待元素【业务管理】可见，鼠标悬浮，等待【数据源管理】
        self.wait_eleVisible(loc.business_management)
        self.hover_element(loc.business_management)
        self.wait_eleVisible(loc.data_source_manager)
        self.click_element(loc.data_source_manager)
    #点击应用管理/业务系统管理
    def into_operation_system(self):
        #等待元素可见：应用管理/业务系统管理
        self.wait_eleVisible(loc.business_management)
        self.click_element(loc.business_management)
        self.wait_eleVisible(loc.operation_system)
        self.click_element(loc.operation_system)
    #点击进入交换关系图
    def into_mindMap(self):
        self.wait_eleVisible(loc.business_management)
        self.hover_element(loc.business_management)
        self.wait_eleVisible(loc.mindMap)
        self.click_element(loc.mindMap)
    #点击进入算法管理-所有算法
    def into_algorithmManagementAll(self):
        self.wait_eleVisible(loc.job_design)
        self.hover_element(loc.job_design)
        self.wait_eleVisible(loc.algorithmManagement)
        self.hover_element(loc.algorithmManagement)
        self.wait_eleVisible(loc.algorithmManagementAll)
        self.click_element(loc.algorithmManagementAll)
    #点击进入算法管理-添加算法
    def into_algorithmManagementAdd(self):
        self.wait_eleVisible(loc.job_design)
        self.hover_element(loc.job_design)
        self.wait_eleVisible(loc.algorithmManagement)
        self.hover_element(loc.algorithmManagement)
        self.wait_eleVisible(loc.algorithmManagementAdd)
        self.click_element(loc.algorithmManagementAdd)


    # 点击进入脚本管理页面
    def into_script_manager(self):
        self.wait_eleVisible(loc.business_management)
        self.click_element(loc.business_management)
        self.wait_eleVisible(loc.script_manager)
        self.click_element(loc.script_manager)






    #添加业务系统
    def add_operation_system(self,zh_name,code,short_zn_name,en_name,short_en_name,sys_remark,
                             sys_version,dept,contacter,mobile,email):
        #调用进入业务系统管理页面的函数
        self.into_operation_system()
        #切入iframe页面进行操作
        # self.switch_iframe(loc.main_frame)
        #点击添加按钮：输入信息
        self.wait_eleVisible(loc.add_button)
        self.click_element(loc.add_button)
        self.wait_eleVisible(loc.zh_name)
        self.input_text(loc.zh_name, zh_name)
        self.input_text(loc.code, code)
        self.input_text(loc.short_zn_name, short_zn_name)
        self.input_text(loc.en_name, en_name)
        self.input_text(loc.short_en_name, short_en_name)
        self.input_text(loc.sys_remark, sys_remark)
        self.input_text(loc.sys_version, sys_version)
        self.input_text(loc.dept, dept)
        self.input_text(loc.contacter, contacter)
        self.input_text(loc.mobile, mobile)
        # self.input_text(loc.email, email)
        self.click_element(loc.ok_button)


    # 选择一个业务系统，点击查看详情
    def look_operation_system_sys_1(self):
        self.into_operation_system()
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.btn_look_sys_1)
        self.click_element(loc.btn_look_sys_1)

    # 判断业务系统详情窗口标题是否显示
    def is_look_operation_system(self):
        try:
            self.wait_eleVisible(loc.modal_title_sys, timeout=5)
            return True
        except:
            return False
    # 编辑业务系统
    def edit_operation_system_sys_1(self,zh_name,code,short_zn_name,en_name,short_en_name,
                                    sys_remark,sys_version,dept,contacter,mobile,email,loc_name=loc.btn_edit_sys_1,):
        self.into_operation_system()
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc_name)
        self.click_element(loc_name)
        self.wait_eleVisible(loc.edit_zh_name)
        self.input_text(loc.edit_zh_name, zh_name)
        self.input_text(loc.edit_code, code)
        self.input_text(loc.edit_short_zn_name, short_zn_name)
        self.input_text(loc.edit_en_name, en_name)
        self.input_text(loc.edit_short_en_name, short_en_name)
        self.input_text(loc.edit_sys_remark, sys_remark)
        self.input_text(loc.edit_sys_version, sys_version)
        self.input_text(loc.edit_dept, dept)
        self.input_text(loc.edit_contacter, contacter)
        self.input_text(loc.edit_mobile, mobile)
        self.input_text(loc.edit_email, email)
        self.click_element(loc.edit_ok_button)

    # 筛选业务系统:中文简称
    def search__short_zn_name(self, text):
        self.into_operation_system()
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.search_short_zn_name)
        self.input_text(loc.search_short_zn_name, text)
        self.click_element(loc.btn_search)
    # 筛选业务系统:中文简称
    def search__short_en_name(self, text):
        self.into_operation_system()
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.search_short_en_name)
        self.input_text(loc.search_short_en_name, text)
        self.click_element(loc.btn_search)
    # 筛选业务系统:部门
    def search_dept(self, text):
        self.into_operation_system()
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.search_dept)
        self.input_text(loc.search_dept, text)
        self.click_element(loc.btn_search)
    # 筛选业务系统:系统状态
    def search_sys_status(self, text):
        self.into_operation_system()
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.search_sys_status)
        s = self.select(loc.search_sys_status)
        s.select_by_visible_text(text)
        self.click_element(loc.btn_search)
    # 数据源管理输入查询时间
    def search_app_time(self, start_time, end_time):
        self.into_operation_system()
        self.switch_iframe(loc.main_frame)
        self.input_text(loc.search_start_time, start_time)
        self.input_text(loc.search_end_time, end_time)
        self.click_element(loc.btn_search)

    # 筛选-数据为空
    def is_search_empty(self):
        try:
            self.wait_eleVisible(loc.search_empty)
            return True
        except:
            return False

    #删除一个业务系统
    def delete_operation_system(self,sys_name):
        # 调用进入业务系统管理页面的函数
        try:
            self.into_operation_system()
        except:
            raise
        finally:
            self.wait_eleVisible(loc.btn_del(sys_name))
            time.sleep(1)
            self.click_element(loc.btn_del(sys_name))
            self.click_element(loc.delete_button)

    #testFile
    def testFile(self):
        # 切入iframe页面进行操作,有两个iframe
        self.switch_iframe(loc.main_frame)
        self.switch_iframe(loc.homeFrame)
        self.switch_iframe(loc.testFrame)



        self.wait_eleVisible(loc.table)

        return "hahah"
#页面切换=====================================================================
    #切换到添加用户页面
    def into_add_user(self):
        self.wait_eleVisible(loc.system)
        self.hover_element(loc.system)
        self.wait_eleVisible(loc.user_management)
        self.hover_element(loc.user_management)
        self.wait_eleVisible(loc.add_user)
        self.click_element(loc.add_user)
    #切换到所有用户页面
    def into_user_list(self):
        self.wait_eleVisible(loc.system)
        self.hover_element(loc.system)
        self.wait_eleVisible(loc.user_management)
        self.hover_element(loc.user_management)
        self.wait_eleVisible(loc.user_list)
        self.click_element(loc.user_list)


    # 点击选择数据类型
    def select_unit_type(self, unit_type):
        self.into_data_source()
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.select_unit_type)
        self.click_element(loc.select_unit_type)
        s = self.select(loc.select_unit_type)
        if unit_type=="文件":
            s.select_by_visible_text(unit_type)
        elif unit_type=="数据库":
            s.select_by_visible_text(unit_type)
        self.click_element(loc.btn_search)


    # 判断页面是否有新增数据源：at_source_1
    def is_at_source_1(self):
        time.sleep(1)
        try:
            self.wait_eleVisible(loc.at_source_1, timeout=5)
            return True
        except:
            return False

    # 点击查看详情：已添加的数据源-at_source_1
    def look_data_source_at_source_1(self, loc_name=loc.btn_look_at_source_1):
        self.select_unit_type("数据库")
        time.sleep(1)
        self.wait_eleVisible(loc_name)
        self.click_element(loc_name)

    # 获取查看详情dialog是否出现，通过title来判断
    def is_look_data_source(self, loc_name=loc.modal_title_data_source):
        try:
            self.wait_eleVisible(loc_name, timeout=5)
            return True
        except:
            return False
    # 数据源管理输入查询时间
    def search_up_datetime(self, start_time, end_time):
        self.select_unit_type("数据库")
        self.input_text(loc.start_time, start_time)
        self.input_text(loc.end_time, end_time)
        self.click_element(loc.btn_search)

    # 删除数据源：at_source_1
    def del_data_source_at_source_1(self, loc_name=loc.btn_del_at_source_1):
        self.select_unit_type("数据库")
        time.sleep(1)
        self.click_element(loc_name)
        self.wait_eleVisible(loc.btn_del_ok)
        self.click_element(loc.btn_del_ok)