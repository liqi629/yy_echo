# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 10:34
# @Author   : l7
# @File     : test_1_login.py
# @Software : PyCharm
from TestDatas import login_datas as ld
from PageObjects.home_page import HomePage
from PageObjects.login_page import LoginPage
import pytest
from TestDatas import Common_Datas as CD
@pytest.mark.usefixtures("login_class")
@pytest.mark.usefixtures("login_case")
class TestLogin:
    # 异常场景：密码错误、用户名错误

    @pytest.mark.parametrize("data", ld.wrong_data)
    def test_login_1_error(self, data, browser):
        """
        名称：使用错误的账号密码信息登录
        步骤：
        1、打开浏览器
        2、输入账号密码
        3、点击登录按钮
        检查点：
        * 检查页面弹出的提示信息。
        """
        LoginPage(browser).login(data["user"], data["pwd"])
        msg = LoginPage(browser).erro_msg()
        assert data["msg"] == msg



    def test_login_2_sucess(self,browser):
        """
        名称：使用正确的账号密码信息登录
        步骤：
        1、打开浏览器
        2、输入正确账号密码
        3、点击登录按钮
        检查点：
        * 检查页面右侧的账户名是否存在。
        """
        LoginPage(browser).login(ld.ID_1["user"], ld.ID_1["pwd"])
        msg = HomePage(browser).is_user_link_exists()
        assert msg== True

    def test_login_3_out(self, browser):
        """
        名称：退出登录
        步骤：
        1、点击用户昵称
        2、点击退出按钮
        检查点：
        * 检查页面右侧的账户名是否存在。
        """
        HomePage(browser).logout()
        msg = HomePage(browser).is_user_link_exists()
        assert msg == False


