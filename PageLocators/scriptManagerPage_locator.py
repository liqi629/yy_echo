# -*- coding: utf-8 -*-
# @Time     : 2019/11/513:48
# @Author   : l7
# @File     : scriptManagerPage_locator.py
# @Software : PyCharm
from selenium.webdriver.common.by import By

class ScriptManagerPageLocator:
    # 脚本管理=============================================================================================================


    # 添加按钮
    btn_add_script = (By.XPATH, '//i[@class="el-icon-document-add"]')


    # 脚本名称
    script_name = (By.XPATH, '//div[@class="el-input el-input--small"]//input[@class="el-input__inner"]')

    # 脚本内容输入框
    script_content = (By.XPATH, '//div[@id="scrpitInput"]')
    # 备注
    mark = (By.XPATH, '//textarea[@class="el-textarea__inner"]')
    # 确定
    btn_sub = (By.XPATH, '//div[@class="el-button el-button--primary el-button--small"]')

    btn_edit_sub = (By.XPATH, '//div[@id="modalTable"]//button[text()="提交"]')
    # 新增的脚本
    script_gbase_loader_1 = (By.XPATH, '//td[text()="gbase_loader_1"]')
    script_gbase_loader_2 = (By.XPATH, '//td[text()="gbase_loader_2"]')



    # 确定删除按钮//div[@id="deleteModalTable"]//button[text()="确定"]
    btnConfirm = (By.XPATH, '//div[@id="deleteModalTable"]//button[text()="确定"]')

    # 修改
    edit_name = (By.XPATH, '//form[@id="model"]//input[@id="name"]')

    # 筛选条件
    # 脚本名称
    search_script_name = (By.XPATH, '//input[@name="name"]')
    # 脚本状态
    search_select_script_status = (By.XPATH, '//select[@name="status"]')
    # 脚本类型
    search_select_script_type = (By.XPATH, '//form[@id="searchForm"]//select[@id="scriptType"]')
    # 数据库类型
    search_select_dbtypt = (By.XPATH, '//form[@id="searchForm"]//select[@id="dbType"]')
    # 开始时间
    search_start_time = (By.XPATH, '//input[@name="beginUpdateDt"]')
    # 结束时间
    search_end_time = (By.XPATH, '//input[@name="endUpdateDt"]')
    # 查询
    btn_search_script = (By.XPATH, '//a[@id="search"]')

    # 筛选结果为空
    search_empty = (By.XPATH, '//td[@class="dataTables_empty"]')
    # 操作
    # 查看详情：gbase_loader_1
    btn_look_gbase_loader_1 = (By.XPATH, '//td[text()="gbase_loader_1"]//parent::tr//a[@data-type="look"]')
    # 编辑：gbase_loader_1
    btn_edit_gbase_loader_1 = (By.XPATH, '//td[text()="gbase_loader_1"]//parent::tr//a[@data-type="edit"]')
    # 删除:gbase_loader_2
    btn_del_gbase_loader_2 = (By.XPATH, '//td[text()="gbase_loader_2"]//parent::tr//a[@data-type="delete"]')
    # gbase_loader_2启用/禁用
    btn_status_gbase_loader_2 = (By.XPATH, '//td[text()="gbase_loader_2"]//parent::tr//a[@data-type="status"]')

    # 已启用
    status_1_gbase_loader_2 = (By.XPATH, '//td[text()="gbase_loader_2"]//parent::tr//a[text()="禁用"]')
    # 窗口
    # 查看脚本
    modal_title_look = (By.XPATH, '//div[@id="lookModalTable"]//h4[@class="modal-title"]')
    modal_title_edit = (By.XPATH, '//div[@id="modalTable"]//h4[@class="modal-title"]')