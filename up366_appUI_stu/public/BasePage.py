# coding:utf-8
# author:huangkun
# datetime:2018/9/13
from selenium.webdriver.support.wait import WebDriverWait
from utils.log import logging


class Base:
    driver = None

    def __init__(self, appium_driver):
        self.driver = appium_driver

    # 重新封装单个元素定位方法
    def find_element(self, loc, wait=6):
        try:
            WebDriverWait(
                self.driver, wait).until(
                lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            logging.error(u"%s 页面中未能找到 %s 元素" % (self, loc))

    # 重新封装一组元素定位方法
    def find_elements(self, loc):
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except:
            logging.error(u"%s 页面中未能找到 %s 元素" % (self, loc))


    # 重新封装输入方法
    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(loc).click()
            if clear_first:
                self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)
        except AttributeError:
            logging.error(u"%s 页面中未能找到 %s 元素" % (self, loc))


    # 重新封装按钮点击方法
    def clickButton(self, loc, find_first=True):
        try:
            if find_first:
                self.find_element(loc)
            self.find_element(loc).click()
        except AttributeError:
            logging.error("%s 页面未能找到 %s 按钮" % (self, loc))

