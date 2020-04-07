# coding:utf-8

import os
import re
import time
from utils.log import logging


class ADB:
    """
        单个设备，可不传入参数device_id
        """

    def __init__(self,device_id=""):
        if device_id == "":
            self.device_id = ""
        else:
            self.device_id = "-s %s" % device_id

    def get_device_id(self):
        """
        获取设备id
        """
        android_devices_list = []
        for device in os.popen('adb devices').readlines():
            if 'device' in device and 'devices' not in device:
                device = device.split('\t')[0]
                android_devices_list.append(device)

        return android_devices_list



    def get_appium_status(self):
        '''根据端口号查看appium是否启动,启动时返回信息，未启动返回空'''
        appium_status = os.popen("netstat -ano | findstr 4723").read()
        if appium_status:
            return True
        else:
            return False

    def start_appium(self):
        os.popen("start appium")
        time.sleep(4)
        logging.info("appium start success")

    def stop_appium(self):
        os.popen("taskkill /f /fi \"imagename eq node.exe\"")
        if ADB.get_appium_status :
            logging.info("stop appium success")
        else:
            logging.info("stop appium faile")

    def get_android_version(self):
        """
        获取android 版本
        """
        return os.popen("adb shell getprop ro.build.version.release").read()

    def get_sdk_version(self):
        """
        获取sdk版本
        """
        return os.popen("adb shell getprop ro.build.version.sdk").read()

    def get_device_model(self):
        """
        获取设备型号
        """
        return os.popen("adb shell getprop ro.product.model").read()

    def get_app_status(self,package_name):
        '''
        根据pid查看app是否已启动
        :param pakage_name:
        :return:
        '''
        pidinfo = os.popen(
            "adb shell ps | findstr %s$" %
            package_name).read()
        if pidinfo == '':
            print("the process doesn't exist.")
            return False

        pattern = re.compile(r"\d+")
        result = pidinfo.split(" ")
        result.remove(result[0])
        print(pattern.findall(" ".join(result))[0])
        return True

    def get_pid(self, package_name):
        """
        获取进程pid
        args:
        - packageName -: 应用包名
        usage: getPid("com.android.settings")
        """
        pidinfo = os.popen(
            "adb shell ps | findstr %s$" %
            package_name).read()
        if pidinfo == '':
            return "the process doesn't exist."

        pattern = re.compile(r"\d+")
        result = pidinfo.split(" ")
        result.remove(result[0])

        return pattern.findall(" ".join(result))[0]

    def start_app(self,packageName,activity):
        '''
        启动app
        '''
        if ADB.get_app_status(self,packageName) == False:

            os.popen("adb shell am start {0}/{1}".format(packageName,activity))
        else:
            print("app在运行中，不需在启动")

    def kill_process(self):
        """
        杀死应用进程
        args:
        - pid -: 进程pid值
        usage: killProcess(154)
        注：杀死系统应用进程需要root权限
        """
        os.popen("adb shell am force-stop com.up366.com")

        # if os.popen("adb shell kill %s" %
        #               str(pid)).read().split(": ")[-1] == "":
        #     return "kill success"
        # else:
        #     return os.popen("adb shell kill %s" %
        #                       str(pid)).read().split(": ")[-1]

    def quit_app(self, package_name):
        """
        退出app，类似于kill掉进程
        usage: quitApp("com.android.settings")
        """
        os.popen(("adb shell am force-stop %s" % package_name))

    def get_focused_pakage_and_activity(self):
        """
        获取当前应用界面的包名和Activity，返回的字符串格式为：packageName/activityName
        """
        out = os.popen(
            "adb shell dumpsys activity activities | %s mFocusedActivity" %
            "findstr").read().strip().split(' ')[3]
        return out

    def get_current_pakage_name(self):
        '''
        获取当前运行的包名
        :return: pakage_name
        '''
        return self.get_focused_pakage_and_activity().split("/")[0]

    def install_app(self,app_file):
        '''
        app名字不能包含中文
        :param app_file:
        '''
        return os.popen("adb shell install -r %s" % app_file)

    def is_install(self,pakageName):
        '''
        判断应用是否安装，已安装返回True，未安装返回False
        :param pakageName:
        '''
        if self.get_matching_app_list(pakageName):
            return True
        else:
            return False

    def get_matching_app_list(self,keyword):
        '''
        模糊查询与keyword匹配的包名
        usage: getMatchingAppList("qq")
        '''
        matapp = []
        for packages in os.popen("adb shell pm list packages %s" % keyword).readlines():
            matapp.append(packages.split(":")[-1].splitlines()[0])
        return matapp

    def remove_app(self,packageName):
        '''
        卸载应用
        :param pakageName: 应用包名，非apk名
        '''
        return os.popen("adb shell uninstall %s" % packageName)

    def clean_app_data(self,packageName):
        '''
        清除应用残留数据
        '''
        if "Success" in os.popen("adb shell pm clear %s "% packageName).read().splitlines():
            return "clear user data success"
        else:
            return "make sure packega exist"

    def get_third_app_list(self):
        """
        获取设备中安装的第三方应用包名列表
        """
        thirdApp = []
        for packages in os.popen("adb shell pm list packages -3").readlines():
            thirdApp.append(packages.split(":")[-1].splitlines()[0])

        return thirdApp




if __name__ == '__main__':
    ad = ADB()
    ad.start_appium()
