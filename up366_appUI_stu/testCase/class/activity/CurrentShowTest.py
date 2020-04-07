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


class current_show(unittest.TestCase):

    def setUp(cls):
        logging.info("CurrentShow.py 用例开始执行")
        cls.driver = Caps.set_caps(None)
        time.sleep(3)
        logIn(cls.driver, "13121826612", '123456')
        # 登录成功后的弹框处理
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        time.sleep(2)
        cls.driver.find_elements_by_id("com.up366.mobile:id/activity_btn_ll")[0].click()
        Base(cls.driver).clickButton((By.XPATH, "//*[@text='展示']"))



    def tearDown(cls):
        logging.info("CurrentShow.py 用例执行完毕")
        cls.driver.quit()


    def test_likeBTN_show(cls):
        '''点赞'''
        time.sleep(2)
        like_ele = cls.driver.find_element_by_id("com.up366.mobile:id/replay_like_num")
        like_num = like_ele.text
        if like_num == 0:
            like_ele.click()
            time.sleep(2)
            like_num_new = cls.driver.find_element_by_id("com.up366.mobile:id/replay_like_num").text
            cls.assertEqual(like_num_new,'1')
        else:
            time.sleep(1)
            like_ele.click()
            time.sleep(2)
            like_num_new = cls.driver.find_element_by_id("com.up366.mobile:id/replay_like_num").text
            cls.assertEqual(like_num_new, '0')


    def test_resubmit_show(cls):
        '''重新提交：文字'''
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/kill_question"))
        Base(cls.driver).send_keys((By.ID,"com.up366.mobile:id/replay_content_et"),"nihao")
        Base(cls.driver).clickButton((By.ID, "com.up366.mobile:id/replay_submit"))
        ele_content = Base(cls.driver).find_element((By.ID,"com.up366.mobile:id/replay_content")).text
        cls.assertEqual(ele_content,"nihao")



if __name__ == '__main__':
    unittest.main