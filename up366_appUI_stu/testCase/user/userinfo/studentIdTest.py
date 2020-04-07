#-*- coding:utf-8 -*-
# author:huangkun
# datetime:2018/9/4
import unittest
from selenium.webdriver.common.by import By
from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging


class studentId(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("studentIdTest.py 用例开始执行")
        cls.driver = Caps.set_caps(None)
        logIn(cls.driver, "15831539813", '123456')
        # 登录成功后的弹框处理
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        Base(cls.driver).clickButton((By.XPATH,".//*[contains(@text,'黄坤')]"))
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='个人资料']"))

    @classmethod
    def tearDownClass(cls):
        logging.info("studentIdTest.py 用例执行结束")
        cls.driver.quit()

    def test_change1(cls):
        '''字母数字少于6位'''
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='学号']"))
        cls.driver.find_element_by_id("com.up366.mobile:id/user_info_amend_name_ev").send_keys("j34kk")
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/rightText"))
        ele_text = Base(cls.driver).find_element((By.ID,"com.up366.mobile:id/title")).text
        cls.assertEqual(ele_text,"修改学号")
        cls.driver.find_element_by_id("com.up366.mobile:id/back").click()

    def test_change2(cls):
        '''字母数字大于20位'''
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='学号']"))
        cls.driver.find_element_by_id("com.up366.mobile:id/user_info_amend_name_ev").send_keys("jsahjfas334n55b24j2j2b")
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/rightText"))
        ele_text = Base(cls.driver).find_element((By.ID,"com.up366.mobile:id/title")).text
        cls.assertEqual(ele_text, "修改学号")
        cls.driver.find_element_by_id("com.up366.mobile:id/back").click()

    def test_change3(cls):
        '''输入汉字'''
        Base(cls.driver).clickButton((By.XPATH, "//*[@text='学号']"))
        cls.driver.find_element_by_id("com.up366.mobile:id/user_info_amend_name_ev").send_keys("你好")
        Base(cls.driver).clickButton((By.ID, "com.up366.mobile:id/rightText"))
        ele_text = Base(cls.driver).find_element((By.ID, "com.up366.mobile:id/title")).text
        cls.assertEqual(ele_text, "修改学号")
        cls.driver.find_element_by_id("com.up366.mobile:id/back").click()


    def test_change4(cls):
        '''输入特殊字符'''
        Base(cls.driver).clickButton((By.XPATH, "//*[@text='学号']"))
        cls.driver.find_element_by_id("com.up366.mobile:id/user_info_amend_name_ev").send_keys("#$@%")
        Base(cls.driver).clickButton((By.ID, "com.up366.mobile:id/rightText"))
        ele_text = Base(cls.driver).find_element((By.ID, "com.up366.mobile:id/title")).text
        cls.assertEqual(ele_text, "修改学号")
        cls.driver.find_element_by_id("com.up366.mobile:id/back").click()


    def test_change5(cls):
        '''正确输入'''
        Base(cls.driver).clickButton((By.XPATH, "//*[@text='学号']"))
        cls.driver.find_element_by_id("com.up366.mobile:id/user_info_amend_name_ev").send_keys("51888888")
        Base(cls.driver).clickButton((By.ID, "com.up366.mobile:id/rightText"))
        ele_text = Base(cls.driver).find_element((By.ID, "com.up366.mobile:id/title")).text
        cls.assertEqual(ele_text, "个人资料")



if __name__ == '__main__':
    unittest.main