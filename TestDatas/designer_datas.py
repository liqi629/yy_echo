# -*- coding: utf-8 -*-
# @Time     : 2019/5/27 15:38
# @Author   : l7
# @File     : designer_datas.py
# @Software : PyCharm
from TestDatas import home_datas as hd

class DesignerDatas:
    script_manager_start_time = None
    script_manager_end_time = None

#新建作业，作业名称
job_at_01 = "作业at_01"
job_at_02 = "作业at_02"
jobname_1 = "自动作业01"

none_job_name=''


run_type = [
    {"type":"local"},
    {"type":"no_local"}
]




none_tosat = "业务名称不能为空!"
sucess_toast = "业务添加成功!"
toast_job_same = "作业名称重复，请重新修改"
#作业发布中toast/发布成功toast

toast_pubing = ["已提交发布请求,请稍后...","发布成功"]
#发布成功toast
toast_pub_success = "发布成功"
#取消发布成功toast
toast_pub_cancel = "取消发布成功"
#映射保存失败
toast_faile="映射保存失败：保存映射，更新源信息失败：10786"
#重复发布tosat
toast_pub_re = "该作业已经发布，请取消发布之后在发布."
#业务系统名称
syaName = "自动化测试业务系统"
#远程服务器信息
remote_ip='172.16.12.28'
remote_port=22
remote_username='root'
remote_pwd='yoyosys'
remote_dir="/user/liqitest/auto_text_01"

#清除远程服务器，文件的内容命令
delete_cmd="> /user/liqitest/auto_text_01"

#数据源和目标，单数为源 双数为目标
#新增数据源
sucess_source ={
    "source_name":"mysql_qc",
    "source_name_2":"at_source_2",
    "ip":"172.16.161.119",
    "port":"3306",
    "user_name":"root",
    "pass_word":"root",
    "sys_name": "功能自动化测试一",
    "db_name":"qc"
}
#目标数据target_data
target_data ={

    "source_name":"at_source_2",
    "ip":"172.16.161.128",
    "port":"3306",
    "user_name":"root",
    "pass_word":"root",
    "sys_name": hd.system_2,
    "db_name":"autotest"
}

oracle_source_1 ={
    "source_name": "oracle_source_1",
    "ip": "172.16.161.129",
    "port": "1521",
    "user_name": "YOYOAT",
    "pass_word": "111111",
    "sys_name": hd.system_2,
    "db_name": "ORCL"

}
db2_source_1 ={
    "source_name": "db2_source_1",
    "ip": "172.16.161.129",
    "port": "50000",
    "user_name": "db2inst1",
    "pass_word": "yoyosys",
    "sys_name": hd.system_2,
    "db_name": "autotest"

}

mongodb_source_1 ={
    "source_name": "mongodb_source_1",
    "ip": "172.16.161.128",
    "port": "27017",
    "user_name": "apple",
    "pass_word": "111111",
    "sys_name": hd.system_2,
    "db_name": "admin",
    "auth_true":"true",
    "auth_mode_SHA":"SCRAM-SHA-1"
}





select_common = 'select * from common'
select_common_bak = 'select * from common_bak'
#新建工作流名字
work_flow_name = "test_work_flow_01"
#工作流名称重复
same_flow_name = "该名称已存在!"
#工作流页面url
work_flow_url = 'http://172.16.12.28:18080/echod_manager/V2/page/workflow/workflow.jsp?id=38'

# 脚本名称、绝对路径、脚本内容、执行机ip
script = {
    "name": "gbase_loader_1",
    "new_name": "gbase_loader_2",
    "AP": "/home/yoyo/gbase_loader_1.sh",
    "scriptType": "客户端命令",
    "dbType": "GBASE",
    "content": '#!/usr/bin/env bash\necho "GBASE数据库脚本"',
    "ip": "172.16.12.28"
}

# 脚本筛选
search = {
    "status_0":"禁用",
    "status_1":"启用",
    "type_0":"导入",
    "type_1":"导出",
    "type_2": "客户端命令",
    "type_3": "数据检测",
    "db_0": "MYSQL",
    "db_1": "DB2",
    "db_2": "HBASE",
    "db_3": "ORACLE",
    "db_4": "KINGBASE",
    "db_5": "SQLSERVER",
    "db_6": "POSTGRESQL",
    "db_7": "GBASE",
    "db_8": "MONGODB",
    "db_9": "yoyo分布式数据库",
    "db_10": "Hive",
    "db_11": "Hive",
}