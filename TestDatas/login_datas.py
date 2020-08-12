# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 10:31
# @Author   : l7
# @File     : login_datas.py
# @Software : PyCharm

#正常场景：登录成功
#账号admin
admin = {"user": "admin", "pwd": "admin"}
#账号1

ID_1 = {"user": "admin", "pwd": "admin"}
#账号2
ID_2 = {"user": "lq", "pwd": "lq"}

#异常场景：密码错误、用户名错误
wrong_data = [
    {"user": "admin", "pwd": "12a3", "msg": "用户名或密码错误!"},
    {"user": "abac", "pwd": "123a4", "msg": "用户名或密码错误!"}
]


