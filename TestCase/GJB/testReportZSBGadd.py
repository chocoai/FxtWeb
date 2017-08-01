#-*- coding:utf-8 -*-

from BaseCase.GJB import reportadd as ra
import unittest
import ddt
import logging
import json
import COMMON.COMMON as CM
from BaseCase.GJB import unittestBase
data =CM.get_xls('ReportZSBGadd','TCNO',unittestBase.dataFile)
argedata=[]
for i in data :
    for j in range(len(i)):
        if i[j]=='':
            i[j]=None
    argedata.append(i)
checkadd=[]
checkautoCalculate=[]
checkappraisers=[]
checkAtt=[]
checksubmitApproval=[]
checkuploadObject=[]
checkaddObject=[]
checkbutton=[]
checkroundColunm=[]

for i in argedata:
    if i[8]=='check_add':
        checkadd.append(i)
    elif i[8]=='check_autoCalculate':
        checkautoCalculate.append(i)
    elif i[8]=='check_appraisers':
        checkappraisers.append(i)
    elif i[8]=='check_Att':
        checkAtt.append(i)
    elif i[8]=='check_submitApproval':
        checksubmitApproval.append(i)
    elif i[8]=='check_uploadObject':
        checkuploadObject.append(i)
    elif i[8]=='check_addObject':
        checkaddObject.append(i)
    elif i[8]=='check_button':
        checkbutton.append(i)
    elif i[8]=='check_roundColumn':
        checkroundColunm.append(i)
@ddt.ddt
class reportAdd(unittestBase.unittestBase):
    """正式报告：新增"""

    @ddt.data(*checkroundColunm)
    @ddt.unpack
    def testcheck_roundColunm(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data
        print u'传入的参数：', data
        rt = ra.reportAddCheck().check_roundColumn(self, self.el, sub, **(json.loads(data.replace("'", '"'))))
        self.assertTrue(rt)

    @ddt.data(*checkadd)
    @ddt.unpack
    def testcheck_add(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data, submode, Inquiry, substate
        print data
        # print json.loads(data.replace("'",'"'))
        result = ra.reportAddCheck().check_add(self, self.el, sub, **(json.loads(data.replace("'", '"'))))
        self.assertTrue(result)

    @ddt.data(*checkautoCalculate)
    @ddt.unpack
    def testcheck_autoCalculate(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data
        tdata = data.split(',')
        print type(tdata[0])
        ldata = []
        for i in range(0, len(tdata)):
            ldata.append(json.loads(tdata[i].replace("'", '"').replace('u', '')))
        print u'传入的参数：', ldata
        result = ra.reportAddCheck().check_autoCalculate(self, self.el, ldata, sub)
        self.assertTrue(result)

    @ddt.data(*checkappraisers)
    @ddt.unpack
    def testcheck_appraisers(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data
        ldata = data.split(',')
        print u'传入的参数：', ldata
        result = ra.reportAddCheck().check_appraisers(self, self.el, ldata, sub)
        self.assertTrue(result)

    @ddt.data(*checkAtt)
    @ddt.unpack
    def testcheck_Att(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data
        print u'传入的参数：', sub
        result = ra.reportAddCheck().check_Att(self, self.el, sub)
        self.assertTrue(result)

    @ddt.data(*checksubmitApproval)
    @ddt.unpack
    def testcheck_submitApproval(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data
        print u'传入的参数：', sub
        rt = ra.reportAddCheck().check_submitApproval(self, self.el, sub)
        self.assertTrue(rt)

    @ddt.data(*checkuploadObject)
    @ddt.unpack
    def testcheck_uploadObject(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
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
        if data==None or data=='None':
            rt = ra.reportAddCheck().check_addObject(self, self.el, sub)
        else:
            rt = ra.reportAddCheck().check_addObject(self, self.el, sub, **(json.loads(data.replace("'", '"'))))
        self.assertTrue(rt)

    @ddt.data(*checkbutton)
    @ddt.unpack
    def testcheck_button(self, testNo, description, sub, data, submode, Inquiry, substate, flag, function):
        logging.info(testNo + '_' + description)
        print testNo, description, sub, data
        print u'传入的参数：', data
        rt = ra.reportAddCheck().check_button(self, self.el, data, sub)
        self.assertTrue(rt)

if __name__=='__main__':
    unittest.main()

