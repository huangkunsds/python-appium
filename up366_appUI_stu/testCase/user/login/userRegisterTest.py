# coding:utf-8
'''
    Created on 2018-8-31
    author: hewenqi
'''
import time
import unittest

from public.BasePage import Base
from public.desire_caps import Caps
from utils.getToast import get_Toast
from utils.log import logging
from utils import reportDeal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Register(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        logging.info("userRegister.py 用例开始执行")
        self.driver = Caps.set_caps(None)
        time.sleep(2)
        self.driver.find_elements_by_id("com.up366.mobile:id/icon")[2].click()
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/login"))
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/register"))

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        logging.info("userRegister.py 用例执行结束")


    def test_Register1(self):
        '''手机号输入10位纯数字'''
        time.sleep(3)
        Base(self.driver).send_keys((By.ID,"com.up366.mobile:id/input_phone_number"),'1355205279')
        Base(self.driver).clickButton((By.ID,"com.up366.mobile:id/send_verification_code"))
        # 获取toast信息
        toast = get_Toast(self.driver,"请输入有效手机号")
        print("toast is: %s" % toast)
        self.assertEqual(toast, u'请输入有效手机号')

    def test_Register10(self):
        '''手机号输入11位纯数字，不是有效手机号格式'''
        time.sleep(3)
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_phone_number"), '11111111111')
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/send_verification_code"))
        # 获取toast信息
        toast = get_Toast(self.driver,"请输入有效手机号")
        print("toast is: %s" % toast)
        self.assertEqual(toast, u'请输入有效手机号')

    def test_Register11(self):
        '''输入正确手机号、验证码，其他不输入，不勾选《使用许可协议》'''
        time.sleep(3)
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_phone_number"), '13552052797')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_verification_code"),'123456')
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/register_btn"))
        # 定位toast元素
        toast = get_Toast(self.driver,"请输入密码")
        print("toast is: %s" % toast)
        self.assertEqual(toast, u'请输入密码'+'\n'+'请输入真实姓名'+'\n'+'请同意《使用许可协议》')

    def test_Register12(self):
        '''输入正确手机号、验证码，正确密码，真实姓名为空，不勾选《使用许可协议》'''
        time.sleep(3)
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_phone_number"), '13552052797')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_verification_code"), '123456')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_password"), 'a12345')
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/register_btn"))
        # 定位toast元素
        toast = get_Toast(self.driver,"请同意")
        print("toast is: %s" % toast)
        self.assertEqual(toast, u'请输入真实姓名'+'\n'+'请同意《使用许可协议》')

    def test_Register13(self):
        '''输入正确手机号、验证码，正确密码，真实姓名为空，不勾选《使用许可协议》'''
        time.sleep(3)
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_phone_number"), '13552052797')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_verification_code"), '123456')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_password"), 'a12345')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_real_name"), '逍遥子')
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/register_btn"))
        # 定位toast元素
        toast_loc = (By.XPATH, ".//*[contains(@text,'请同意《使用许可协议》')]")
        toast = WebDriverWait(self.driver, 3, 0.1).until(EC.presence_of_element_located(toast_loc)).text
        print("toast is: %s" % toast)
        self.assertEqual(toast, u'请同意《使用许可协议》')

    def test_Register14(self):
        '''手机（邮箱）验证码错误或已过期'''
        time.sleep(3)
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_phone_number"), '13552052798')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_verification_code"), '123456')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_password"), 'a12345')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_real_name"), '逍遥子')
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/accept_deal_checbox"))
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/register_btn"))
        # 定位toast元素
        toast_loc = (By.XPATH, ".//*[contains(@text,'手机(邮箱)验证码错误或已过期')]")
        toast = WebDriverWait(self.driver, 3, 0.1).until(EC.presence_of_element_located(toast_loc)).text
        print("toast is: %s" % toast)
        self.assertEqual(toast, u'手机(邮箱)验证码错误或已过期')

    def test_Register15(self):
        '''输入错误密码（密码比要求长度短一位）'''
        time.sleep(3)
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_phone_number"), '15133990081')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_verification_code"), '123456')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_password"), 'a1234')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_real_name"), '逍遥子')
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/register_btn"))
        # 定位toast元素
        toast_loc = (By.XPATH, ".//*[contains(@text,'密码格式不对，请输入6-15位字母加数字组合')]")
        toast = WebDriverWait(self.driver, 3, 0.1).until(EC.presence_of_element_located(toast_loc)).text
        print("toast is: %s" % toast)
        self.assertEqual(toast, u'密码格式不对，请输入6-15位字母加数字组合')

    def test_Register16(self):
        '''输入错误密码（密码比要求长度长一位）'''
        time.sleep(3)
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_phone_number"), '15133990081')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_verification_code"), '123456')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_password"), 'a123456789123456')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_real_name"), '逍遥子')
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/register_btn"))
        # 定位toast元素
        toast_loc = (By.XPATH, ".//*[contains(@text,'密码格式不对，请输入6-15位字母加数字组合')]")
        toast = WebDriverWait(self.driver, 3, 0.1).until(EC.presence_of_element_located(toast_loc)).text
        print("toast is: %s" % toast)
        self.assertEqual(toast, u'密码格式不对，请输入6-15位字母加数字组合')

    def test_Register17(self):
        '''输入错误密码（六位纯数字）'''
        time.sleep(3)
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_phone_number"), '15133990081')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_verification_code"), '123456')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_password"), '123456')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_real_name"), '逍遥子')
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/register_btn"))
        # 定位toast元素
        toast_loc = (By.XPATH, ".//*[contains(@text,'密码格式不对，请输入6-15位字母加数字组合')]")
        toast = WebDriverWait(self.driver, 3, 0.1).until(EC.presence_of_element_located(toast_loc)).text
        print("toast is: %s" % toast)
        self.assertEqual(toast, u'密码格式不对，请输入6-15位字母加数字组合')

    def test_Register18(self):
        '''输入错误密码（十五位纯字母）'''
        time.sleep(3)
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_phone_number"), '15133990081')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_verification_code"), '123456')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_password"), 'abcdefghijklmno')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_real_name"), '逍遥子')
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/register_btn"))
        # 定位toast元素
        toast_loc = (By.XPATH, ".//*[contains(@text,'密码格式不对，请输入6-15位字母加数字组合')]")
        toast = WebDriverWait(self.driver, 3, 0.1).until(EC.presence_of_element_located(toast_loc)).text
        print("toast is: %s" % toast)
        self.assertEqual(toast, u'密码格式不对，请输入6-15位字母加数字组合')

    def test_Register19(self):
        '''输入错误真实姓名（真实姓名比要求长度短一位）'''
        time.sleep(3)
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_phone_number"), '15133990081')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_verification_code"), '123456')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_password"), 'a12345')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_real_name"), '逍')
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/register_btn"))
        # 定位toast元素
        toast_loc = (By.XPATH, ".//*[contains(@text,'真实姓名格式不对，仅支持2-30位中文')]")
        toast = WebDriverWait(self.driver, 3, 0.1).until(EC.presence_of_element_located(toast_loc)).text
        print("toast is: %s" % toast)
        self.assertEqual(toast, u'真实姓名格式不对，仅支持2-30位中文')

    def test_Register20(self):
        '''输入错误真实姓名（真实姓名比要求长度长一位）'''
        time.sleep(3)
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_phone_number"), '15133990081')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_verification_code"), '123456')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_password"), 'a12345')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_real_name"), '当你觉得但后悔会更难过的')
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/register_btn"))
        # 定位toast元素
        toast_loc = (By.XPATH, ".//*[contains(@text,'手机(邮箱)验证码错误或已过期')]")
        toast = WebDriverWait(self.driver, 3, 0.1).until(EC.presence_of_element_located(toast_loc)).text
        print("toast is: %s" % toast)
        self.assertEqual(toast, u'手机(邮箱)验证码错误或已过期')

    def test_Register21(self):
        '''输入错误真实姓名（存在特殊字符）'''
        time.sleep(3)
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_phone_number"), '15133990081')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_verification_code"), '123456')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_password"), 'a12345')
        Base(self.driver).send_keys((By.ID, "com.up366.mobile:id/input_real_name"), '逍&遥')
        Base(self.driver).clickButton((By.ID, "com.up366.mobile:id/register_btn"))
        # 定位toast元素
        toast_loc = (By.XPATH, ".//*[contains(@text,'真实姓名格式不对，仅支持2-30位中文')]")
        toast = WebDriverWait(self.driver, 3, 0.1).until(EC.presence_of_element_located(toast_loc)).text
        print("toast is: %s" % toast)
        self.assertEqual(toast, u'真实姓名格式不对，仅支持2-30位中文')


if __name__ == '__main__':
    #unittest.main
    u'''添加用例'''
    suite = reportDeal.createSuite()

    u'''ִ执行测试用例，并生成测试报告'''
    reportDeal.createReport(suite)

