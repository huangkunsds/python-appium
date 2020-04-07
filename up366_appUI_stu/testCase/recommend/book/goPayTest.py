# coding:utf-8
# author: huangkun
import time
import unittest

from selenium.webdriver.common.by import By

from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.log import logging


class gopay(unittest.TestCase):

    def setUp(self):
        logging.info("goStudy.py用例开始执行")
        self.driver = Caps.set_caps(self)
        time.sleep(2)
        logIn(self.driver, "15831539813", "123456")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        time.sleep(1)
        self.driver.find_elements_by_id("com.up366.mobile:id/name")[0].click()
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/tip1"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/tip2"))
        time.sleep(1)
        self.driver.find_elements_by_id("com.up366.mobile:id/book_picture")[0].click()
        #点击购买按钮
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/buyIt"))


    def tearDown(self):
        self.driver.quit()

    def test_WeChat_pay(self):
        '''微信支付页面跳转'''
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/user_buy_to_buy_btn"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/dialog_common_confirm"))
        self.driver.find_elements_by_id("com.up366.mobile:id/pay_type_item_radio_im")[0].click()
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/pay_dialog_to_pay_btn"))
        ele_text = Base(self.driver).find_element((By.ID,"com.tencent.mm:id/mp")).text
        self.assertEqual(ele_text,"微信号/QQ/邮箱登录")

    def test_Alipay_pay(self):
        '''支付宝支付页面跳转'''
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/user_buy_to_buy_btn"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/dialog_common_confirm"))
        self.driver.find_elements_by_id("com.up366.mobile:id/pay_type_item_radio_im")[1].click()
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/pay_dialog_to_pay_btn"))
        ele = Base(self.driver).find_element((By.CLASS_NAME,"android.webkit.WebView"))
        self.assertIsNotNone(ele,"element is None")


    def test_pay_falie(self):
        '''购买失败，查看订单'''

        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/user_buy_to_buy_btn"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/dialog_common_confirm"))
        self.driver.find_elements_by_id("com.up366.mobile:id/pay_type_item_radio_im")[0].click()
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/pay_dialog_to_pay_btn"))
        Base(self.driver).clickButton((By.ID,"com.tencent.mm:id/j8"))
        ele_text = Base(self.driver).find_element((By.ID,"com.up366.mobile:id/dialog_common_title")).text
        self.assertEqual(ele_text,"购买失败")
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/dialog_common_confirm"))
        ele2_text = Base(self.driver).find_element((By.ID,"com.up366.mobile:id/title")).text
        self.assertEqual(ele2_text,"购买记录")

    def test_recharge(self):
        '''充值'''
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/user_buy_to_buy_btn"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/dialog_common_confirm"))
        self.driver.find_elements_by_id("com.up366.mobile:id/pay_type_item_radio_im")[0].click()
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/pay_dialog_to_recharge_btn"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/user_pay_50_rmb"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/user_pay_100_rmb"))
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/user_pay_200_rmb"))
        self.driver.find_element_by_id("com.up366.mobile:id/userPayAnyRmb").send_keys('300')
        self.driver.find_elements_by_id("com.up366.mobile:id/pay_type_item_radio_im")[0].click()
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/user_pay_money_btn"))
        ele_text = Base(self.driver).find_element((By.ID,"com.tencent.mm:id/mp")).text
        self.assertEqual(ele_text,"微信号/QQ/邮箱登录")



if __name__ == '__main__':
    unittest.main