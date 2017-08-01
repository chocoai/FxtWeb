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
data =CM.get_xls('ReportYPBGbase','TCNO',unittestBase.dataFile)
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
    elif i[8]=='check_reassignBtn':
        checkreassignBtn.append(i)
    elif i[8]=='check_reportTilte':
        checkreportTilte.append(i)
    elif i[8]=='check_importData':
        checkimportData.append(i)

@ddt.ddt
class reportBase(unittestBase.unittestBase):
    """预评报告：功能"""

    @ddt.data(*checkTab)
    @ddt.unpack
    def testcheck_Tab(self,testNo,description,sub,data,submode,Inquiry,substate,flag,function):
        logging.info(testNo+'_'+description)
        print testNo,description,sub,data,submode,Inquiry,substate
        print data
        rt = rb.reportTest().check_Tab(self, self.el,sub, submode)
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
        print sub,data
        rt = rb.reportTest().check_copyBtn(self, self.el, sub,int(data))
        self.assertTrue(rt)

    @ddt.data(*checkdeleteBtn)
    @ddt.unpack
    def testcheck_deleteBtn(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data, submode, Inquiry, substate
        print sub, data
        rt = rb.reportTest().check_deleteBtn(self, self.el, sub, int(data))
        self.assertTrue(rt)

    @ddt.data(*checkreassignBtn)
    @ddt.unpack
    def testcheck_reassignBtn(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data, submode, Inquiry, substate
        print sub, data
        rt = rb.reportTest().check_reassignBtn(self, self.el, sub, submode,int(data))
        self.assertTrue(rt)

    @ddt.data(*checkimportData)
    @ddt.unpack
    def testcheck_importData(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data, submode, Inquiry, substate
        print sub, data
        rt = rb.reportTest().check_importData(self, self.el, sub, submode, int(data))
        self.assertTrue(rt)
    '''
    #@LG.caseLog(u'GJB_YPBG_GN_001_预评报告')
    def testGJB_YPBG_GN_001(self):
        """进入预评报告"""
        rt=rb.reportTest().check_reportTilte(self,self.el,u'预评报告')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_002_Tab页【全部】')
    def testGJB_YPBG_GN_002(self):
        """检查Tab页【全部】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'预评报告', u'全部')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_003_Tab页【我要撰写的】')
    def testGJB_YPBG_GN_003(self):
        """检查Tab页【我要撰写的】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'预评报告', u'我要撰写的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_004_Tab页【转交待我确认的】')
    def testGJB_YPBG_GN_004(self):
        """检查Tab页【转交待我确认的】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'预评报告', u'已转交他人的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_005_Tab页【我提审的】')
    def testGJB_YPBG_GN_005(self):
        """检查Tab页【我提审的】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'预评报告', u'我提审的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_006_Tab页【待我审的】')
    def testGJB_YPBG_GN_006(self):
        """检查Tab页【待我审的】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'预评报告', u'待我审的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_007_Tab页【我已审的】')
    def testGJB_YPBG_GN_007(self):
        """检查Tab页【我已审的】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'预评报告', u'我已审的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_008_Tab页【我已完成的】')
    def testGJB_YPBG_GN_008(self):
        """检查Tab页【我已完成的】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'预评报告', u'我已完成的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_009_复制新增【未选择数据】')
    def testGJB_YPBG_GN_009(self):
        """复制新增【未选择数据】"""
        rt = rb.reportTest().check_copyBtn(self, self.el, u'预评报告', 0)
        self.assertTrue(rt)
    
    #@LG.caseLog(u'GJB_YPBG_GN_010_复制新增【多条数据】')
    def testGJB_YPBG_GN_010(self):
        """复制新增【选择多条数据】"""
        rt = rb.reportTest().check_copyBtn(self, self.el, u'预评报告', 2)
        self.assertTrue(rt)
    
    #@LG.caseLog(u'GJB_YPBG_GN_011_复制新增【选择一条数据】')
    def testGJB_YPBG_GN_011(self):
        """复制新增【一条数据】"""
        rt = rb.reportTest().check_copyBtn(self, self.el, u'预评报告', 1)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_012_删除【未选择数据】')
    def testGJB_YPBG_GN_012(self):
        """删除【未选择数据】"""
        rt = rb.reportTest().check_deleteBtn(self, self.el, u'预评报告', 0)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_013_删除【选择一条数据】')
    def testGJB_YPBG_GN_013(self):
        """删除【一条数据】"""
        rt = rb.reportTest().check_deleteBtn(self, self.el, u'预评报告', 1)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_014_删除【选择多条数据】')
    def testGJB_YPBG_GN_014(self):
        """删除【选择多条数据】"""
        rt = rb.reportTest().check_deleteBtn(self, self.el, u'预评报告', 2)
        self.assertTrue(rt)
    
    #@LG.caseLog(u'GJB_YPBG_GN_015_我要撰写的_转交【未选择数据】')
    def testGJB_YPBG_GN_015(self):
        """我要撰写的_转交【未选择数据】"""
        rt = rb.reportTest().check_reassignBtn(self, self.el, u'预评报告', u'我要撰写的', 0)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_016_我要撰写的_转交【选择一条数据】')
    def testGJB_YPBG_GN_016(self):
        """我要撰写的_转交【一条数据】"""
        rt = rb.reportTest().check_reassignBtn(self, self.el, u'预评报告', u'我要撰写的', 1)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_017_我要撰写的_转交【选择多条数据】')
    def testGJB_YPBG_GN_017(self):
        """我要撰写的_转交【多条数据】"""
        rt = rb.reportTest().check_reassignBtn(self, self.el, u'预评报告', u'我要撰写的', 2)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_018_待我审的_转交【未选择条数据】')
    def testGJB_YPBG_GN_018(self):
        """待我审的_转交【未选择条数据】"""
        rt = rb.reportTest().check_reassignBtn(self, self.el, u'预评报告', u'待我审的', 0)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_019_待我审的_转交【选择一条数据】')
    def testGJB_YPBG_GN_019(self):
        """待我审的_转交【一条数据】"""
        rt = rb.reportTest().check_reassignBtn(self, self.el, u'预评报告', u'待我审的', 1)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_020_待我审的_转交【选择多条数据】')
    def testGJB_YPBG_GN_020(self):
        """待我审的_转交【多条数据】"""
        rt = rb.reportTest().check_reassignBtn(self, self.el, u'预评报告', u'待我审的', 2)
        self.assertTrue(rt)
    
    #@LG.caseLog(u'GJB_YPBG_GN_021_导出数据【一条数据】')
    def testGJB_YPBG_GN_021(self):
        """导出数据【一条数据】"""
        rt = rb.reportTest().check_importData(self, self.el, u'预评报告', u'全部', 1)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_022_导出数据【建立模板导出】')
    def testGJB_YPBG_GN_022(self):
        """导出数据【建立模板导出】"""
        rt = rb.reportTest().check_importData(self, self.el, u'预评报告', u'全部', 3)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_024_导出数据【删除模板】')
    def testGJB_YPBG_GN_024(self):
        """导出数据【删除模板】"""
        rt = rb.reportTest().check_importData(self, self.el, u'预评报告', u'全部', 2)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YPBG_GN_023_导出数据【未选择数据】')
    def testGJB_YPBG_GN_023(self):
        """导出数据【未选择数据】"""
        rt = rb.reportTest().check_importData(self, self.el, u'预评报告', u'全部', 0)
        self.assertTrue(rt)
    '''
if __name__=='__main__':
    unittest.main()
