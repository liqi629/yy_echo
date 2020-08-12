# -*- coding: utf-8 -*-
# @Time     : 2019/10/319:24
# @Author   : l7
# @File     : sql_oracle.py
# @Software : PyCharm


# 新建表空间
create_tablespace = "CREATE TABLESPACE \"YOYOAT\" DATAFILE  '/opt/oracle/product/11g/dbs/yoyoatdatas' SIZE 100 M AUTOEXTEND ON"
# 新建用户，设置表空间
create_user = "CREATE USER \"YOYOAT\" IDENTIFIED BY \"111111\" DEFAULT TABLESPACE \"YOYOAT\" TEMPORARY TABLESPACE \"TEMP\""
# 授权用户SYSDBA权限
grant_sysdba = "GRANT SYSDBA TO \"YOYOAT\""
# 赋上create session权限
grant_create_session = "grant create session,resource to \"YOYOAT\""
# 授予用户表空间使用权限
alter_user = "ALTER USER \"YOYOAT\" QUOTA UNLIMITED ON \"YOYOAT\""
# 创建表及字段:number、char、int、DATATIME
create_table_common = "CREATE TABLE \"YOYOAT\".\"common\" (" \
       "\"id\" NUMBER ," \
       "\"name\" VARCHAR2(255) ," \
       "\"price\" NUMBER(30,15) ," \
       "\"count\" NUMBER ," \
       "\"create_time\" TIMESTAMP ," \
       "  PRIMARY KEY (\"id\"))"

insert_1 = "INSERT INTO \"YOYOAT\".\"common\" VALUES (1,'java从入门到精通1',69.61,122, to_date('2019-9-16 12:20:33','YYYY-MM-DD HH24:MI:SS') ) "
