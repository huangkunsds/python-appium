# coding:utf-8
# author:huangkun
# datetime:2018/9/3
import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import   expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from public.BasePage import Base
from public.desire_caps import Caps
from public.login import logIn
from utils.getToast import get_Toast
from utils.log import logging


class setup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.info("setUoTest.py 用例开始执行")
        cls.driver = Caps.set_caps(None)
        logIn(cls.driver, "up0864", '123456')
        # 登录成功后的弹框处理
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/welcome_dialog_dismiss_btn"))
        Base(cls.driver).clickButton((By.XPATH,".//*[contains(@text,'黄坤')]"))
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='设置']"))

    @classmethod
    def tearDownClass(cls):
        logging.info("setUoTest.py 用例执行结束")
        cls.driver.quit()

    def test_Update(cls):
        '''检查更新'''
        time.sleep(3)
        Base(cls.driver).clickButton((By.XPATH, "//*[@text='检查更新']"))
        toast = get_Toast(cls.driver,"当前已是最新版本")
        print("toast is :%s" % toast)
        cls.assertEqual(toast,"当前已是最新版本")

    def test_courseManage_page(cls):
        '''课程管理页面'''
        time.sleep(3)
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='课程管理']"))
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/back"))

    def test_message_page(cls):
        '''消息通知页面'''
        time.sleep(3)
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='消息通知']"))
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/back"))

    def test_uploadTestResult(cls):
        '''上传测试结果'''
        time.sleep(3)
        Base(cls.driver).clickButton((By.XPATH,"//*[@text='设置']"))
        cls.driver.find_element_by_xpath("//*[@text='上传测试结果']").click()
        message = '//*[@text=\'{}\']'.format("数据上传成功")
        WebDriverWait(cls.driver, 30).until(
            expected_conditions.presence_of_element_located((By.XPATH, message)))
        ele_text = cls.driver.find_element_by_id("com.up366.mobile:id/upload_text").text
        cls.assertEqual(ele_text,"数据上传成功")
        cls.driver.find_element_by_id("com.up366.mobile:id/hw_submit_upload_success_tv_sure").click()
        Base(cls.driver).clickButton((By.ID,"com.up366.mobile:id/back"))


if __name__ == '__main__':
    unittest.main