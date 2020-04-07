# coding:utf-8
import time

from selenium.webdriver.common.by import By
from public.BasePage import Base


def logIn (driver,username,password):
    Base(driver).clickButton((By.XPATH, ".//*[contains(@text,'智能课堂')]"))
    Base(driver).clickButton((By.ID,"com.up366.mobile:id/no_data_login_btn"))
    time.sleep(2)
    Base(driver).find_element((By.ID,"com.up366.mobile:id/username")).send_keys(username)
    Base(driver).find_element((By.ID,"com.up366.mobile:id/password")).send_keys(password)
    Base(driver).clickButton((By.ID,"com.up366.mobile:id/login"))


def logInimg(driver, username, password):
    Base(driver).clickButton((By.ID,"com.up366.mobile:id/login"))
    Base(driver).find_element((By.ID, "com.up366.mobile:id/username")).send_keys(username)
    Base(driver).find_element((By.ID, "com.up366.mobile:id/password")).send_keys(password)
    Base(driver).clickButton((By.ID,"com.up366.mobile:id/login"))


def logInPage(driver,username,password):
    Base(driver).find_element((By.ID, "com.up366.mobile:id/username")).send_keys(username)
    Base(driver).find_element((By.ID, "com.up366.mobile:id/password")).send_keys(password)
    Base(driver).clickButton((By.ID,"com.up366.mobile:id/login"))
