# -*- coding: utf-8 -*-
# @Time     : 2019/5/27 15:09
# @Author   : l7
# @File     : designer_page.py
# @Software : PyCharm
from Common.BasePage import BasePage
from PageObjects.home_page import HomePage
from PageLocators.designerPage_locator import DesignerPageLocator as loc
from PageLocators.designerPage.oracle_locator import OracleLocator as orcl_loc
from PageLocators.designerPage.db2_locator import DB2Locator as db_loc
from PageLocators.designerPage.mongodb_locator import MongoLocator as mo_loc
from selenium.webdriver.support.ui import Select
import logging
from Common import logger
import time


class DesignerPage(HomePage):

    # 新建作业名称为空
    def none_job_name(self, none_job_name):
        # 等待+号元素可见
        self.wait_eleVisible(loc.add_job)
        # 点击新建作业的加号
        self.click_element(loc.add_job)
        # 等待作业名称输入框可见
        self.wait_eleVisible(loc.job_name_input)
        # 清空输入框
        self.clear_input_text(loc.job_name_input)
        # 输入作业名称
        self.input_text(loc.job_name_input, none_job_name)
        # 点击确定按钮
        self.click_element(loc.job_button)

    # 新建作业
    def add_job(self, job_name):
        time.sleep(2)
        # 等待+号元素可见
        self.wait_eleVisible(loc.add_job)
        # 点击新建作业的加号
        self.click_element(loc.add_job)
        time.sleep(2)
        # 等待作业名称输入框可见
        self.wait_eleVisible(loc.job_name_input)
        # 清空输入框
        self.clear_input_text(loc.job_name_input)
        # 输入作业名称
        self.input_text(loc.job_name_input, job_name)
        # 点击确定按钮
        self.click_element(loc.job_button)

    # 根据业务系统名称，选择业务系统
    def select_sys_name(self, sys_name):
        """

        :param sys_name: 传入应用名称
        :return:
        """
        self.wait_eleVisible(loc.select_option)
        # self.click_element(loc.select_option)
        s1 = self.select(loc.select_option)
        # s1.select_by_value(sys_name)
        s1.select_by_visible_text(sys_name)
        # self.wait_eleVisible(loc.select_option)
        # select_ele = self.get_Element(loc.select_option)
        # s = Select(select_ele)
        # s.select_by_visible_text(sys_name)



    def select_loc(self, loc):
        """
        点击选择
        :param loc: 传入要点击的元素定位
        :return:
        """
        time.sleep(3)
        self.wait_eleVisible(loc)
        self.click_element(loc)


    # 编辑作业名称
    def edit_job(self, newname):
        # self.select_job(loc.job_list_new)
        self.wait_eleVisible(loc.job_list_new)
        self.click_element(loc.job_list_new)
        self.wait_eleVisible(loc.edit_job_button)
        self.click_element(loc.edit_job_button)
        self.wait_eleVisible(loc.edit_name_input)
        self.clear_input_text(loc.edit_name_input)
        self.input_text(loc.edit_name_input, newname)
        self.click_element(loc.edit_name_button)

    # 判断作业名称(at_02)是否修改成功
    def is_job_at_02(self):
        try:
            self.wait_eleVisible(loc.job_at_02)
            return True
        except:
            return False

    # 删除新建的作业
    def delete_job(self, loc_job_name):
        # 等待新建作业可见
        self.wait_eleVisible(loc_job_name)
        # 鼠标点击
        self.click_element(loc_job_name)
        # 点击删除按钮
        self.wait_eleVisible(loc.delete_job_button)
        self.click_element(loc.delete_job_button)
        time.sleep(2)
        # 点击dialog中的删除
        self.wait_eleVisible(loc.dialog_delete_button)
        self.click_element(loc.dialog_delete_button)
        time.sleep(2)

    # 判断作业是否被删除
    def is_delete_job(self, job_name):
        time.sleep(1)
        try:
            self.wait_eleVisible(job_name, timeout=5)
            return True
        except:
            return False

    # 封装添加mysql的操作，无论数据源还是目标源，均可使用
    def add_data_node_mysql(self, data_type, job_name, source_name, ip, port, user_name, pass_word,
                            db_name,tab_name, sysname):
        '''

        :param data_type:
        :param type: 添加数据源还是目标，使用name参数传入相应的元素定位
        :param job_name: 作业的元素定位，添加数据源需要在作业的基础之上
        :param source_name: 添加数据源的时候，数据源名称
        :param ip: 数据库ip
        :param port: 数据库端口
        :param user_name: 数据库用户名
        :param pass_word: 数据库密码
        :param sys_name: 业务系统名称
        :param db_name: 数据库名
        :param tab_name: 数据表名
        :return:
        '''
        # 选择一个作业
        try:
            self.select_loc(job_name)
        except:
            self.driver.refresh()
            raise
        time.sleep(1)
        # 获取窗口句柄，要放在新窗口出现之前
        current_handles = self.current_handles()
        # 判断添加的数据源类型：数据源还是目标
        if data_type == "source":
            # 点击数据源
            self.wait_eleVisible(loc.data_source)
            self.click_element(loc.data_source)
        else:
            # 点击目标
            self.wait_eleVisible(loc.target_source)
            self.click_element(loc.target_source)
        # 点击添加按钮
        self.wait_eleVisible(loc.add_button)
        self.click_element(loc.add_button)
        # 展开数据库对象树
        self.wait_eleVisible(loc.data_tree_1)
        self.click_element(loc.data_tree_1)
        # 选择点击MySQL
        self.wait_eleVisible(loc.MySQL)
        self.click_element(loc.MySQL)
        # 点击确定按钮
        self.wait_eleVisible(loc.db_button)
        self.click_element(loc.db_button)
        # 切换到新窗口
        self.switch_window("new", current_handles)

        time.sleep(1)  # 加硬等待，增强稳定性
        # 填写数据库连接信息，测试链接
        self.test_connect_mysql(source_name, ip, port, user_name, pass_word, db_name, sysname)
        self.wait_eleVisible(loc.test_msg)
        time.sleep(1)  # 加硬等待，增强稳定性
        # 点击下一步
        self.click_element(loc.next_step)
        time.sleep(2)
        # 选择数据库的表
        self.select_table(tab_name)
        time.sleep(2)  # 加硬等待，增强稳定性
        # 点击下一步
        self.click_element(loc.next_step)
        time.sleep(2)  # 加硬等待，增强稳定性
        # 继续点击下一步
        self.wait_eleVisible(loc.next_step)
        self.click_element(loc.next_step)
        time.sleep(2)  # 加硬等待，增强稳定性
        # 点击确定按钮
        self.wait_eleVisible(loc.confirm_button)
        self.click_element(loc.confirm_button)
        # 切换回html窗口
        all_windows = self.current_handles()
        self.switch_window(all_windows[-1])
        time.sleep(1)
        # 点击保存
        self.save_map()
        logging.info("创建时间是：{0}".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        # 选择数据库的表

    # 添加mysql数据源时输入数据库信息测试链接
    def test_connect_mysql(self, source_name, ip, port, user_name, pass_word, db_name, sys_name ):
        # 等待新增按钮
        self.wait_eleVisible(loc.add_button_mysql)
        # 点击新增
        time.sleep(1)
        self.click_element(loc.add_button_mysql)
        # 输入数据源名称
        self.input_text(loc.source_name, source_name)
        # 输入ip、端口
        self.input_text(loc.ip, ip)
        self.input_text(loc.port, port)
        # 输入用户名、密码
        self.input_text(loc.user_name, user_name)
        self.input_text(loc.pass_word, pass_word)
        # 选择所属系统
        # self.click_element(loc.select_option)
        self.select_sys_name(sys_name)
        # 输入数据库名称
        self.input_text(loc.db_name, db_name)


        # 选择环境类型
        pass
        # 选择是否跨域
        pass
        # 编码设置
        pass
        # 备注
        pass
        # 点击测试连接
        self.click_element(loc.test_connect)

    # oracle添加数据节点
    def add_data_node_oracle(self, data_type, job_name, source_name, ip, port, user_name, pass_word, sys_name,
                             db_name,
                             tab_name):
        # 选择一个作业
        time.sleep(1)
        self.select_loc(job_name)
        time.sleep(1)
        # 获取窗口句柄，要放在新窗口出现之前
        current_handles = self.current_handles()
        # 判断添加的数据源类型：数据源还是目标
        if data_type == "source":
            # 点击数据源
            self.wait_eleVisible(loc.data_source)
            self.click_element(loc.data_source)
        else:
            # 点击目标
            self.wait_eleVisible(loc.target_source)
            self.click_element(loc.target_source)
        # 点击添加按钮
        self.wait_eleVisible(loc.add_button)
        self.click_element(loc.add_button)
        # 展开数据库对象树
        self.wait_eleVisible(loc.data_tree_1)
        self.click_element(loc.data_tree_1)
        # 选择点击ORACLE
        self.wait_eleVisible(loc.ORACLE)
        self.click_element(loc.ORACLE)
        # 点击确定按钮
        self.wait_eleVisible(loc.db_button)
        self.click_element(loc.db_button)
        # 切换到新窗口
        self.switch_window("new", current_handles)

        time.sleep(1)  # 加硬等待，增强稳定性
        # 填写数据库连接信息，测试链接
        self.test_connect_oracle(source_name, ip, port, user_name, pass_word, sys_name, db_name)
        self.wait_eleVisible(orcl_loc.test_msg)
        # 点击下一步
        self.click_element(loc.next_step)
        time.sleep(2)
        # schema选择
        self.wait_eleVisible(orcl_loc.schema)
        self.click_element(orcl_loc.schema)
        self.wait_eleVisible(orcl_loc.schema_ECHOAT)
        self.click_element(orcl_loc.schema_ECHOAT)
        # 选择数据库的表

        self.select_table(tab_name)
        time.sleep(2)  # 加硬等待，增强稳定性
        # 点击下一步
        self.click_element(loc.next_step)
        time.sleep(2)  # 加硬等待，增强稳定性
        # 继续点击下一步
        self.wait_eleVisible(loc.next_step)
        self.click_element(loc.next_step)
        time.sleep(2)  # 加硬等待，增强稳定性
        # 点击确定按钮
        self.wait_eleVisible(loc.confirm_button)
        self.click_element(loc.confirm_button)
        # 切换回html窗口
        self.switch_window("default", current_handles)
        time.sleep(1)
        # 点击保存
        self.save_map()

    # 添加oracle数据源时输入数据库信息测试链接
    def test_connect_oracle(self, source_name, ip, port, user_name, pass_word, sys_name, db_name):
        # 等待新增按钮
        self.wait_eleVisible(orcl_loc.add_button_oracle)
        # 点击新增
        self.click_element(orcl_loc.add_button_oracle)
        # 输入数据源名称
        self.input_text(orcl_loc.source_name, source_name)
        # 输入ip、端口
        self.input_text(orcl_loc.ip, ip)
        self.input_text(orcl_loc.port, port)
        # 输入用户名、密码
        self.input_text(orcl_loc.user_name, user_name)
        self.input_text(orcl_loc.pass_word, pass_word)
        # 选择所属系统
        self.select_sys_name(sys_name)
        # 输入数据库名称
        self.input_text(orcl_loc.db_name, db_name)
        # 选择环境类型
        pass
        # 选择是否跨域
        pass
        # 编码设置
        pass
        # 备注
        pass
        # 点击测试连接
        self.click_element(orcl_loc.test_connect)
    # DB2数据节点添加
    def add_data_node_db2(self, data_type, job_name, source_name, ip, port, user_name, pass_word, sys_name,
                             db_name,
                             tab_name):
        # 选择一个作业
        time.sleep(1)
        self.select_loc(job_name)
        time.sleep(1)
        # 获取窗口句柄，要放在新窗口出现之前
        current_handles = self.current_handles()
        # 判断添加的数据源类型：数据源还是目标
        if data_type == "source":
            # 点击数据源
            self.wait_eleVisible(loc.data_source)
            self.click_element(loc.data_source)
        else:
            # 点击目标
            self.wait_eleVisible(loc.target_source)
            self.click_element(loc.target_source)
        # 点击添加按钮
        self.wait_eleVisible(loc.add_button)
        self.click_element(loc.add_button)
        # 展开数据库对象树
        self.wait_eleVisible(loc.data_tree_1)
        self.click_element(loc.data_tree_1)
        # 选择点击ORACLE
        self.wait_eleVisible(db_loc.DB2)
        self.click_element(db_loc.DB2)
        # 点击确定按钮
        self.wait_eleVisible(loc.db_button)
        self.click_element(loc.db_button)
        # 切换到新窗口
        self.switch_window("new", current_handles)

        time.sleep(1)  # 加硬等待，增强稳定性
        # 填写数据库连接信息，测试链接
        self.test_connect_db2(source_name, ip, port, user_name, pass_word, sys_name, db_name)
        self.wait_eleVisible(db_loc.test_msg)
        # 点击下一步
        self.click_element(db_loc.next_step)
        time.sleep(5)
        # 选择数据库的表
        self.select_table(tab_name)
        time.sleep(5)  # 加硬等待，增强稳定性
        # 点击下一步
        self.click_element(loc.next_step)
        time.sleep(5)  # 加硬等待，增强稳定性
        # 继续点击下一步
        self.wait_eleVisible(loc.next_step)
        self.click_element(loc.next_step)
        time.sleep(5)  # 加硬等待，增强稳定性
        # 点击确定按钮
        self.wait_eleVisible(loc.confirm_button)
        self.click_element(loc.confirm_button)
        # 切换回html窗口
        self.switch_window("default", current_handles)
        time.sleep(1)
        # 点击保存
        self.save_map()

    # 添加db2数据源时输入数据库信息测试链接
    def test_connect_db2(self, source_name, ip, port, user_name, pass_word, sys_name, db_name):
        # 等待新增按钮
        self.wait_eleVisible(db_loc.add_button_db2)
        # 点击新增
        self.click_element(db_loc.add_button_db2)
        # 输入数据源名称
        self.input_text(db_loc.source_name, source_name)
        # 输入ip、端口
        self.input_text(db_loc.ip, ip)
        self.input_text(db_loc.port, port)
        # 输入用户名、密码
        self.input_text(db_loc.user_name, user_name)
        self.input_text(db_loc.pass_word, pass_word)
        # 选择所属系统
        self.select_sys_name(sys_name)
        # 输入数据库名称
        self.input_text(db_loc.db_name, db_name)
        # 选择环境类型
        pass
        # 选择是否跨域
        pass
        # 编码设置
        pass
        # 备注
        pass
        # 点击测试连接
        self.click_element(db_loc.test_connect)

    # 添加mongodb数据源时输入数据库信息测试链接
    def test_connect_mongo(self, source_name, ip, port, user_name, pass_word, sys_name, db_name="admin"):
        # 等待新增按钮
        self.wait_eleVisible(mo_loc.add_button_mongo)
        # 点击新增
        self.click_element(mo_loc.add_button_mongo)
        # 输入第一个连接名称
        time.sleep(2)
        self.input_text(mo_loc.conn_name, source_name)
        time.sleep(2)
        # 输入ip、端口
        self.input_text(mo_loc.ip, ip)
        self.input_text(mo_loc.port, port)
        # 选择使用权限认证
        s = self.select(mo_loc.auth)
        s.select_by_visible_text("true")
        # 选择所属系统
        self.select_sys_name(sys_name)
        # 输入认证数据库名称
        self.input_text(mo_loc.auth_database, db_name)
        # 选择认证模式：SCRAM-SHA-1
        s = self.select(mo_loc.auth_mode)
        s.select_by_visible_text("SCRAM-SHA-1")
        # 输入用户名、密码
        self.input_text(mo_loc.user_name, user_name)
        self.input_text(mo_loc.pwd, pass_word)
        # # 输入第二个连接名称
        # self.input_text(mo_loc.conn_name, source_name)
        # 选择环境类型
        pass
        # 备注
        pass
        # 点击测试连接
        self.click_element(mo_loc.test_connect)

    # MongoDB数据节点添加
    def add_data_node_mongo(self, data_type, job_name, source_name, ip, port,
                            user_name, pass_word,sys_name,tab_name):
        # 选择一个作业
        time.sleep(1)
        self.select_loc(job_name)
        time.sleep(1)
        # 获取窗口句柄，要放在新窗口出现之前
        current_handles = self.current_handles()
        # 判断添加的数据源类型：数据源还是目标
        if data_type == "source":
            # 点击数据源
            self.wait_eleVisible(loc.data_source)
            self.click_element(loc.data_source)
        else:
            # 点击目标
            self.wait_eleVisible(loc.target_source)
            self.click_element(loc.target_source)
        # 点击添加按钮
        self.wait_eleVisible(loc.add_button)
        self.click_element(loc.add_button)
        # 展开数据库对象树
        self.wait_eleVisible(loc.data_tree_1)
        self.click_element(loc.data_tree_1)
        # 选择点击MongoDB
        self.wait_eleVisible(mo_loc.MongoDB)
        self.click_element(mo_loc.MongoDB)
        # 点击确定按钮:确定数据类型
        self.wait_eleVisible(mo_loc.btn_onfirm_type)
        self.click_element(mo_loc.btn_onfirm_type)
        # 切换到新窗口
        self.switch_window("new", current_handles)

        time.sleep(1)  # 加硬等待，增强稳定性
        # 填写数据库连接信息，测试链接
        self.test_connect_mongo(source_name, ip, port, user_name, pass_word, sys_name)
        self.wait_eleVisible(mo_loc.test_msg)
        # 点击下一步
        self.click_element(mo_loc.next_step)
        time.sleep(2)
        # 选择数据库的表
        self.wait_eleVisible(mo_loc.database)
        self.input_text(mo_loc.database, "autotest")
        self.click_element(mo_loc.btn_get_tb)
        s =self.select(mo_loc.select_tb)
        s.select_by_visible_text("city")


        time.sleep(2)  # 加硬等待，增强稳定性
        # 点击下一步,字段设置
        self.click_element(mo_loc.next_step)
        time.sleep(2)  # 加硬等待，增强稳定性
        # 点击确定
        self.wait_eleVisible(mo_loc.confirm_button)
        self.click_element(mo_loc.confirm_button)
        # 切换回html窗口
        self.switch_window("default", current_handles)
        time.sleep(1)
        # 点击保存
        self.save_map()

    # 添加源时选择表
    def select_table(self, tab_name):

        self.wait_eleVisible(loc.more_table)
        select_ele = self.get_Element(loc.select_page)
        s = Select(select_ele)
        s.select_by_visible_text("All")
        self.wait_eleVisible(tab_name)
        self.click_element(tab_name)

    # 保存映射
    def save_map(self):
        # 点击保存
        self.wait_eleVisible(loc.save_button)
        self.click_element(loc.save_button)
        # 在弹出窗点击确定
        self.wait_eleVisible(loc.map_config_button)
        self.click_element(loc.map_config_button)

    def view_target_data(self):
        pass

    # 建立映射并发布
    def on_line(self, map_name):
        self.wait_eleVisible(loc.map_text_loc(map_name))
        self.click_element(loc.map_text_loc(map_name))
        time.sleep(1)
        # 点击数据源
        self.click_element(loc.data_source)
        # 点击映射关系
        self.click_element(loc.mapping_relation)
        time.sleep(1)
        # 点击批量连线
        self.click_element(loc.on_line)
        time.sleep(1)
        # 点击批量连线确定按钮
        self.wait_eleVisible(loc.on_line_btn)
        self.click_element(loc.on_line_btn)
        time.sleep(1)
        # 保存
        self.save_map()
        time.sleep(1)
        # 发布
        self.wait_eleVisible(loc.publish_button)
        self.click_element(loc.publish_button)
        time.sleep(3)
    # 快速生成工作流
    def cre_work_flow(self,workflowname, remark):
        self.wait_eleVisible(loc.btn_creat_work_flow)
        self.click_element(loc.btn_creat_work_flow)
        self.wait_eleVisible(loc.work_flow_input)
        self.input_text(loc.work_flow_input, workflowname)
        self.input_text(loc.workflowName_remark, remark)
        self.click_element(loc.workflowName_confirm)
        # 获取窗口句柄，要放在新窗口出现之前
        current_handles = self.current_handles()
        self.switch_window(current_handles[-2])
        self.refresh()


    def pilt_run(self, work_flow_name):
        """
        选择工作流，点击试运行，然后跳转到运行实例页
        :param work_flow_name:
        :return:
        """

        self.select_loc(loc.text_to_loc(work_flow_name))
        time.sleep(1)
        self.click_element(loc.btn_pilt_run_c)
        self.click_element(loc.btn_pilt_run)
        self.wait_eleVisible(loc.btn_pilt_run_c)
        self.click_element(loc.btn_pilt_run_c)
        time.sleep(1)
        self.wait_eleVisible(loc.btn_pilt_run_c)
        self.click_element(loc.btn_pilt_run_c)

    def is_run_status(self):
        """
        判断是否运行成功
        :return:
        """
        try:
            self.get_text(loc.run_status_succ_loc)
            return True
        except:
            return False


    def del_work_flow(self, text):
        """
        删除工作流
        :param text:工作流名称
        :return:
        """
        self.wait_eleVisible(loc.menu_work_flow_des)
        self.click_element(loc.menu_work_flow_des)
        self.select_loc(loc.text_to_loc(text=text))
        self.click_element(loc.btn_del_work_flow_text_loc(text))
        self.wait_eleVisible(loc.confirm)
        self.click_element(loc.confirm)


    def del_job(self, text):
        """
        删除作业
        :param text:
        :return:
        """
        self.wait_eleVisible(loc.menu_work_flow_des)
        self.click_element(loc.menu_work_flow_des)
        self.select_loc(loc.text_to_loc(text=text))
        self.click_element(loc.btn_del_job_text_loc(text))
        self.wait_eleVisible(loc.confirm)
        self.click_element(loc.confirm)

    def del_map(self, map_name, del_loc_text="删除"):
        """
        删除映射
        :param map_name: 映射名字
        :param del_loc_text: 映射对应的删除
        :return:
        """
        self.wait_eleVisible(loc.map_text_loc(map_name))
        self.click_element(loc.map_text_loc(map_name))
        self.wait_eleVisible(loc.text_to_loc(del_loc_text))
        self.click_element(loc.text_to_loc(del_loc_text))
        # 删除的二次确认
        self.wait_eleVisible(loc.btn_del_job_confirm)
        self.click_element(loc.btn_del_job_confirm)


    def is_loc_show(self, loc):
        """
        判断页面是否有元素显现
        :param loc: 元素定位
        :return:
        """
        try:
            self.wait_eleVisible(loc,timeout=5)
            return True
        except:
            return False











    # 运行mysql到mysql的作业,本地还是分布式运行 通过传参
    def run_job(self, method, job_name):
        self.select_loc(job_name)
        # self.wait_eleVisible(loc.publish_button)
        # self.click_element(loc.publish_button)
        time.sleep(1)
        if method == 'local':
            self.wait_eleVisible(loc.run_locally)
            self.click_element(loc.run_locally)
            time.sleep(10)
        else:
            self.wait_eleVisible(loc.run_distributed)
            self.click_element(loc.run_distributed)
            time.sleep(10)

    # 运行mysql转换文本的作业
    def run_job_MySQL_text(self, method):
        self.wait_eleVisible(loc.MySQL_text)
        self.click_element(loc.MySQL_text)
        self.wait_eleVisible(loc.publish_button)
        self.click_element(loc.publish_button)
        time.sleep(2)
        if method == 'local':
            self.wait_eleVisible(loc.run_locally)
            self.click_element(loc.run_locally)
            time.sleep(5)
        else:
            self.wait_eleVisible(loc.run_distributed)
            self.click_element(loc.run_distributed)
            time.sleep(5)

    # 切换作业
    def switch_job(self):
        self.wait_eleVisible(loc.select_job)
        self.click_element(loc.select_job)
        # self.wait_eleVisible(loc.select_job_mysql)
        # self.click_element(loc.select_job_mysql)
        self.wait_eleVisible(loc.select_job_text)
        self.click_element(loc.select_job_text)

    # 判断作业是否切换成功
    def is_switch_job(self):
        try:
            self.wait_eleVisible(loc.text_name)
            return True
        except:
            return False

    # 发布作业
    def publish(self):
        self.select_loc(loc.not_delete_job)
        self.wait_eleVisible(loc.publish_button)
        self.click_element(loc.publish_button)

    # 判断作业是否发布成功
    def is_publish(self):
        try:
            self.wait_eleVisible(loc.toast_pub_success)
            return True
        except:
            return False

    # 判断取消的toast
    def is_unpublish(self):
        try:
            self.wait_eleVisible(loc.toast_pub_cancel)
            return True
        except:
            return False

    # 运行工作流
    def run_work_flow(self):
        self.wait_eleVisible(loc.run_work_flow)
        self.click_element(loc.run_work_flow)

    # 等待工作流完成
    def is_work_flow(self):
        try:
            self.wait_eleVisible(loc.work_flow_finished_1)
            res_1 = self.get_text(loc.work_flow_finished_1)
            self.wait_eleVisible(loc.work_flow_finished_2)
            res_2 = self.get_text(loc.work_flow_finished_2)
            self.wait_eleVisible(loc.work_flow_finished_3)
            res_3 = self.get_text(loc.work_flow_finished_3)
            res = res_1 + res_2 + res_3
            logging.info("获取的文本是：" + res)
            if "helloworld" in res:
                return True
        except:
            logging.error("没有运行成功！")
            return False

    # 新建工作流-废除
    # def add_work_flow(self, work_flow_name):
    #     self.select_loc(loc.not_delete_job)
    #     self.wait_eleVisible(loc.work_flow)
    #     # self.click_element(loc.work_flow)
    #     self.hover_element(loc.work_flow)
    #     self.wait_eleVisible(loc.add_work_folw_btn)
    #     self.click_element(loc.add_work_folw_btn)
    #     self.wait_eleVisible(loc.work_flow_input)
    #     self.input_text(loc.work_flow_input, work_flow_name)
    #     self.click_element(loc.btn_workflow_add)

    # 判断新增的工作流是否存在
    def is_new_work_flow(self):
        try:
            # dialog还没有消失，导致点击事件失败，加入应等待增强稳定性
            time.sleep(1)
            self.wait_eleVisible(loc.work_flow)
            self.click_element(loc.work_flow)
            self.wait_eleVisible(loc.new_work_flow)
            return True
        except:
            return False

    # 删除新增的工作流
    def delete_work_flow(self):
        self.select_loc(loc.not_delete_job)
        # 点击工作流 展开
        self.wait_eleVisible(loc.work_flow)
        self.click_element(loc.work_flow)
        # 鼠标悬浮在新增的工作流上
        self.hover_element(loc.new_work_flow)
        self.wait_eleVisible(loc.delete_work_flow)
        self.click_element(loc.delete_work_flow)
        self.wait_eleVisible(loc.btn_workflow_delete)
        self.click_element(loc.btn_workflow_delete)

    # 判断是否删除成功
    def is_delete_work_flow(self):
        try:
            self.wait_eleVisible(loc.new_work_flow, timeout=2)
            return True
        except:
            return False

    # 添加工作流
    def add_work_flow(self, name, mark):
        self.wait_eleVisible(loc.add_work_flow)
        self.click_element(loc.add_work_flow)
        self.input_text(loc.work_flow_name, name)
        self.input_text(loc.work_flow_mark, mark)
        self.click_element(loc.btn_ack)

    # 拖拽命令脚本
    def tree_text(self, script_name):
        self.select_loc(loc.text_to_loc(script_name))
        self.drag_and_drop_by_offset(loc.text_to_loc("命令/脚本"), 600,200)
        time.sleep(1)
        self.hover_element(loc.start)
        self.wait_eleVisible(loc.arrow)
        self.click_and_hold(loc.arrow)
        self.move_to_element(loc.ml)
        self.move_to_element_release(loc.ml_in_arrow)
        time.sleep(1)
        self.wait_eleVisible(loc.bar_open)
        self.click_element(loc.bar_open)
        time.sleep(1)
        self.hover_element(loc.ml)
        self.wait_eleVisible(loc.ml_out_arrow)
        self.click_and_hold(loc.ml_out_arrow)
        self.move_to_element(loc.end)
        self.move_to_element_release(loc.end_arrow)
        time.sleep(1)
        self.click_element(loc.work_flow_save)

        time.sleep(10)

# 分布式运行
# 查询源数据
# 删除目标源一的 AUTO_test_02内容
