# coding:utf-8
import time

import termcolor

def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

class color:

    @staticmethod
    def c(msg,color):
        try:
            p = lambda x: termcolor.cprint(x, color)
            return p(msg)
        except:
            print(msg)

    @staticmethod
    def show_verbose(msg):
        color.c(msg,"white")

    @staticmethod
    def show_debug(msg):
        color.c(msg,"blue")

    @staticmethod
    def show_info(msg):
        color.c(msg, 'green')

    @staticmethod
    def show_warn(msg):
        color.c(msg, 'yellow')

    @staticmethod
    def show_error(msg):
        color.c(msg,'red')

class logging:
    flag = True

    @staticmethod
    def error(msg):
        if logging.flag == True:
            color.show_error(get_now_time()+"[error]:"+ msg)

    @staticmethod
    def warn(msg):
        if logging.flag == True:
            color.show_warn(get_now_time()+"[warn]:" + msg)

    @staticmethod
    def info(msg):
        if logging.flag == True:
            color.show_info(get_now_time()+"[info]:" + msg)

    @staticmethod
    def debug(msg):
        if logging.flag == True:
            color.show_debug(get_now_time()+"[debug]:" + msg)

    @staticmethod
    def success(msg):
        if logging.flag == True:
            color.show_verbose(get_now_time()+"[Success]:" + msg)

if __name__ == '__main__':
    # co = color()
    # co.show_verbose("nihao")

    lo = logging()
    lo.debug("sdsaf")