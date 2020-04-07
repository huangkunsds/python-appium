# coding:utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def get_Toast(driver,message):  # 查找toast值
    try:
        toast_loc = (By.XPATH, ".//*[contains(@text,\'{}\')]".format(message))
        ele = WebDriverWait(driver, 5,0.5).until(
            expected_conditions.presence_of_element_located(toast_loc))
        return ele.get_attribute("text")
    except:
        return False
