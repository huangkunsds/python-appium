# coding:utf-8
# author:huangkun
import time
import unittest

from selenium.webdriver.common.by import By

from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging

class orderlist(unittest.TestCase):
    logging.info("orderListTest.py用例开始执行")

    def setUp(self):
        self.driver = Caps.set_caps(self)

    def tearDown(self):
        self.driver.quit()

    def test_emptyList(self):
        '''空页面'''
        logging.info("空页面")
        logIn(self.driver, "up0864", "123456")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        time.sleep(1)
        self.driver.find_elements_by_id("com.up366.mobile:id/icon")[2].click()
        Base(self.driver).clickButton((By.XPATH,"//*[@text='购买记录']"))
        ele_text = self.driver.find_element_by_id("com.up366.mobile:id/no_data_login_tv").text
        self.assertEqual(ele_text,"目前还没有购买记录")


    def test_orderList(self):
        '''非空页面'''
        logging.info("非空页面")
        time.sleep(2)
        logIn(self.driver, "15831539813", "123456")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        time.sleep(1)
        self.driver.find_elements_by_id("com.up366.mobile:id/icon")[2].click()
        Base(self.driver).clickButton((By.XPATH,"//*[@text='购买记录']"))
        ele = self.driver.find_element_by_id("com.up366.mobile:id/user_order_transaction_status")
        self.assertIsNotNone(ele)

if __name__ == '__main__':
    unittest.main