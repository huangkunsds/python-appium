#coding:utf-8
# author:ChuNaMei
import unittest
import time

from selenium.webdriver.common.by import By

from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging


class myBooks(unittest.TestCase):

    def setUp(self):
        logging.info("mybooksTest.py 用例开始执行")
        self.driver = Caps.set_caps(None)
        time.sleep(3)
        logIn(self.driver, "up0821", '123456')
        #登录成功后的弹框处理
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_enter_mybook(self):
        '''测试教材列表页'''
        logging.info("测试用例描述：点击作业图标，进入教材列表页")
        self.driver.find_elements_by_id("com.up366.mobile:id/book_btn_ll")[0].click()
        time.sleep(2)
        title=self.driver.find_element_by_id("com.up366.mobile:id/title").text
        time.sleep(2)
        self.assertIsNotNone(title)

    def test_footer_mybook(self):
        '''测试页面底部图标状态'''
        logging.info("测试用例描述：测试页面底部图标状态")
        self.driver.find_elements_by_id("com.up366.mobile:id/book_btn_ll")[0].click()
        time.sleep(2)
        status = self.driver.find_element_by_id("com.up366.mobile:id/book").is_enabled()
        self.assertFalse(status)


    def test_booklist(self):
        '''测试列表页'''
        logging.info("测试用例描述：测试列表页")
        self.driver.find_elements_by_id("com.up366.mobile:id/book_btn_ll")[0].click()
        try:
            self.driver.find_element_by_id("com.up366.mobile:id/no_data_login_iv").is_displayed()
            ele_txt=self.driver.find_element_by_id("com.up366.mobile:id/book_name").text
            self.assertEqual(ele_txt,"暂无教材")
        except:
            ele_txt2=self.driver.find_element_by_id("com.up366.mobile:id/book_name").text
            self.assertIsNotNone(ele_txt2)

    def test_bookdetail_enter(self):
        '''测试进入教材'''
        logging.info("测试用例描述:测试进入教材")
        self.driver.find_elements_by_id("com.up366.mobile:id/book_btn_ll")[0].click()
        if self.driver.find_element_by_id("com.up366.mobile:id/book_name").is_displayed():
            self.driver.find_elements_by_id("com.up366.mobile:id/book_picture")[0].click()
            time.sleep(5)
            text=self.driver.find_element_by_id("com.up366.mobile:id/title").text
            self.assertIsNotNone(text)

    def test_bookdetail_back(self):
        '''测试教材页面返回按钮'''
        logging.info("测试用例描述:测试教材页面返回按钮")
        self.driver.find_elements_by_id("com.up366.mobile:id/book_btn_ll")[0].click()
        time.sleep(5)
        if self.driver.find_element_by_id("com.up366.mobile:id/book_name").is_displayed():
            self.driver.find_element_by_id("com.up366.mobile:id/book_picture").click()
            time.sleep(5)
            self.driver.find_element_by_id("com.up366.mobile:id/back").click()
            ele_txt=self.driver.find_element_by_id("com.up366.mobile:id/title").text
            self.assertIsNotNone(ele_txt)

if __name__ == '__main__':
    unittest.main
