#-*- coding:utf-8 -*-
# author:huangkun
# datetime:2018/9/05
import os
import time
import unittest

from selenium.webdriver.common.by import By
from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging


class wordsnote(unittest.TestCase):

    def setUp(self):
        logging.info("wordsNoteTest.py 用例开始执行")
        self.driver = Caps.set_caps(None)
        time.sleep(3)
        logIn(self.driver, "up0864", '123456')
        # 登录成功后的弹框处理
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/word_note_btn_ll"))

    def tearDown(self):
        self.driver.quit()

    def test_words_info(self):
        '''单词来源--生词详情'''
        logging.info("用例描述：单词来源--生词详情")
        time.sleep(1)
        self.driver.find_elements_by_id("com.up366.mobile:id/word_name_mask")[0].click()
        time.sleep(1)
        self.driver.find_elements_by_id("com.up366.mobile:id/word_from_adapter_example_tv")[0].click()
        time.sleep(1)
        ele_text = self.driver.find_element_by_id("com.up366.mobile:id/title").text
        self.assertEqual(ele_text,"单词详情")


    def test_words_bookList(self):
        '''飞书下拉列表'''
        logging.info("用例描述：飞书下拉列表")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/title"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/list_item"))
        ele_text = self.driver.find_element_by_id("com.up366.mobile:id/word_wrongCount").text
        self.assertEqual(ele_text,"加入次数")


    def test_words_rankkList(self):
        '''错词排行榜'''
        logging.info("用例描述：错词排行榜")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/rightIcon"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/title"))
        self.driver.find_elements_by_id("com.up366.mobile:id/list_item")[0].click()
        ele_text = self.driver.find_element_by_id("com.up366.mobile:id/type_rank_wrongCount").text
        self.assertEqual(ele_text,"剩余生词")


if __name__ == '__main__':
    unittest.main