# coding:utf-8
# author:huangkun

import time
import unittest

from selenium.webdriver.common.by import By

from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.getToast import get_Toast
from utils.log import logging
from utils.operaYaml import operayaml


class findcourse(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logging.info("recommendFront/classCode.py 用例开始执行")
        self.driver = Caps.set_caps(None)
        logIn(self.driver, "up0864", '123456')
        # 登录成功后，关闭弹框
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        logging.info("recommendFront/classCode.py 用例执行结束")



    def test_course_none(self):
        '''查找没有的课程'''
        logging.info("用例描述：查找没有的课程")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/findCourse"))
        time.sleep(2)
        self.driver.find_element_by_id("com.up366.mobile:id/input").send_keys("sdasd")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/rightText"))  # 查找按钮
        toast = get_Toast(self.driver,"没有相关课程，请确认课程码后重新输入")
        print("toast is :%s"% toast)
        self.assertEqual(toast,"没有相关课程，请确认课程码后重新输入")
        self.driver.find_element_by_id("com.up366.mobile:id/back").click()

    def test_course_join(self):
        '''输入未加入的课程码，点击搜索'''

        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/findCourse"))
        # 判断环境 1是测试环境
        if operayaml.get_device_info(self)["appEnviroment"] == 1:
            self.driver.find_element_by_id("com.up366.mobile:id/input").send_keys(152433)
            Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/rightText"))
            self.assertIsNotNone("com.up366.mobile:id/class_code_join_btn")
        else:
            self.driver.find_element_by_id("com.up366.mobile:id/input").send_keys(170532)
            Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/rightText"))
            self.assertIsNotNone("com.up366.mobile:id/class_code_join_btn")
        self.driver.find_element_by_id("com.up366.mobile:id/back").click()



    def test_course_rejoin(self):
        '''搜索已经结束的课程'''
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/findCourse"))

        # 判断环境 1是测试环境
        if operayaml.get_device_info(self)["appEnviroment"] == 1:
            self.driver.find_element_by_id("com.up366.mobile:id/input").send_keys(128232)
            Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/rightText"))
            ele_text = Base(self.driver).find_element((By.ID, "com.up366.mobile:id/class_code_status")).text
            self.assertEqual(ele_text,"已结束")
        else:
            self.driver.find_element_by_id("com.up366.mobile:id/input").send_keys(170475)
            Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/rightText"))
            ele_text = Base(self.driver).find_element((By.ID, "com.up366.mobile:id/class_code_status")).text
            self.assertEqual(ele_text, "已结束")
        self.driver.find_element_by_id("com.up366.mobile:id/back").click()


if __name__ == '__main__':
    unittest.main