# coding:utf-8
import time
import unittest
from selenium.webdriver.common.by import By

from public.BasePage import Base
from public.desire_caps import Caps
from utils.getToast import get_Toast
from utils.log import logging


class changepwd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("changepwdTest.py用例开始执行")
        cls.driver = Caps.set_caps(cls)
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='智能课堂']"))
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/no_data_login_btn"))

    @classmethod
    def tearDownClass(cls):
        logging.info("changepwdTest.py用例执行结束")
        cls.driver.quit()

    def test_changepwd_page(cls):
        '''页面跳转'''
        time.sleep(2)
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/forget_password"))
        ele_text = Base(cls.driver).find_element((By.ID,"com.up366.mobile:id/title")).text
        cls.assertEqual(ele_text,"重置密码")
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/back"))

    def test_changepwd_wrong_mobile(cls):
        '''输入错误的电话，点击发送验证码'''
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/forget_password"))
        Base(cls.driver).find_element((By.ID,"com.up366.mobile:id/phone_number")).send_keys("87993374647")
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/send_verification_code"))
        toast = get_Toast(cls.driver,"请输入有效手机号")
        print("toast is :%s" % toast)
        cls.assertIsNotNone(toast,"请输入有效手机号")
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/back"))


    def test_changepwd_NoBind_mobile(cls):
        '''输入并非绑定的手机号'''
        Base(cls.driver).clickButton((By.ID, "com.up366.mobile:id/forget_password"))
        Base(cls.driver).find_element((By.ID, "com.up366.mobile:id/phone_number")).send_keys("15834546786")
        Base(cls.driver).clickButton((By.ID, "com.up366.mobile:id/send_verification_code"))
        ele_text = Base(cls.driver).find_element((By.ID,"com.up366.mobile:id/dialog_common_msg")).text
        cls.assertIsNotNone(ele_text, "该帐号未绑定手机，无法找回密码，请联系客服！")
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/dialog_common_confirm"))   # 点击重新输入按钮
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/back"))



    def test_changepwd_InputCodeOnly(cls):
        '''只输入验证码点击下一步'''
        Base(cls.driver).clickButton((By.ID, "com.up366.mobile:id/forget_password"))
        Base(cls.driver).find_element((By.ID, "com.up366.mobile:id/verification_code")).send_keys("8866")
        Base(cls.driver).clickButton((By.ID, "com.up366.mobile:id/next_btn"))  # 点击下一步
        toast = get_Toast(cls.driver, "请输入手机号")
        print("toast is :%s" % toast)
        cls.assertIsNotNone(toast, "请输入手机号")
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/back"))


    def test_changepwd_InputWrongCode(cls):
        '''输入正确的手机号、错误的验证码点击下一步'''
        Base(cls.driver).clickButton((By.ID, "com.up366.mobile:id/forget_password"))
        Base(cls.driver).find_element((By.ID, "com.up366.mobile:id/phone_number")).send_keys("15831539813")
        Base(cls.driver).find_element((By.ID, "com.up366.mobile:id/verification_code")).send_keys("8866")
        Base(cls.driver).clickButton((By.ID, "com.up366.mobile:id/next_btn"))  # 点击下一步
        toast = get_Toast(cls.driver, "手机验证码错误或已过期")
        print("toast is :%s" % toast)
        cls.assertIsNotNone(toast, "手机验证码错误或已过期")
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/back"))


if __name__ == '__main__':
    unittest.main


