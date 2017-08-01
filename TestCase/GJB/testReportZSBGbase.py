#-*- coding:utf-8 -*-
# import os
# import time
# import unittest
# import COMMON.LOG as LG
# from BaseCase.GJB import commond as cm
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
data =CM.get_xls('ReportZSBGbase','TCNO',unittestBase.dataFile)
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
    """正式报告：功能"""

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

    @ddt.data(*checkreassignBtn)
    @ddt.unpack
    def testcheck_reassignBtn(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data, submode, Inquiry, substate
        print sub, data
        rt = rb.reportTest().check_reassignBtn(self, self.el, sub, submode, int(data))
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
    #@LG.caseLog(u'GJB_ZSBG_GN_001_正式报告')
    def testGJB_ZSBG_GN_001(self):
        """正式报告"""
        rt=rb.reportTest().check_reportTilte(self,self.el,u'正式报告')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_002_Tab页【全部】')
    def testGJB_ZSBG_GN_002(self):
        """Tab页【全部】"""
        rt=rb.reportTest().check_Tab(self,self.el,u'正式报告',u'全部')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_003_Tab页【我要撰写的】')
    def testGJB_ZSBG_GN_003(self):
        """Tab页【我要撰写的】"""
        rt=rb.reportTest().check_Tab(self,self.el,u'正式报告',u'我要撰写的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_004_Tab页【转交待我确认的】')
    def testGJB_ZSBG_GN_004(self):
        """Tab页【转交待我确认的】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'正式报告', u'转交待我确认的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_005_Tab页【已转交他人的】')
    def testGJB_ZSBG_GN_005(self):
        """Tab页【已转交他人的】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'正式报告', u'已转交他人的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_006_Tab页【待我分配的】')
    def testGJB_ZSBG_GN_006(self):
        """Tab页【待我分配的】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'正式报告', u'待我分配的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_007_Tab页【我已分配的】')
    def testGJB_ZSBG_GN_007(self):
        """Tab页【我已分配的】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'正式报告', u'我已分配的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_008_Tab页【我提审的】')
    def testGJB_ZSBG_GN_008(self):
        """Tab页【我提审的】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'正式报告', u'我提审的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_009_Tab页【待我审的】')
    def testGJB_ZSBG_GN_009(self):
        """Tab页【待我审的】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'正式报告', u'待我审的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_010_Tab页【我已审的】')
    def testGJB_ZSBG_GN_010(self):
        """Tab页【我已审的】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'正式报告', u'我已审的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_011_Tab页【我已完成的】')
    def testGJB_ZSBG_GN_011(self):
        """Tab页【我已完成的】"""
        rt = rb.reportTest().check_Tab(self, self.el, u'正式报告', u'我已完成的')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_012_复制新增【未选择数据】')
    def testGJB_ZSBG_GN_012(self):
        """复制新增【未选择数据】"""
        rt=rb.reportTest().check_copyBtn(self,self.el,u'正式报告',0)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_013_复制新增【选择多条数据】')
    def testGJB_ZSBG_GN_013(self):
        """复制新增【选择多条数据】"""
        rt=rb.reportTest().check_copyBtn(self,self.el,u'正式报告',2)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_014_复制新增【选择一条数据】')
    def testGJB_ZSBG_GN_014(self):
        """复制一条数据"""
        rt=rb.reportTest().check_copyBtn(self,self.el,u'正式报告',1)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_015_删除【未选择数据】')
    def testGJB_ZSBG_GN_015(self):
        """删除【未选择数据】"""
        rt=rb.reportTest().check_deleteBtn(self,self.el,u'正式报告',0)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_016_删除【选择一条数据】')
    def testGJB_ZSBG_GN_016(self):
        """删除【一条数据】"""
        rt=rb.reportTest().check_deleteBtn(self,self.el,u'正式报告',1)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_017_删除【选择多条数据】')
    def testGJB_ZSBG_GN_017(self):
        """删除【多条数据】"""
        rt=rb.reportTest().check_deleteBtn(self,self.el,u'正式报告',2)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_018_我要撰写的_转交【未选择数据】')
    def testGJB_ZSBG_GN_018(self):
        """我要撰写的_转交【未选择数据】"""
        rt = rb.reportTest().check_reassignBtn(self, self.el, u'正式报告',u'我要撰写的', 0)
        self.assertTrue(rt)

    #@LG.caseLog(u'GJB_ZSBG_GN_019_我要撰写的_转交【选择一条数据】')
    def testGJB_ZSBG_GN_019(self):
        """我要撰写的_转交【选择一条数据】"""
        rt = rb.reportTest().check_reassignBtn(self, self.el, u'正式报告',u'我要撰写的', 1)
        self.assertTrue(rt)

    #@LG.caseLog(u'GJB_ZSBG_GN_020_我要撰写的_转交【选择多条数据】')
    def testGJB_ZSBG_GN_020(self):
        """我要撰写的_转交【多条数据】"""
        rt=rb.reportTest().check_reassignBtn(self,self.el,u'正式报告',u'我要撰写的',2)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_021_我要撰写的_确定【未选择条数据】')
    def testGJB_ZSBG_GN_021(self):
        """我要撰写的_确定【未选择条数据】"""
        rt=rb.reportTest().check_OKBtn(self,self.el,u'正式报告',1)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_022_我要撰写的_确定【选择一条数据】')
    def testGJB_ZSBG_GN_022(self):
        """我要撰写的_确定【一条数据】"""
        rt = rb.reportTest().check_OKBtn(self, self.el, u'正式报告', 1)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_023_我要撰写的_确定【选择多条数据】')
    def testGJB_ZSBG_GN_023(self):
        """我要撰写的_确定【多条数据】"""
        rt = rb.reportTest().check_OKBtn(self, self.el, u'正式报告', 2)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_024_待我分配的_分配【未选择条数据】')
    def testGJB_ZSBG_GN_024(self):
        """待我分配的_分配【未选择条数据】"""
        rt = rb.reportTest().check_assignButton(self, self.el, u'正式报告', 0)
    #@LG.caseLog(u'GJB_ZSBG_GN_025_待我分配的_分配【选择一条数据】')
    def testGJB_ZSBG_GN_025(self):
        """待我分配的_分配【一条数据】"""
        rt = rb.reportTest().check_assignButton(self, self.el, u'正式报告', 1)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_026_待我分配的_分配【选择多条数据】')
    def testGJB_ZSBG_GN_026(self):
        """待我分配的_分配【选择多条数据】"""
        rt = rb.reportTest().check_assignButton(self, self.el, u'正式报告', 2)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_027_待我审的_转交【未选择条数据】')
    def testGJB_ZSBG_GN_027(self):
        """待我审的_转交【未选择条数据】"""
        rt = rb.reportTest().check_reassignBtn(self, self.el,u'正式报告',u'待我审的', 0)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_029_待我审的_转交【选择多条数据】')
    def testGJB_ZSBG_GN_029(self):
        """待我审的_转交【多条数据】"""
        rt = rb.reportTest().check_reassignBtn(self, self.el, u'正式报告', u'待我审的', 2)
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_GN_028_待我审的_转交【选择一条数据】')
    def testGJB_ZSBG_GN_028(self):
        """待我审的_转交【一条数据】"""
        rt = rb.reportTest().check_reassignBtn(self, self.el,u'正式报告',u'待我审的', 1)
        self.assertTrue(rt)
    '''
if __name__=='__main__':
    unittest.main()
