# coding:utf-8
# author:huangkun
import time
import unittest

from selenium.webdriver.common.by import By

from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging


class message(unittest.TestCase):

    def setUp(self):
        logging.info("messageTest.py 用例开始执行")
        self.driver = Caps.set_caps(None)
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
        logging.info("messageTest.py 用例执行结束")

    def test_message(self):
        '''消息页面是否为空'''
        logging.info("用例描述：查找没有的课程")
        logIn(self.driver, "up0864", '123456')
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/message_iv"))
        self.assertIsNotNone("com.up366.mobile:id/no_data_login_tv")

if __name__ == '__main__':
    unittest.main

