# coding:utf-8
# author:huangkun
# datetime:2018/9/3
import time
import unittest

from selenium.webdriver.common.by import By
from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.getToast import get_Toast
from utils.log import logging


class userpicture(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("userPictureTest.py 用例开始执行")
        cls.driver = Caps.set_caps(None)
        logIn(cls.driver, "up0864", '123456')
        # 登录成功后的弹框处理
        Base(cls.driver).clickButton((By.ID, "com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        Base(cls.driver).clickButton((By.XPATH, ".//*[contains(@text,'黄坤')]"))
        Base(cls.driver).clickButton((By.XPATH, "//*[@text='个人资料']"))

    @classmethod
    def tearDownClass(cls):
        logging.info("userPictureTest.py 用例执行结束")
        cls.driver.quit()


    def test_takePhoto(cls):
        '''拍照'''
        Base(cls.driver).clickButton((By.ID, "com.up366.mobile:id/user_info_img"))
        Base(cls.driver).clickButton((By.XPATH, "//*[@text='拍照']"))
        Base(cls.driver).clickButton((By.ID, "com.android.camera:id/shutter_button"))
        Base(cls.driver).clickButton((By.ID, "com.android.camera:id/done_button"))
        Base(cls.driver).clickButton((By.XPATH, "//*[@text='确定']"))
        toast = get_Toast(cls.driver,"头像更新成功")
        print("toast is :%s" % toast)
        cls.assertEqual(toast,"头像更新成功")


    def test_selectPicture(cls):
        '''相册选择图片'''
        Base(cls.driver).clickButton((By.ID, "com.up366.mobile:id/user_info_img"))
        Base(cls.driver).clickButton((By.XPATH, "//*[@text='相册选取']"))
        time.sleep(2)
        Base(cls.driver).find_elements((By.ID,"com.up366.mobile:id/album_pic_image"))[0].click()
        Base(cls.driver).clickButton((By.XPATH, "//*[@text='确定']"))
        toast = get_Toast(cls.driver, "头像更新成功")
        print("toast is :%s" % toast)
        cls.assertEqual(toast, "头像更新成功")


if __name__ == '__main__':
    unittest.main

