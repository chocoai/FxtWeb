# -*- coding: utf-8 -*-
import os
import unittest
import ddt
import logging
import xlrd
import paramunittest
import COMMON.DRIVER as DR
import COMMON.ELEMNET as EL
import COMMON.LOG as LG
import COMMON.COMMON as CM
from BaseCase.GJB import query as QY
from COMMON import CONFIG as CFG
from BaseCase.GJB import unittestBase
dataPath=os.path.join(CFG.prjDir,'BaseCase','GJB','data',unittestBase.testpath)
dataFile=os.path.join(dataPath,'testData.xlsx')
#downData=os.path.join(CFG.downloadDir,'0_2017-01-18.xls')
#data=xlrd.open_workbook(dataFile)
data =CM.get_xls('ArtificialQuery','TCNO',dataFile)
argedata=[]
for i in data :
    for j in range(len(i)):
        if i[j]=='':
            i[j]=None
    argedata.append(i)

@ddt.ddt
class ArtificialQuery(unittestBase.unittestBase):
    """人工询价-查询"""
    '''
    def setParameters(self,msgmode,data,submode,substate):
        self.msgmode=msgmode
        self.data=data
        self.submode=submode
        self.substate=substate
    def testMul(self):
        """aaaaa"""
        result=QY.Query(self,self.el,self.msgmode,self.data,self.submode,self.substate)
    '''
    @ddt.data(*argedata)
    @ddt.unpack
    def testArtificialQuery(self,testNo,description,msgmode,data,submode,Inquiry,substate,flag):
        if type(data)==float:
            data=str(int(data))
        logging.info(testNo+'_'+description)
        logging.info(u"参数为：%s,%s,%s,%s,%s"%(msgmode,data,submode,Inquiry,substate))
        print testNo,description,msgmode,data,submode,Inquiry,substate
        result=QY.Query(self,self.el,msgmode,data,submode,Inquiry,substate)
        self.assertTrue(result)
if __name__=="__main__":
    unittest.main()
