#-*- coding:utf-8 -*-
# import os
# import time
# import unittest
# import COMMON.LOG as LG
# from BaseCase.GJB import unittestBase
from BaseCase.GJB import reportQuery as rq
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
data =CM.get_xls('ReportZSBGquery','TCNO',unittestBase.dataFile)
argedata=[]
for i in data :
    for j in range(len(i)):
        if i[j]=='':
            i[j]=None
    argedata.append(i)

@ddt.ddt
class reportquerytest(unittestBase.unittestBase):
    """正式报告：查询"""
    @ddt.data(*argedata)
    @ddt.unpack
    def testcheck_query(self, testNo, description, sub, kwargs, tab, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, kwargs, tab, Inquiry, substate
        print sub, kwargs
        ldata = kwargs.split(',')
        for i in range(len(ldata)):
            ldata[i] = ldata[i].strip()
            if ldata[i].strip() == u'None':
                ldata[i] = None
        rt = rq.QueryCheck().check_query(self, self.el, tab, sub, *ldata)
        self.assertTrue(rt)
    '''
    #@LG.caseLog(u'GJB_ZSBG_CX_001_查询_项目城市省份')
    def testGJB_ZSBG_CX_001(self):
        """查询_项目城市省份"""
        rt=rq.QueryCheck().check_query(self, self.el, u'全部',u'正式报告',*[u'省份', u'广东省'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_002_查询_项目城市城市')
    def testGJB_ZSBG_CX_002(self):
        """查询_项目城市城市"""
        rt= rq.QueryCheck().check_query(self,self.el,u'全部',u'正式报告',*[u'省份',u'广东省深圳市南山区'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_003_查询_添加指定城市市区')
    def testGJB_ZSBG_CX_003(self):
        """查询_添加指定城市市区"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'省份', u'广东省深圳市'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_004_查询_分支机构')
    def testGJB_ZSBG_CX_004(self):
        """查询_分支机构"""
        rt=rq.QueryCheck().check_query(self, self.el,u'全部',u'正式报告', *[u'分支机构', u'房讯通'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_005_查询_部门')
    def testGJB_ZSBG_CX_005(self):
        """查询_部门"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'部门', u'房讯通 总经办'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_006_查询_报告类型')
    def testGJB_ZSBG_CX_006(self):
        """查询_报告类型"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告类型', u'房地产评估'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_007_查询_评估目的')
    def testGJB_ZSBG_CX_007(self):
        """查询_评估目的"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'评估目的', u'房地产评估 测试抵押估价'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_008_查询_报告状态【撰写中】')
    def testGJB_ZSBG_CX_008(self):
        """查询_报告状态【撰写中】"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告状态', u'撰写中'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_009_查询_报告状态【待撰写】')
    def testGJB_ZSBG_CX_009(self):
        """查询_报告状态【待撰写】"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告状态', u'待撰写'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_010_查询_报告状态【已完成】')
    def testGJB_ZSBG_CX_010(self):
        """查询_报告状态【已完成】"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告状态', u'已完成'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_011_查询_报告状态【待分配】')
    def testGJB_ZSBG_CX_011(self):
        """查询_报告状态【待分配】"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告状态', u'待分配'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_012_查询_报告状态【已作废】')
    def testGJB_ZSBG_CX_012(self):
        """查询_报告状态【已作废】"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告状态', u'已作废'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_013_查询_报告状态【已锁定】')
    def testGJB_ZSBG_CX_013(self):
        """查询_报告状态【已锁定】"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告状态', u'已锁定'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_014_查询_报告状态【审核中】')
    def testGJB_ZSBG_CX_014(self):
        """查询_报告状态【审核中】"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告状态', u'审核中'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_015_查询_委托客户')
    def testGJB_ZSBG_CX_015(self):
        """查询_委托客户"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'委托客户', u'包商银行'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_016_查询_委托客户【分行】')
    def testGJB_ZSBG_CX_016(self):
        """查询_委托客户【分行】"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'委托客户', u'包商银行 深圳南山分行'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_017_查询_委托客户【支行】')
    def testGJB_ZSBG_CX_017(self):
        """查询_委托客户【支行】"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'委托客户', u'包商银行 深圳南山分行 科技园支行'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_018_查询_撰写人')
    def testGJB_ZSBG_CX_018(self):
        """查询_撰写人"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'撰写人', u'tan1'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_019_查询_业务员')
    def testGJB_ZSBG_CX_019(self):
        """查询_业务员"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'业务员', u'tan1'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_020_查询_报告创建时间（开始时间）')
    def testGJB_ZSBG_CX_020(self):
        """查询_报告创建时间（开始时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告创建时间', u'2016-10-28'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_021_查询_报告创建时间（结束时间）')
    def testGJB_ZSBG_CX_021(self):
        """查询_报告创建时间（结束时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告创建时间', u':2016-10-28'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_022_查询_报告创建时间（开始-结束时间）')
    def testGJB_ZSBG_CX_022(self):
        """查询_报告创建时间（开始-结束时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告创建时间', u'2016-10-28:2016-10-30'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_023_查询_业务创建时间（开始时间）')
    def testGJB_ZSBG_CX_023(self):
        """查询_业务创建时间（开始时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'业务创建时间', u'2016-10-28'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_024_查询_业务创建时间（结束时间）')
    def testGJB_ZSBG_CX_024(self):
        """查询_业务创建时间（结束时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'业务创建时间', u':2016-10-28'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_025_查询_业务创建时间（开始-结束时间）')
    def testGJB_ZSBG_CX_025(self):
        """查询_业务创建时间（开始-结束时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'业务创建时间', u'2016-10-28:2016-10-30'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_026_查询_报告归档时间（开始时间）')
    def testGJB_ZSBG_CX_026(self):
        """查询_报告归档时间（开始时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告归档时间', u'2016-1-28'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_027_查询_报告归档时间（结束时间）')
    def testGJB_ZSBG_CX_027(self):
        """查询_报告归档时间（结束时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告归档时间', u':2016-10-28'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_028_查询_报告归档时间（开始-结束时间）')
    def testGJB_ZSBG_CX_028(self):
        """查询_报告归档时间（开始-结束时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告归档时间', u'2016-01-28:2016-10-30'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_029_查询_报告归档时间（开始时间）')
    def testGJB_ZSBG_CX_029(self):
        """查询_报告归档时间（开始时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告归档时间', u'2016-1-28'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_030_查询_报告归档时间（结束时间）')
    def testGJB_ZSBG_CX_030(self):
        """查询_报告归档时间（结束时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告归档时间', u':2016-10-28'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_031_查询_报告归档时间（开始-结束时间）')
    def testGJB_ZSBG_CX_031(self):
        """查询_报告归档时间（开始-结束时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'报告归档时间', u'2016-01-28:2016-10-30'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_032_查询_是否上报协会（是）')
    def testGJB_ZSBG_CX_032(self):
        """查询_是否上报协会（是）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'是否上报协会', u'是'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_033_查询_是否上报协会（否）')
    def testGJB_ZSBG_CX_033(self):
        """查询_是否上报协会（否）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'是否上报协会', u'否'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_034_查询_关键字搜索（业务编号）')
    def testGJB_ZSBG_CX_034(self):
        """查询_关键字搜索（业务编号）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'关键字查询', u'20161031006'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_035_查询_关键字搜索（报告编号）')
    def testGJB_ZSBG_CX_035(self):
        """查询_关键字搜索（报告编号）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'关键字查询', u'房讯通估字(G)(2016)第10081号'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_036_查询_关键字搜索（预评编号）')
    def testGJB_ZSBG_CX_036(self):
        """查询_关键字搜索（预评编号）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'关键字查询', u'预评测试201607190023'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_037_查询_关键字搜索（业务联系人）')
    def testGJB_ZSBG_CX_037(self):
        """查询_关键字搜索（业务联系人）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'关键字查询', u'lilm'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_038_查询_关键字搜索（委托方）')
    def testGJB_ZSBG_CX_038(self):
        """查询_关键字搜索（委托方）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'关键字查询', u'华夏基金'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_039_查询_关键字搜索（处理人）')
    def testGJB_ZSBG_CX_039(self):
        """查询_关键字搜索（处理人）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'关键字查询', u'tan1'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_040_查询_关键字搜索（业务联系人电话）')
    def testGJB_ZSBG_CX_040(self):
        """查询_关键字搜索（业务联系人电话）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'关键字查询', u'13200114422'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_041_查询_关键字搜索（项目名称）')
    def testGJB_ZSBG_CX_041(self):
        """查询_关键字搜索（项目名称）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'关键字查询', u'825报告测试A01'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_042_查询_关键字搜索（委托方联系电话）')
    def testGJB_ZSBG_CX_042(self):
        """查询_关键字搜索（委托方联系电话）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'全部', u'正式报告', *[u'关键字查询', u'0755-12345678'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_043_查询_提交审批时间（开始时间）')
    def testGJB_ZSBG_CX_043(self):
        """查询_提交审批时间（开始时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'待我审的', u'正式报告', *[u'提交审批时间', u'2016-1-28'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_044_查询_提交审批时间（结束时间）')
    def testGJB_ZSBG_CX_044(self):
        """查询_提交审批时间（结束时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'待我审的', u'正式报告', *[u'提交审批时间', u':2016-10-28'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_CX_045_查询_提交审批时间（开始-结束时间）')
    def testGJB_ZSBG_CX_045(self):
        """提交审批时间（开始-结束时间）"""
        rt = rq.QueryCheck().check_query(self, self.el, u'待我审的', u'正式报告', *[u'提交审批时间', u'2015-01-28:2016-10-30'])
        self.assertTrue(rt)
    '''
if __name__=='__main__':
    unittest.main()