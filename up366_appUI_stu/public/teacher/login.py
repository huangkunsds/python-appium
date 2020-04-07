#coding:utf-8
import os
import time


class P:
    def start_appium(self):
        res = os.popen('appium -p 4700 -bp 4800 -U 88d04696').read()
        time.sleep(5)
        print(res)
        time.sleep(10)



if __name__ == '__main__':
    p = P()
    p.start_appium()