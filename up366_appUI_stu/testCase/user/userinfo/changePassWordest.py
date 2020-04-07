#-*- coding:utf-8 -*-
# author:huangkun
# datetime:2018/9/4
import time
import unittest

from selenium.webdriver.common.by import By
from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.getToast import get_Toast
from utils.log import logging
from utils.reperform import failrun


class changePWD(unittest.TestCase):
    driver = Caps.set_caps(None)

    @classmethod
    def setUpClass(cls):
        logging.info("changePassWordest.py 用例开始执行")
        cls.driver = Caps.set_caps(None)
        logIn(cls.driver, "15831539813", '123456')
        # 登录成功后的弹框处理
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        Base(cls.driver).clickButton((By.XPATH,".//*[contains(@text,'黄坤')]"))
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='个人资料']"))

    @classmethod
    def tearDownClass(cls):
        logging.info("changePassWordest.py 用例执行结束")
        cls.driver.quit()

    def test_PWD_oldWrong1(cls):
        '''新密码格式错误'''
        time.sleep(2)
        Base(cls.driver).clickButton((By.XPATH,".//*[contains(@text,'修改密码')]"))
        Base(cls.driver).send_keys((By.ID,"com.up366.mobile:id/amend_password_old_pwd"),'12345678')
        Base(cls.driver).send_keys((By.ID,"com.up366.mobile:id/amend_password_new_pwd"),'ssswer')
        time.sleep(2)
        Base(cls.driver).send_keys((By.ID,"com.up366.mobile:id/amend_password_new_pwd_again"),'ssswer')
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/user_info_save_pwd"))
        toast = get_Toast(cls.driver,'新密码为6-15位字母数字组合'+ '\n' +
                          '确认密码为6-15位字母数字组合')
        print("toast is: %s" % toast)
        cls.assertEqual(toast,'新密码为6-15位字母数字组合'+ '\n' +
                        '确认密码为6-15位字母数字组合')

    def test_PWD_oldWrong2(cls):
        '''原密码格式错误'''
        time.sleep(2)
        Base(cls.driver).clickButton((By.XPATH,".//*[contains(@text,'修改密码')]"))
        Base(cls.driver).send_keys((By.ID,"com.up366.mobile:id/amend_password_old_pwd"),'123')
        Base(cls.driver).send_keys((By.ID,"com.up366.mobile:id/amend_password_new_pwd"),'sss123')
        time.sleep(2)
        Base(cls.driver).send_keys((By.ID,"com.up366.mobile:id/amend_password_new_pwd_again"),'sss123')
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/user_info_save_pwd"))
        toast = get_Toast(cls.driver,"原密码为6-15位字母数字组合")
        print("toast is: %s" % toast)
        cls.assertEqual(toast,"原密码为6-15位字母数字组合"+'\n')

    def test_PWD_newWrong1(cls):
        '''新密码不相等'''
        time.sleep(2)
        Base(cls.driver).clickButton((By.XPATH, ".//*[contains(@text,'修改密码')]"))
        Base(cls.driver).send_keys((By.ID, "com.up366.mobile:id/amend_password_old_pwd"), '123456')
        Base(cls.driver).send_keys((By.ID, "com.up366.mobile:id/amend_password_new_pwd"), 'sss123')
        time.sleep(2)
        Base(cls.driver).send_keys((By.ID, "com.up366.mobile:id/amend_password_new_pwd_again"), 'sss1235')
        Base(cls.driver).clickButton((By.ID, "com.up366.mobile:id/user_info_save_pwd"))
        toast = get_Toast(cls.driver, "输入的新密码不一致")
        print("toast is: %s" % toast)
        cls.assertEqual(toast, "输入的新密码不一致")


if __name__ == '__main__':
    unittest.main()


