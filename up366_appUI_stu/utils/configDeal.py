#coding=utf-8

import configparser

from utils import pathDeal


def configGet(section, option):
    config = configparser.ConfigParser()
    try:
        conf = pathDeal.getSpecialFile('config.ini')
        if(conf):
            f = open(conf)
            config.readfp(f)
            url = config.get(section, option)
            return url
        else:
            print('Config file read fail')
            return False
    except configparser.NoSectionError:
        print('Section is not found')
        return False
    except configparser.NoOptionError: 
        print('Option is not found')
        return False
    
if __name__ == "__main__":
    test = configGet('BOOK','url')
    
