#-*- coding:utf-8 -*-
# import os
# import time
# import unittest
import COMMON.LOG as LG
# from BaseCase.GJB import commond as cm
# from BaseCase.GJB import unittestBase
from BaseCase.GJB import reportModificaton as rm
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
data =CM.get_xls('ReportZSBGModification','TCNO',unittestBase.dataFile)
argedata=[]
for i in data :
    for j in range(len(i)):
        if i[j]=='':
            i[j]=None
    argedata.append(i)

@ddt.ddt
class reportModification(unittestBase.unittestBase):
    """正式报告：修改"""

    @ddt.data(*argedata)
    @ddt.unpack
    def testcheck_updateGeneral(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data, submode, Inquiry, substate
        ldata = data.split(',')
        for i in range(len(ldata)):
            ldata[i] = ldata[i].strip()
            if ldata[i].strip() == u'None':
                ldata[i] = None
        print ldata
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, sub, *ldata)
        self.assertTrue(rt)
    """
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_075_修改【报告信息】_编号类型')
    def testGJB_ZSBG_XG_QB_075(self):
        #修改【报告信息】_编号类型
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'编号类型',u'正常编号'])
        self.assertTrue(rt)

    #@LG.caseLog(u'GJB_ZSBG_XG_QB_048_修改【委托信息】_查勘员')
    def testGJB_ZSBG_XG_QB_048(self):
        #修改【委托信息】_查勘员
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'查勘员', 'tan1'])
        self.assertTrue(rt)

    #@LG.caseLog(u'GJB_ZSBG_XG_QB_067_修改【报告信息】_报告撰写辅助人')
    def testGJB_ZSBG_XG_QB_067(self):
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'报告撰写辅助人', 'tan1'])
        self.assertTrue(rt)

    #@LG.caseLog(u'GJB_ZSBG_XG_QB_001_修改【委托信息】_项目城市(城市)')
    def testGJB_ZSBG_XG_QB_001(self):
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'城市', u'北京直辖北京市'])
        self.assertTrue(rt)
    
    @LG.caseLog(u'GJB_ZSBG_XG_QB_081_修改【报告信息】_估价师')
    def testGJB_ZSBG_XG_QB_081(self):
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'估价师', 'tan1'])
        self.assertTrue(rt)
    
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_082_修改【报告信息】_多个估价师')
    def testGJB_ZSBG_XG_QB_082(self):
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'估价师', 'tan1, tan2'])
        self.assertTrue(rt)

    #@LG.caseLog(u'GJB_ZSBG_XG_QB_001_修改【委托信息】_分支机构')
    def testGJB_ZSBG_XG_QB_001(self):
        #修改【委托信息】_分支机构
        rt=rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'分支机构', u'深圳总部'])
        self.assertTrue(rt)
    """

    '''
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_002_修改【委托信息】_项目城市（省份）')
    def testGJB_ZSBG_XG_QB_002(self):
        """修改【委托信息】_项目城市（省份）"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'省份', u'北京直辖市'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_006_修改【委托信息】_业务部门')
    def testGJB_ZSBG_XG_QB_006(self):
        """修改【委托信息】_业务部门"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'业务部门',None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_007_修改【委托信息】_委托类型')
    def testGJB_ZSBG_XG_QB_007(self):
        """修改【委托信息】_委托类型"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'委托类型', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_008_修改【委托信息】_技术团队')
    def testGJB_ZSBG_XG_QB_008(self):
        """修改【委托信息】_技术团队"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'技术团队', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_009_修改【委托信息】_客户类型')
    def testGJB_ZSBG_XG_QB_009(self):
        """修改【委托信息】_客户类型"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'客户类型', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_010_修改【委托信息】_委托客户')
    def testGJB_ZSBG_XG_QB_010(self):
        """修改【委托信息】_委托客户"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'客户类型', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_012_修改【委托信息】_报告类型')
    def testGJB_ZSBG_XG_QB_012(self):
        """修改【委托信息】_报告类型"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'报告类型', None])
        self.assertTrue(rt)
    ###
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_014_修改【委托信息】_业务员')
    def testGJB_ZSBG_XG_QB_014(self):
        """修改【委托信息】_业务员"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'业务员', 'tan1'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_015_修改【委托信息】_业务跟进人')
    def testGJB_ZSBG_XG_QB_015(self):
        """修改【委托信息】_业务跟进人"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'业务跟进人', 'tan1'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_011_修改【委托信息】_客户全称')
    def testGJB_ZSBG_XG_QB_011(self):
        """修改【委托信息】_客户全称"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'客户全称', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_013_修改【委托信息】_评估目的')
    def testGJB_ZSBG_XG_QB_013(self):
        """修改【委托信息】_评估目的"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'评估目的', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_016_修改【委托信息】_项目名称')
    def testGJB_ZSBG_XG_QB_016(self):
        """修改【委托信息】_项目名称"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'项目名称', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_017_修改【委托信息】_业务员电话')
    def testGJB_ZSBG_XG_QB_017(self):
        """修改【委托信息】_业务员电话"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'业务员电话', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_018_修改【委托信息】_借款人是否为产权人')
    def testGJB_ZSBG_XG_QB_018(self):
        """修改【委托信息】_借款人是否为产权人"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'借款人是否为产权人', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_019_修改【委托信息】_业务联系人')
    def testGJB_ZSBG_XG_QB_019(self):
        """修改【委托信息】_业务联系人"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'业务联系人', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_020_修改【委托信息】_业务联系人电话')
    def testGJB_ZSBG_XG_QB_020(self):
        """修改【委托信息】_业务联系人电话"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'业务联系人电话', '13800000001'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_021_修改【委托信息】_委托方')
    def testGJB_ZSBG_XG_QB_021(self):
        """修改【委托信息】_委托方"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'业务联系人电话', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_022_修改【委托信息】_委托方联系电话')
    def testGJB_ZSBG_XG_QB_022(self):
        """修改【委托信息】_委托方联系电话"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'委托方联系电话', '13800000001'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_023_修改【委托信息】_估价对象位置')
    def testGJB_ZSBG_XG_QB_023(self):
        """修改【委托信息】_估价对象位置"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'估价对象位置', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_024_修改【委托信息】_中介公司')
    def testGJB_ZSBG_XG_QB_024(self):
        """修改【委托信息】_中介公司"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'中介公司', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_025_修改【委托信息】_中介经纪人')
    def testGJB_ZSBG_XG_QB_025(self):
        """修改【委托信息】_中介经纪人"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'中介经纪人', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_026_修改【委托信息】_委托合同编号')
    def testGJB_ZSBG_XG_QB_026(self):
        """修改【委托信息】_委托合同编号"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'委托合同编号', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_027_修改【委托信息】_委托人地址')
    def testGJB_ZSBG_XG_QB_027(self):
        """修改【委托信息】_委托人地址"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'委托人地址', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_028_修改【委托信息】_委托人身份证')
    def testGJB_ZSBG_XG_QB_028(self):
        """修改【委托信息】_委托人身份证"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'委托人身份证', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_029_修改【委托信息】_委托人法人代表')
    def testGJB_ZSBG_XG_QB_029(self):
        """修改【委托信息】_委托人法人代表"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'委托人法人代表', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_030_修改【委托信息】_收费类型')
    def testGJB_ZSBG_XG_QB_030(self):
        """修改【委托信息】_收费类型"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'收费类型', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_031_修改【委托信息】_报告投递方式')
    def testGJB_ZSBG_XG_QB_031(self):
        """修改【委托信息】_报告投递方式"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'报告投递方式', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_032_修改【委托信息】_是否月结')
    def testGJB_ZSBG_XG_QB_032(self):
        """修改【委托信息】_是否月结"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'是否月结', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_033_修改【委托信息】_银行申请状态')
    def testGJB_ZSBG_XG_QB_033(self):
        """修改【委托信息】_银行申请状态"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'银行申请状态', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_034_修改【委托信息】_报告子类型')
    def testGJB_ZSBG_XG_QB_034(self):
        """修改【委托信息】_报告子类型"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'报告子类型', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_035_修改【委托信息】_报告复印份数')
    def testGJB_ZSBG_XG_QB_035(self):
        """修改【委托信息】_报告复印份数"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'报告复印份数', '9'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_036_修改【委托信息】_业务员所属部门')
    def testGJB_ZSBG_XG_QB_036(self):
        """修改【委托信息】_业务员所属部门"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'业务员所属部门', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_037_修改【委托信息】_业务员所属部门负责人')
    def testGJB_ZSBG_XG_QB_037(self):
        """修改【委托信息】_业务员所属部门负责人"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'业务员所属部门负责人', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_038_修改【委托信息】_业务来源')
    def testGJB_ZSBG_XG_QB_038(self):
        """修改【委托信息】_业务来源"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'业务来源', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_039_修改【委托信息】_业务类型')
    def testGJB_ZSBG_XG_QB_039(self):
        """修改【委托信息】_业务类型"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'业务类型', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_040_修改【委托信息】_委托方与权利人关系')
    def testGJB_ZSBG_XG_QB_040(self):
        """修改【委托信息】_委托方与权利人关系"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'委托方与权利人关系', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_041_修改【委托信息】_委托人户籍')
    def testGJB_ZSBG_XG_QB_041(self):
        """修改【委托信息】_委托人户籍"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'委托人户籍', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_042_修改【委托信息】_按揭贷款是否有共同保证人')
    def testGJB_ZSBG_XG_QB_042(self):
        """修改【委托信息】_按揭贷款是否有共同保证人"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'按揭贷款是否有共同保证人', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_043_修改【委托信息】_委托方联系人')
    def testGJB_ZSBG_XG_QB_043(self):
        """修改【委托信息】_委托方联系人"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'委托方联系人', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_044_修改【委托信息】_备注')
    def testGJB_ZSBG_XG_QB_044(self):
        """修改【委托信息】_备注"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'备注', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_045_修改【委托信息】_查勘开始时间')
    def testGJB_ZSBG_XG_QB_045(self):
        """修改【委托信息】_查勘开始时间"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'查勘开始时间', '2016-10-24'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_046_修改【委托信息】_查勘结束时间')
    def testGJB_ZSBG_XG_QB_046(self):
        """修改【委托信息】_查勘结束时间"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'查勘结束时间', '2016-10-24'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_047_修改【委托信息】_查勘状态')
    def testGJB_ZSBG_XG_QB_047(self):
        """修改【委托信息】_查勘状态"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'查勘状态', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_049_修改【报告信息】_报告编号')#有些数据没有完成时间，需要检查完成时间
    def testGJB_ZSBG_XG_QB_049(self):
        """修改【报告信息】_报告编号"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'报告编号', time.strftime('%Y%m%d%H%M%S', time.localtime())])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_050_修改【报告信息】_评估总面积')
    def testGJB_ZSBG_XG_QB_050(self):
        """修改【报告信息】_评估总面积"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'评估总面积', '200'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_051_修改【报告信息】_是否上报协会')
    def testGJB_ZSBG_XG_QB_051(self):
        """修改【报告信息】_是否上报协会"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'是否上报协会', None])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_052_修改【报告信息】_评估总值')
    def testGJB_ZSBG_XG_QB_052(self):
        """修改【报告信息】_评估总值"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'评估总值', '200'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_054_修改【报告信息】_总税费')
    def testGJB_ZSBG_XG_QB_054(self):
        """修改【报告信息】_总税费"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'总税费', '200'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_055_修改【报告信息】_总净值')
    def testGJB_ZSBG_XG_QB_055(self):
        """修改【报告信息】_总净值"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'总净值', '200'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_057_修改【报告信息】_价值时点')
    def testGJB_ZSBG_XG_QB_057(self):
        """修改【报告信息】_价值时点"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'价值时点', '2016-10-25'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_058_修改【报告信息】_报告有效期开始')
    def testGJB_ZSBG_XG_QB_058(self):
        """修改【报告信息】_报告有效期开始"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'报告有效期开始', '2016-10-25'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_059_修改【报告信息】_报告有效期结束')
    def testGJB_ZSBG_XG_QB_059(self):
        """修改【报告信息】_报告有效期结束"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'报告有效期结束', '2016-10-25'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_060_修改【报告信息】_报告作业日期开始')
    def testGJB_ZSBG_XG_QB_060(self):
        """修改【报告信息】_报告作业日期开始"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'报告作业日期开始', '2016-10-25'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_061_修改【报告信息】_报告作业日期结束')
    def testGJB_ZSBG_XG_QB_061(self):
        """修改【报告信息】_报告作业日期结束"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'报告作业日期结束', time.strftime('%Y-%m-%d', time.localtime())])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_062_修改【报告信息】_完成时间')
    def testGJB_ZSBG_XG_QB_062(self):
        """修改【报告信息】_完成时间"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'完成时间', '2016-10-25'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_063_修改【报告信息】_应补地价总额')
    def testGJB_ZSBG_XG_QB_063(self):
        """修改【报告信息】_应补地价总额"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'应补地价总额', '200'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_064_修改【报告信息】_法定优先受偿款总额')
    def testGJB_ZSBG_XG_QB_064(self):
        """修改【报告信息】_法定优先受偿款总额"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'法定优先受偿款总额', '200'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_065_修改【报告信息】_其它估价人员')
    def testGJB_ZSBG_XG_QB_065(self):
        """修改【报告信息】_其它估价人员"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'其它估价人员', '200'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_066_修改【报告信息】_撰写人联系电话')
    def testGJB_ZSBG_XG_QB_066(self):
        """修改【报告信息】_撰写人联系电话"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'撰写人联系电话', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_068_修改【报告信息】_评估方法')
    def testGJB_ZSBG_XG_QB_068(self):
        """修改【报告信息】_评估方法"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'评估方法', u'比较法'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_069_修改【报告信息】_报告细分类型')
    def testGJB_ZSBG_XG_QB_069(self):
        """修改【报告信息】_报告细分类型"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'报告细分类型', 'autotestModification'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_070_修改【报告信息】_附属房屋评估总值')
    def testGJB_ZSBG_XG_QB_070(self):
        """修改【报告信息】_附属房屋评估总值"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'附属房屋评估总值', '100'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_071_修改【报告信息】_归档资料负责人')
    def testGJB_ZSBG_XG_QB_071(self):
        """修改【报告信息】_归档资料负责人"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'归档资料负责人', 'tan1'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_072_修改【报告信息】_土地评估总值')
    def testGJB_ZSBG_XG_QB_072(self):
        """修改【报告信息】_土地评估总值"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'土地评估总值', '200'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_073_修改【报告信息】_主房评估总值')
    def testGJB_ZSBG_XG_QB_073(self):
        """修改【报告信息】_主房评估总值"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'主房评估总值', '200'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_074_修改【报告信息】_打印日期')
    def testGJB_ZSBG_XG_QB_074(self):
        """修改【报告信息】_打印日期"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'打印日期', '2016-10-25'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_076_修改【报告信息】_土地总面积')
    def testGJB_ZSBG_XG_QB_076(self):
        """修改【报告信息】_土地总面积"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'土地总面积', '200'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_077_修改【报告信息】_打印份数')
    def testGJB_ZSBG_XG_QB_077(self):
        """修改【报告信息】_打印份数"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'打印份数', '9'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_078_修改【报告信息】_强制变现税费总额')
    def testGJB_ZSBG_XG_QB_078(self):
        """修改【报告信息】_强制变现税费总额"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'强制变现税费总额', '200'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_079_修改【报告信息】_强制变现值总额')
    def testGJB_ZSBG_XG_QB_079(self):
        """修改【报告信息】_强制变现值总额"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'强制变现值总额', '200'])
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_ZSBG_XG_QB_080_修改【报告信息】_备注')
    def testGJB_ZSBG_XG_QB_080(self):
        """修改【报告信息】_备注"""
        rt = rm.ModificationCheck().check_updateGeneral(self, self.el, u'正式报告', *[u'报告备注', 'autotestModification'])
        self.assertTrue(rt)
    '''
if __name__=='__main__':
    unittest.main()