#coding:utf-8
import logging
import time
import os
from time import sleep
import threading
import ELEMNET as ET
import codecs
import traceback

class Log:
    def __init__(self,cmdPut='ON',path=''):
        """
        :param name:GJB class name
        :param cmdPut: console put switch
        """
        global logger,resultPath,logPath

        if path!='':
            resultPath=os.path.join(path,'report')
        else:
            resultPath=os.path.join(os.getcwd(),'Report')

        logPath=os.path.join(resultPath,(time.strftime('%Y%m%d%H%M%S', time.localtime())))
        if os.path.exists(logPath) is False:
            os.makedirs(logPath)
        self.checkNo=0
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.INFO)
        self.cmdPut=cmdPut
        #creat handler ,write log to file
        fh = logging.FileHandler(os.path.join(logPath, 'MyOutPut.log'))
        #fh=logging.FileHandler(os.path.join(logPath,'MyOutPut.log'),encoding='utf-8')
        #Define the MyLog format of formatter handler
        #formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s- %(filename)s[line:%(lineno)d] - %(funcName)s --- %(message)s')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s- %(filename)s[line:%(lineno)d] ---%(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        #Define the MyLog format to out of console
        if cmdPut=='ON':
            ch=logging.StreamHandler()
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

    def get_logFile(self):
        return logPath

    def get_resultPath(self):
        '''get the resultPath of html
        :return: path of report
        '''
        report_path=os.path.join(logPath,'MyLog.html')
        return report_path

    def get_myLogger(self):
        '''get the logger
        :return: logger(My Log)
        '''
        return self.logger

    def build_startLine(self,caseNo):
        '''build the log of start
        :param caseNo:
        :return:
        '''
        startLine="--------- " +caseNo+' START  --------'
        self.logger.info(startLine)

    def build_endLine(self,caseNo):
        '''build the end log
        :param caseNo:
        :return:
        '''
        endLine="--------- " +caseNo+' END   ---------'
        self.logger.info(endLine)

    def write_resutl(self,result):
        '''
        :param result:
        :return:
        '''
        reportPath=os.path.join(logPath,'report.txt')
        flogging=open(reportPath,'a')
        #flogging=codecs.open(reportPath,'a+','utf-8')
        try:
            flogging.write(result+"\n")
        except:
            flogging.close()

    def take_shot(self,driver,caseName):
        '''screen shot by selenium screen shot
        :param driver:
        :param caseName:
        :return:
        '''
        #screenshotName=str(self.checkNo)+'.png'
        screenshotName=caseName+'.png'
        #screenshotPath=os.path.join(logPath,caseName)
        imgPath=os.path.join(logPath,'Image')
        if not os.path.exists(imgPath):
            os.makedirs(imgPath)

        #screenshotPath=os.path.join(imgPath,caseName)
        #if not os.path.exists(screenshotPath):
            #os.makedirs(screenshotPath)

        screenshot=os.path.join(imgPath,screenshotName)
        sleep(1)
        #driver.get_screenshot_as_file(screenshot)
        driver.save_screenshot(screenshot)
        #print screenshot
        self.checkNo+=1
        return os.path.join(screenshot.replace(resultPath,'../../report'))

class MyLog(object):
    """
    Log run mole
    """
    log=None
    mutex=threading.Lock()
    def __init__(self):
        pass
    @staticmethod
    def get_log(cmdPut='ON',path=''):
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log=Log(cmdPut,path)
            MyLog.mutex.release()
        return MyLog.log

def caseLog(name, log=''):
    """
    装饰器
    :param name:
    :param log:
    :return:
    """
    if log=='':
        log=MyLog.get_log()
        #logger=log.get_myLogger()
    def _Mylog(func):
        def outLog(*args,**kwargs):
            log.build_startLine(name)
            try:
                res=func(*args,**kwargs)
            except Exception as e:
                log.take_shot(ET.Element.getdriver(),func.__name__)
                #traceback.print_exc()#系统错误日志屏幕显示，不显示HTML报告
                logging.exception(e.__unicode__())#报告显示到自动LOG文件
                raise e
            finally:
                log.build_endLine(name)
            return res
        return outLog
    return _Mylog

def endLog(func):
    """
    脚本装饰器
    :param func:
    :return:
    """
    logger = MyLog.get_log().get_myLogger()
    def _outLog(*args,**kwargs):
        logger.info('-'*70)
        res=func(*args,**kwargs)
        return res
    return _outLog


