# coding:utf-8
from selenium.webdriver.common.by import By
from public.BasePage import Base


class LoginPage(Base):

    def login(self, username, password):
        Base.clickButton(By.XPATH, ".//*[contains(@text,'智能课堂')]")
        Base.clickButton(By.ID, "com.up366.mobile:id/no_data_login_btn")

