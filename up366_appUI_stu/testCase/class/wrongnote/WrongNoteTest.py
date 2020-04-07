# -*- coding:utf-8 -*-
# author:huangkun
# datetime:2018/9/03

import time
import unittest

from selenium.webdriver.common.by import By

from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging


class wrongnote(unittest.TestCase):

    def setUp(self):
        logging.info("wrongNoteTest.py 用例开始执行")
        self.driver = Caps.set_caps(None)
        time.sleep(3)
        logIn(self.driver, "up0864", '123456')
        #登录成功后的弹框处理
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))



    def tearDown(self):
        self.driver.quit()
        logging.info("wrongNoteTest.py 用例执行结束")

    def test_class_myWrongNote(self):
        '''我的错题本'''
        logging.info("用例描述：我的错题本页面")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/wrong_note_btn_ll"))
        ele = Base(self.driver).find_element((By.XPATH,"//*[@text='我的错题本']"))
        self.assertIsNotNone(ele)

    def test_GZ_questionsKill(self):
        '''高中英语-点击消灭错题弹框'''
        logging.info("用例描述：高中英语-消灭错题按钮")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/wrong_note_btn_ll"))
        self.driver.find_elements_by_id("com.up366.mobile:id/remain_num")[0].click()
        ele_text = Base(self.driver).find_element((By.ID,"com.up366.mobile:id/kill_question")).text
        self.assertEqual(ele_text,"消灭错题")

    def test_GZ_bookLIst(self):
        '''高中英语-书籍列表下拉框切换'''
        logging.info("用例描述：高中英语-书籍列表下拉框切换")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/wrong_note_btn_ll"))
        self.driver.find_elements_by_id("com.up366.mobile:id/remain_num")[0].click()
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/title"))
        time.sleep(2)
        self.driver.find_elements_by_id("com.up366.mobile:id/list_item")[2].click()
        ele_text = Base(self.driver).find_element((By.ID,"com.up366.mobile:id/textView11")).text
        self.assertEqual(ele_text,"今日消灭(道)")

    def test_GZ_rankList(self):
        '''高中英语-排行榜-课程下拉列表-进入页面'''
        logging.info("用例描述：排行榜-课程下拉列表-进入页面")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/wrong_note_btn_ll"))
        time.sleep(1)
        self.driver.find_elements_by_id("com.up366.mobile:id/remain_num")[0].click()
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/rightIcon"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/title"))
        time.sleep(1)
        self.driver.find_elements_by_id("com.up366.mobile:id/list_item")[1].click()
        ele_text = Base(self.driver).find_element((By.ID,"com.up366.mobile:id/type_rank_wrongCount")).text
        self.assertEqual(ele_text,"剩余错题")

    def test_CZ_questionsKill(self):
        '''初中英语-点击消灭错题弹框'''
        logging.info("用例描述：初中英语-点击消灭错题弹框")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/wrong_note_btn_ll"))
        time.sleep(1)
        self.driver.find_elements_by_id("com.up366.mobile:id/remain_num")[1].click()
        ele_text = Base(self.driver).find_element((By.ID,"com.up366.mobile:id/kill_question")).text
        self.assertEqual(ele_text,"消灭错题")

    def test_CZ_bookList(self):
        '''初中英语-飞书列表下拉框切换'''
        logging.info("用例描述：初中英语-飞书列表下拉框切换")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/wrong_note_btn_ll"))
        time.sleep(1)
        self.driver.find_element_by_id("com.up366.mobile:id/remain_num").click()
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/title"))
        time.sleep(2)
        self.driver.find_elements_by_id("com.up366.mobile:id/list_item")[2].click()
        ele_text = Base(self.driver).find_element((By.ID,"com.up366.mobile:id/textView11")).text
        self.assertEqual(ele_text,"今日消灭(道)")

    def test_CZ_rankList(self):
        '''初中英语-排行榜-课程下拉列表-进入页面'''
        logging.info("用例描述：排行榜-课程下拉列表-进入页面")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/wrong_note_btn_ll"))
        time.sleep(1)
        self.driver.find_elements_by_id("com.up366.mobile:id/remain_num")[1].click()
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/rightIcon"))
        ele_text = Base(self.driver).find_element((By.ID,"com.up366.mobile:id/title")).text
        self.assertEqual(ele_text,"排行榜")

if __name__ == '__main__':
    unittest.main