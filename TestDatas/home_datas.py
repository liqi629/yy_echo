# -*- coding: utf-8 -*-
# @Time     : 2019/6/4 13:57
# @Author   : l7
# @File     : home_datas.py
# @Software : PyCharm
from faker import Faker


f = Faker(locale='zh_cn')


shortZhName = f.name() + "的应用"







# 系统初始创建的业务系统名称
init_system_name= "Echo"
# 自己创建的业务系统：功能自动化测试二
system_2 = "测试应用"
# 系统初始化业务系统详细信息一
init_operation_system={
    "zh_name": "功能自动化业务系统",
    "code": "123456789",
    "short_zn_name": "自动化业务系统",
    "en_name": "AutoTest",
    "short_en_name": "at",
    "sys_remark": "这个业务系统是用来做自动化测试的，请勿删除",
    # "sys_status":"",
    "sys_version": "1.0",
    "dept": "产品质量保障部",
    "contacter": "产品测试员一",
    "mobile": "18610430001",
    "email": "li.qi@yoyosys.com.cn"
}
# 业务系统：功能自动化测试一
operation_system_1 ={
    "zh_name": "功能自动化测试一",
    "code": "123456789",
    "short_zn_name": "自动化测试一",
    "en_name": "uiAutoTestOne",
    "short_en_name": "autoTestOne",
    "sys_remark": "这个业务系统是用来做自动化测试的，请勿删除",
    # "sys_status":"",
    "sys_version": "1.0",
    "dept": "产品质量保障一部",
    "contacter": "产品测试员一",
    "mobile": "18610430001",
    "email": "li.qi@yoyosys.com.cn"

}
# 业务系统：功能自动化测试二
operation_system_2 ={
    "zh_name": "功能自动化测试二",
    "code": "123456788",
    "short_zn_name": "自动化测试二",
    "en_name": "uiAutoTestTwo",
    "short_en_name": "autoTestTwo",
    "sys_remark": "这个业务系统是用来做自动化测试的，请勿删除",
    "sys_status":"正常",
    "sys_status_e":"异常",
    "sys_version": "2.0",
    "dept": "产品质量保障二部",
    "contacter": "产品测试员二",
    "mobile": "18610430002",
    "email": "li.qi@yoyosys.com.cn"

}

class HomeDatas:
    app_manager_start_time = None
    app_manager_end_time = None
