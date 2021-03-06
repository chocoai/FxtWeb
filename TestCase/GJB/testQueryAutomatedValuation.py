# -*- coding: utf-8 -*-
import os
import ddt
import unittest
import logging
import paramunittest
import COMMON.DRIVER as DR
import COMMON.ELEMNET as EL
import COMMON.LOG as LG
import COMMON.COMMON as CM
from BaseCase.GJB import query as QY
from COMMON import CONFIG as CFG
from BaseCase.GJB import unittestBase
from BaseCase.GJB import examineModification as QM
xmlpath=os.path.join(CFG.prjDir,'BaseCase\GJB')
url=CFG.ReadConfig().getConfigValue('Url')
logger=LG.MyLog().get_log().get_myLogger()

# dataPath=os.path.join(CFG.prjDir,'BaseCase','GJB','data',unittestBase.testpath)
# dataFile=os.path.join(dataPath,'testData.xlsx')

data =CM.get_xls('QueryAutomatedValuation','TCNO',unittestBase.dataFile)
argedata=[]
for i in data :
    for j in range(len(i)):
        if i[j]=='':
            i[j]=None
    argedata.append(i)


@ddt.ddt
class AutomatedValuationQuery(unittestBase.unittestBase):
    """自动估价-查询"""

    @ddt.data(*argedata)
    @ddt.unpack
    def testAutomatedValuationQuery(self, testNo, description, msgmode, data, submode, Inquiry, substate, flag):
        logging.info(testNo + '_' + description)
        print testNo, description, msgmode, data, submode, Inquiry, substate
        result = QY.Query(self, self.el, msgmode, data, submode, Inquiry, substate)
        self.assertTrue(result)

    # @LG.caseLog(u'XJ_ZDGJ_008_自动估价记录_查询_客户单位_本部')
    # def testXJ_ZDGJ_008(self):
    #     """查询客户单位本部"""
    #     result = QY.Query(self, self.el, u'客户单位', u'包商银行', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_002_自动估价记录_查询_来源_估价宝')
    # def XJ_ZDGJ_002(self):#自动估价没有来源没有估价宝一项
    #     """查询来源估价宝"""
    #     result = QY.Query(self, self.el, u'来源', u'估价宝', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_018_自动估价记录_查询_日期_开始-结束日期')
    # def testXJ_ZDGJ_018(self):
    #     result = QY.Query(self, self.el, u'询价时间', u'2016-04-04:2016-8-08', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_029_自动估价记录_查询_条件查询_客户名称')
    # def testXJ_ZDGJ_029(self):
    #     result = QY.Query(self, self.el, u'关键字查询', u'zl', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_016_自动估价记录_查询_日期_结束日期')
    # def testXJ_ZDGJ_016(self):
    #     result = QY.Query(self, self.el, u'询价时间', u':2016-08-08', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_001_自动估价记录_查询_来源_默认')
    # def testXJ_ZDGJ_001(self):
    #     result=QY.Query(self, self.el, u'来源', u'CAS', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_004_自动估价记录_查询_来源_CAS')
    # def testXJ_ZDGJ_004(self):
    #     result=QY.Query(self, self.el, u'来源', u'CAS', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_003_自动估价记录_查询_来源_微信')
    # def testXJ_ZDGJ_003(self):
    #     result = QY.Query(self, self.el, u'来源', u'微信', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_005_自动估价记录_查询_用户类型_默认')
    # def XJ_ZDGJ_005(self):
    #     result=QY.Query(self, self.el, u'用户类型', u'默认', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    @LG.caseLog(u'XJ_ZDGJ_006_自动估价记录_查询_用户类型_内部用户')
    def XJ_ZDGJ_006(self):
        result=QY.Query(self, self.el, u'用户类型', u'内部用户', Inquiry='Zidongxujia')
        self.assertTrue(result)
    @LG.caseLog(u'XJ_ZDGJ_007_自动估价记录_查询_用户类型_外部用户')
    def XJ_ZDGJ_007(self):
        result=QY.Query(self, self.el, u'用户类型', u'外部用户', Inquiry='Zidongxujia')
        self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_009_自动估价记录_查询_客户单位_分行')
    # def testXJ_ZDGJ_009(self):
    #     result=QY.Query(self, self.el, u'客户单位', u'包商银行 包商银行深圳分部', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_010_自动估价记录_查询_客户单位_支行')
    # def testXJ_ZDGJ_010(self):
    #     result=QY.Query(self, self.el, u'客户单位', u'包商银行 包商银行深圳分部 134455', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_017_自动估价记录_查询_日期_开始日期')
    # def testXJ_ZDGJ_017(self):
    #     result=QY.Query(self, self.el, u'询价时间', u'2016-04-04', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_015_自动估价记录_查询_日期_开始与结束日期清空')
    # def testXJ_ZDGJ_015(self):
    #     result=QY.Query(self, self.el, u'询价时间', u'清空', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_22_自动估价记录_查询_查询面积_默认')
    # def testXJ_ZDGJ_22(self):
    #     result=QY.Query(self, self.el, u'面积', u'默认', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_25_自动估价记录_查询_查询面积_区间面积')
    # def testXJ_ZDGJ_25(self):
    #     result=QY.Query(self, self.el, u'面积', u'100-300', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_23_自动估价记录_查询_查询面积_最大面积')
    # def testXJ_ZDGJ_23(self):
    #     result=QY.Query(self, self.el, u'面积', u'-200', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_24_自动估价记录_查询_查询面积_最小面积')
    # def testXJ_ZDGJ_24(self):
    #     result=QY.Query(self, self.el, u'面积', u'100', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_26_自动估价记录_查询_条件查询_未输入')
    # def testXJ_ZDGJ_26(self):
    #     result=QY.Query(self, self.el, u'关键字查询', u'', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_28_自动估价记录_查询_条件查询_物业名称')
    # def testXJ_ZDGJ_28(self):
    #     result=QY.Query(self, self.el, u'关键字查询', u'苹果园', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_27_自动估价记录_查询_条件查询_物业名称')
    # def testXJ_ZDGJ_27(self):
    #     result=QY.Query(self, self.el, u'关键字查询', u'苹果园双鱼座4层4G', Inquiry='Zidongxujia')
    #     self.assertTrue(result)
    # @LG.caseLog(u'XJ_ZDGJ_29_自动估价记录_查询_条件查询_输入字符')
    # def testXJ_ZDGJ_29(self):
    #     result=QY.Query(self, self.el, u'关键字查询', u'园', Inquiry='Zidongxujia')
    #     self.assertTrue(result)

if __name__=='__main__':
    unittest.main()