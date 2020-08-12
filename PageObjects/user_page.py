from Common.BasePage import BasePage
from PageLocators.userPage_locator import UserPageLocator as loc


class UserPage(BasePage):
    # 填写用户信息,并提交
    def fill_in_user(self, user, pwd1, pwd2, name, employee_id,
                     department, email, mobile, phone, loc_role):
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.user_input)
        self.input_text(loc.user_input, user)
        self.input_text(loc.pwd_input, pwd1)
        self.input_text(loc.confirmpwd_input, pwd2)
        self.input_text(loc.name_input, name)
        self.input_text(loc.employee_ID, employee_id)
        self.input_text(loc.department_input, department)
        self.input_text(loc.Email, email)
        self.input_text(loc.mobile, mobile)
        self.input_text(loc.phone, phone)
        try:
            self.click_element(loc_role)
        except:
            pass
        self.save_user()
        # self.click_element(loc.dialog_add_succ)

    # 修改用户信息，依次输入内容，保存
    def modify_user(self, user, name, pwd1, employee_id,
                    department, email, mobile, phone):
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc.modify_user_x_10)
        self.click_element(loc.modify_user_x_10)
        self.wait_eleVisible(loc.user_input_1)
        self.clear_input_text(loc.user_input_1)
        self.input_text(loc.user_input_1, user)
        self.clear_input_text(loc.pwd_input)
        self.input_text(loc.pwd_input, pwd1)
        self.clear_input_text(loc.name_input)
        self.input_text(loc.name_input, name)
        self.clear_input_text(loc.employee_ID)
        self.input_text(loc.employee_ID, employee_id)
        self.clear_input_text(loc.department_input)
        self.input_text(loc.department_input, department)
        self.clear_input_text(loc.Email)
        self.input_text(loc.Email, email)
        self.clear_input_text(loc.mobile)
        self.input_text(loc.mobile, mobile)
        self.clear_input_text(loc.phone)
        self.input_text(loc.phone, phone)
        self.save_user()

    # 删除用户
    def del_user(self, loc_user_x):
        self.switch_iframe(loc.main_frame)
        self.wait_eleVisible(loc_user_x)
        self.click_element(loc_user_x)
        self.switch_alert()
        self.switch_window("default")

    # 保存用户
    def save_user(self):
        self.wait_eleVisible(loc.submit)
        self.click_element(loc.submit)

    # 判断是否弹出添加用户成功的dialog
    def is_add_user(self):
        try:
            # self.switch_iframe(loc.main_frame)
            # self.wait_eleVisible(loc_user_x, timeout=3)
            self.wait_eleVisible(loc.dialog_add_succ)
            return True
        except:
            return False

    # 判断是否弹出用户已存在的dialog
    def is_already_user(self):
        try:
            # self.switch_iframe(loc.main_frame)
            # self.wait_eleVisible(loc_user_x, timeout=3)
            self.wait_eleVisible(loc.dialog_already_user)
            return True
        except:
            return False
    # 判断是否弹出修改用户成功的dialog
    def is_modify_user(self):
        try:
            # self.switch_iframe(loc.main_frame)
            # self.wait_eleVisible(loc_user_x, timeout=3)
            self.wait_eleVisible(loc.dialog_modify_succ)
            return True
        except:
            return False

    # 判断用户列表有某个用户
    def is_user_list(self, loc_user_x):
        try:
            self.switch_iframe(loc.main_frame)
        except:
            raise
        try:
            self.wait_eleVisible(loc_user_x, timeout=4)
            return True
        except:
            return False
