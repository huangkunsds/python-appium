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


class feedback(unittest.TestCase):
    logging.info("feedBackTest.py用例开始执行")

    def setUp(self):
        self.driver = Caps.set_caps(self)
        time.sleep(2)
        logIn(self.driver, "15831539813", "123456")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        time.sleep(1)
        Base(self.driver).find_elements((By.ID,"com.up366.mobile:id/icon"))[2].click()
        Base(self.driver).clickButton((By.XPATH,"//*[@text='帮助与反馈']"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/rightText"))

    def tearDown(self):
        self.driver.quit()

    def test_feedBack1(self):
        '''不输入手机号，提交'''
        logging.info("不输入手机号，提交")
        Base(self.driver).find_element((
            By.ID,"com.up366.mobile:id/feedback_content_et"
        )).send_keys("测试%sad#$%1288990")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/feedback_submit_btn"))
        toast = get_Toast(self.driver,"请填写一下您的手机号！")
        print("toast is :%s" % toast)
        self.assertEqual(toast,"请填写一下您的手机号！")

    def test_feedBack3(self):
        '''输入错误的手机号提交'''
        logging.info("输入错误的手机号提交")
        Base(self.driver).find_element((
            By.ID, "com.up366.mobile:id/feedback_content_et"
        )).send_keys("测试%sad#$%1288990")
        Base(self.driver).find_element((By.ID, "com.up366.mobile:id/feedback_phone_et")).send_keys("234234")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/feedback_submit_btn"))
        toast = get_Toast(self.driver, "手机号格式")
        print("toast is :%s" % toast)
        self.assertEqual(toast, "手机号格式不正确！")

    def test_feedBack2(self):
        '''输入正确是手机号提交'''
        logging.info("输入正确是手机号提交")
        Base(self.driver).find_element((
            By.ID,"com.up366.mobile:id/feedback_content_et"
        )).send_keys("测试%sad#$%1288990")
        Base(self.driver).find_element((By.ID,"com.up366.mobile:id/feedback_phone_et")).send_keys("13256786576")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/view_pic_image"))
        Base(self.driver).clickButton((By.XPATH,"//*[@text='相册选取']"))   # 点击相册选取
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/album_pic_image"))
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/album_finish_button"))    # 点击完成按钮
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/feedback_submit_btn"))
        ele = Base(self.driver).find_element((By.ID,"com.up366.mobile:id/dialog_common_confirm"))   # 成功弹框提示
        self.assertIsNotNone(ele)
        ele.click()

if __name__ == '__main__':
    unittest.main

