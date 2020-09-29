# -*- coding: utf-8 -*-
# @Time     : 2019/5/23 10:04
# @Author   : l7
# @Email    :liqi_629@163.com
# @File     : BasePage.py
# @Software : PyCharm
# import logging
import time

from loguru import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.keys import Keys
from Common import dir_config
# from Common import logger

'''
需要引入logger，才能使用自己定义好的日志
封装操作页面时候用的常用操作
'''

# loguru_logger = dir_config.logs_dir+"/Web_Autotest_{time}.log"
logger.add(dir_config.logs_dir+"/Web_Autotest_{time}.log")


class BasePage:
    def __init__(self, driver):  # 必须外部传入driver  同一个driver经历多个页面
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, loc, timeout=10, poll_frequency=0.5, model=None):
        '''
        :param loc: 元素定位表达式。元素类型，表达方式（元素定位类型，元素定位方法）
        :param timeout: 等待超时时间上限
        :param poll_frequency: 轮询周期
        :param model:等待失败时，截图操作，图片文件中需要显示的功能模块标注
        :return: None
        '''
        logger.info("{1}：等待元素可见：{0}".format(loc, model))
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(loc))
            end = time.time()
            logger.info("等待时长{0}：以秒为单位".format(round(end - start, 2)))
        except:
            logger.error("等待元素可见失败。")
            # 截图
            self.save_webImgs(model)
            raise
    # 查找一个元素
    def get_Element(self, loc, model=None):
        logger.info("{1}：查找元素：{0}".format(loc, model))
        try:
            return self.driver.find_element(*loc)
        except:
            logger.error("查找元素失败。")
            # 截图
            self.save_webImgs(model)
            raise

    # 输入操作
    def input_text(self, loc, text, model=None):
        # 查找元素
        ele = self.get_Element(loc, model)
        # 输入元素
        logger.info("{0}：在元素{1}中输入文本：{2}".format(model, loc, text))
        try:
            ele.clear()
            ele.send_keys(text)
        except:
            logger.error("输入操作失败。")
            self.save_webImgs(model)
            raise

    # 点击操作
    def click_element(self, loc, model=None):
        # 找元素再点击
        ele = self.get_Element(loc, model)
        # 点击操作
        logger.info("{0}:元素：{1}点击事件".format(model, loc))
        try:
            ele.click()
        except:
            logger.error("元素：{0}点击事件失败".format(loc))
            self.save_webImgs(model)
            raise
        # finally:
        #     ele.click
        #     logger.info("{0}:元素：{1}第二次点击事件".format(model, loc))
    # 鼠标悬浮
    def hover_element(self, loc, model=None):
        # 查找元素
        ele = self.get_Element(loc, model)
        logger.info("{0}:元素：{1}鼠标悬停事件".format(model, loc))
        try:
            AC(self.driver).move_to_element(ele).perform()
            logger.info("{0}:元素：{1}鼠标悬停成功".format(model, loc))
        except:
            logger.error("鼠标悬停操作失败。")
            self.save_webImgs(model)
            raise
    def click_and_hold(self, loc, model=None):
        ele = self.get_Element(loc, model)
        AC(self.driver).click_and_hold(ele).perform()

    def move_to_element(self, loc, model=None):

        ele = self.get_Element(loc, model)
        AC(self.driver).move_to_element(ele).perform()
    def move_to_element_release(self, loc, model=None):
        ele = self.get_Element(loc, model)
        AC(self.driver).move_to_element(ele).release().perform()
    # 双击操作
    def double_click_element(self, loc, model=None):
        ele = self.get_Element(loc, model)
        try:
            AC(self.driver).double_click(ele).perform()
            logger.info("{0}:元素：{1}鼠标双击成功".format(model, loc))
        except:
            logger.error("鼠标双击操作失败。")
            self.save_webImgs(model)
            raise

    # 右键点击
    def context_click_element(self, loc, model=None):
        # 找元素再点击
        ele = self.get_Element(loc, model)
        try:
            AC(self.driver).context_click(ele).perform()
            logger.info("{0}:元素：{1}鼠标右键点击成功".format(model, loc))
        except:
            logger.error("鼠标右键点击：{0}:元素：{1}操作失败。".format(model, loc))
            self.save_webImgs(model)
            raise
    # tab

    def keyboard_tab(self, loc, model=None):
        # 找元素再点击
        ele = self.get_Element(loc, model)
        try:
            ele.send_keys(Keys.TAB)
            logger.info("tab换行")
        except:
            logger.error("tab换行失败")
            self.save_webImgs(model)
            raise
    # 鼠标拖拽
    def drag_and_drop(self, loc1, loc2):
        AC(self.driver).drag_and_drop(loc1, loc2).perform()

    def drag_and_drop_by_offset(self, loc, x, y, model=None):

        ele = self.get_Element(loc, model)
        # for i in range(5):
        AC(self.driver).drag_and_drop_by_offset(ele, x, y).perform()

    # 清除操作
    def clear_input_text(self, loc, model=None):
        # 找元素再清除
        ele = self.get_Element(loc, model)
        logger.info("{0}：清除元素：{1}".format(model, loc))
        try:
            ele.clear()
        except:
            logger.error("清除失败")
            self.save_webImgs(model)
            raise

    # 获取文本内容
    def get_text(self, loc, model=None):
        # 找到元素
        self.wait_eleVisible(loc)
        ele = self.get_Element(loc, model)
        # 获取元素的文本内容
        logger.info("{0}:获取元素:{1}的文本内容".format(model, loc))
        try:
            text = ele.text
            logger.info("{0}:元素:{1}的文本内容为:{2}".format(model, loc, text))
            return text
        except:
            # 捕获异常到日志
            logger.error("获取元素:{0}的文本内容失败。".format(loc))
            # 截图
            self.save_webImgs(model)
            # 抛出异常
            raise

    # 获取元素属性
    def get_element_attribuute(self, loc, attr_name, model=None):
        # 找到元素
        ele = self.get_Element(loc, model)
        # 获取元素属性
        logger.info("{0}:获取元素：{1}的属性：{2}".format(model, loc, attr_name))
        try:
            value = ele.get_attribute(attr_name)
            logger.info("{0}:元素：{1}的属性：{2}值为：{3}".format(model, loc, attr_name, value))
            return value
        except:
            logger.error("获取元素：{0}的属性：{1}失败，异常信息".format(loc, attr_name))
            self.save_webImgs(model)
            raise

    # 截图
    def save_webImgs(self, model= None):
        # filepath=制定的图片保存目录/model(页面功能名称)_当前时间到秒.png
        filepath = dir_config.screenshot_dir + \
                   "/{0}_{1}.png".format(model, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        try:
            self.driver.save_screenshot(filepath)
            logger.info("截屏成功,图片路径为{0}".format(filepath))
        except:
            logger.error("截屏失败")

    # iframe切换
    def switch_iframe(self, frame_refer, timeout=30, poll_frequency=0.5, model=None):
        # 等待iframe存在
        logger.info("iframe切换操作：")
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(
                EC.frame_to_be_available_and_switch_to_it(frame_refer))
            time.sleep(0.5)
            logger.info("切换成功")
        except:
            logger.error("iframe切换失败！")
            self.save_webImgs(model)
            raise
        # 切换回初始还没有完善
        # self.driver.switch_to_default_content()

        # 切换==index、name\id\WebElement

    # alert切换
    def switch_alert(self, timeout=10, poll_frequency=0.5, model=None):
        '''
        正常获取到弹出窗的text内容就返回alert这个对象（注意这里不是返回Ture），没有获取到就返回False
        :param timeout:
        :param poll_frequency:
        :param model:
        :return:
        '''
        try:
            result = EC.alert_is_present()(self.driver)
            if result:
                msg = result.text
                logger.info("alert出现，内容为：{0}".format(msg))
                result.accept()
                logger.info("alert已经关闭")
                return msg
            else:
                logger.info("未弹出alert")

        except:
            logger.error("alert切换失败！")
            self.save_webImgs(model)
            raise

    # 获取窗口句柄
    def current_handles(self):
        current_handles = self.driver.window_handles
        return current_handles

    # 窗口切换==如果是切换到新窗口，new，如果是回到默认窗口，default。切换前，在新窗口打开前获取handles
    def switch_window(self, name, current_handles=None, timeout=30, poll_frequency=0.5, model=None):
        '''
        :param name: new代表最新打开的一个窗口。default代表第一个窗口。其他的值表示为窗口的handles
        :param current_handles:
        :param timeout:
        :param poll_frequency:
        :param model:
        :return:
        '''
        try:
            if name == "new" and current_handles is not None:
                logger.info("切换到最新打开的窗口")
                WebDriverWait(self.driver, timeout, poll_frequency).until(EC.new_window_is_opened(current_handles))
                window_handles = self.driver.window_handles  # 获取所有窗口句柄
                self.driver.switch_to.window(window_handles[-1])
            elif name == "default":
                logger.info("切换到第一个窗口")
                window_handles = self.driver.window_handles
                self.driver.switch_to.window(window_handles[0])
                # self.driver.switch_to_default_content()
            else:
                logger.info("切换到指定handles")
                self.driver.switch_to.window(name)
        except:
            logger.error("切换失败")
            self.save_webImgs(model)
            raise

    # select操作
    def select(self, loc):
        # 等待Select出现
        self.wait_eleVisible(loc)
        # 找到select元素
        select_ele = self.get_Element(loc)
        # 初始化select类
        s = Select(select_ele)
        return s
        # # 1、下标
        # s.select_by_index()
        # # 2、value属性
        # s.select_by_value()
        # # 3、文本内容
        # s.select_by_visible_text()



    def url(self):
        """ 获取当前页面的url方法BasePage.py"""
        try :
            momonent=self.driver.current_url()
            return momonent
        except Exception:
            raise ValueError("获取当前页面URL失败了")
        finally:
            momonent = self.driver.current_url()
            return momonent

    def refresh(self):
        self.driver.refresh()