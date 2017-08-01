# -*- coding:utf-8 -*-
# import os
# import time
# import unittest
# import COMMON.LOG as LG
# from BaseCase.GJB import unittestBase
from BaseCase.GJB import reportadd as ra
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
data =CM.get_xls('ReportYWDJadd','TCNO',unittestBase.dataFile)
argedata=[]
for i in data :
    for j in range(len(i)):
        if i[j]=='':
            i[j]=None
    argedata.append(i)

checkadd=[]
checkAtt=[]
checkuploadObject=[]
checkaddObject=[]
checkbutton=[]

for i in argedata:
    if i[8]=='check_add':
        checkadd.append(i)
    elif i[8]=='check_Att':
        checkAtt.append(i)
    elif i[8]=='check_uploadObject':
        checkuploadObject.append(i)
    elif i[8]=='check_addObject':
        checkaddObject.append(i)
    elif i[8]=='check_button':
        checkbutton.append(i)
@ddt.ddt
class reportAdd(unittestBase.unittestBase):
    """业务登记：新增"""
    @ddt.data(*checkadd)
    @ddt.unpack
    def testcheck_add(self,testNo,description,sub,data,submode,Inquiry,substate,flag,function):
        logging.info(testNo+'_'+description)
        print testNo,description,sub,data,submode,Inquiry,substate
        print data
        result=ra.reportAddCheck().check_add(self,self.el,sub,**(json.loads(data.replace("'",'"'))))
        self.assertTrue(result)

    @ddt.data(*checkuploadObject)
    @ddt.unpack
    def testcheck_uploadObject(self,testNo,description,sub,data,submode,Inquiry,substate,flag,function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data
        print u'传入的参数：', sub
        rt = ra.reportAddCheck().check_uploadObject(self, self.el, sub)
        self.assertTrue(rt)

    @ddt.data(*checkaddObject)
    @ddt.unpack
    def testcheck_addObject(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data
        print u'传入的参数：', sub, data
        rt = ra.reportAddCheck().check_addObject(self, self.el, sub, **(json.loads(data.replace("'", '"'))))
        self.assertTrue(rt)

    @ddt.data(*checkAtt)
    @ddt.unpack
    def testcheck_Att(self,testNo,description,sub,data,submode,Inquiry,substate,flag,function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data
        print u'传入的参数：', sub
        result = ra.reportAddCheck().check_Att(self, self.el, sub)
        self.assertTrue(result)



    @ddt.data(*checkbutton)
    @ddt.unpack
    def testcheck_button(self,testNo,description,sub,data,submode,Inquiry,substate,flag,function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data
        print u'传入的参数：', data
        rt = ra.reportAddCheck().check_button(self, self.el, data, sub)
        self.assertTrue(rt)

    """
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_051_新增【查勘信息】_查勘员')
    def testGJB_YWDJ_XZ_QB_051(self):
        #新增【查勘信息】_查勘员
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'查勘员': u'tan1'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_001_新增_分支机构')#影响必填项技术团队
    def testGJB_YWDJ_XZ_QB_066_001(self):
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'分支机构': u'房讯通'})
        self.assertTrue(rt)

    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_00x_新增_项目城市【省份】')#用例里没此项
    def testGJB_YWDJ_XZ_QB_002(self):
        rt= ra.reportAddCheck().check_add(self,self.el,sub=u'业务登记',**{u'省份':u'广东省'})
        self.assertTrue(rt)

    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_146_新增_附件生成')
    def testGJB_YWDJ_XZ_QB_146(self):
        '''新增_附件生成'''
        rt=ra.reportAddCheck().check_button(self,self.el,button=u'附件生成',sub=u'业务登记')
        self.assertTrue(rt)


    #怎么解决字典顺序问题
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_011_新增_委托客户【支行】')
    def testGJB_YWDJ_XZ_QB_011(self):
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'委托客户': u'B包商银行', u'委托客户分行': u'深圳南山分行',u'委托客户支行':u'科技园支行'})
        self.assertTrue(rt)
    """
    '''
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_002_新增【委托信息】_项目城市【城市】')
    def testGJB_YWDJ_XZ_QB_002(self):
        """新增【委托信息】_项目城市【城市】"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'省份': u'广东省', u'城市': u'深圳市'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_003_新增【委托信息】_项目城市【市区】')
    def testGJB_YWDJ_XZ_QB_003(self):
        """新增【委托信息】_项目城市【市区】"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'省份': u'广东省', u'城市': u'深圳市',u'区':u'南山区'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_004_新增【委托信息】_项目城市【片区】')
    def testGJB_YWDJ_XZ_QB_004(self):
        """新增【委托信息】_项目城市【片区】"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'省份': u'广东省', u'城市': u'深圳市', u'区': u'南山区',u'片区':u'大南山片区'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_005_新增【委托信息】_业务部门')
    def testGJB_YWDJ_XZ_QB_005(self):
        """新增【委托信息】_业务部门"""
        #rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'业务部门': u'技术部'})#09
        rt = ra.reportAddCheck().check_add(self, self.el, sub=u'业务登记', **{u'业务部门': u'总经办[房]'})#10
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_006_新增【委托信息】_委托类型')
    def testGJB_YWDJ_XZ_QB_006(self):
        """新增【委托信息】_委托类型"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'委托类型': u'个人'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_008_新增【委托信息】_客户类型')
    def testGJB_YWDJ_XZ_QB_008(self):
        """新增【委托信息】_客户类型"""
        """新增客户类型"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'客户类型': u'银行'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_009_新增【委托信息】_委托客户【银行】')
    def testGJB_YWDJ_XZ_QB_009(self):
        """新增【委托信息】_委托客户【银行】"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'委托客户': u'B包商银行'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_010_新增【委托信息】_委托客户【分行】')
    def testGJB_YWDJ_XZ_QB_010(self):
        """新增【委托信息】_委托客户【分行】"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'委托客户': u'B包商银行',u'委托客户分行':u'深圳南山分行'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_012_新增【委托信息】_客户全称')
    def testGJB_YWDJ_XZ_QB_012(self):
        """新增【委托信息】_客户全称"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'客户全称': u'自动化测试'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_013_新增【委托信息】_报告类型')
    def testGJB_YWDJ_XZ_QB_013(self):
        """新增【委托信息】_报告类型"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'报告类型': u'房地产评估'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_014_新增【委托信息】_评估目的')
    def testGJB_YWDJ_XZ_QB_014(self):
        """新增【委托信息】_评估目的"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'评估目的': u'测试抵押估价'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_016_新增【委托信息】_业务跟进人')
    def testGJB_YWDJ_XZ_QB_016(self):
        """新增【委托信息】_业务跟进人"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'业务跟进人': 'tan1'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_017_新增【委托信息】_项目名称')
    def testGJB_YWDJ_XZ_QB_017(self):
        """新增【委托信息】_项目名称"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'项目名称': u'自动化测试项目名称'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_018_新增【委托信息】_业务员电话')
    def testGJB_YWDJ_XZ_QB_018(self):
        """新增【委托信息】_业务员电话"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'业务员电话': u'13812345678'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_019_新增【委托信息】_借款人是否为产权人')
    def testGJB_YWDJ_XZ_QB_019(self):
        """新增【委托信息】_借款人是否为产权人"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'借款人是否为产权人': u'是'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_020_新增【委托信息】_业务联系人')
    def testGJB_YWDJ_XZ_QB_020(self):
        """新增【委托信息】_业务联系人"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'业务联系人': u'自动化测试业务联系人'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_021_新增【委托信息】_业务联系人电话')
    def testGJB_YWDJ_XZ_QB_021(self):
        """新增【委托信息】_业务联系人电话"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'业务联系人电话': u'13812345678'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_022_新增【委托信息】_委托方')
    def testGJB_YWDJ_XZ_QB_022(self):
        """新增【委托信息】_委托方"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'委托方': u'自动化测试委托方'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_023_新增【委托信息】_委托方联系电话')
    def testGJB_YWDJ_XZ_QB_023(self):
        """新增【委托信息】_委托方联系电话"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'委托方联系电话': u'13812345678'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_024_新增【委托信息】_估价对象位置')
    def testGJB_YWDJ_XZ_QB_024(self):
        """新增【委托信息】_估价对象位置"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'估价对象位置': u'自动化测试估价对象位置'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_025_新增【委托信息】_中介公司')
    def testGJB_YWDJ_XZ_QB_025(self):
        """新增【委托信息】_中介公司"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'中介公司': u'自动化测试中介公司'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_026_新增【委托信息】_中介经纪人')
    def testGJB_YWDJ_XZ_QB_026(self):
        """新增【委托信息】_中介经纪人"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'中介经纪人': u'自动化测试中介经纪人'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_027_新增【委托信息】_委托合同编号')
    def testGJB_YWDJ_XZ_QB_027(self):
        """新增【委托信息】_委托合同编号"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'委托合同编号': u'自动化测试委托合同编号'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_028_新增【委托信息】_要求出具报告时间')
    def testGJB_YWDJ_XZ_QB_028(self):
        """新增【委托信息】_要求出具报告时间"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'要求出具报告时间': u'2016-10-24'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_029_新增【委托信息】_委托人地址')
    def testGJB_YWDJ_XZ_QB_029(self):
        """新增【委托信息】_委托人地址"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'委托人地址': u'自动化测试委托人地址'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_030_新增【委托信息】_委托人身份证')
    def testGJB_YWDJ_XZ_QB_030(self):
        """新增【委托信息】_委托人身份证"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'委托人身份证': u'自动化测试委托人身份证'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_031_新增【委托信息】_委托人法人代表')
    def testGJB_YWDJ_XZ_QB_031(self):
        """新增【委托信息】_委托人法人代表"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'委托人法人代表': u'自动化测试委托人法人代表'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_032_新增【委托信息】_收费类型')
    def testGJB_YWDJ_XZ_QB_032(self):
        """新增【委托信息】_收费类型"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'收费类型': u'法院'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_033_新增【委托信息】_报告投递方式')
    def testGJB_YWDJ_XZ_QB_033(self):
        """新增【委托信息】_报告投递方式"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'报告投递方式': u'自取'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_034_新增【委托信息】_是否月结')
    def testGJB_YWDJ_XZ_QB_034(self):
        """新增【委托信息】_是否月结"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'是否月结': u'是'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_035_新增【委托信息】_银行申请状态')
    def testGJB_YWDJ_XZ_QB_035(self):
        """新增【委托信息】_银行申请状态"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'银行申请状态': u'申请前'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_037_新增【委托信息】_报告复印份数')
    def testGJB_YWDJ_XZ_QB_037(self):
        """新增【委托信息】_报告复印份数"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记'  ,**{u'报告复印份数': u'5'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_038_新增【委托信息】_业务员所属部门')
    def testGJB_YWDJ_XZ_QB_038(self):
        """新增【委托信息】_业务员所属部门"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'业务员所属部门': u'自动化测试业务员所属部门'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_039_新增【委托信息】_业务员所属部门负责人')
    def testGJB_YWDJ_XZ_QB_039(self):
        """新增【委托信息】_业务员所属部门负责人"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'业务员所属部门负责人': u'自动化测试业务员所属部门负责人'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_040_新增【委托信息】_备注')
    def testGJB_YWDJ_XZ_QB_040(self):
        """新增【委托信息】_备注"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'备注': u'自动化测试备注'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_041_新增【委托信息】_业务类型')
    def testGJB_YWDJ_XZ_QB_041(self):
        """新增【委托信息】_业务类型"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'业务类型': u'抵押'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_042_新增【委托信息】_业务来源')
    def testGJB_YWDJ_XZ_QB_042(self):
        """新增【委托信息】_业务来源"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'业务来源': u'自动化测试业务来源'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_043_新增【委托信息】_委托方与权利人关系')
    def testGJB_YWDJ_XZ_QB_043(self):
        """新增【委托信息】_委托方与权利人关系"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'委托方与权利人关系': u'本人'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_044_新增【委托信息】_委托人户籍')
    def testGJB_YWDJ_XZ_QB_044(self):
        """新增【委托信息】_委托人户籍"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'委托人户籍': u'本市'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_045_新增【委托信息】_按揭贷款是否有共同保证人')
    def testGJB_YWDJ_XZ_QB_045(self):
        """新增【委托信息】_按揭贷款是否有共同保证人"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'按揭贷款是否有共同保证人': u'是'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_046_新增【委托信息】_委托方联系人电话')
    def testGJB_YWDJ_XZ_QB_046(self):
        """新增【委托信息】_委托方联系人电话"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'委托方联系人电话': u'13812345678'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_047_新增【委托信息】_委托方联系人')
    def testGJB_YWDJ_XZ_QB_047(self):
        """新增【委托信息】_委托方联系人"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'委托方联系人电话': u'自动化测试委托方联系人'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_048_新增【查勘信息】_查勘开始时间')
    def testGJB_YWDJ_XZ_QB_048(self):
        """新增【查勘信息】_查勘开始时间"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'查勘开始时间': u'2016-10-24'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_049_新增【查勘信息】_查勘结束时间')
    def testGJB_YWDJ_XZ_QB_049(self):
        """新增【查勘信息】_查勘结束时间"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'查勘结束时间': u'2016-10-24'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_050_新增【查勘信息】_查勘状态')
    def testGJB_YWDJ_XZ_QB_050(self):
        """新增【查勘信息】_查勘状态"""
        rt = ra.reportAddCheck().check_add(self, self.el,sub=u'业务登记' ,**{u'查勘状态': u'待分配'})
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_052_新增【附件】_上传附件')
    def testGJB_YWDJ_XZ_QB_052(self):
        """新增【附件】_上传附件"""
        rt =ra.reportAddCheck().check_Att(self, self.el,u'业务登记')
        self.assertTrue(rt)
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_053_新增【委估对象】_导入委估对象')
    def testGJB_YWDJ_XZ_QB_053(self):
        """新增【委估对象】_导入委估对象"""
        rt = ra.reportAddCheck().check_uploadObject(self, self.el,sub=u'业务登记')
        self.assertTrue(rt)
    
    #@LG.caseLog(u'GJB_YWDJ_XZ_QB_054_145_新增【委估对象】_添加委估对象')
    def testGJB_YWDJ_XZ_QB_054_145(self):
        """新增【委估对象】_添加委估对象"""
        rt = ra.reportAddCheck().check_addObject(self, self.el,sub=u'业务登记',**{u"法定用途":u"商业",})
        self.assertTrue(rt)
    '''
if __name__ == '__main__':
    unittest.main()
    """
    path = os.getcwd()
    ut = unittest.TestSuite()
    sutest = unittest.defaultTestLoader.discover(path, pattern='testReportYWDJadd.py')
    # testsuite=ut.addTest(sutest)
    filename = "./myAppiumLog.html"  # 定义个报告存放路径，支持相对路径。
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告',
                                           description=u'估价宝询价模块')  # 使用HTMLTestRunner配置参数，输出报告路径、报告标题、描述
    runner.run(sutest)
    """
