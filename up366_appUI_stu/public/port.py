#coding:utf-8

import os

from utils.log import logging


class P:

    def port_is_used(self,port):
        '''
        判断端口是否被占用
        :param port:端口
        :return:占用返回TRUE  没有返回False
        '''
        command = 'netstat -ano | findstr ' + str(port)
        result = os.popen(command).readlines()
        if result is not None:
            flag = False
            if len(result)>0:
                flag = True
            return flag

        else:
            logging.info("%s 此端口被占用"% port)

    def create_port_list(self,start_port,device_list):
        '''
        生成可用端口列表
        :param start_port: 4701
        :param device_list: 设备列表
        :return: port_list
        '''
        port_list = []
        if device_list != None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_port) is not True:
                    port_list.append(start_port)
                start_port += 1
            return port_list
        else:
            logging.error("设备列表为空，请检查设备连接是否正常")


if __name__ == '__main__':
    p = P()
    devicelist = []
    print(p.create_port_list(4723,devicelist))
    #p.port_is_used('80')

