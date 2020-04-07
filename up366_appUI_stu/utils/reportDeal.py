#coding:utf-8

import shutil
import unittest
import time, sys, logging, os

from utils import pathDeal, HTMLTestRunner, log, configDeal

u'''遍历Case目录下的所有case，将case中的所有方法添加到suite中'''
u'''case命名规则：*Test.py'''
def createSuiteAll(caseDir='testCase'):
    casePath = pathDeal.getSpecialPath(caseDir)
    #print(casePath)

    if(casePath):
        suite=unittest.TestSuite() #构造测试用例容器
        #print(suite)
        #加载测试用例
        discover=unittest.defaultTestLoader.discover(casePath,pattern='*Test.py',top_level_dir=None)
        try:
            for test_suite in discover:
                for test_case in test_suite:
                    suite.addTests(test_case)
            return suite
        except:
            print("\n用例加载失败：%s" % test_case)
            return False
    else:
        return False


u'''将一个case文件中的所有方法添加到suite中'''
def createSuite(caseFile="".join(os.path.splitext(os.path.basename(sys.argv[0]))), caseDir='testCase'):
    casePath = pathDeal.getSpecialPath(caseDir)
    if(casePath and caseFile):
        suite=unittest.TestSuite()
        test_suite=unittest.defaultTestLoader.discover(casePath,pattern=caseFile,top_level_dir=None)
        for test_case in test_suite:
            suite.addTests(test_case)
        return suite
    else:
        return False

u'''执行测试用例，并生成测试报告'''
def createReport(suite, reportTitle=u'天学网新版APP学生UI自动化测试', reportDir='testResult'):
    date_now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
    filePath = pathDeal.getSpecialPath(reportDir)
    #fname = "".join(os.path.splitext(os.path.basename(sys.argv[0])))
    
    fname = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    print(fname)
    filename = filePath + 'UI' + fname + date_now + '_check_results.html'

    if(suite):
        try:
            fp=open(filename,'wb')
            u'''定义测试报告'''
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=reportTitle, description=u"用例执行情况：")
            runner.run(suite)
            fp.close()
            
            #用于Jenkins HTML report查看
            shutil.copyfile(filename,filePath+'index.html')
                    
        except TypeError:
            print(u'生成测试报告失败')
    else:
        logging.debug(u'测试用例执行失败，没有测试报告生成')


if __name__ == '__main__':
    createReport(createSuiteAll())



    
    