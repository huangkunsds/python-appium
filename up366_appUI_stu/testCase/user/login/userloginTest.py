# coding:utf-8
'''
    Created on 2018-8-31
    author: hewenqi
'''
import unittest

from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logInPage
from utils.log import logging
from selenium.webdriver.common.by import By


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logging.info("userlogin.py 用例开始执行")
        self.driver = Caps.set_caps(None)
        Base(self.driver).clickButton((By.XPATH, ".//*[contains(@text,'未登录')]"))
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/login"))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        logging.info("userLogin.py 用例执行结束")


    def test_login_WrongName(self):
        '''输入错误用户名，正确密码。'''
        logging.info('用例描述：用户名错误！')
        username = "1355862626"
        password = '123456'
        logInPage(self.driver,username,password)
        ele_text = Base(self.driver).find_element((By.ID,"com.up366.mobile:id/dialog_common_msg")).text
        self.assertEqual(ele_text, u'用户名或密码错误，请重新输入！')
        Base(self.driver).clickButton((By.XPATH,".//*[contains(@text,'确定')]"))

    def test_keeplogin_Failword(self):
        '''输入正确用户名，错误密码。'''
        username = "up0850"
        password = "1234567"
        logging.info('用例描述：密码错误')
        logInPage(self.driver,username,password)
        ele_text = Base(self.driver).find_element((By.ID,"com.up366.mobile:id/dialog_common_msg")).text
        self.assertEqual(ele_text, u'用户名或密码错误，请重新输入！')
        Base(self.driver).clickButton((By.XPATH,".//*[contains(@text,'确定')]"))


    def test_keeplogin_Symbol(self):
        '''输入正确用户名，密码存在特殊字符。'''
        username = "up0850"
        password = "12**.."
        logging.info("用例描述：密码存在特殊字符")
        logInPage(self.driver,username,password)
        ele_text = Base(self.driver).find_element((By.ID,"com.up366.mobile:id/dialog_common_msg")).text
        self.assertEqual(ele_text, u'用户名或密码错误，请重新输入！')
        Base(self.driver).clickButton((By.XPATH,".//*[contains(@text,'确定')]"))


if __name__ == '__main__':
    unittest.main


