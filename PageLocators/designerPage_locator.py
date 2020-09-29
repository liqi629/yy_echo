#  -*- coding: utf-8 -*-
#  @Time     : 2019/5/27 14:55
#  @Author   : l7
#  @File     : designerPage_locator.py
#  @Software : PyCharm
from selenium.webdriver.common.by import By


class DesignerPageLocator:

    @staticmethod
    def text_to_loc(text):
        """
        通用：通过传入元素定位的text信息获取自身的元素定位
        :param text: 元素定位中的text信息
        :return: 元素定位
        """
        text_loc = (By.XPATH, '//span[text()="{}"]'.format(text))
        return text_loc

    @staticmethod
    def job_loc(text):
        """
        映射设计页面：通过传入作业的名字获取自身的元素定位
        :param text:作业的名字
        :return: 作业的定位
        """
        job_loc = (By.XPATH, '//ul[@id="treeDemo"]//span[text()="{}"]'.format(text))
        return job_loc

    @staticmethod
    def tab_loc(text):
        """
        映射设计：通过传入数据表的名字获取自身的元素定位
        :param text: 数据表的名字
        :return: 数据表的名字
        """
        tab_loc = (By.XPATH, '//input[@data-name="{}"]'.format(text))
        return tab_loc

    @staticmethod
    def run_status_loc(text):
        """
        实例运行页：通过传入不同运行状态文字获取自身的元素定位
        :param text: 运作状态：成功、失败、运行中
        :return:
        """
        run_status_loc = (By.XPATH, '//div[@class="clearfix"]//span[text()="{}"]'.format(text))
        return run_status_loc

    @staticmethod
    def btn_del_work_flow_text_loc(text):
        """
        工作流设计页面：传入工作流的名称，获取对应的删除按钮
        :return:
        """
        loc = (By.XPATH, '//span[text()="{}"]//ancestor::span//i[@class="el-tooltip el-icon-delete left-icon item"]'.format(text))
        return loc

    @staticmethod
    def btn_del_job_text_loc(text):
        """
        工作流设计页面：传入作业的名称，获取对应的删除按钮
        :return:
        """
        loc = (By.XPATH, '//span[text()="{}"]//ancestor::span//i[@class="el-tooltip el-icon-delete left-icon item"]'.format(text))
        return loc
    @staticmethod
    def map_text_loc(text):
        """
        映射设计器页面：传入映射的名称，获取定位
        :return:
        """
        loc = (By.XPATH, '//ul[@id="treeDemo"]//span[text()="{}"]'.format(text))
        return loc


    # 映射设计器页面
    # 删除映射，弹出窗口的删除按钮
    btn_del_job_confirm = (By.XPATH, '//a[@id="btn-delete"]')

    # 实例运行状态的元素定位
    a = '//div[@class="clearfix"]//span[text()="成功"]'
    run_status_succ_loc = (By.XPATH, '//span[@class="el-tag el-tag--success el-tag--small el-tag--light"]')
    run_status_fail_loc = (By.XPATH, 'class="el-tag el-tag--danger el-tag--small el-tag--light"')
    # 重新运行
    btn_re_run = (By.XPATH, '//button[@class="el-button el-button--default el-button--mini"]')


    # 工作流设计器
    # 菜单-工作流设计器
    menu_work_flow_des = (By.XPATH, '//ul[@class="el-menu"]//span[text()="工作流设计器"]')
    # 工作流的添加 + 号
    add_work_flow = (By.XPATH, '//i[@autotest="add_workflow"]')
    # 添加工作流-工作流名称
    work_flow_name = (By.XPATH, '//input[@autotest="form_workflow_name"]')
    # 工作流备注
    work_flow_mark = (By.XPATH, '//textarea[@autotest="form_workflow_remark"]')
    # 添加工作流页面确定按钮
    btn_ack = (By.XPATH, '//div[@aria-label="添加工作流"]//span[text()="确 定"]')

    toast_msg = (By.XPATH, '//div[@id="toast-container"]')

    toast_msg_1 = (By.XPATH, '//div[@class="toast-message"]')
    # 删除工作流、删除作业
    toast_msg_del = (By.XPATH, '//*[text()="删除成功!"]')

    # 开始图标
    start = (By.XPATH, '//div[@id="graphContainer"]//*[name()="svg"]/*[name()="g"]/*[name()="g"][2]/*[name()="g"][1]/*[name()="rect" and @fill="#fff"]')
    end = (By.XPATH, '//*[@id="graphContainer"]/*[name()="svg"]/*[name()="g"]/*[name()="g"]/*[name()="g"][2]/*[name()="rect" and @fill="gray"]')

    # 箭头标志
    arrow = (By.XPATH, '//div[@id="graphContainer"]//*[name()="svg"]/*[name()="g"]/*[name()="g"][4]/*[name()="g"]/*[name()="image"]')
    end_arrow = (By.XPATH, '//*[@id="graphContainer"]/*[name()="svg"]/*[name()="g"]/*[name()="g"][4]')

    # 命令脚本的图标
    ml = (By.XPATH, '//div[@id="graphContainer"]//*[name()="svg"]/*[name()="g"]/*[name()="g"][2]/*[name()="g"][3]')
    # 命令脚本的图标.连线的时候的箭头 进入箭头
    ml_in_arrow = (By.XPATH, '//*[@id="graphContainer"]/*[name()="svg"]/*[name()="g"]/*[name()="g"][4]/*[name()="g"][2]')
    ml_out_arrow = (By.XPATH, '//*[@id="graphContainer"]/*[name()="svg"]/*[name()="g"]/*[name()="g"][4]/*[name()="g"][1]')
    bar_open = (By.XPATH, '//div[@class="bar open"]')

    # 工作流设计器，设计区的保存按钮
    work_flow_save = (By.XPATH, '//div[@class="fr graph-action-btn"]//button[@autotest="save"]')

    # 按钮====================================================================================================================
    # 新建作业+号

    add_job = (By.XPATH, '//img[@id="addBgBac"]')
    # 作业名称输入框//input[@id="bisName"]
    job_name_input = (By.XPATH, '//input[@id="bisName"]')
    # 修改作业，名称输入
    edit_name_input = (By.XPATH, '//input[@id="editBus"]')
    # 修改按钮
    edit_name_button = (By.XPATH, '//a[@id="btn-edit"]')
    # 新建作业确认按钮
    job_button = (By.XPATH, '//a[@id="btnBusinessAdd"]')
    # 新建完成的作业，列表中的定位 //span[text()="auto_test_2"]


    #  鼠标悬浮作业，编辑按钮
    edit_job_button = (By.XPATH, '//span[@class="fa fa-edit btn-edit-business"]')
    # 鼠标悬浮新建作业，删除按钮
    delete_job_button = (By.XPATH, '//span[@class="fa fa-trash btn-del-business"]')
    # 删除作业弹窗 的删除按钮
    dialog_delete_button = (By.XPATH, '//a[@id="btn-delete"]')

    # 数据源
    data_source = (By.XPATH, '//span[@title="数据源"]')

    # 添加按钮、保存按钮、发布按钮、快速工作流
    add_button = (By.XPATH, '//span[@title="添加"]')
    save_button = (By.XPATH, '//span[text()="保存"]')
    publish_button = (By.XPATH, '//span[text()="发布"]')
    btn_creat_work_flow = (By.XPATH, '//span[@id="quicklyGeneateWorkflow"]')



    # 弹出窗口-确认按钮


    # 点击试运行的窗口确认按钮/是否跳转到实例的确认按钮
    btn_pilt_run_c = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    btn_wkf_save = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    # 设计器页面-工作流保存按钮
    btn_wf_save = (By.XPATH, '//button[@autotest="save"]')
    btn_pilt_run = (By.XPATH, '//*[@class="el-button el-button--text el-button--mini"][4]')

    # 工作流设计器页面，删除工作流后，弹窗的确认按钮
    confirm = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')





    # 取消发布按钮
    unpublish_button = (By.XPATH, '//span[text()="取消发布"]')
    # 本地运行按钮
    run_locally = (By.XPATH, '//span[text()="本地运行"]')
    # 分布式运行按钮
    run_distributed = (By.XPATH, '//span[text()="分布运行"]')
    # 删除节点//a[text()="删除节点"]
    delete_node = (By.XPATH, '//a[text()="删除节点"]')
    # 工作流 运行按钮
    run_work_flow = (By.XPATH, '//span[text()="运行"]')
    # 映射关系按钮
    mapping_relation = (By.XPATH, '//span[text()="映射关系"]')
    # 批量连线按钮
    on_line = (By.XPATH, '//span[text()="批量连线"]')
    # 批量连线的确认按钮
    on_line_btn = (By.XPATH, '//div[@id="modalTableConfig"]//a[text()="确定"]')
    # TOAST=================================================================================================
    # 新建作业成功/名称重复toast提示//div[@class="toast-message"]，下面的toast 共用
    job_toast = (By.XPATH, '//div[@class="toast-message"]')
    # 发布成功toast
    toast_pub_success = (By.XPATH, '//div[text()="发布成功"]')
    # 取消发布成功toast
    toast_pub_cancel = (By.XPATH, '//div[text()="取消发布成功"]')
    # 重复发布tosat
    toast_pub_re = (By.XPATH, '')
    # 作业窗口=========================================================================================
    # 作业窗口的下拉按钮
    select_job = (By.XPATH, '//div[@class="select pull-right"]//span[@class="select2-selection__arrow"]')


    # 作业========================================================================
    # 作业：MySQL_text
    MySQL_text = (By.XPATH, '//ul[@class="level0 "]//span[text()="MySQL_text"]')
    # 作业：MySQL_text目标文件源
    text_name = (By.XPATH, '//span[text()="自动化测试目标文件源一"]')

    # 作业：作业at_02
    job_at_02 = (By.XPATH, '//ul[@id="treeDemo"]//span[text()="作业at_02"]')
    # 作业：自动作业01
    mysql_auto_job01 = (By.XPATH, '//ul[@id="treeDemo"]//span[text()="自动作业01"]')
    # 作业：自动Mysql01
    mysql_auto_job02 = (By.XPATH, '//ul[@id="treeDemo"]//span[text()="自动Mysql01"]')
    #  作业：自动Mysql01
    mysql_oracle_1 = (By.XPATH, '//ul[@id="treeDemo"]//span[text()="自动Mysql-Oracle"]')
    #  作业========================================================================

    # 数据库，树加号，展开作用//span[@id="dataTree_1_switch"]
    data_tree_1 = (By.XPATH, '//span[@id="dataTree_1_switch"]')
    # 目标//span[text()="目标"]
    target_source = (By.XPATH, '//span[@title="数据目标"]')
    # 映射关系
    map = (By.XPATH, '//span[text()="映射关系"]')
    # 保存，映射配置弹出窗的确定按钮
    map_config_button = (By.XPATH, '//a[@id="btn-relation-add"]')
    # 更新映射成功的toast：//div[text()="更新映射成功"]
    toast_message = (By.XPATH, '//div[text()="更新映射成功"]')
    # 多表配置
    table_config = (By.XPATH, '//span[text()="多表配置"]')
    # 多元配置弹出窗-确定按钮//a[@class="btn btn-primary btn-Config-confirm"]
    config_button = (By.XPATH, '//a[@class="btn btn-primary btn-Config-confirm"]')

    # MySQL数据库，操作相关========================================================================
    # 数据库-MySQL
    MySQL = (By.XPATH, ' //span[text()="MySQL"]')

    # 数据库选择后的确认按钮
    db_button = (By.XPATH, '//a[@id="btn-db-type"]')
    # 新增数据库按钮
    add_button_mysql = (By.XPATH, '//form[@name="sameTOMysqlDriver"]//button[@id="addSource"]')

    # 连接名称输入框
    source_name = (By.XPATH, '//form[@name="sameTOMysqlDriver"]//input[@id="sourceName"]')
    # ip输入框
    # ip = (By.ID, 'ip')
    ip = (By.XPATH, '//form[@name="sameTOMysqlDriver"]//input[@id="ip"]')
    # 端口
    port = (By.XPATH, '//form[@name="sameTOMysqlDriver"]//input[@id="port"]')
    # 用户名
    user_name = (By.XPATH, '//form[@name="sameTOMysqlDriver"]//input[@id="userName"]')
    # 密码
    pass_word = (By.XPATH, '//form[@name="sameTOMysqlDriver"]//input[@id="passWord"]')
    # 所属系统下拉三角按钮
    select_system = (
    By.XPATH, '//span[@id="select2-belongToSysName-container"]//parent::span//span[@class="select2-selection__arrow"]')
    # 所属系统的select
    select_option = (By.XPATH, '//*[@name="sameTOMysqlDriver"]//*[@id="belongToSysName"]')
    select = (By.XPATH, '//*[@id="form-fieldset"]//span[@class="select2-selection__arrow"]')
    # 数据库名称
    db_name = (By.XPATH, '//form[@name="sameTOMysqlDriver"]//input[@id="dbName"]')
    # 环境类型
    environment_type = (By.XPATH, '//form[@name="sameTOMysqlDriver"]//select[@id="environmentType"]')
    # 是否跨域
    cross_domain = (By.XPATH, '//form[@name="sameTOMysqlDriver"]//select[@id="crossDomain"]')
    # 编码设置
    character_encoding = (By.XPATH, '//form[@name="sameTOMysqlDriver"]//select[@id="characterEncoding"]')
    # 备注
    mark = (By.XPATH, '//form[@name="sameTOMysqlDriver"]//input[@id="remark"]')
    # 测试连接按钮
    test_connect = (By.XPATH, '//form[@name="sameTOMysqlDriver"]//a[@id="test-connect"]')
    # 测试连接的toast:
    test_msg = (By.XPATH, '//span[text()="连接成功"]')
    # 上一步按钮
    last_step = (By.XPATH, '//a[text()="上一步"]')
    # 下一步按钮
    next_step = (By.XPATH, '//a[text()="下一步"]')
    # 多表选择
    more_table = (By.XPATH, '//button[@id="tableSelect"]')
    # 表
    #  table_name = (By.XPATH, '//input[@data-name="soldiers_bak"]')
    # select_page
    select_page = (By.XPATH, '//select[@name="tableTab_length"]')



    # mysql_common
    mysql_common = (By.XPATH, '//input[@data-name="city"]')
    # mysql_common_bak
    mysql_common_bak = (By.XPATH, '//input[@data-name="common_bak"]')

    #  数据库第二个表
    #  second_tab = (By.XPATH, '//input[@data-name="soldiers_bak"]')
    # 下一步
    next_step = (By.XPATH, '//a[text()="下一步"]')
    # 最终确定按钮
    confirm_button = (By.XPATH, '//a[text()="确定"]')
    # MySQL数据库，操作相关========================================================================

    # 添加成功后的数据源
    source_title = (By.XPATH, '//span[text()="at_source_1"]')
    #  添加成功后的目标源
    out_source_title = (By.XPATH, '//span[text()="at_source_2"]')
    # 数据节点================================================================================================
    # 数据源节点
    source_node_1 = (By.XPATH, '//table[@id="at_source01"]//td[text()="INT"]')
    # 目标节点
    target_node_1 = (By.XPATH, '//table[@id="at_target01"]//td[text()="INT"]')
    # 数据节点，连线箭头
    connector = (By.XPATH, '//img[@src="../assets/images/connector.gif"]')

    # 工作流==================================================================================================
    # 作业 的工作流
    work_flow = (By.XPATH, '//span[text()="工作流"]')
    # 添加工作流按钮
    add_work_folw_btn = (By.XPATH, '//ul[@id="treeDemo_1_ul"]//span[text()="添加"]')
    # 工作流脚本完成的信息 捕捉(几行日志的定位一样)
    work_flow_finished_1 = (By.XPATH, '//span[contains(@class, "loading")][1]')
    #  工作流脚本完成的信息 捕捉(几行日志的定位一样)
    work_flow_finished_2 = (By.XPATH, '//span[contains(@class, "loading")][2]')
    #  工作流脚本完成的信息 捕捉(几行日志的定位一样)
    work_flow_finished_3 = (By.XPATH, '//span[contains(@class, "loading")][3]')
    # 工作流名字输入框
    work_flow_input = (By.XPATH, '//input[@id="workflowName"]')
    workflowBtn = (By.XPATH, '//a[@id="workflowBtn"]')
    # 确定按钮
    btn_workflow_add = (By.XPATH, '//a[@class="btn btn-primary btn-workflow-add"]')
    # 新增的工作流
    new_work_flow = (By.XPATH, '//span[text()="test_work_flow_01"]')
    # 工作流删除test_work_flow_01
    delete_work_flow = (By.XPATH, '//span[text()="test_work_flow_01"]//parent::a//span[text()="删除"]')
    # 工作流删除dialog  删除按钮
    btn_workflow_delete = (By.XPATH, '//a[@id="btn-workflow-delete"]')


    # oracle数据库相关=============================================================================
    # 数据库-ORACLE
    ORACLE = (By.XPATH, ' //span[text()="ORACLE"]')
    # 数据类型为oracle，新增按钮
    add_button_oracle = (By.XPATH, '//form[@name="oracle.jdbc.driver.OracleDriver"]//button[@id="addSource"]')


if __name__ == '__main__':
    a = DesignerPageLocator.job_loc("hel")
    print(a)