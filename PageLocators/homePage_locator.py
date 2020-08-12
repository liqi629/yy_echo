# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 14:18
# @Author   : l7
# @File     : homePage_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By


class HomePageLocator:

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
    def btn_del(text):
        """

        :param text: 删除按钮对应的应用名字
        :return: 应用名字对应的删除按钮的定位
        """
        btn_del = (By.XPATH, '//*[text()="{}"]//ancestor::tr//*[text()="删除"]'.format(text))
        return btn_del

    @staticmethod
    def btn_del_work_dir(text):
        """
        工作目录的删除:传入要删除的工作目录的名字返回对应的删除按钮的定位
        :param text:工作目录的名字
        :return:
        """
        loc = (By.XPATH, '//*[text()="{}"]//ancestor::tr//i[@class="el-icon-delete"]'.format(text))
        return loc

    @staticmethod
    def btn_into_work_dir(text):
        """
        工作目录的进入:传入要进入的工作目录的名字返回对应的进入按钮的定位
        :param text:工作目录的名字
        :return:
        """
        loc = (By.XPATH, '//div[text()="{}"]//ancestor::tr//*[@class="el-icon-position"]'.format(text))
        return loc
    # 进入工作目录自动化测试目录
    into_work_dir = (By.XPATH, '//div[text()="自动化测试目录"]//ancestor::tr//*[@class="el-icon-position"]')

    # 通用=========================================================================================
    # 用户昵称
    user_link = (By.XPATH, '//div[@role="button"]')
    # 推出按钮
    logout_button = (By.XPATH, '//span[text()="退出"]')
    # 页面弹出的msg
    toast_msg = (By.XPATH, '//p[@class="el-message__content"]')
    # 导航菜单=========================================================================================

    # 工作目录
    work_dir = (By.XPATH, '//span[text()="工作目录管理"]')
    # 添加
    btn_add = (By.XPATH, '//span[text()="添加"]')
    # 工作目录名称
    work_dir_name = (By.XPATH, '// input[@autotest="workDirectoryName"]')
    # 工作目录描述
    remark = (By.XPATH, '//textarea[@autotest="remark"]')
    # 确定
    btn_confirm = (By.XPATH, '//button[@autotest="submit"]')
    # 添加成功msg-通用



    # 映射设计器
    map_designer = (By.XPATH, '//span[text()="映射设计器"]')

    # 系统管理
    system = (By.XPATH, '//span[text()="系统管理"]')
    # 系统管理-用户管理
    user_management = (By.XPATH, '//span[text()="用户管理"]')
    # 系统管理-用户管理-添加用户
    add_user = (By.XPATH, '//span[text()="添加用户"]')
    # 系统管理-用户管理-所有用户
    user_list = (By.XPATH, '//span[text()="所有用户"]')
    # 作业设计
    job_design = (By.XPATH, '//span[text()="作业设计"]')
    # 设计器
    designer = (By.XPATH, '//span[text()="设计器"]')
    # 资源管理==================================================================================================
    business_management = (By.XPATH, '//span[text()="资源管理"]')
    # 子菜单数据源管理
    data_source_manager = (By.XPATH, '//span[text()="数据源管理"]')
    # 子菜单数应用管理/业务系统
    operation_system = (By.XPATH, '//span[text()="应用管理"]')
    # 子菜单脚本管理
    script_manager = (By.XPATH, '//span[text()="脚本管理"]')
    # 子菜单算法管理
    algorithmManagement = (By.XPATH, '//span[text()="算法管理"]')

    # 子菜单交换关系图
    mindMap = (By.XPATH, '//span[text()="交换关系图"]')
    # 子菜单作业示例
    sampleJob = (By.XPATH, '//span[text()="作业示例"]')
    # 子菜单作业示例-导入作业
    importJob = (By.XPATH, '//span[text()="导入作业"]')
    # 子菜单作业示例-导入数据
    importData = (By.XPATH, '//span[text()="导入数据"]')

    # 子菜单算法管理-所有算法
    algorithmManagementAll = (By.XPATH, '//span[text()="所有算法"]')
    # 子菜单算法管理-添加算法dd
    algorithmManagementAdd = (By.XPATH, '//span[text()="添加算法"]')
    # 页面标题数据源管理
    page_data_source_manager = (By.XPATH, '//ol[@class="breadcrumb bc-3"]//*[text()="数据源管理"]')
    # 页面标题业务体系管理/应用管理
    page_operation_system = (By.XPATH, '//strong[text()="应用管理"]')

    # 作业设计-脚本管理
    page_script_manager = (By.XPATH, '//ol[@class="breadcrumb bc-3"]//*[text()="脚本管理"]')

    # 首页数据元素============================================================================================

    # 今日任务数//div[@data-type="todayTaskCnt"]//i[@class="num"]
    todayTaskCnt = (By.XPATH, '//div[@data-type="todayTaskCnt"]//i[@class="num"]')


    # 业务系统================================================================================================
    # 搜索功能的元素定位===================================================
    # 中文简称
    search_short_zn_name = (By.XPATH, '//input[@name="shortZhName"]')
    # 英文简称
    search_short_en_name = (By.XPATH, '//input[@name="shortEnName"]')
    # 所属部门
    search_dept = (By.XPATH, '//input[@name="dept"]')
    # 查询按钮
    btn_search = (By.XPATH, '//a[@id="search"]')
    # 系统状态
    search_sys_status = (By.XPATH, '//div[@id="searchCol"]//select[@name="status"]')
    # 开始时间
    search_start_time = (By.XPATH, '//input[@name="gtUpdateDt"]')
    # 结束时间
    search_end_time = (By.XPATH, '//input[@name="ltUpdateDt"]')
    # 筛选结果为空
    search_empty = (By.XPATH, '//td[@class="dataTables_empty"]')
    # 添加业务系统的元素定位===============================================
    # 添加按钮/
    add_button = (By.XPATH, '//span[text()="添加"]')
    # 中文全称输入框
    zh_name = (By.XPATH, '//form[@class="el-form speDialogForm"]//input[@placeholder="请输入中文名称"]')
    # 编码输入框
    code = (By.XPATH, '//form[@class="el-form speDialogForm"]//input[@placeholder="请输入编码"]')
    # 中文简称输入框
    short_zn_name = (By.XPATH, '//form[@class="el-form speDialogForm"]//input[@placeholder="请输入中文简称"]')
    # 英文全称
    en_name = (By.XPATH, '//form[@class="el-form speDialogForm"]//input[@placeholder="请输入英文名称"]')
    # 英文简称
    short_en_name = (By.XPATH, '//form[@class="el-form speDialogForm"]//input[@placeholder="请输入英文简称"]')
    # 系统概述
    sys_remark = (By.XPATH, '//form[@class="el-form speDialogForm"]//textarea[@placeholder="请输入描述"]')
    # 系统状态
    sys_status = (By.XPATH, '//form[@class="el-form speDialogForm"]//select[@id="status"]')
    # 系统版本
    sys_version = (By.XPATH, '//form[@class="el-form speDialogForm"]//input[@placeholder="请输入版本号"]')
    # 所属部门
    dept = (By.XPATH, '//form[@class="el-form speDialogForm"]//input[@placeholder="请输入部门"]')
    # 联系人,html页面id属性值拼写有错误
    contacter = (By.XPATH, '//form[@class="el-form speDialogForm"]//input[@placeholder="请输入联系人"]')
    # 联系电话
    mobile = (By.XPATH, '//form[@class="el-form speDialogForm"]//input[@placeholder="请输入手机"]')
    # 联系人邮箱
    # email = (By.XPATH, '//form[@class="el-form speDialogForm"]//input[@placeholder="请输入中文名称"]')
    # 确定按钮
    ok_button = (By.XPATH, '//div[@aria-label="新增应用"]//span[text()="确 定"]')



    # 编辑业务系统的元素定位=================================================================================
    # 中文全称输入框
    edit_zh_name = (By.XPATH, '//div[@id="modalTable"]//input[@id="zhName"]')
    # 编码输入框
    edit_code = (By.XPATH, '//div[@id="modalTable"]//input[@id="code"]')
    # 中文简称输入框
    edit_short_zn_name = (By.XPATH, '//div[@id="modalTable"]//input[@id="shortZhName"]')
    # 英文全称
    edit_en_name = (By.XPATH, '//div[@id="modalTable"]//input[@id="enName"]')
    # 英文简称
    edit_short_en_name = (By.XPATH, '//div[@id="modalTable"]//input[@id="shortEnName"]')
    # 系统概述
    edit_sys_remark = (By.XPATH, '//div[@id="modalTable"]//input[@id="remark"]')
    # 系统状态
    edit_sys_status = (By.XPATH, '//div[@id="modalTable"]//select[@id="status"]')
    # 系统版本
    edit_sys_version = (By.XPATH, '//div[@id="modalTable"]//input[@id="version"]')
    # 所属部门
    edit_dept = (By.XPATH, '//div[@id="modalTable"]//input[@id="dept"]')
    # 联系人,html页面id属性值拼写有错误
    edit_contacter = (By.XPATH, '//div[@id="modalTable"]//input[@id="contactor"]')
    # 联系电话
    edit_mobile = (By.XPATH, '//div[@id="modalTable"]//input[@id="mobile"]')
    # 联系人邮箱
    edit_email = (By.XPATH, '//div[@id="modalTable"]//input[@id="email"]')
    # 确定按钮
    edit_ok_button = (By.XPATH, '//div[@id="modalTable"]// button[@class ="btn btn-primary btn-edit"]')


    # 新增成功的业务系统中文全称
    sys_name_at_1 = (By.XPATH, '//*[text()="功能自动化测试一"]')
    # 功能自动化测试二
    sys_name_at_2 = (By.XPATH, '//*[text()="功能自动化测试二"]')


    # //*[text()="自动化测试一"]//ancestor  ::tr//*[text()="删除"]
    # 业务系统：功能自动化测试二，的删除按钮
    btn_del_at_2 = (By.XPATH, '//*[text()="功能自动化测试二"]//parent::tr//*[text()="删除"]')

    # 初始化业务系统
    init_sys_name = (By.XPATH, '//*[text()="功能自动化业务系统"]//parent::tr//*[text()="删除"]')
    # 新增成功的业务系统（功能自动化测试一）的查看详情按钮
    btn_look_sys_1 = (By.XPATH, '//*[text()="功能自动化测试一"]//parent::tr//*[text()="查看详情"]')
    # 新增成功的业务系统（功能自动化测试一）的编辑按钮
    btn_edit_sys_1 = (By.XPATH, '//*[text()="功能自动化测试一"]//parent::tr//*[text()="编辑"]')
    # 业务系统详情窗口标题
    modal_title_sys = (By.XPATH, '//h4[text()="应用信息"]')
    # 删除业务系统的确定按钮/删除工作目录的确认按钮
    delete_button = (By.XPATH, '//button[@class="el-button el-button--default el-button--small el-button--primary "]')
    # 删除业务系统的取消按钮
    cancel_button = (By.XPATH, '//div[ @id="deleteModalTable"]//button[text()="取消"]')



    # 数据传输总览
    # table
    # table=(By.XPATH,'//table[@id="statHeaderTable"]')
    table = (By.ID, 'statHeaderTable')
    # testFile
    testFile = (By.XPATH, '//*[@id="statTable"]')
    # 业务系统
    sys = (By.XPATH, '//span[text()="业务系统"]')
    # 今日任务数
    taskText = (By.XPATH, '//div[text()="今日任务数"]')

    # 交换关系图===========================================================================================================================
    # 表节点视图//a[@id="btnOpenTable"]
    openTable = (By.XPATH, '//a[@id="btnOpenTable"]')

    # 作业示例-导入作业============================================================================
    # 导入作业
    title_importJob = (By.XPATH, '//strong[text()="导入作业"]')

    # 作业示例-导入数据============================================================================
    # 导入作业
    title_importData = (By.XPATH, '//strong[text()="导入数据"]')

    # 所有算法=======================================================================================
    # 算法列表
    title_algorithm = (By.XPATH, '//strong[text()="算法列表"]')

    # 添加算法=======================================================================================
    # 添加算法
    title_addAlgorithm = (By.XPATH, '//strong[text()="添加算法"]')



    # 数据源管理页面================================================================================================================================

    # 数据类型选择
    select_unit_type = (By.XPATH, '//select[@name="unit_type"]')
    # 查询按钮
    btn_search = (By.XPATH, '//a[@id="search"]')
    # 数据源名称
    at_source_1 = (By.XPATH, '//td[text()="at_source_1"]')

    # 查看详情数据源:at_source_1
    btn_look_at_source_1 = (By.XPATH, '//*[text()="at_source_1"]//parent::tr//*[text()="查看详情"]')
    # 删除按钮
    btn_del_at_source_1 = (By.XPATH, '//*[text()="at_source_1"]//parent::tr//*[text()="删除"]')
    # 删除dialog的 确定按钮
    btn_del_ok = (By.XPATH, '//button[@class="btn btn-primary btn-delete"]')
    # 更新时间
    updatetime = (By.XPATH, '//*[text()="at_source_1"]//parent::tr//*[@class="sorting_1"]')
    # 开始时间
    start_time = (By.XPATH, '//input[@name="beginTime"]')
    # 结束时间
    end_time =  (By.XPATH, '//input[@name="endTime"]')
    # 应用详情
    # 标题
    modal_title_data_source = (By.XPATH, '//h4[text()="数据源信息"]')
if __name__ == '__main__':
    a = HomePageLocator.btn_del("hhah")
    print(a)