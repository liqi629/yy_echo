import time

from PageLocators.designerPage_locator import DesignerPageLocator as dp_loc

ts = int(time.time())





work_dir_name = "自动化测试目录{}".format(ts)
map_name = "映射_mysql_city{}".format(ts)
work_flow_name = "mysql_qc_city{}".format(ts)
# 用户故事1：映射的定位
map_name_loc = dp_loc.job_loc(map_name)
mysql_node_info = [
    {"data_type":"source", "job": map_name_loc, "source_name": "mysql_qc", "ip": "172.16.161.119", "port": "3306",
     "user_name":"root", "pass_word":"root", "table":dp_loc.tab_loc("city"), "sys_name": "功能自动化测试一","db_name":"qc"},

    {"data_type":"target", "job": map_name_loc,"source_name": "mysql_qc", "ip": "172.16.161.119", "port": "3306",
     "user_name":"root", "pass_word":"root", "table":dp_loc.tab_loc("city_t"),"sys_name": "功能自动化测试一","db_name":"qc"}
]

# 业务系统：功能自动化测试一
operation_system_1 =[{
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

}]