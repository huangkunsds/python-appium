#-*- coding:utf-8 -*-
# author:huangkun
# datetime:2018/9/10
import time
import unittest

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging


class my_question(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logging.info("MyQuestion.py 用例开始执行")
        self.driver = Caps.set_caps(None)
        time.sleep(3)
        logIn(self.driver, "13121826612", '123456')
        # 登录成功后的弹框处理
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/question_btn_ll"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/radioMine"))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        logging.info("MyQuestion.py 用例执行结束")

    def test_question_a(self):
        '''解决问题'''
        Base(self.driver).clickButton((By.XPATH, "//*[@text='nihao']"))
        Base(self.driver).clickButton((By.XPATH, "//*[@text='解决问题']"))
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/dialog_common_confirm"))
        ele = Base(self.driver).find_element((By.XPATH,"//*[@text='已解决']"))
        self.assertIsNotNone(ele)
        self.driver.find_element_by_id("com.up366.mobile:id/back").click()

    def test_question_b(self):
        '''删除问题'''
        ele = Base(self.driver).find_element((By.XPATH,"//*[@text='nihao']"))
        action1 = TouchAction(self.driver)
        action1.long_press(ele).wait(4000).perform()
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/dialog_common_confirm"))
        ele_text = Base(self.driver).find_element((By.XPATH,"//*[@text='问答']"))
        self.assertIsNotNone(ele_text)


if __name__ == '__main__':
    unittest.main