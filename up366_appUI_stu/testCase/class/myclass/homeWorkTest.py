#coding:utf-8
# author:ChuNaMei
import unittest
import time

from selenium.webdriver.common.by import By

from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging


class homework(unittest.TestCase):

    def setUp(self):
        logging.info("homeWorkTest.py 用例开始执行")
        self.driver = Caps.set_caps(None)
        time.sleep(2)
        logIn(self.driver, "up0821", '123456')
        #登录成功后的弹框处理
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))


    def tearDown(self):
        self.driver.quit()
        logging.info("homeWorkTest.py 用例执行结束")

    def test_enter_homework(self):
        '''测试进入作业列表页'''
        logging.info("测试用例描述：点击作业图标，进入作业列表页")
        self.driver.find_elements_by_id("com.up366.mobile:id/homework_btn_ll")[0].click()
        time.sleep(2)
        title=self.driver.find_element_by_id("com.up366.mobile:id/title").text
        time.sleep(2)
        self.assertIsNotNone(title)

    def test_back(self):
        '''测试返回按钮'''
        logging.info("用例描述：测试作业页面返回按钮")
        self.driver.find_elements_by_id("com.up366.mobile:id/homework_btn_ll")[0].click()
        #time.sleep(2)
        time.sleep(1)
        self.driver.find_element_by_id("com.up366.mobile:id/back").click()
        time.sleep(1)
        ele_txt=self.driver.find_element_by_id("com.up366.mobile:id/title").text
        self.assertEqual(ele_txt,"天学网智能课堂")

    def test_passed_homework(self):
        '''测试往期作业'''
        logging.info("用例描述：测试往期作业")
        self.driver.find_elements_by_id("com.up366.mobile:id/homework_btn_ll")[0].click()
        time.sleep(2)
        self.driver.find_element_by_id("com.up366.mobile:id/radioOld").click()
        try:
           self.driver.find_element_by_id("com.up366.mobile:id/no_data_login_iv").is_displayed() #若果往期作业列表为空，校验文本
           #self.driver.find_element_by_id("com.up366.mobile:id/radioCurrent").click()
           ele_txt = self.driver.find_element_by_id("com.up366.mobile:id/no_data_login_tv").text
           self.assertEqual(ele_txt, "暂无作业")
        except:
            text=self.driver.find_elements_by_id("com.up366.mobile:id/name")[0].text
            time.sleep(2)
            self.assertIsNotNone(text)
            #mobileSwipe().swipeLeft(1000)


    def test_default_homeworklist(self):
        '''测试默认显示当前作业'''
        logging.info("用例描述：测试默认显示当前作业列表页")
        self.driver.find_elements_by_id("com.up366.mobile:id/homework_btn_ll")[0].click()
        time.sleep(2)
        try:
            self.driver.find_element_by_id("com.up366.mobile:id/no_data_login_iv").is_displayed()#若果当前作业列表为空,校验文本
            ele_txt = self.driver.find_element_by_id("com.up366.mobile:id/no_data_login_tv").text
            self.assertEqual(ele_txt, "暂无作业")
        except:
            text=self.driver.find_elements_by_id("com.up366.mobile:id/name")[0].text
            time.sleep(2)
            self.assertIsNotNone(text)
            #mobileSwipe().swipeLeft(1000)
            
    def test_footer_homework(self):
        '''测试页面底部图标状态'''
        logging.info("测试用例描述：测试页面底部图标状态")
        self.driver.find_elements_by_id("com.up366.mobile:id/homework_btn_ll")[0].click()
        time.sleep(2)
        status = self.driver.find_element_by_id("com.up366.mobile:id/homework").is_enabled()
        self.assertFalse(status)

    def test_switch_homeworktab(self):
        '''测试从往期作业切换到当前作业列表页'''
        logging.info("用例描述：测试从往期作业切换到当前作业列表页")
        time.sleep(2)
        self.driver.find_elements_by_id("com.up366.mobile:id/homework_btn_ll")[0].click()
        Base(self.driver).find_elements((By.ID,"com.up366.mobile:id/radioCurrent"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/name"))
        Base(self.driver).find_element((By.XPATH,"我知道了"))
        time.sleep(5)

        # self.driver.find_element_by_id("com.up366.mobile:id/radioOld").click()


if __name__ == '__main__':
    unittest.main
