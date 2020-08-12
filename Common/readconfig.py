# -*- coding: utf-8 -*-
# @Time     : 2019/6/17 9:43
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : readconfig.py
# @Software : PyCharm
#配置文件：.ini   .properties  .Config   .xml  .conf
#主要讲文本形式的   configparser模块  专门处理配置文件
#配置文件的数据读取都是字符串类型  需要使用eval（）  转换
import configparser
from Common import dir_config
class ReadConfig:
    def read_config(self, file_path, section, option):
        '''
        :param file_path: 被读取的文件路径
        :param section:配置文件的标题即[]里面的内容
        :param option:文件类型
        :return:
        '''
        cf=configparser.ConfigParser()#实例化
        cf.read(file_path, encoding='UTF-8')#调用read函数 打开文件

        #获取数据
        value = cf.get(section, option)
        # print("获取到的值是：{0}".format(eval(value)))
        return eval(value)
if __name__=='__main__':
    value=ReadConfig().read_config(dir_config.db_config_path,"Mongo_DB_SYS","config")
    print(value)
    a=ReadConfig().read_config(dir_config.browser_config_path, "browser", "config")
    print(a)