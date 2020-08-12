# -*- coding: utf-8 -*-
# @Time     : 2019/10/309:30
# @Author   : l7
# @File     : sql_mysql.py
# @Software : PyCharm



'''
    存放各种数据类型的数据，用于数据库脚本使用。

'''

create_database = "CREATE DATABASE `autotest` CHARACTER SET 'utf8' COLLATE 'utf8_unicode_ci';"
create_table_common = "CREATE TABLE `autotest`.`common`  (`id` int(0) NOT NULL,`name` varchar(255) NULL," \
                      "`price` double(255, 15) NULL,`count` int(0) NULL,`create_time` datetime(0) NULL,PRIMARY KEY (`id`));"
create_table_common_bak = "CREATE TABLE `autotest`.`common_bak`  (`id` int(0) NOT NULL,`name` varchar(255) NULL," \
                      "`price` double(255, 15) NULL,`count` int(0) NULL,`create_time` datetime(0) NULL,PRIMARY KEY (`id`));"

insert_1 = 'INSERT INTO `autotest`.`common` VALUES (1,"《java从入门到精通一》",69.61,122, "2019-02-22 13:25:07")'


select_table_common = "select * from`autotest`.`common`"

drop_table_common = "drop table common"

drop_database = "drop database autotest"
