from selenium.webdriver.common.by import By


class MysqlLocator:
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
    select_system = (By.XPATH,'//span[@id="select2-belongToSysName-container"]//parent::span//span[@class="select2-selection__arrow"]')
    # 所属系统的select
    select_option = (By.XPATH, '//span[@dir="ltr"]//parent::div//select[@id="belongToSysName"]')
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
    # mysql目标表1
    mysql_target_table01 = (By.XPATH, '//input[@data-name="soldiers_bak"]')
    #  mysql目标表2
    mysql_target_table02 = (By.XPATH, '//input[@data-name="soldiers2_bak"]')
    # mysql数据源目标表1
    mysql_source_table01 = (By.XPATH, '//input[@data-name="soldiers"]')
    #  mysql数据源目标表2
    mysql_source_table02 = (By.XPATH, '//input[@data-name="soldiers2"]')
    # 最终确定按钮
    confirm_button = (By.XPATH, '//a[text()="确定"]')
    # MySQL数据库，操作相关========================================================================

    # 添加成功后的数据源
    source_title = (By.XPATH, '//span[text()="at_source_1"]')
    #  添加成功后的目标源
    out_source_title = (By.XPATH, '//span[text()="at_source_2"]')