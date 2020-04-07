# coding=utf-8

import subprocess
from public.desire_caps import Caps
from utils import reportDeal
from utils.adbUtils import ADB
from utils.checkEnvironment import checkenvironment
from utils.log import logging


class run:
    def RunAll(self):
        # 检查appium是否已安装
        checkenvironment().check()

        # 判断电脑是否已链接device
        androidList = ADB().get_device_id()
        logging.info("链接devices数为 %s 个" % len(androidList))
        if androidList:
            logging.info("the conncting device is %s" % androidList)
            '''判断appium是否已启动'''
            if not ADB().get_appium_status():
                ADB().start_appium()
            u'''添加testCase目录下所有用例'''
            suite = reportDeal.createSuiteAll()

            u'''执行测试用例，并生成测试报告'''
            reportDeal.createReport(suite)
            ADB().stop_appium()
        else:
            logging.error("the computer is not connect any devices")


if __name__ == '__main__':
    r = run()
    r.RunAll()

