#coding:utf-8
import os

from utils.log import logging


class checkenvironment:

    def check(self):
        appium_version = os.popen("appium -v").read()
        if '1.' in appium_version:
            logging.info("appium version {}" .format(appium_version))
            return True
        else:
            logging.error("appium not in computer")
            return False
        exit()


if __name__ == '__main__':
    che = checkenvironment()
    che.check()