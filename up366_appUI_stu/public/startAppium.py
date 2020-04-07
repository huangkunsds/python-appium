#-*- coding:utf-8 -*-
# author:huangkun
# datetime:2018/12/18

import subprocess
import threading
import time
from public.port import P
from utils.adbUtils import ADB
from utils.log import logging


class StartAppium:

    def start_appium(self, aport, bpport, device):
        '''
        启动appium
        '''
        cmd = "appium -p %s -bp %s -U %s" %(aport, bpport, device)
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,bufsize=1)
        while True:
            appium_line = result.stdout.readline().strip()
            time.sleep(1)
            appium_line = appium_line.decode()
            logging.info(appium_line)
            if 'listener started' in appium_line or 'Error: listen' in appium_line:
                break

    def start_appium_all(self):
        '''
        根据device的个数生成port和bpport，
        多线程启动appium
        '''
        ss = StartAppium()
        p = P()
        thread_list = []
        device_list = ADB.get_device_id(self)
        #device_list = ['88d04696','89999999']
        aport = p.create_port_list(4700, device_list)
        if len(device_list) != 0:
            bpport = p.create_port_list(4800, device_list)
            for device in range(len(device_list)):
                appium_start = threading.Thread(
                    target=ss.start_appium,args=(aport[device],bpport[device],device_list[device],))
                logging.info("appium -p %s -bp %s -U %s" % (aport[device], bpport[device], device_list[device]))

                thread_list.append(appium_start)
            for i in thread_list:
                i.start()
                time.sleep(10)
        else:
            logging.info("请链接设备...")





if __name__ == '__main__':
    ss = StartAppium()
    ss.start_appium_all()
