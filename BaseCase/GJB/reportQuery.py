#-*- coding:utf-8 -*-
import os
from COMMON import COMMON as CN
import commond as cn
import config as cg
import COMMON.ELEMNET as EL
import logging
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
from time import sleep
import time
from reportbase import reportBase
import COMMON.CONFIG as CFG

elData=cg.elData
query=cg.reportQuery
DetailData=cg.reportDataDetail
User=cg.reportUser
reportFrame=cg.reportFrame
EntrustObject=cg.entrustObject
tabchk=cg.reportTabchk

class reportquery(reportBase):
    def query(self,func,el,sub,tab,*args):
        """
        通过不同的条件查询数据
        :param func:
        :param el:
        :param sub: 报告类型
        :param tab: tab页
        :param args:
        :return:
        """
        elementList = []
        self.reportTab(func,el,sub,tab)
        if args[0]!=u'提交审批时间':
            func.driver.find_element_by_id('aMoreSearch').click()
        #print args,len(args)
        data=args[1]
        el.getFunctionName(query[0])
        if args[0] == u'省份':
            if data == None:
                pass
            else:
                for i in [u'直辖市', u'省', u'特区', u'自治区']:
                    if i in data:
                        if u'直辖市' in data or u'特区' in data:
                            if u'直辖市' in data:
                                provinceKey = u'直辖市'
                                city = data.split(provinceKey)[0] + u'市'
                            else:
                                provinceKey = u'特区'
                                city = data.split(provinceKey)[0]
                            dataprList = data.split(provinceKey)
                            provincetext = data.split(provinceKey)[0] + provinceKey
                            el.get_element('province')
                            elementList.append('province')
                            provinceList = Select(el.get()).options
                            for i in range(len(provinceList)):
                                if provinceList[i].text.strip() == provincetext:
                                    value = provinceList[i].get_attribute('value')
                                    Select(el.get()).select_by_value(value)
                                    # index=provinceList.index(provinceList[i])
                                    # Select(el.get()).select_by_index(index)
                                    break

                            el.get_element('city')
                            elementList.append('city')
                            cityList = Select(el.get()).options
                            for i in range(len(cityList)):
                                if cityList[i].text.strip() == city:
                                    index = cityList.index(cityList[i])
                                    Select(el.get()).select_by_index(index)
                                    break

                            if len(dataprList) >= 2:
                                area = data.split(provinceKey)[1]
                                el.get_element('area')
                                elementList.append('area')
                                areaList = Select(el.get()).options
                                for i in range(len(areaList)):
                                    if areaList[i].text.strip() == area:
                                        index = areaList.index(areaList[i])
                                        Select(el.get()).select_by_index(index)
                                        break
                        else:
                            if u'省' in data:
                                provinceKey = u'省'
                            elif u'自治区' in data:
                                provinceKey = u'自治区'
                            else:
                                logging.error(u'数据格式不正确，请确认')
                                exit(u'数据格式不正确，请确认')
                            dataprList = data.split(provinceKey)

                            provincetext = dataprList[0] + provinceKey
                            el.get_element('province')
                            elementList.append('Province')
                            self.select_data(el, provincetext)

                            el.get_element('city')
                            if dataprList[1] != '':
                                elementList.append('city')
                                if u'市' in dataprList[1]:
                                    cityKey = u'市'
                                elif u'县' in dataprList[1]:
                                    cityKey = u'地区'
                                elif u'州' in dataprList[1]:
                                    cityKey = u'自治州'
                                elif u'盟' in dataprList[1]:
                                    cityKey = u'盟'

                                cityList = dataprList[1].split(cityKey, 1)
                                city = cityList[0] + cityKey
                                # el.get_element('city')
                                self.select_data(el, city)
                                if cityList[1] != '':
                                    area = cityList[1]
                                    el.get_element('area')
                                    self.select_data(el, area)
                                    time.sleep(5)
                                else:
                                    area = ''
                            else:
                                city = ''
                                resultText = []
                                cityOptions = Select(el.get()).options
                                for i in cityOptions:
                                    # print i.text
                                    resultText.append(i.text)

                        break
                else:
                    logging.info(u'请检查数据格式')
                    exit(u'请检查数据格式')
                if city == '':
                    pass
                    # resultText=''#待解决
                elif area == '':
                    resultText = city
                else:
                    resultText = city + '[' + area + ']'
        elif args[0] == u'分支机构' or args[0]==u'部门':
            if data != None:
                dataList = data.split()
                company = dataList[0]
                el.get_element('company')
                self.select_data(el, company)
                if len(dataList) > 1:
                    department = dataList[1]
                    elementList.append('department')
                    el.get_element('department')
                    self.select_data(el, department)
        elif args[0] == u'委估对象类型':
            elementList.append('xunjialeixing')
            el.get_element('valuationTypeMode')
            self.select_data(el, data)
        elif args[0] == u'来源':
            if data == u'默认':
                data = args[0]
            el.get_element('source')
            self.select_data(el, data)
        elif args[0] == u'委托客户' or args[0] == u'客户单位':
            dataList = data.split()
            entrustCorrespondent = dataList[0]
            el.get_element('entrustCorrespondent')
            elementList.append('bankid')
            self.select_data(el, entrustCorrespondent)
            if len(dataList) > 1:
                bankBranch = dataList[1]
                el.get_element('bankBranch')
                elementList.append('bankbranchid')
                self.select_data(el, bankBranch)
                time.sleep(1)
            if len(dataList) > 2:
                bankSubbranch = dataList[2]
                el.get_element('bankSubbranch')
                elementList.append('banksubbranchid')
                self.select_data(el, bankSubbranch)
        elif args[0] == u'状态':
            el.get_element('state')
            self.select_data(el, data)
        elif args[0] == u'查勘状态':
            surveystate = data
            xpath = 'td[15]/div'
            el.get_element('surveystate')
            self.select_data(el, surveystate)
        elif args[0] == u'报告创建时间' or args[0] == u'业务创建时间'or args[0]==u'创建时间'or args[0] == u'盖章完成时间':

            if args[0]==u'业务创建时间':
                el.get_element('chuangjianshijian')
                self.select_data(el, u'业务创建时间')
            elif args[0]==u'盖章完成时间':
                Sdriver = Select(func.driver.find_element_by_id('selcompletedatetype'))
                for i in range(len(Sdriver.options)):
                    #print Sdriver.options[i].text
                    if Sdriver.options[i].text == u'盖章完成时间':
                        logging.info(Sdriver.options[i].text)
                        Sdriver.select_by_index(i)
                        break
                else:
                    logging.info('not found options')
            else:
               pass

            if '-' in data:
                dataList = data.split(':')
                begintime = dataList[0]
            else:
                dataList = []
                begintime = ''
            el.get_element('beginData')
            # self.driver.execute_script(
            # "var setDate=document.getElementById(\""+el.path+"\");setDate.removeAttribute('readonly');")
            # print el.path
            if args[0]== u'盖章完成时间':
                #func.driver.execute_script("var setDate=document.getElementById('txtcompletedateBegin');setDate.removeAttribute('readonly');")
                func.driver.execute_script(
                    "var setDate=function $(id){ return document.getElementById(id); };setDate('txtcompletedateBegin').removeAttribute('readonly');")

                if begintime != '':
                    # print begintime
                    #el.get().send_keys(begintime)
                    func.driver.find_element_by_id('txtcompletedateBegin').send_keys(begintime)
                #el.get_element('endData')
                func.driver.execute_script(
                    "var setDate=document.getElementById('txtcompletedateEnd');setDate.removeAttribute('readonly');")
                if len(dataList) > 1:
                    endtime = dataList[1]
                    func.driver.find_element_by_id('txtcompletedateEnd').send_keys(endtime)
            else:
                func.driver.execute_script(
                    "var setDate=document.getElementById(\"" + el.path + "\");setDate.removeAttribute('readonly');")
                func.driver.execute_script(
                    "var setDate=function $(id){ return document.getElementById(id); };setDate(\"" + el.path + "\").removeAttribute('readonly');")

                if begintime != '':
                    el.get().clear()
                    el.get().send_keys(begintime)
                el.get_element('endData')
                func.driver.execute_script(
                    "var setDate=document.getElementById(\"" + el.path + "\");setDate.removeAttribute('readonly');")
                if len(dataList) > 1:
                    endtime = dataList[1]
                    el.get().clear()
                    el.get().send_keys(endtime)
        elif args[0] == u'报告归档时间' or args[0] == u'报告收费时间':
            if '-' in data:
                dataList = data.split(':')
                begintime = dataList[0]
            else:
                dataList = []
                begintime = ''

            if args[0]==u'报告归档时间':
                el.get_element('BackupBeginDate')
            else:
                el.get_element('FeeBeginDate')



            func.driver.execute_script(
                "var setDate=document.getElementById(\"" + el.path + "\");setDate.removeAttribute('readonly');")
            func.driver.execute_script(
                "var setDate=function $(id){ return document.getElementById(id); };setDate(\"" + el.path + "\").removeAttribute('readonly');")

            if begintime != '':
                el.get().send_keys(begintime)

            if args[0]==u'报告归档时间':
                el.get_element('BackupEndDate')
            else:
                el.get_element('FeeEndDate')
            func.driver.execute_script(
                "var setDate=document.getElementById(\"" + el.path + "\");setDate.removeAttribute('readonly');")
            if len(dataList) > 1:
                endtime = dataList[1]
                el.get().send_keys(endtime)
        elif args[0] == u'面积':
            dataList = data.split('-')
            minArea = dataList[0]
            if minArea != '':
                el.get_element('minArea')
                el.get().clear()
                el.get().send_keys(minArea)
            if len(dataList) > 1:
                maxArea = dataList[1]
                el.get_element('maxArea')
                el.get().click()
                el.get().send_keys(maxArea)
        elif args[0] == u'关键字查询':
            el.get_element('fuzzyQuery')
            el.get().clear()
            el.get().send_keys(data)
        elif args[0]==u'提交审批时间':
            dataList = data.split(':')

            begintime = dataList[0]
            time.sleep(1)
            el.get_element('submitBeginData')

            # Chrome浏览器无法执行下面的代码与js
            # self.driver.find_element_by_xpath('//*[@id="txtQueryBeginDate"]')
            func.driver.execute_script(
                "var setDate=document.getElementById(\"" + el.path + "\");setDate.removeAttribute('readonly');")
            el.get().clear()
            if begintime != '':
                el.get().send_keys(begintime)

            el.get_element('submitEndData')
            func.driver.execute_script(
                "var setDate=document.getElementById(\"" + el.path + "\");setDate.removeAttribute('readonly');")

            el.get().clear()
            if len(dataList) > 1:
                endtime = dataList[1]
                el.get().send_keys(endtime)
        elif args[0] == u'询价单类型':
            elementList.append('xujiadanleixing')
            el.get_element('xujiadanleixing')
            self.select_data(el, data)
        elif args[0] == u'物业类型':
            elementList.append('wuyeleixing')
            el.get_element('wuyeleixing')
            self.select_data(el, data)
        elif args[0]==u'报告类型' or args[0]==u'评估目的':
            if data != None:
                dataList = data.split()
                ReportType = dataList[0]
                el.get_element('ReportType')
                self.select_data(el, ReportType)
                if len(dataList) > 1:
                    Assesstype = dataList[1]
                    el.get_element('Assesstype')
                    self.select_data(el, Assesstype)
                    logging.info(args[0])
        elif args[0]==u'报告状态':
            if args[0]==u'':
                elementList.append('tbFollowUP')
            if data != None:
                dataList = data.split()
                reportstate = dataList[0]
                el.get_element('statetype')
                self.select_data(el, reportstate)
            else:
                logging.info('not selected options!')
        elif args[0]==u'撰写人' or args[0]==u'业务员':
            if args[0]==u'撰写人':
                el.get_element('SelectAppsUser')
            else:
                if sub==u'业务登记':
                    el.get_element('YWDJselectBusinessUser')
                else:
                    el.get_element('SelectBusinessUser')
            el.get().click()
            self.choices_Quser(func,el,data)
            self.mswitchfrname(func,el,sub)
        elif args[0]==u'是否上报协会':
            el.get_element('reportedresults')
            self.select_data(el, data)
        elif args[0]==u'业务报告类型' or args[0]==u'业务评估目的':
            if data != None:
                dataList = data.split()
                ReportType = dataList[0]
                el.get_element('selReporttypecode')
                self.select_data(el, ReportType)
                if len(dataList) > 1:
                    Assesstype = dataList[1]
                    el.get_element('selAssesstype')
                    self.select_data(el, Assesstype)
                    logging.info(args[0])
        elif args[0]==u'业务报告状态':
            if data != None:
                dataList = data.split()
                reportstate = dataList[0]
                el.get_element('selBusinessStage')
                self.select_data(el, reportstate)
            else:
                logging.info('not selected options!')
        elif args[0]==u'登记人':
            DSdirver=Select(func.driver.find_element_by_id('selCreateUserId'))
            for i in range(len(DSdirver.options)):
                if DSdirver.options[i].text==data:
                    DSdirver.select_by_index(i)
                    break
            else:
                logging.info('not found selCreateUser!')
                exit()
        else:
            logging.error(u'请检查询的字段是否正确!')
            exit(u'请检查询的字段是否正确')

        func.driver.find_element_by_id('btnsearch').click()
        time.sleep(3)
        if args[0] == u'省份':
            el.getFunctionName(elData[0])
            el.get_element(elData[1])
            # for i in range(len(el.gets())):
            time.sleep(1)
            el.getDriver().implicitly_wait(1)
            try:
                lnGets = len(el.gets()) - 1
            except:
                el.get_element('tabNotice')
                logging.info(el.get().text)
                return True
            rd = random.randint(0, lnGets)
            logging.info(u'第' + str(rd + 1) + u'条')
            dId = el.gets()[rd].find_element_by_xpath('td[2]/div').text
            logging.info(u'业务编号：' + dId)
            ActionChains(func.driver).double_click(el.gets()[rd].find_element_by_xpath('td[2]/div')).perform()
            return self.getDetail(func,el,data,DetailData,elementList)
        elif args[0] == u'分支机构' or args[0]==u'部门':

            if args[0]==u'分支机构':
                if sub==u'正式报告':
                    xpath = 'td[8]/div'
                #elif sub==u'预评报告':
                else:
                    xpath='td[6]/div'
                result = self.getAssignData(el, data, xpath)
                return result

            else:
                el.getFunctionName(elData[0])
                el.get_element('checkbox')
                el.getDriver().implicitly_wait(1)
                try:
                    logging.info(u'共' + str(len(el.gets())) + u'条数据')
                    rd = random.randint(0, len(el.gets()) - 1)
                except:
                    el.get_element('tabNotice')
                    logging.info(el.get().text)
                    return True

                logging.info(u'第' + str(rd + 1) + u'条数据')
                dId = el.gets()[rd].find_element_by_xpath('td[3]/div').text
                logging.info(u'业务编号：'+dId)
                ActionChains(func.driver).double_click(el.gets()[rd].find_element_by_xpath('td[3]/div')).perform()
                result = self.getDetail(func,el,department ,DetailData,elementList)
                return  result
        elif args[0] == u'委估对象类型':
            el.getFunctionName(elData[0])
            el.get_element(elData[1])
            # for i in range(len(el.gets())):
            time.sleep(1)
            el.getDriver().implicitly_wait(1)
            try:
                lnGets = len(el.gets()) - 1
            except:
                el.get_element('tabNotice')
                logging.info(el.get().text)
                return True
            rd = random.randint(0, lnGets)
            logging.info(u'第' + str(rd + 1) + u'条')
            dId = el.gets()[rd].find_element_by_xpath('td[3]/div').text
            dLink = el.gets()[rd].find_element_by_xpath('td[8]/div').text
            logging.info(u'询价编号：' + dId)
            ActionChains(func.driver).double_click(el.gets()[rd].find_element_by_xpath('td[3]/div')).perform()
            result = self.getDetail(func, el, data, query, elementList)
            return result
        elif args[0] == u'委托客户' or args[0] == u'客户单位':
            if sub==u'正式报告':
                xpath='td[16]/div'
            elif sub==u'预评报告':
                xpath='td[13]/div'
            else:
                xpath='td[7]/div'
            valuationText = ''.join(data)
            result = self.getAssignData(el, valuationText, xpath)

            """
            el.getFunctionName(elData[0])
            el.get_element('checkbox')
            el.getDriver().implicitly_wait(1)
            try:
                logging.info(u'共' + str(len(el.gets())) + u'条数据')
                rd = random.randint(0, len(el.gets()) - 1)
            except:
                el.get_element('tabNotice')
                logging.info(el.get().text)
                return True

            logging.info(u'第' + str(rd + 1) + u'条数据')
            dId = el.gets()[rd].find_element_by_xpath('td[2]/div').text
            logging.info(u'业务编号：' + dId)
            ActionChains(func.driver).double_click(el.gets()[rd].find_element_by_xpath('td[2]/div')).perform()
            result = self.getDetail(func, el, valuationText, DetailData, elementList)
            """
            return result
        elif args[0] == u'状态':
            elementList.append('xunjiazhuantai')
            el.getFunctionName(elData[0])
            el.get_element(elData[1])
            time.sleep(1)
            el.getDriver().implicitly_wait(1)
            try:
                lnGets = len(el.gets()) - 1
            except:
                el.get_element('tabNotice')
                logging.info(el.get().text)
                return True
            rd = random.randint(0, lnGets)
            logging.info(u'第' + str(rd + 1) + u'条')
            dId = el.gets()[rd].find_element_by_xpath('td[3]/div').text
            dLink = el.gets()[rd].find_element_by_xpath('td[7]/div').text
            logging.info(u'询价编号：' + dId)
            ActionChains(self.driver).double_click(el.gets()[rd].find_element_by_xpath('td[3]/div')).perform()
            result = self.getDetail(self, el, data, query, elementList)
            return result
        elif args[0] == u'查勘状态':
            result = self.getAssignData(el, data, xpath)
            return result
        elif args[0] == u'报告创建时间' or args[0] == u'业务创建时间'or args[0]==u'创建时间':

            # xpath='td[22]/div'#这是估价时间，不是询价时间
            elementList.append('chuangjianshijian')
            el.getFunctionName(elData[0])
            el.get_element('checkbox')
            el.getDriver().implicitly_wait(1)
            if data == u'清空':
                if len(el.gets()) > 0:
                    return True
                else:
                    try:
                        el.getDriver().implicitly_wait(1)
                        el.get_element('tabNotice')
                        logging.info(el.get().text)
                        return True
                    except:
                        logging.error(u'出错！')
                        return False
            try:
                # for i in range(len(el.gets())):
                rd = random.randint(0, len(el.gets()) - 1)
            except:
                el.get_element('tabNotice')
                logging.info(el.get().text)
                return True
            logging.info(u'第' + str(rd + 1) + u'条数据')
            idtxt=el.gets()[rd].find_element_by_xpath('td[2]/div').text
            logging.info(u'业务编号：'+idtxt )
            time.sleep(1)
            ActionChains(func.driver).double_click(el.gets()[rd].find_element_by_xpath('td[2]/div')).perform()
            result = self.getDetail(func, el, dataList, EntrustObject, elementList)
            return result

            #result = self.getAssignData(el, dataList, xpath)
            # result
        elif args[0] == u'报告归档时间' or args[0] == u'报告收费时间':
            # xpath='td[22]/div'#这是估价时间，不是询价时间
            #elementList.append('chuangjianshijian')
            el.getFunctionName(elData[0])
            el.get_element('checkbox')
            el.getDriver().implicitly_wait(1)
            if data == u'清空':
                if len(el.gets()) > 0:
                    return True
                else:
                    try:
                        el.getDriver().implicitly_wait(1)
                        el.get_element('tabNotice')
                        logging.info(el.get().text)
                        return True
                    except:
                        logging.error(u'出错！')
                        return False
            try:
                # for i in range(len(el.gets())):
                rd = random.randint(0, len(el.gets()) - 1)
            except:
                el.get_element('tabNotice')
                logging.info(el.get().text)
                return True
            return True
        elif args[0] == u'面积':
            result = self.getAssignData(el, dataList, xpath)
            return result
        elif args[0] == u'关键字查询':
            result = self.showAllData(el, data)
            return result
        elif args[0]==u'提交审批时间':
            xpath = 'td[11]/div'
            result = self.getAssignData(el, dataList, xpath)
            return result
        elif args[0] == u'询价单类型':
            if data == u'询价单类型':
                data = [u'自动询价', u'人工询价']
            xpath = 'td[2]/div'
            result = self.getAssignData(el, data, xpath)
            return result
        elif args[0] == u'物业类型':
            xpath = 'td[5]/div'
            if data == u'物业类型':
                data = [u'住宅', u'办公', u'商业', u'工业', u'土地', u'资产', u'其他']

            result = self.getAssignData(el, data, xpath)
            return result
        elif args[0] == u'报告类型'or args[0]==u'评估目的':
            if args[0]==u'报告类型':
                if sub==u'正式报告':
                    xpath='td[9]/div'
                elif sub==u'预评报告':
                    xpath='td[7]/div'
                rdata=data
            else:
                rdata=Assesstype
                if sub == u'正式报告':
                    xpath='td[10]/div'
                elif sub==u'预评报告':
                    xpath='td[8]/div'
            result=self.getAssignData(el,rdata,xpath)
            return result
        elif args[0]==u'报告状态':
            if sub==u'正式报告':
                xpath='td[14]/div'
                if data==u'撰写中' or data==u'待撰写':
                    rdata=[data,u'已转交，待确认']
                    result=self.getAssignData(el,rdata,xpath)
                elif data==u'审核中':
                    elementList.append('lbReportStateName')
                    el.getFunctionName(elData[0])
                    el.get_element('checkbox')
                    el.getDriver().implicitly_wait(1)
                    try:
                        logging.info(u'共' + str(len(el.gets())) + u'条数据')
                        rd = random.randint(0, len(el.gets()) - 1)
                    except:
                        el.get_element('tabNotice')
                        logging.info(el.get().text)
                        return True

                    logging.info(u'第' + str(rd + 1) + u'条数据')
                    dId = el.gets()[rd].find_element_by_xpath('td[2]/div').text
                    logging.info(u'业务编号：' + dId)
                    ActionChains(func.driver).double_click(el.gets()[rd].find_element_by_xpath('td[2]/div')).perform()
                    result = self.getDetail(func, el, data, DetailData, elementList)
                else:
                    result=self.getAssignData(el,data,xpath)
            #elif sub == u'预评报告':
            else:
                elementList.append('lbStateName')
                el.getFunctionName(elData[0])
                el.get_element('checkbox')
                el.getDriver().implicitly_wait(1)
                try:
                    # for i in range(len(el.gets())):
                    rd = random.randint(0, len(el.gets()) - 1)
                except:
                    el.get_element('tabNotice')
                    logging.info(el.get().text)
                    return True

                logging.info(u'第' + str(rd + 1) + u'条数据')
                idnum=el.gets()[rd].find_element_by_xpath('td[2]/div').text
                logging.info(u'业务编号：'+idnum)
                time.sleep(1)
                ActionChains(func.driver).double_click(el.gets()[rd].find_element_by_xpath('td[2]/div')).perform()
                result =self.getDetail(func,el,args[1],query,elementList)
                sleep(2)
            print result
            return result
        elif args[0] == u'撰写人' or args[0] == u'业务员':
            if sub==u'正式报告':
                if args[0]==u'撰写人':
                    xpath='td[12]/div'
                else:
                    xpath='td[11]/div'
            elif sub==u'业务登记':
                if args[0]==u'撰写人':
                    xpath='td[12]/div'
                else:
                    xpath='td[10]/div'
            else:
                if args[0]==u'撰写人':
                    xpath='td[10]/div'
                else:
                    xpath='td[9]/div'
            return  self.getAssignData(el,data,xpath)
        elif args[0] == u'是否上报协会':
            elementList.append('reportedresults')
            el.getFunctionName(elData[0])
            el.get_element(elData[1])
            time.sleep(1)
            el.getDriver().implicitly_wait(1)
            try:
                lnGets = len(el.gets()) - 1
            except:
                el.get_element('tabNotice')
                logging.info(el.get().text)
                return True
            rd = random.randint(0, lnGets)
            logging.info(u'第' + str(rd + 1) + u'条')
            dId = el.gets()[rd].find_element_by_xpath('td[2]/div').text
            logging.info(u'业务编号：' + dId)
            ActionChains(func.driver).double_click(el.gets()[rd].find_element_by_xpath('td[2]/div')).perform()
            result = self.getDetail(func, el, data, DetailData, elementList)
            return result
        elif args[0]==u'业务报告类型'or args[0]==u'业务评估目的':
            if args[0]==u'业务报告类型':
                elementList.append('reporttypecode')
            else:
                elementList.append('assesstype')
            el.getFunctionName(elData[0])
            el.get_element(elData[1])
            time.sleep(1)
            el.getDriver().implicitly_wait(1)
            try:
                lnGets = len(el.gets()) - 1
            except:
                el.get_element('tabNotice')
                logging.info(el.get().text)
                return True
            rd = random.randint(0, lnGets)
            logging.info(u'第' + str(rd + 1) + u'条')
            dId = el.gets()[rd].find_element_by_xpath('td[2]/div').text
            logging.info(u'业务编号：' + dId)
            ActionChains(func.driver).double_click(el.gets()[rd].find_element_by_xpath('td[2]/div')).perform()
            result = self.getDetail(func, el, data, DetailData, elementList)
            return result
        elif args[0]==u'业务报告状态':
            if args[1]==u'已出预评':
                xpath = 'td[12]/div'
            else:
                xpath = 'td[13]/div'

            time.sleep(1)
            el.getFunctionName(elData[0])
            el.get_element(elData[1])
            el.getDriver().implicitly_wait(1)
            #result = self.getAssignData(el,data, xpath)
            result=self.judgeTableData(el,u'否',xpath)
            return result
        elif args[0]==u'盖章完成时间':
           xpath='td[25]/div'
           result = self.judgedatetime(el,data, xpath)
           return result
        elif args[0]==u'登记人':
            xpath='td[22]/div'
            rt=self.getAssignData(el,data,xpath)
            return rt
        else:
            logging.error(u'请检查询的字段是否正确!')
            exit(u'请检查询的字段是否正确')
    def select_data(self, el, Detailstr):
        """
        选择查询条件的数据项
        :param el:
        :param Detailstr:
        :return:
        """
        time.sleep(5)
        dataList = Select(el.get()).options
        for i in range(len(dataList)):
            #print dataList[i].text,Detailstr.strip(), type(dataList[i].text.strip()) ,type(Detailstr.strip())
            if Detailstr.strip() in dataList[i].text.strip():
                index=dataList.index(dataList[i])
                Select(el.get()).select_by_index(index)
                break
        else:
            logging.error(u'没有数据:'+Detailstr+u'，请确认')
            exit(u'没有此数据，请确认')
    def getAssignData(self,el, data, xpath, inquiry=None):
        """
        获取列表中，指定类型的值
        :param el:
        :param data: 输入的数据
        :param xpath: 元素xpath位置
        :return:
        """

        time.sleep(1)
        el.getFunctionName(elData[0])
        el.get_element(elData[1])
        el.getDriver().implicitly_wait(1)
        if data == [] or data == '':

            #判断是否包含数据
            if len(el.gets()) > 0:
                # for i in el.gets():
                # logging.info(i.text.replace('\n','  '))
                return True
            else:
                try:
                    el.getDriver().implicitly_wait(1)
                    el.get_element('tabNotice')
                    logging.info(el.get().text)
                    return True
                except:
                    logging.error(u'出错！')
                    return False
        try:
            sleep(3)
            lnGets = len(el.gets())
            print lnGets
        except:
            el.get_element('tabNotice')
            logging.info(el.get().text)
            return True
        for i in range(lnGets):

            """
            if inquiry != 'Zidongxujia':
                dId = el.gets()[i].find_element_by_xpath('td[2]/div').text
                dLink = el.gets()[i].find_element_by_xpath('td[7]/div').text
            else:
                dId = inquiry
            # print dId

            if xpath == u'td[2]/div/img' or xpath == u'td[1]/div/img':
                sourceText = el.gets()[i].find_element_by_xpath(xpath).get_attribute('src').split('/')[-1].split('.')[0]

                if sourceText == 'cas':
                    resulttext = 'CAS'
                elif sourceText == 'web':
                    resulttext = u'估价宝'
                else:
                    resulttext = u'微信'
            else:
            """
            try:

                timestr = el.gets()[i].find_element_by_xpath(xpath).text.split()
                logging.info(timestr)
                if not timestr:  # if el.gets()[i].find_element_by_xpath(xpath).text.split()==[]:
                    resulttext = 0
                else:
                    resulttext = el.gets()[i].find_element_by_xpath(xpath).text.split()[0]
            except:
                logging.error(xpath)
                exit(u'请确认元素是否正确')
            if isinstance(data, list):
                if data[0] != '':
                    resulttext = data[0]
                    if data[0].isdigit():
                        resultArea = float(resulttext)
                        minArea = float(data[0])
                    else:
                        if resulttext == 0:
                            resulttext = '1990-01-01'
                        try:
                            beginTime = time.strptime(data[0], '%Y-%m-%d')
                            resultTime = time.strptime(resulttext.split()[0], '%Y-%m-%d')
                        except:
                            pass
                else:
                    resulttext = data[1]
                    if data[1].isdigit():
                        minArea = 0
                        resultArea = float(resulttext)
                    else:
                        try:
                            beginTime = time.strptime('1971-01-01', '%Y-%m-%d')
                            try:

                                resultTime = time.strptime(resulttext, '%Y-%m-%d %H:%M:%S')
                            except:
                                resultTime = time.strptime(resulttext, '%Y-%m-%d')
                        except:
                            logging.info(u'数据不为时间格式')
                if len(data) > 1:
                    if data[1] != '':
                        if data[1].isdigit():
                            maxArea = int(data[1])
                            if resultArea < minArea or resultArea > maxArea:
                                return False
                        else:
                            # 判断是否为日期格式
                            try:
                                time.strptime(data[1], '%Y-%m-%d')
                                subendtime = data[1] + ' 23:59:59'
                                endTime = time.strptime(subendtime, '%Y-%m-%d %H:%M:%S')
                            except:
                                # print resulttext,data
                                if resulttext in data:
                                    return True
                                else:
                                    subresulttext = resulttext.split(u'[')[0]
                                    # print subresulttext
                                    if subresulttext in data:
                                        return True
                                    else:
                                        return False

                            if time.mktime(resultTime) < time.mktime(beginTime) or time.mktime(
                                    resultTime) > time.mktime(endTime):

                                logging.error(resulttext)
                                return False
            else:
                oldData = data.replace(' ', '')

                if oldData not in resulttext:
                    logging.error(oldData + '!=' + resulttext)
                    return False
            return True
    def judgedatetime(self,el,dtime,xpath):
        time.sleep(1)
        el.getFunctionName(elData[0])
        el.get_element(elData[1])
        el.getDriver().implicitly_wait(1)
        if dtime == [] or dtime == '':

            # 判断是否包含数据
            if len(el.gets()) > 0:
                # for i in el.gets():
                # logging.info(i.text.replace('\n','  '))
                return True
            else:
                try:
                    el.getDriver().implicitly_wait(1)
                    el.get_element('tabNotice')
                    logging.info(el.get().text)
                    return True
                except:
                    logging.error(u'出错！')
                    return False
        try:
            sleep(3)
            lnGets = len(el.gets())

        except:
            el.get_element('tabNotice')
            logging.info(el.get().text)
            return True

        for i in range(lnGets):
            try:

                timestr = el.gets()[i].find_element_by_xpath(xpath).text.split()
                logging.info(timestr)
                if not timestr:  # if el.gets()[i].find_element_by_xpath(xpath).text.split()==[]:
                    resulttext = 0
                else:
                    resulttext = el.gets()[i].find_element_by_xpath(xpath).text.split()[0]
            except:
                logging.error(xpath)
                exit(u'请确认元素是否正确')
            if isinstance(dtime, list):
                if dtime[0] != '':
                    resulttext = dtime[0]
                    if dtime[0].isdigit():
                        resultArea = float(resulttext)
                        minArea = float(dtime[0])
                    else:
                        if resulttext == 0:
                            resulttext = '1990-01-01'
                        try:
                            beginTime = time.strptime(dtime[0], '%Y-%m-%d')
                            resultTime = time.strptime(resulttext.split()[0], '%Y-%m-%d')
                        except:
                            pass
                else:
                    resulttext = dtime[1]
                    if dtime[1].isdigit():
                        minArea = 0
                        resultArea = float(resulttext)
                    else:
                        try:
                            beginTime = time.strptime('1971-01-01', '%Y-%m-%d')
                            try:

                                resultTime = time.strptime(resulttext, '%Y-%m-%d %H:%M:%S')
                            except:
                                resultTime = time.strptime(resulttext, '%Y-%m-%d')
                        except:
                            logging.info(u'数据不为时间格式')
                if len(dtime) > 1:
                    if dtime[1] != '':
                        if dtime[1].isdigit():
                            maxArea = int(dtime[1])
                            if resultArea < minArea or resultArea > maxArea:
                                return False
                        else:
                            # 判断是否为日期格式
                            try:
                                time.strptime(dtime[1], '%Y-%m-%d')
                                subendtime = dtime[1] + ' 23:59:59'
                                endTime = time.strptime(subendtime, '%Y-%m-%d %H:%M:%S')
                            except:
                                # print resulttext,dtime
                                if resulttext in dtime:
                                    return True
                                else:
                                    subresulttext = resulttext.split(u'[')[0]
                                    # print subresulttext
                                    if subresulttext in dtime:
                                        return True
                                    else:
                                        return False

                            if time.mktime(resultTime) < time.mktime(beginTime) or time.mktime(
                                    resultTime) > time.mktime(endTime):

                                logging.error(resulttext)
                                return False
            else:
                '''
                oldData = dtime.replace(' ', '')
                # if oldData!=resulttext or oldData not in resulttext:
                print oldData,resulttext
                if oldData not in resulttext:
                    logging.error(oldData + '!=' + resulttext)
                    return False
                '''

                if dtime!= '':
                    resulttext = dtime
                    if dtime.isdigit():
                        resultArea = float(resulttext)
                        minArea = float(dtime)
                    else:
                        if resulttext == 0:
                            resulttext = '1990-01-01'
                        try:
                            beginTime = time.strptime(dtime, '%Y-%m-%d')
                            resultTime = time.strptime(resulttext.split()[0], '%Y-%m-%d')
                        except:
                            pass
                else:
                    resulttext = dtime
                    if dtime.isdigit():
                        minArea = 0
                        resultArea = float(resulttext)
                    else:
                        try:
                            beginTime = time.strptime('1971-01-01', '%Y-%m-%d')
                            try:

                                resultTime = time.strptime(resulttext, '%Y-%m-%d %H:%M:%S')
                            except:
                                resultTime = time.strptime(resulttext, '%Y-%m-%d')
                        except:
                            logging.info(u'数据不为时间格式')
                if dtime!= '':
                    if dtime.isdigit():
                        maxArea = int(dtime)
                        if resultArea < minArea or resultArea > maxArea:
                            return False
                    else:
                        # 判断是否为日期格式
                        try:
                            time.strptime(dtime, '%Y-%m-%d')
                            subendtime = dtime + ' 23:59:59'
                            endTime = time.strptime(subendtime, '%Y-%m-%d %H:%M:%S')
                        except:
                            # print resulttext,dtime
                            if resulttext in dtime:
                                return True
                            else:
                                subresulttext = resulttext.split(u'[')[0]
                                # print subresulttext
                                if subresulttext in dtime:
                                    return True
                                else:
                                    return False

                        if time.mktime(resultTime) < time.mktime(beginTime) or time.mktime(
                                resultTime) > time.mktime(endTime):

                            logging.error(resulttext)
                            return False
            return True
    def judgeTableData(self,el,data,xpath):
        time.sleep(1)
        el.getFunctionName(elData[0])
        el.get_element(elData[1])
        el.getDriver().implicitly_wait(1)
        try:
            lnGets = len(el.gets())
        except:
            el.get_element('tabNotice')
            logging.info(el.get().text)
            return True
        listdata=[]
        for i in range(lnGets):
            j= el.gets()[i].find_element_by_xpath(xpath).text.split()
            listdata.append(j)
        #print listdata
        for x in listdata:
            if x==data:
                logging.error(listdata[x])
                return False
        return True
    def showData(self,el,data):
        """
            获取列表中的值，并判断所有显示的值中是否包含指定值
            :param el: Element类实例
            :param data: 指定值
            :return: bool
            """

        time.sleep(1)
        el.getFunctionName(elData[0])
        try:
            el.getDriver().implicitly_wait(1)
            el.get_element(elData[1])
            for i in range(len(el.gets())):
                trData = el.gets()[i].text.split('\n')
                # print trData
                # dId = el.gets()[i].find_element_by_xpath('td[3]/div').text
                # dLink = el.gets()[i].find_element_by_xpath('td[7]/div').text
                if data not in trData:
                    for i in trData:
                        if data in i:
                            break
                    else:
                        return False
                    continue
        except:
            el.get_element('tabNotice')
            logging.info(el.get().text)
            exit()
        return True
    def getDetail(self, func, el, data, xmlList, eList):
        """
        获取详细信息里的数据
        :param self:
        :param el:
        :param xmlList:xml function list
        :param eList: element list
        :return:
        """
        #print eList,xmlList
        cn.switchToDetailUI(func, el)
        # 判断是否为Tab方式
        el.getFunctionName(tabchk[0])
        '''
        el.get_element('tabshowdiv')
        tabatb = el.get().get_attribute('class')
        logging.info(u'查看Tab是否勾选')
        if 'chked' in tabatb:
            logging.info(u'不勾选Tab')
            el.get_element('tabchkbox')
            el.get().click()
        else:
            logging.info(u'Tab未被勾选')
        '''
        '''
        el.get_element('tabstate')
        tabatb=el.get().get_attribute('style')
        logging.info(u'查看Tab是否勾选')
        if 'block' in tabatb:
            logging.info(u'不勾选Tab')
            el.get_element('tabchkbox')
            el.get().click()
        else:
            logging.info(u'Tab未被勾选')
        '''
        el.get_element('tabshow')
        logging.info(u'查看Tab是否勾选')
        try:
            tabatb = el.get().get_attribute('checked')
            #print tabatb
            if tabatb=='true':
                logging.info(u'不勾选Tab')
                el.get_element('tabchkbox')
                el.get().click()
        except:
            logging.info(u'Tab未被勾选')


        el.getFunctionName(xmlList[0])
        for i in range(len(eList)):
            dictFunction = EL.get_el_dict(xmlList[0], eList[i], cg.path)

            el.get_element(eList[i])
            tagname = ' '
            try:
                tagname = el.get().get_attribute('tagname')
            except:
                pass
            #logging.info('tagname:'+tagname)
            if tagname == None:
                tagname = ''
                currenttext = u'没有类型'
            #print dictFunction
            if 'elementType' in dictFunction:
                if dictFunction['elementType'] == 'select':
                    #print Select(el.get()).options[0].text
                    currenttext = Select(el.get()).all_selected_options[0].text
                elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                    try:
                        currenttext = el.get().get_attribute('value').strip()
                    except:
                        currenttext = el.get().text.strip()
                else:
                    currenttext = el.get().text.strip()
            logging.info(currenttext)
            if isinstance(data, list):
                #print currenttext
                resulttext = currenttext
                #print resulttext
                if data[0] != '':
                    if data[0].isdigit():
                        resultArea = float(resulttext)
                        minArea = float(data[0])
                    else:
                        if resulttext == 0:
                            resulttext = '1980-01-01'
                        try:
                            beginTime = time.strptime(data[0], '%Y-%m-%d')
                            resultTime = time.strptime(resulttext.split()[0], '%Y-%m-%d')
                        except:
                            pass

                else:
                    if data[1].isdigit():
                        minArea = 0
                        resultArea = float(resulttext)
                    else:
                        try:
                            beginTime = time.strptime('1971-01-01', '%Y-%m-%d')
                            try:
                                resultTime = time.strptime(resulttext, '%Y-%m-%d %H:%M:%S')
                            except:
                                resultTime = time.strptime(resulttext, '%Y-%m-%d')
                        except:
                            logging.info(u'数据不为时间格式')
                            pass

                if len(data) > 1:
                    if data[1] != '':
                        if data[1].isdigit():
                            maxArea = int(data[1])
                            if resultArea < minArea or resultArea > maxArea:
                                return False
                        else:
                            # print data[1]
                            # 判断是否为日期格式
                            try:
                                # endTime=time.strptime(data[1], '%Y-%m-%d')
                                subtime = data[1] + ' 23:59:59'
                                endTime = time.strptime(subtime, '%Y-%m-%d %H:%M:%S')
                            except:
                                logging.info(u'数据不为时间格式')
                                return resulttext in data

                            if time.mktime(resultTime) < time.mktime(beginTime) or time.mktime(resultTime) > time.mktime(endTime):

                                logging.error(resulttext)
                                return False
                            else:
                                logging.info(resultTime)
                                return True
                else:
                    if time.mktime(beginTime)<time.mktime(resultTime):
                        logging.info(data[0])
                        return True
            else:
                #print currenttext,data
                #if data not in currenttext.strip() :#or currenttext.strip() not in data
                if data in currenttext.strip() or currenttext.strip() in data:
                    # print currenttext,data

                    logging.info(tagname + u'：' + currenttext)
                    #return False
                    return True

            #logging.error('not data')
            #return True
            return False
    def choices_Quser(self,func,el,user):
        """
        选择用户
        :param func:
        :param el:
        :param user:
        :return:
        """
        self.switcthToDefault(func)
        sleep(5)
        self.swithcfrname(el)
        sleep(3)
        print func.driver.current_url
        el.getFunctionName(User[0])

        el.get_element('sinput')
        el.get().send_keys(user)
        el.get().send_keys(Keys.ENTER)
        js=True
        i=1
        while js:

            try:
                txt=func.driver.find_element_by_id('userchkTree_' + str(i) + '_span').text.split(']')[1]
                #print txt
                if txt==user:
                    func.driver.find_element_by_id('userchkTree_' + str(i) + '_check').click()
                    js=False
            except:
                pass
            finally:
                i+=1


        """
        el.get_element('users')
        liels=el.get().find_elements_by_xpath('li')
        for i in range(len(liels)):
            ulels=liels[i].find_elements_by_xpath('ul')
            for j in range(len(ulels)):
                liels1=ulels[j].find_elements_by_xpath('li')
                for x in range(len(liels1)):
                    susers=liels1[x].text
                    suserslist=susers.split(']')
                    print x
                    print susers,suserslist,222
                    if len(suserslist)<2:
                        continue
                    username=suserslist[1]
                    print username,1111
                    print user ,username
                    if user == username.strip():
                        chID=liels1[x].find_elements_by_tag_name('span')[1].get_attribetu('id')
                        print chID
                        el.get_element('sinput')
                        el.get().send_keys(user)
                        el.get().send_keys(Keys.ENTER)
                        func.driver.find_element_by_id(chID).click()
                        return
        else:
            logging.info('not user')
            exit()
        """


        #el.get().click()
        el.get_element('btnOk')
        el.get().click()
    def showAllData(self,el, data):
        """
        获取列表中的值，并判断所有显示的值中是否包含指定值
        :param el: Element类实例
        :param data: 指定值
        :return: bool
        """

        time.sleep(1)
        el.getFunctionName(elData[0])
        try:
            el.getDriver().implicitly_wait(1)
            el.get_element(elData[1])
            for i in range(len(el.gets())):
                trData = el.gets()[i].text.split('\n')
                # print trData
                # dId = el.gets()[i].find_element_by_xpath('td[3]/div').text
                # dLink = el.gets()[i].find_element_by_xpath('td[7]/div').text
                if data not in trData:
                    for i in trData:
                        #print i
                        if data in i:
                            break
                    else:
                        return True
                    continue
        except:
            el.get_element('tabNotice')
            logging.info(el.get().text)
            return True
        return True

class QueryCheck(reportquery):
    def check_query(self,func,el,tab=u'全部',sub=u'正式报告',*args):
        return  self.query(func,el,sub,tab,*args)


