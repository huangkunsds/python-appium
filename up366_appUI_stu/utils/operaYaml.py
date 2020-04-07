#coding:utf-8
from utils.adbUtils import ADB
from utils.pathDeal import getSpecialFile

import yaml
'''
1.设备链接后，查看设备的device，和device_info中的deviceName比对
2.如果不相等，更新deviceNmae和platformVersion
'''


class operayaml:

    def get_device_info(self):
        device_id = ADB().get_device_id()[0]
        platformVersion = ADB().get_android_version()
        try:
            filepath = getSpecialFile("device_info.yaml")
            with open(filepath,'r') as f:
                device_info = yaml.load(f)
                if device_id != device_info["deviceName"]:
                    device_info["deviceName"] = device_id
                    device_info["platformVersion"] = platformVersion.strip()
                return device_info
        except yaml.YAMLError as e:
            print(e)
        except FileNotFoundError as o:
            print(o)

    def get_user_info(self):
        try:
            filepath = getSpecialFile("user_info.yaml")
            with open(filepath,'r') as f:
                user_info = yaml.load(f)
                return user_info
        except yaml.YAMLError as e:
            print(e)
        except FileNotFoundError as o:
            print(o)

if __name__ == '__main__':
    op = operayaml()
    user = op.get_user_info()
    print(user["username"])
    print(user["password"])