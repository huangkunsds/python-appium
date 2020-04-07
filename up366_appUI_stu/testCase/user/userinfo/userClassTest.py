#-*- coding:utf-8 -*-
# author:huangkun
# datetime:2018/9/4
import time
import unittest
from selenium.webdriver.common.by import By
from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging


class userClass(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("userClassTest.py 用例开始执行")
        cls.driver = Caps.set_caps(None)
        logIn(cls.driver, "15831539813", '123456')
        # 登录成功后的弹框处理
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        Base(cls.driver).clickButton((By.XPATH,".//*[contains(@text,'黄坤')]"))
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='个人资料']"))

    @classmethod
    def tearDownClass(cls):
        logging.info("userClassTest.py 用例执行结束")
        cls.driver.quit()


    def test_class_notExist1(cls):
        '''输入不存在的班级："班级" '''
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='所属班级']"))
        time.sleep(1)
        cls.driver.find_element_by_id("com.up366.mobile:id/amend_class_input_code").send_keys('班级')
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/amend_class_code_find"))
        ele_text = Base(cls.driver).find_element((By.XPATH,"//*[@text='没有找到班级哦~']")).text
        cls.assertEqual(ele_text,"没有找到班级哦~")
        cls.driver.find_element_by_id("com.up366.mobile:id/back").click()

    def test_class_notExist2(cls):
        '''输入特殊字符：#￥*√ '''
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='所属班级']"))
        time.sleep(1)
        cls.driver.find_element_by_id("com.up366.mobile:id/amend_class_input_code").send_keys('#￥*√')
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/amend_class_code_find"))
        ele_text = Base(cls.driver).find_element((By.XPATH,"//*[@text='没有找到班级哦~']")).text
        cls.assertEqual(ele_text,"没有找到班级哦~")
        cls.driver.find_element_by_id("com.up366.mobile:id/back").click()

    def test_class_notJoin(cls):
        '''查找未加入的班级：1'''
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='所属班级']"))
        time.sleep(1)
        cls.driver.find_element_by_id("com.up366.mobile:id/amend_class_input_code").send_keys('89')
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/amend_class_code_find"))
        ele_text = Base(cls.driver).find_element((By.ID,"com.up366.mobile:id/amend_class_code_join_btn")).text
        cls.assertEqual(ele_text, "我要加入")
        cls.driver.find_element_by_id("com.up366.mobile:id/back").click()

if __name__ == '__main__':
    unittest.main
