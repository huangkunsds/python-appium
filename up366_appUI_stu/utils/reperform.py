#-*- coding:utf-8 -*-
# author:huangkun
# datetime:2018/9/26

def failrun(n=3):
    def decorater(func):
        def warpper(*args,**kwargs):
            for i in range(n):
                try:
                    r = func(*args,**kwargs)
                    return r
                except AssertionError as err:
                    print("用例第一次失败原因 %s" % err)
            raise AssertionError
        return warpper
    return decorater