#coding:utf-8
# author:huangkun
# datetime:2018/9/3
import time
import unittest
from selenium.webdriver.common.by import By
from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging


class realname(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("userPictureTest.py 用例开始执行")
        cls.driver = Caps.set_caps(None)
        logIn(cls.driver, "up0864", '123456')
        # 登录成功后的弹框处理
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        Base(cls.driver).clickButton((By.XPATH,".//*[contains(@text,'黄坤')]"))
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='个人资料']"))

    @classmethod
    def tearDownClass(cls):
        logging.info("userPictureTest.py 用例执行结束")
        cls.driver.quit()

    def test_changeName_faile(cls):
        '''输入无效字符,"@" '''
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='真实姓名']"))
        time.sleep(2)
        cls.driver.find_element_by_id("com.up366.mobile:id/user_info_amend_name_ev").send_keys('@')
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/rightText"))
        ele_text = Base(cls.driver).find_element((By.ID,"com.up366.mobile:id/title")).text
        cls.assertEqual(ele_text,"修改姓名")
        cls.driver.find_element_by_id("com.up366.mobile:id/back").click()

    def test_changeName_faile1(cls):
        '''输入长度不够的有效字符，"0" '''
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='真实姓名']"))
        time.sleep(2)
        cls.driver.find_element_by_id("com.up366.mobile:id/user_info_amend_name_ev").send_keys('0')
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/rightText"))
        ele_text = Base(cls.driver).find_element((By.ID,"com.up366.mobile:id/title")).text
        cls.assertEqual(ele_text, "修改姓名")
        cls.driver.find_element_by_id("com.up366.mobile:id/back").click()

    def test_changeName_success(cls):
        '''更换成功 '''
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='真实姓名']"))
        time.sleep(2)
        cls.driver.find_element_by_id("com.up366.mobile:id/user_info_amend_name_ev").send_keys("黄坤")
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/rightText"))
        ele_text = Base(cls.driver).find_element((By.ID,"com.up366.mobile:id/title")).text
        cls.assertEqual(ele_text, "个人资料")
        time.sleep(1)

if __name__ == '__main__':
    unittest.main



