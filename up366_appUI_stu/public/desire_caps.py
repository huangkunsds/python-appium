# coding:utf-8
import subprocess
import threading
import time

from appium import webdriver
from utils.adbUtils import ADB
from utils.log import logging
from utils.operaYaml import operayaml

class Caps:

    def set_caps(self):
        '''
        :param port: 设备列表的下标
        :return: driver
        '''
        device_info = operayaml().get_device_info()
        platformName = device_info["platformName"]
        deviceName = device_info["deviceName"]
        platformVersion = device_info["platformVersion"]
        devices = ADB().get_device_id()

        # 定义初始化的属性信息
        desired_caps = {
            'platformName': platformName,
            'deviceName': deviceName,
            'platformVersion': platformVersion,
            'appPackage': 'com.up366.mobile',
            'appActivity': '.SplashActivity',
            'noReset': False,
            'resetKeyboard': True,
            'autoGrantPermissions': True,
            'automationName': 'Uiautomator2'
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return driver

    # def start_mutil(self):
    #     devices_list = ADB.get_device_id(self)
    #     thread_list = []
    #
    #     for i in range(len(devices_list)):
    #         port = 4700+i
    #         start_th = threading.Thread(target=Caps.set_caps,args=(self,devices_list[i],port),)
    #         logging.info("device:%s is" %i)
    #         thread_list.append(start_th)
    #     for i in thread_list:
    #         i.start()
    #         time.sleep(10)

# if __name__ == '__main__':
#     cap = Caps()
#     cap.start_mutil()