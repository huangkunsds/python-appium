#coding:utf-8
# author:ChuNaMei
import time
import unittest

from selenium.webdriver.common.by import By

from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging

class liveclass(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logging.info("liveClassTest.py 用例开始执行")
        self.driver = Caps.set_caps(None)
        time.sleep(3)
        logIn(self.driver, "up0864", '123456')
        #登录成功后的弹框处理
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        logging.info("liveClassTest.py 用例执行结束")

    def test_enter_livingclasslist(self):
        '''测试进入直播课列表页'''
        logging.info("用例描述：测试进入直播课列表页")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/living_view_ll"))
        ele_txt = Base(self.driver).find_element((By.ID,"com.up366.mobile:id/title")).text
        self.assertIsNotNone(ele_txt)

    def test_pass_classlist(self):
        '''测试已经结束的直播课列表'''
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/living_view_ll"))
        logging.info("用例描述：测试已结束的直播课列表")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/live_act_tab_indicator_old"))
        ele_txt = Base(self.driver).find_element((By.ID, "com.up366.mobile:id/live_item_live_name")).text
        self.assertIsNotNone(ele_txt)

    def test_onliving_classlist(self):
        '''测试要进行的直播课列表'''
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/living_view_ll"))
        logging.info("用例描述：测试要进行的直播课列表")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/live_act_tab_indicator_current"))
        ele_txt = Base(self.driver).find_element((By.ID,"com.up366.mobile:id/live_big_item_come_in_btn")).text
        self.assertIsNotNone(ele_txt,"上课")


if __name__ == '__main__':
    unittest.main