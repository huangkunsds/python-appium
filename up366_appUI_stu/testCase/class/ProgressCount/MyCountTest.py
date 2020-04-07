#-*- coding:utf-8 -*-
# author:chunamei
# datetime:2018/9/11

import unittest
from utils.log import logging
from public.desire_caps import Caps
from public.login import logIn
import time


class MyCounts(unittest.TestCase):

    def setUp(self):
        logging.info("MyCountTest.py开始执行")
        self.driver=Caps.set_caps(None)
        time.sleep(5)
        logIn(self.driver,"up0821","123456")
        time.sleep(4)
        #处理登录后的popup
        self.driver.find_element_by_id("com.up366.mobile:id/welcome_dialog_dismiss_btn").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
        logging.info("MycountTest.py执行结束")

    def test_click_count(self):
        logging.info("测试用例描述：测试点击统计按钮")
        self.driver.find_elements_by_id("com.up366.mobile:id/count_btn_ll")[0].click()
        time.sleep(3)
        txt=self.driver.find_element_by_id("com.up366.mobile:id/rightText").text
        self.assertEqual(txt,"筛选")
        time.sleep(5)

    def test_choose_option(self):
        logging.info("测试用例描述:测试测试选择筛选列表中的选项")
        self.driver.find_elements_by_id("com.up366.mobile:id/count_btn_ll")[0].click()
        time.sleep(9)
        txt = self.driver.find_element_by_id("com.up366.mobile:id/title").text
        # 判断下来菜单第一个选项是否和默认的统计教材一致
        self.driver.find_element_by_id("com.up366.mobile:id/rightText").click()
        time.sleep(2)
        txt1 = self.driver.find_element_by_id("com.up366.mobile:id/list_item").text
        self.assertEqual(txt,txt1)

    def test_click_choose(self):
        logging.info("测试用例描述： 测试点击统计页面筛选按钮")
        self.driver.find_elements_by_id("com.up366.mobile:id/count_btn_ll")[0].click()
        time.sleep(9)
        self.driver.find_element_by_id("com.up366.mobile:id/rightText").click()
        #判断下拉菜单选项框是否可见
        time.sleep(5)
        status=self.driver.find_element_by_id("com.up366.mobile:id/list_item").is_displayed()
        self.assertTrue(status)
        
    def test_count_footer(self):
        logging.info("测试用例描述：测试页面底部统计按钮")
        self.driver.find_elements_by_id("com.up366.mobile:id/count_btn_ll")[0].click()
        time.sleep(9)
        status=self.driver.find_element_by_id("com.up366.mobile:id/count").is_enabled()
        self.assertFalse(status)

    def test_return(self):
        logging.info("测试用例描述:测试从统计页面返回智能课堂页面")
        self.driver.find_elements_by_id("com.up366.mobile:id/count_btn_ll")[0].click()
        time.sleep(9)
        self.driver.find_element_by_id("com.up366.mobile:id/back").click()
        time.sleep(2)
        txt=self.driver.find_element_by_id("com.up366.mobile:id/title").text
        self.assertEqual(txt,"天学网智能课堂")

if __name__=='__main__':
    unittest.main









