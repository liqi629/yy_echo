from selenium.webdriver.common.by import By


class UserPageLocator:
    # mainFrame
    main_frame = (By.XPATH, '//iframe[@id="mainFrame"]')
    # 添加页面的用户名输入
    user_input = (By.XPATH, '//input[@name="name"]')
    # 修改页面的用户名输入
    user_input_1 = (By.XPATH, '//input[@name="username"]')
    # 密码输入
    pwd_input = (By.XPATH, '//input[@name="password"]')
    # 确认密码输入
    confirmpwd_input = (By.XPATH, '//input[@name="confirmpwd"]')
    # 姓名输入
    name_input = (By.XPATH, '//input[@name="trueName"]')
    # 用户类型选择
    # 性别选择
    select_gender = (By.XPATH, '//select[@name="gender"]')
    # 员工号输入
    employee_ID = (By.XPATH, '// input[ @ name = "serialNumber"]')
    # 部门输入
    department_input = (By.XPATH, '//input[@name="department"]')
    # Email输入
    Email = (By.XPATH, '//input[@name="email"]')
    # 手机输入
    mobile = (By.XPATH, '//input[@name="mobile"]')
    # 电话输入
    phone = (By.XPATH, '//input[@name="phone"]')
    # 角色——系统管理员
    system = (By.XPATH, '//span[text()="系统管理员"]')
    # 保存按钮
    submit = (By.XPATH, '//input[@id="save-user"]')

    # 添加用户成功dialog
    dialog_add_succ = (By.XPATH, '//div[text()="添加用户成功"]')
    # 添加用户已存在dialog
    dialog_already_user = (By.XPATH, '//div[text()="该用户已存在"]')
    # 用户信息修改成功的dialog
    dialog_modify_succ = (By.XPATH, '//div[text()="修改用户信息成功"]')
    # 确定
    make_sure = (By.XPATH, '//button[text()="确定"]')

    # 用户列表的某个用户:auto10、auto11
    user_x_10 = (By.XPATH, '//td[text()="auto10"]')
    user_x_11 = (By.XPATH, '//td[text()="auto11"]')
    # 用户列表某用户的删除按钮:auto11
    del_user_x_11 = (By.XPATH, '//td[text()="自动测试十一"]//parent::tr//a[text()="删除"]')
    # 用户列表某用户的修改按钮：auto10
    modify_user_x_10 = (By.XPATH, '//td[text()="自动测试十"]//parent::tr//a[text()="修改"]')
