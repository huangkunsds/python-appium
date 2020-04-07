#-*- coding:utf-8 -*-
# author:huangkun
# datetime:2018/9/7
import time
import unittest

from selenium.webdriver.common.by import By

from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging


class finished_vote(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("FinishedVote.py 用例开始执行")
        cls.driver = Caps.set_caps(None)
        time.sleep(1)
        logIn(cls.driver, "13121826612", '123456')
        # 登录成功后的弹框处理
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        time.sleep(2)
        cls.driver.find_elements_by_id("com.up366.mobile:id/activity_btn_ll")[0].click()
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/radioOld"))


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logging.info("FinishedVote.py 用例执行结束")

    def test_show(cls):
        '''往期活动-查看展示'''
        Base(cls.driver).clickButton((By.XPATH, "//*[@text='展示']"))
        ele_text = Base(cls.driver).find_element((By.XPATH, "//*[@text='目前还没有回复哦']")).text
        cls.assertEqual(ele_text, "目前还没有回复哦")
        cls.driver.find_element_by_id("com.up366.mobile:id/back").click()

    def test_vote(cls):
        '''往期活动-查看投票人员'''
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='投票']"))
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/kill_question"))
        ele_text = Base(cls.driver).find_element((By.XPATH,"//*[@text='目前还没有人投票哦']")).text
        cls.assertEqual(ele_text,"目前还没有人投票哦")
        cls.driver.find_element_by_id("com.up366.mobile:id/back").click()


if __name__ == '__main__':
    unittest.main
