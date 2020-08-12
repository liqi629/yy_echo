# -*- coding: utf-8 -*-
# @Time     : 2019/5/29 14:13
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : db_mysql.py
# @Software : PyCharm
import pymysql
import logging

from Common import dir_config
from Common.readconfig import ReadConfig
from Common import logger

class DoMysql:
    def __init__(self):
        self.config = ReadConfig().read_config(dir_config.db_config_path, "MYSQL_DB", "Config")
        logging.info("开始连接数据库")
        try:
            self.db = pymysql.connect(**self.config)
            logging.info("连接数据库成功")
        except:
            logging.info("数据库连接失败")
            raise

    def ExecQuery(self, sql):
        '''
        执行查询语句
        :param sql:
        :return:
        '''
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)  # 执行sql、
            logging.info("执行sql成功")
        except:
            logging.info("执行sql失败")
            raise
        # res=cursor.fetchone() #单  返回的是一个元组
        res = cursor.fetchall()  # 多  返回的是一个嵌套元组的列表
        # 关掉游标 关掉连接
        cursor.close()
        self.db.close()
        logging.info("执行结果返回值:{0}".format(res))
        return res

    def ExecNonQuery(self, sql):
        '''
        执行非查询语句
        :param sql:
        :return:
        '''
        cursor = self.db.cursor()
        try:
            cursor.execute(sql)
            logging.info("执行sql:{0}成功".format(sql))
        except:
            logging.info("执行sql:{0}失败".format(sql))
            raise
        # commit()方法：在数据库里增、删、改的时候，必须要进行提交，否则插入的数据不生效。
        self.db.commit()
        cursor.close()
        self.db.close()



if __name__ == '__main__':
    mysql = DoMysql().ExecNonQuery
    # # 创建数据库
    # sql1 = "CREATE DATABASE `yoyoat` CHARACTER SET 'utf8' COLLATE 'utf8_unicode_ci';"
    # mysql(sql1)
    # # 创建数据表及字段
    # sql2 = "CREATE TABLE `yoyoat`.`soource_datas`  (`id` int(0) NOT NULL,`varchar` varchar(255) NULL,`bigint` bigint(255) NULL,`double` double(255, 0) NULL,`time` time(6) NULL,PRIMARY KEY (`id`));"
    # mysql(sql2)
    # # 插入数据
    # sql3 = 'INSERT INTO `yoyoat`.`soource_datas` VALUES (1,"《java从入门到精通一》",341,23.1, "11:06:04")'
    # sql4 = 'INSERT INTO `yoyoat`.`soource_datas` VALUES (3,null,null,null, null)'
    # mysql(sql3)
    # mysql(sql4)
    sql = "select * from common"
    res = DoMysql().ExecQuery(sql)
    print(res)

