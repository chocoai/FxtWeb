# -*- coding: utf-8 -*-
import os
import sys
import COMMON.DRIVER as DR
import COMMON.ELEMNET as EL
import COMMON.LOG as LG
import unittest
from COMMON import CONFIG as CFG
xmlpath=os.path.join(CFG.prjDir,'BaseCase/GJB')
logger=LG.MyLog().get_log().get_myLogger()
AddNewDetail=EL.get_el_name('AddNewDetail',xmlpath)

if len(sys.argv)>=2:
    if sys.argv[1]=='09':
        url=CFG.ReadConfig().getConfigValue('09Url')
        logger.info(u'当前测试环境为09环境')
    elif sys.argv[1]=='10':
        url=CFG.ReadConfig().getConfigValue('10Url')
        logger.info(u'当前测试环境为10环境')
    testpath=sys.argv[1]
else:
    url=CFG.ReadConfig().getConfigValue('Url')
    testpath='09'

dataPath=os.path.join(CFG.prjDir,'BaseCase','GJB','data',testpath)
dataFile=os.path.join(dataPath,'testData.xlsx')
unittest.TestLoader()
logger.info(u'测试环境网址: %s'%url)
class unittestBase(unittest.TestCase):

    def setUp(self):

        # driver=DR.MyDriver.driverGrid()
        #Firefox
        #driver = DR.MyDriver.get_driver('Firefox')
        #chrome
        #driver = DR.MyDriver.get_driver('Chrome')
        #IE
        #driver=DR.MyDriver.get_driver()
        #driver.maximize_window()

        driver=DR.MyDriver.getDriver()

        #self.el=EL.Element(driver,'http://gjb.fxtchina.com/?type=logout',path)
        #self.el = EL.Element(driver, 'http://gjb.yungujia.com/?type=logout', path)

        self.el = EL.Element(driver, url, xmlpath)
        self.driver = self.el.getDriver()
        self.log = LG.MyLog().get_log()
        self.logger = self.log.get_myLogger()

    @LG.endLog
    def tearDown(self):
        self.driver.quit()
