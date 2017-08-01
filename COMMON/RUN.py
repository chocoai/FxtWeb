#!/usr/bin/python
#coding:utf-8
import unittest
from Lib import HTMLTestRunner
#import HTMLTestRunner
import LOG as Log
import CONFIG as readConfig
import SENDEMAIL as Se
import threading
import os
import sys
import subprocess
import time
Distributed=readConfig.ReadConfig().getConfigValue('Distributed')
readConfigLocal=readConfig.ReadConfig()
class MyRun(object):
    def __init__(self,npath,ncmdput):
        global path,cmdput,log,logpath
        path=npath
        cmdput=ncmdput
        log=Log.MyLog.get_log(cmdput,path)
        logpath=log.get_resultPath()

        self.serverPath=os.path.join(readConfig.prjDir, "ExtraTools/selenium-server-standalone-2.53.0.jar")

        self.caseListPath = os.path.join(npath, "caseList.txt")
        self.casePath =npath
        self.caseList = []
    def set_case_list(self):
        """from the caseList get the caseName,set in caseList
        :return:
        """
        if len(sys.argv) >= 3:

            argvlists=sys.argv[2].split(',')
            for i in argvlists:
                self.caseList.append(i.strip())
        else:
            fp = open(self.caseListPath)
            for data in fp.readlines():

                s_data = str(data)
                if s_data != '' and not s_data.startswith("#"):
                    self.caseList.append(s_data.replace("\n", "").strip())
                fp.close()
        print self.caseList
    def createCasesuit(self):
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module_list = []

        if len(self.caseList) > 0:

            for case_name in self.caseList:
                discover = unittest.defaultTestLoader.discover(self.casePath, pattern=case_name + '.py',
                                                               top_level_dir=None)
                suite_module_list.append(discover)

        if len(suite_module_list) > 0:

            for suite in suite_module_list:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            return None

        return test_suite
    def start(self):
        """开始测试"""
        alltestnames = self.createCasesuit()
        if Distributed=='NO':
            self.startGirdSever()
        log.build_startLine('Test')
        fp=open(logpath,'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例详情')
        runner.run(alltestnames)
        fp.close()
        log.build_endLine('Test ')
    def mailSend(self,attfile):
        Se.MyEmail(path).sendEmail(attfile)
    def starttest(self):
        threads=[]
        case=threading.Thread(target=self.startCase)
        threads.append(case)
        girdServer=threading.Thread(target=self.startGirdSever)
        threads.append(girdServer)

        for i in threads:
            i.setDaemon(True)
            i.start()
    def attFile(self):
        attpath = readConfig.ReadConfig(path).getEmailAttPath(log.get_logFile())
        return attpath
    def startGirdSever(self):
       #print self.serverPath
       subprocess.Popen('java -jar '+self.serverPath+'  -role hub -timeout 10')
       time.sleep(2)




