#-*- coding:utf-8 -*-
# author:huangkun
# datetime:2018/9/7
import time
import unittest

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging


class new_question(unittest.TestCase):

    def setUp(self):
        logging.info("NewQuestion.py 用例开始执行")
        self.driver = Caps.set_caps(None)
        time.sleep(3)
        logIn(self.driver, "13121826612", '123456')
        # 登录成功后的弹框处理
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/question_btn_ll")) # 问答

    def tearDown(self):
        self.driver.quit()

    def est_new_question(self):
        '''新建提问'''
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/rightIcon"))  # 新建按钮
        self.driver.find_element_by_id("com.up366.mobile:id/ask_title").send_keys("nihao")
        self.driver.find_element_by_id("com.up366.mobile:id/ask_content").send_keys("nisdfisdnfidsncbbsdbbd")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/ask_people"))  # 提醒谁看
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/question_people_select"))  # 全选
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/rightText"))  # 点击完成
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/submit"))
        time.sleep(3)
        ele_text = Base(self.driver).find_element((By.XPATH,"//*[@text='nihao']")).text
        #ele_text = self.driver.find_elements_by_xpath("//*[@text='jiejue']").text
        self.assertEqual(ele_text,"nihao")

    def test_question_reply(self):
        '''回复提问'''
        Base(self.driver).clickButton((By.XPATH,"//*[@text='nihao']"))
        self.driver.find_element_by_id("com.up366.mobile:id/replay_content_et").send_keys("jiejue")
        #Base(self.driver).send_keys((By.ID,"com.up366.mobile:id/replay_content_et"),"jiejue")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/replay_add_pic"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/view_pic_image"))
        Base(self.driver).clickButton((By.XPATH,"//*[@text='拍照']"))
        Base(self.driver).clickButton((By.ID,"com.android.camera:id/shutter_button"))
        Base(self.driver).clickButton((By.ID,"com.android.camera:id/btn_done"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/replay_submit"))
        ele = Base(self.driver).find_element((By.XPATH,"//*[@text='jiejue']"))
        self.assertIsNotNone(ele)


if __name__ == '__main__':
    unittest.main