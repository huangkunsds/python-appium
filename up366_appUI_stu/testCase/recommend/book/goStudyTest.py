# coding:utf-8
# author:huangkun
import time
import unittest

from selenium.webdriver.common.by import By

from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging

class gostudy(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("goStudy.py用例开始执行")
        cls.driver = Caps.set_caps(cls)
        logIn(cls.driver,"up0864","123456")

        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        time.sleep(1)
        cls.driver.find_elements_by_id("com.up366.mobile:id/name")[0].click()
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/tip1"))
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/tip2"))
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='听力满分·培优营（高中）']"))
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/studyIt"))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logging.info("goStudy.py用例执行结束")

    def test_courseJoin(cls):
        '''去学习-加入课程页面'''
        logging.info("去学习-加入课程页面")
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='接口自动化测试_课程']"))
        ele = Base(cls.driver).find_element((By.XPATH,"//*[@text='听力满分·培优营（高中）']"))
        cls.assertIsNotNone(ele)

if __name__ == '__main__':
    unittest.main

