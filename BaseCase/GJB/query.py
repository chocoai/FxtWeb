#coding:utf-8
import os
import time
import random
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import COMMON.ELEMNET as EL
from BaseCase.GJB import commond
from BaseCase.GJB import addnew
from COMMON import CONFIG as CFG
xmlpath=os.path.join(CFG.prjDir,'BaseCase/GJB')
query=EL.get_el_name('Query',xmlpath)
elData=EL.get_el_name('Checkbox',xmlpath)

def getSelData(el, Detailstr):
    """
    选择查询条件的数据项
    :param el:
    :param Detailstr:
    :return:
    """
    time.sleep(1)
    dataList = Select(el.get()).options
    for i in range(len(dataList)):
        #if dataList[i].text.strip() == Detailstr.strip():
        if Detailstr.strip() in dataList[i].text:
            #time.sleep(1)
            #value = dataList[i].get_attribute('value')
            #Select(el.get()).select_by_value(value)
            index=dataList.index(dataList[i])
            Select(el.get()).select_by_index(index)
            break
    else:
        logging.error(u'没有数据'+Detailstr+u'，请确认')
        exit(u'没有此数据，请确认')
def getDetail(self, el, data, function, elementList):
    """
    获取详细信息里的数据
    :param self:
    :param el:
    :param function:xml
    :param elementList:
    :return:
    """
    commond.switchToDetailUI(self,el)
    el.getFunctionName(function[0])
    for i in range(len(elementList)):
        el.get_element(elementList[i])
        dictFunction = EL.get_el_dict(function[0], elementList[i], xmlpath)
        tagname=' '
        try:
            tagname = el.get().get_attribute('tagname')
        except:
            pass
        if tagname==None:
            tagname=''
            currenttext=u'没有类型'
        if 'elementType' in dictFunction:
            if dictFunction['elementType'] == 'select':
                currenttext = Select(el.get()).all_selected_options[0].text
            elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                currenttext = el.get().get_attribute('value').strip()
            else:
                currenttext = el.get().text.strip()
        if isinstance(data,list):
            resulttext=currenttext
            if data==[]:
                exit(u'空列表')
            if data[0] != '':
                if data[0].isdigit():
                    resultArea=float(resulttext)
                    minArea=float(data[0])
                else:
                    if resulttext==0:
                        resulttext='1980-01-01'
                    try:
                        beginTime = time.strptime(data[0], '%Y-%m-%d')
                        resultTime = time.strptime(resulttext.split()[0], '%Y-%m-%d')
                    except:
                        pass

            else:
                if data[1].isdigit():
                    minArea=0
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

            if len(data)>1:
                if data[1]!='':
                    if data[1].isdigit():
                        maxArea=int(data[1])
                        if resultArea<minArea or resultArea>maxArea:
                            return False
                    else:
                        #print data[1]
                        #判断是否为日期格式
                        try:
                            #endTime=time.strptime(data[1], '%Y-%m-%d')
                            subtime=data[1]+' 23:59:59'
                            endTime =time.strptime(subtime, '%Y-%m-%d %H:%M:%S')
                        except:
                            logging.info(u'数据不为时间格式')
                            return resulttext in data

                        if time.mktime(resultTime) < time.mktime(beginTime) or time.mktime(
                                resultTime) > time.mktime(endTime):
                            print time.mktime(resultTime)<time.mktime(beginTime),time.mktime(resultTime)>time.mktime(endTime),resultTime,endTime
                            logging.error(resulttext)
                            return False
        else:
            if currenttext.strip() not in data:
                #print currenttext,data
                logging.error()
                return False
        logging.info(tagname + u'：' + currenttext)

    return True
def Query(self,el,msgmode=None,data=None,submode=None,Inquiry=None,substate=None):
    """

    :param self:
    :param el:
    :param msgmode:
    :param data:
    :param submode:
    :param Inquiry:
    :param substate:
    :return:
    """

    if Inquiry == None:
        commond.Duantao(self,el,submode,substate)
    else:
        commond.OtherXujia(self,el,Inquiry,substate)
    el.getFunctionName(query[0])
    if Inquiry!='Gaizhang':
        if substate!='daishenpi'and substate!='yishenpi':
            el.get_element('moreConditions')
            el.get().click()
    elementList = []
    resultText=''
    if data==u'默认':
        data=msgmode
    logging.info(u'查询关键字为：%s'%msgmode)
    if msgmode==u'省份':
        if data==None:
            pass
        else:
            for i in [u'直辖市',u'省',u'特区',u'自治区']:
                if i in data:
                    if u'直辖市' in data or u'特区' in data:
                        if u'直辖市' in data:
                            provinceKey=u'直辖市'
                            city = data.split(provinceKey)[0] + u'市'
                        else:
                            provinceKey=u'特区'
                            city = data.split(provinceKey)[0]
                        dataprList=data.split(provinceKey)
                        provincetext=data.split(provinceKey)[0]+provinceKey
                        el.get_element('province')

                        provinceList=Select(el.get()).options
                        for i in range(len(provinceList)):
                            if provinceList[i].text.strip()==provincetext:
                                value=provinceList[i].get_attribute('value')
                                Select(el.get()).select_by_value(value)
                                #index=provinceList.index(provinceList[i])
                                #Select(el.get()).select_by_index(index)
                                #time.sleep(5)
                                break

                        el.get_element('city')
                        cityList=Select(el.get()).options
                        for i in range(len(cityList)):
                            if cityList[i].text.strip()==city:
                                index=cityList.index(cityList[i])
                                Select(el.get()).select_by_index(index)
                                break

                        if len(dataprList)>=2:
                            area=data.split(provinceKey)[1]
                            el.get_element('area')

                            areaList=Select(el.get()).options
                            for i in range(len(areaList)):
                                if areaList[i].text.strip()==area:
                                    index=areaList.index(areaList[i])
                                    Select(el.get()).select_by_index(index)
                                    break

                    else:
                        if u'省' in data:
                            provinceKey=u'省'
                        elif u'自治区' in data:
                            provinceKey =u'自治区'
                        else:
                            logging.error(u'数据格式不正确，请确认')
                            exit(u'数据格式不正确，请确认')
                        dataprList = data.split(provinceKey)

                        provincetext = dataprList[0] + provinceKey
                        el.get_element('province')
                        getSelData(el, provincetext)

                        el.get_element('city')
                        if dataprList[1]!='':
                            if u'市' in dataprList[1]:
                                cityKey=u'市'
                            elif u'县' in dataprList[1]:
                                cityKey=u'地区'
                            elif u'州' in dataprList[1]:
                                cityKey =u'自治州'
                            elif u'盟' in dataprList[1]:
                                cityKey=u'盟'

                            cityList = dataprList[1].split(cityKey,1)
                            city = cityList[0]+ cityKey
                            #el.get_element('city')
                            getSelData(el, city)

                            if cityList[1]!='':
                                area=cityList[1]
                                el.get_element('area')
                                getSelData(el, area)
                                time.sleep(5)
                            else:
                                area=''
                        else:
                            city=''
                            resultText=[]
                            cityOptions=Select(el.get()).options
                            for i in cityOptions:
                                #print i.text
                                resultText.append(i.text)

                    break
            else:
                logging.info(u'请检查数据格式')
                exit(u'请检查数据格式')
            if city=='':
                pass
                #resultText=''#待解决
            elif area=='':
                resultText=city
            else:
                resultText=city+'['+area+']'
    elif msgmode==u'分支机构':
        if data!=None:
            elementList.append('fenzhijigou')
            dataList=data.split()
            company=dataList[0]
            el.get_element('company')
            getSelData(el, company)

            if len(dataList)>1:
                elementList.append('yewuyuansuoshubumen')
                department=dataList[1]
                el.get_element('department')
                getSelData(el, department)
    elif msgmode==u'委估对象类型':
        elementList.append('xunjialeixing')
        el.get_element('valuationTypeMode')
        getSelData(el, data)
    elif msgmode==u'来源':
        if data==u'默认':
            data=msgmode
        el.get_element('source')
        getSelData(el, data)
    elif msgmode==u'委托客户' or msgmode==u'客户单位':
        dataList=data.split()
        entrustCorrespondent=dataList[0]
        el.get_element('entrustCorrespondent')
        getSelData(el, entrustCorrespondent)
        if len(dataList)>1:
            bankBranch=dataList[1]
            el.get_element('bankBranch')
            getSelData(el, bankBranch)
            time.sleep(1)
        if len(dataList)>2:
            bankSubbranch=dataList[2]
            el.get_element('bankSubbranch')
            getSelData(el, bankSubbranch)
    elif msgmode==u'状态':
        el.get_element('state')
        getSelData(el, data)
    elif msgmode==u'估价师':
        #因为功能涉及流程比较复杂暂不开发
        pass
    elif msgmode==u'查勘状态':
        surveystate=data
        xpath='td[15]/div'
        el.get_element('surveystate')
        getSelData(el, surveystate)
    elif msgmode==u'询价时间'or msgmode==u'申请时间' or msgmode==u'盖章时间':
        strdata=str(data)
        if '-' in strdata:
            dataList = strdata.split(':')
            begintime = dataList[0]
        else:
            dataList=[]
            begintime=''
        el.get_element('beginData')
        #self.driver.execute_script(
            #"var setDate=document.getElementById(\""+el.path+"\");setDate.removeAttribute('readonly');")
        #print el.path
        self.driver.execute_script(
           "var setDate=document.getElementById(\"" + el.path + "\");setDate.removeAttribute('readonly');")
        self.driver.execute_script("var setDate=function $(id){ return document.getElementById(id); };setDate(\""+el.path+"\").removeAttribute('readonly');")
        if Inquiry!='Gaizhang':
            el.get().clear()
        if begintime!='':
            #print begintime
            el.get().send_keys(begintime)
        el.get_element('endData')
        self.driver.execute_script(
            "var setDate=document.getElementById(\""+el.path+"\");setDate.removeAttribute('readonly');")
        if Inquiry!='Gaizhang':
            el.get().clear()
        if len(dataList)>1:
            endtime=dataList[1]
            el.get().send_keys(endtime)
    elif msgmode==u'面积':
        strdata=str(data)
        dataList=strdata.split('-')
        minArea=dataList[0]
        if minArea!='':
            el.get_element('minArea')
            el.get().clear()
            el.get().send_keys(minArea)
        if len(dataList)>1:
            maxArea=dataList[1]
            el.get_element('maxArea')
            el.get().click()
            el.get().send_keys(maxArea)
    elif msgmode==u'关键字查询':
        el.get_element('fuzzyQuery')
        el.get().clear()
        if type(data)==float:
            data=str(data)
        if data==None:
            pass
        else:
            el.get().send_keys(data)
    elif msgmode==u'提交时间':
        if type(data)==float:
            data=str(data)
        dataList = data.split(':')

        begintime = dataList[0]
        time.sleep(1)
        el.get_element('submitBeginData')

        # Chrome浏览器无法执行下面的代码与js
        #self.driver.find_element_by_xpath('//*[@id="txtQueryBeginDate"]')
        self.driver.execute_script("var setDate=document.getElementById(\"" + el.path + "\");setDate.removeAttribute('readonly');")
        el.get().clear()
        if begintime != '':
            el.get().send_keys(begintime)

        el.get_element('submitEndData')
        self.driver.execute_script("var setDate=document.getElementById(\"" + el.path + "\");setDate.removeAttribute('readonly');")

        el.get().clear()
        if len(dataList) > 1:
            endtime = dataList[1]
            el.get().send_keys(endtime)
    elif msgmode==u'询价单类型':
        elementList.append('xujiadanleixing')
        el.get_element('xujiadanleixing')
        getSelData(el, data)
    elif msgmode==u'物业类型':
        elementList.append('wuyeleixing')
        el.get_element('wuyeleixing')
        getSelData(el, data)
    elif msgmode==u'用户类型':
        if data==u'默认':
            data=msgmode
        el.get_element('UserType')
        getSelData(el, data)
    else:
        logging.error(u'请检查询的字段是否正确!')
        exit(u'请检查询的字段是否正确')
    time.sleep(2)
    el.get_element('queryKey')
    el.get().click()
    time.sleep(1)
    if msgmode == u'省份':
        xpath = u'td[13]/div'
        result=getAssignData(el, resultText, xpath)
        return result
    elif msgmode==u'分支机构':
        el.getFunctionName(elData[0])
        el.get_element('checkbox')
        el.getDriver().implicitly_wait(1)
        try:
            # for i in range(len(el.gets())):
            logging.info(u'共'+str(len(el.gets()))+u'条数据')
            rd = random.randint(0, len(el.gets()) - 1)
        except:
            el.get_element('tabNotice')
            logging.info(el.get().text)
            return True

        logging.info(u'第' + str(rd + 1) + u'条数据')
        if substate=='yishenpi'or substate=='daishenpi':
            #dId=el.gets()[rd].find_element_by_xpath('td[2]/div').text
            dId=u'列表没有询价编号一列'
        else:
            dId = el.gets()[rd].find_element_by_xpath('td[3]/div').text
        #dLink = el.gets()[rd].find_element_by_xpath('td[7]/div').text
        logging.info(u'询价编号：' + dId)
        time.sleep(1)
        # if substate!=None:
        #     # if 'shenpi' in substate:
        #     #     #el.gets()[rd].find_element_by_xpath('td[3]/div').click()
        #     # else:
        #     ActionChains(self.driver).double_click(el.gets()[rd].find_element_by_xpath('td[3]/div')).perform()
        # else:
        #     ActionChains(self.driver).double_click(el.gets()[rd].find_element_by_xpath('td[3]/div')).perform()
        ActionChains(self.driver).double_click(el.gets()[rd].find_element_by_xpath('td[3]/div')).perform()
        result = getDetail(self, el, data, query, elementList)
        return result
    elif msgmode==u'来源':
        if Inquiry=='Zidongxujia':
            xpath=u'td[1]/div/img'
        else:
            xpath = u'td[2]/div/img'
        result=getAssignData(el, data, xpath,Inquiry)
        return result
    elif msgmode==u'委估对象类型' :
        el.getFunctionName(elData[0])
        el.get_element(elData[1])
        # for i in range(len(el.gets())):
        time.sleep(1)
        el.getDriver().implicitly_wait(1)
        try:
            lnGets=len(el.gets())-1
        except:
            el.get_element('tabNotice')
            logging.info(el.get().text)
            return True
        rd = random.randint(0,lnGets)
        logging.info(u'第'+str(rd+1)+u'条')
        dId = el.gets()[rd].find_element_by_xpath('td[3]/div').text
        dLink = el.gets()[rd].find_element_by_xpath('td[7]/div').text
        logging.info(u'询价编号：' + dId)
        ActionChains(self.driver).double_click(el.gets()[rd].find_element_by_xpath('td[3]/div')).perform()
        result = getDetail(self, el, data, query, elementList)
        return result
    elif msgmode==u'委托客户'or msgmode==u'客户单位':
        valuationText = ''.join(data)
        #print valuationText
        if Inquiry=='Duotao':
            xpath = 'td[13]/div'
        elif Inquiry=='Zidongxujia':
            xpath='td[2]/div'
        else:
            xpath='td[9]/div'
        result=getAssignData(el, valuationText, xpath)
        #print result
        return result
    elif msgmode==u'状态':
        elementList.append('xunjiazhuantai')
        el.getFunctionName(elData[0])
        el.get_element(elData[1])
        time.sleep(1)
        el.getDriver().implicitly_wait(1)
        try:
            lnGets=len(el.gets()) - 1
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
        result = getDetail(self, el, data, query, elementList)
        return result
    elif msgmode==u'查勘状态':
        result=getAssignData(el, data,xmlpath)
        return result
    elif msgmode==u'询价时间'or msgmode==u'申请时间'or msgmode==u'盖章时间':
        if Inquiry=='Zidongxujia':
            xpath='td[17]/div'
        elif Inquiry=='Gaizhang':
            xpath='td[11]/div'
        elif Inquiry=='Duotao':
            #xpath='td[22]/div'#这是估价时间，不是询价时间
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
                rd = random.randint(0, len(el.gets())-1)
            except:
                el.get_element('tabNotice')
                logging.info(el.get().text)
                return True

            logging.info(u'第' + str(rd + 1) + u'条数据')
            if substate == 'yishenpi' or substate == 'daishenpi':
                # dId=el.gets()[rd].find_element_by_xpath('td[2]/div').text
                dId = u'列表未询价编号'
            else:
                dId = el.gets()[rd].find_element_by_xpath('td[3]/div').text
            # dLink = el.gets()[rd].find_element_by_xpath('td[7]/div').text
            logging.info(u'询价编号：' + dId)
            time.sleep(1)
            ActionChains(self.driver).double_click(el.gets()[rd].find_element_by_xpath('td[3]/div')).perform()
            result = getDetail(self, el, dataList, query, elementList)
            return result
        else:
            if substate=='Zhuzai':
                xpath = 'td[30]/div'
            else:
                xpath= 'td[27]/div'
        result=getAssignData(el, dataList, xpath)
        return result

        #以下代码查询其中一条数据，并进入详细界面，获取创建时间
        '''
        elementList.append('chuangjianshijian')
        el.getFunctionName(elData[0])
        el.get_element('checkbox')
        el.getDriver().implicitly_wait(1)
        if data == u'清空':
            if len(el.gets())>0:
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
        if substate == 'yishenpi' or substate == 'daishenpi':
            # dId=el.gets()[rd].find_element_by_xpath('td[2]/div').text
            dId = u'列表未询价编号'
        else:
            dId = el.gets()[rd].find_element_by_xpath('td[3]/div').text
        # dLink = el.gets()[rd].find_element_by_xpath('td[7]/div').text
        logging.info(u'询价编号：' + dId)
        time.sleep(1)
        ActionChains(self.driver).double_click(el.gets()[rd].find_element_by_xpath('td[3]/div')).perform()
        result = getDetail(self, el, dataList, query, elementList)
        return result
        '''
    elif msgmode==u'面积':
        if Inquiry=='Zidongxujia':
            xpath='td[6]/div'
        elif Inquiry=="Duotao":
            xpath = 'td[16]/div'
        else:
            xpath='td[17]/div'
        result=getAssignData(el, dataList, xpath)
        return result
    elif msgmode==u'关键字查询':
        result=showAllData(el,data)
        return result
    elif msgmode==u'提交时间':
        xpath = 'td[9]/div'
        result = getAssignData(el, dataList, xpath)
        return result
    elif msgmode == u'询价单类型':
        if data==u'询价单类型':
            data=[u'自动询价',u'人工询价']
        xpath='td[2]/div'
        result=getAssignData(el,data,xpath)
        return result
    elif msgmode==u'物业类型':
        xpath = 'td[5]/div'
        if data==u'物业类型':
            data=[u'住宅',u'办公',u'商业',u'工业',u'土地',u'资产',u'其他']

        result = getAssignData(el, data, xpath)
        return result
    elif msgmode==u'用户类型':
        #xpath = u'td[2]/div'
        result = showAllData(el, data)
        return result
    else:
        logging.error(u'请检查询的字段是否正确!')
        exit(u'请检查询的字段是否正确')
def showAllData(el,data):
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
        if data==None:
            pass
        else:
            if len(el.gets())>0:
                return True
            else:
                return False
            # for i in range(len(el.gets())):
            #     trData=el.gets()[i].text.split('\n')
            #     if data not in trData:
            #         for i in trData:
            #             if data in i:
            #                 break
            #         else:
            #             return False
            #         continue
    except:
        el.get_element('tabNotice')
        logging.info(el.get().text)
        exit(el.get().text)
    return True
def getAssignData(el, data, xpath,inquiry=None):
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
    if data ==[] or data=='':
        if len(el.gets()) > 0:
            #for i in el.gets():
                #logging.info(i.text.replace('\n','  '))
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
        lnGets=len(el.gets())
    except:
        el.get_element('tabNotice')
        logging.info(el.get().text)
        return True
    for i in range(lnGets):

        if inquiry!='Zidongxujia':
            dId = el.gets()[i].find_element_by_xpath('td[3]/div').text
            dLink = el.gets()[i].find_element_by_xpath('td[7]/div').text
        else:
            dId=inquiry
        #print dId
        if xpath==u'td[2]/div/img' or xpath==u'td[1]/div/img':
            sourceText = el.gets()[i].find_element_by_xpath(xpath).get_attribute('src').split('/')[-1].split('.')[0]

            if sourceText=='cas':
                resulttext='CAS'
            elif sourceText=='web':
                resulttext=u'估价宝'
            else:
                resulttext=u'微信'
        else:
            try:
                timestr=el.gets()[i].find_element_by_xpath(xpath).text.split()
                if not timestr:# if el.gets()[i].find_element_by_xpath(xpath).text.split()==[]:
                    resulttext=0
                else:
                    resulttext = el.gets()[i].find_element_by_xpath(xpath).text.split()[0]
            except:
                logging.error(xpath)
                exit(u'请确认元素是否正确')
        if isinstance(data,list):
            if data[0] != '':
                resulttext=data[0]
                if data[0].isdigit():
                    resultArea=float(resulttext)
                    minArea=float(data[0])
                else:
                    if resulttext==0:
                        resulttext='1990-01-01'
                    try:
                        beginTime = time.strptime(data[0], '%Y-%m-%d')
                        resultTime = time.strptime(resulttext.split()[0], '%Y-%m-%d')
                    except:
                        pass

            else:
                resulttext=data[1]
                if data[1].isdigit():
                    minArea=0
                    resultArea = float(resulttext)
                else:
                    try:
                        beginTime = time.strptime('1971-01-01', '%Y-%m-%d')
                        try:
                            print resulttext
                            resultTime = time.strptime(resulttext, '%Y-%m-%d %H:%M:%S')
                        except:
                            resultTime = time.strptime(resulttext, '%Y-%m-%d')
                    except:
                        logging.info(u'数据不为时间格式')


            if len(data)>1:
                if data[1]!='':
                    if data[1].isdigit():
                        maxArea=int(data[1])
                        if resultArea<minArea or resultArea>maxArea:
                            return False
                    else:
                        #判断是否为日期格式
                        try:
                            time.strptime(data[1], '%Y-%m-%d')
                            subendtime=data[1]+ ' 23:59:59'
                            endTime =time.strptime(subendtime, '%Y-%m-%d %H:%M:%S')
                        except:
                            #print resulttext,data
                            if resulttext in data:
                                return True
                            else:
                                subresulttext=resulttext.split(u'[')[0]
                                #print subresulttext
                                if subresulttext in data:
                                    return True
                                else:
                                    return False

                        if time.mktime(resultTime) < time.mktime(beginTime) or time.mktime(
                                resultTime) > time.mktime(endTime):
                            print time.mktime(resultTime)<time.mktime(beginTime),time.mktime(resultTime)>time.mktime(endTime),resultTime,endTime
                            logging.error(resulttext)
                            return False
        else:
            oldData=data.replace(' ','')
            #if oldData!=resulttext or oldData not in resulttext:

            if oldData not in resulttext:
                logging.error(u'询价编号：'+dId)
                logging.error(oldData+ '!=' + resulttext)
                return False
        return True