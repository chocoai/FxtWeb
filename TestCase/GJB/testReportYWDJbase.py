#-*- coding:utf-8 -*-
# import unittest
# from BaseCase.GJB import unittestBase
from BaseCase.GJB import reportbase as rb
import os
import unittest
import ddt
import logging
import json

import COMMON.COMMON as CM
from BaseCase.GJB import query as QY
from COMMON import CONFIG as CFG
from BaseCase.GJB import unittestBase
# dataPath=os.path.join(CFG.prjDir,'BaseCase','GJB','data',unittestBase.testpath)
# dataFile=os.path.join(dataPath,'testData.xlsx')
data =CM.get_xls('ReportYWDJbase','TCNO',unittestBase.dataFile)
argedata=[]
for i in data :
    for j in range(len(i)):
        if i[j]=='':
            i[j]=None
    argedata.append(i)

checkTab=[]
checkcopyBtn=[]
checkdeleteBtn=[]
checkreassignBtn=[]
checkreportTilte=[]
checkimportData=[]
for i in argedata:
    if i[8]=='check_Tab':
        checkTab.append(i)
    elif i[8]=='check_copyBtn':
        checkcopyBtn.append(i)
    elif i[8]=='check_deleteBtn':
        checkdeleteBtn.append(i)
    elif i[8]=='check_reportTilte':
        checkreportTilte.append(i)
    elif i[8]=='check_importData':
        checkimportData.append(i)

@ddt.ddt
class reportBase(unittestBase.unittestBase):
    """业务登记：功能"""

    @ddt.data(*checkTab)
    @ddt.unpack
    def testcheck_Tab(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data, submode, Inquiry, substate
        print data
        rt = rb.reportTest().check_Tab(self, self.el, sub, submode)
        self.assertTrue(rt)

    @ddt.data(*checkreportTilte)
    @ddt.unpack
    def testcheck_reportTilte(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data, submode, Inquiry, substate
        print data
        rt = rb.reportTest().check_reportTilte(self, self.el, sub)
        self.assertTrue(rt)

    @ddt.data(*checkcopyBtn)
    @ddt.unpack
    def testcheck_copyBtn(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data, submode, Inquiry, substate
        print sub, data
        rt = rb.reportTest().check_copyBtn(self, self.el, sub, int(data))
        self.assertTrue(rt)

    @ddt.data(*checkdeleteBtn)
    @ddt.unpack
    def testcheck_deleteBtn(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data, submode, Inquiry, substate
        print sub, data
        rt = rb.reportTest().check_deleteBtn(self, self.el, sub, int(data))
        self.assertTrue(rt)

    @ddt.data(*checkimportData)
    @ddt.unpack
    def testcheck_importData(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data, submode, Inquiry, substate
        print sub, data
        rt = rb.reportTest().check_importData(self, self.el, sub, submode, data)
        self.assertTrue(rt)

    '''
    #@LG.caseLog(u'GJB_YWDJ_GN_001_业务登记')
    def testGJB_YWDJ_GN_001(self):
        """业务登记"""
        rt=rb.reportTest().check_reportTilte(self,self.el,u'业务登记')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_GN_002_Tab页【全部】')
    def testGJB_YWDJ_GN_002(self):
        """Tab页【全部】"""
        rt=rb.reportTest().check_Tab(self,self.el,u'业务登记',u'全部')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_GN_003_Tab页【我的业务】')
    def testGJB_YWDJ_GN_003(self):
        """Tab页【我的业务】"""
        rt=rb.reportTest().check_Tab(self,self.el,u'业务登记',u'我的业务')
        self.assertTrue(rt)
    #todo 微信个人业务需要权限
    #@LG.caseLog(u'GJB_YWDJ_GN_004_Tab页【微信个人业务】')
    #def testGJB_YWDJ_GN_004(self):
        #"""Tab页【微信个人业务】"""
        #rt = rb.reportTest().check_Tab(self, self.el, u'业务登记', u'微信个人业务')
        #self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_GN_005_复制新增【未选择数据】')
    def testGJB_YWDJ_GN_005(self):
        """复制新增【未选择数据】"""
        rt=rb.reportTest().check_copyBtn(self,self.el,u'业务登记',0)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_GN_006_复制新增【选择多条数据】')
    def testGJB_YWDJ_GN_006(self):
        """复制新增【选择多条数据】"""
        rt=rb.reportTest().check_copyBtn(self,self.el,u'业务登记',2)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_GN_007_复制新增【选择一条数据】')
    def testGJB_YWDJ_GN_007(self):
        """复制新增【一条数据】"""
        rt=rb.reportTest().check_copyBtn(self,self.el,u'业务登记',1)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_GN_008_删除【未选择数据】')
    def testGJB_YWDJ_GN_008(self):
        """删除【未选择数据】"""
        rt=rb.reportTest().check_deleteBtn(self,self.el,u'业务登记',0)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_GN_009_删除【一条数据】')
    def testGJB_YWDJ_GN_009(self):
        """删除【一条数据】"""
        rt=rb.reportTest().check_deleteBtn(self,self.el,u'业务登记',1)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_GN_010_删除【多条数据】')
    def testGJB_YWDJ_GN_010(self):
        """删除【多条数据】"""
        rt=rb.reportTest().check_deleteBtn(self,self.el,u'业务登记',2)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_GN_011_导出数据【导出一条数据】')
    def testGJB_YWDJ_GN_011(self):
        """导出数据【一条数据】"""
        rt = rb.reportTest().check_importData(self, self.el, u'业务登记',u'全部',1)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_GN_014_导出数据【删除模板】')
    def testGJB_YWDJ_GN_014(self):
        """导出数据【删除模板】"""
        rt = rb.reportTest().check_importData(self, self.el, u'业务登记', u'全部', 2)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_GN_013_导出数据【未选择数据】')
    def testGJB_YWDJ_GN_013(self):
        """导出数据【未选择数据】"""
        rt = rb.reportTest().check_importData(self, self.el, u'业务登记', u'全部',0)
        self.assertTrue(rt)
    # @LG.caseLog(u'GJB_YWDJ_GN_012_导出数据【建立模板导出】')
    def testGJB_YWDJ_GN_012(self):
        """导出数据【建立模板导出】"""
        rt = rb.reportTest().check_importData(self, self.el, u'业务登记', u'全部', 3)
        self.assertTrue(rt)
    '''
if __name__=='__main__':
    unittest.main()
