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
import reportadd as ra
import reportQuery as rq
import COMMON.CONFIG as CFG
dataDetail=cg.reportDataDetail
key=None
tabledate=cg.tableData
examineModif=cg.ExamineModif
User=cg.reportUser
reportFrame=cg.reportFrame
Usertxt=cg.reportUserText
EjsonData=cg.EjsonData
tableid='td[3]/div'
tablink='td[15]/div'
reportwriter='td[12]/div'
class Modification(reportBase):
    """修改数据"""
    def select_elementdata(self,el,data):
        currentscttext = Select(el.get()).all_selected_options[0].text
        if data in currentscttext and u'请选择' not in currentscttext:
            pass
        else:
            allOptions = Select(el.get()).options
            for selem in allOptions:
                if data.strip() == selem.text.strip():
                    index = allOptions.index(selem)
                    Select(el.get()).select_by_index(index)
                    break
            else:
                logging.error(u'未找到此选项：' + data)
    def updateGeneral(self, func, el, sub, *args):
        self.reportTab(func,el,sub)
        dataId=self.chose_data(el,sub=sub,data=args)
        cn.switchToDetailUI(func,el)
        self.chkTab(el)

        a = EL.get_el_list('RPdataDetail', cg.path)
        idatatype=args[0]
        currenttxtList = []
        if idatatype.strip() == u'评估方法':
            if type(idatatype) == list:
                pass
            else:
                if args[1] == u'比较法':
                    if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[1]').get_attribute(
                            'checked') != 'true':
                        func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[1]').click()
                    currenttxtList.append(u'比较法')
                elif args[1] == u'收益法':
                    if func.driver.find_element_by_xpath(
                            '//*[@id="field_valuationmethods"]/input[2]').get_attribute('checked') != 'true':
                        func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[2]').click()
                    currenttxtList.append(u'收益法')
                elif args[1] == u'成本法':
                    if func.driver.find_element_by_xpath(
                            '//*[@id="field_valuationmethods"]/input[3]').get_attribute('checked') != 'true':
                        func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[3]').click()
                    currenttxtList.append(u'成本法')
                elif args[1] == u'假设开发法':
                    if func.driver.find_element_by_xpath(
                            '//*[@id="field_valuationmethods"]/input[4]').get_attribute('checked') != 'true':
                        func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[4]').click()
                    currenttxtList.append(u'假设开发法')
                elif args[1] == u'基准地价修正法':
                    if func.driver.find_element_by_xpath(
                            '//*[@id="field_valuationmethods"]/input[5]').get_attribute('checked') != 'true':
                        func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[5]').click()
                    currenttxtList.append(u'基准地价修正法')
                elif args[1] == u'路线价法':
                    if func.driver.find_element_by_xpath(
                            '//*[@id="field_valuationmethods"]/input[6]').get_attribute('checked') != 'true':
                        func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[6]').click()
                    currenttxtList.append(u'路线价法')
                elif args[1] == u'长期趋势法':
                    if func.driver.find_element_by_xpath(
                            '//*[@id="field_valuationmethods"]/input[7]').get_attribute('checked') != 'true':
                        func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[7]').click()
                    currenttxtList.append(u'长期趋势法')


                # if args[1].strip() == u'比较法':
                #     if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[1]').get_attribute(
                #             'checked') == 'true':
                #         currenttxtList.append(func.driver.find_element_by_xpath(
                #             '//*[@id="field_valuationmethods"]/input[1]').get_attribute('value'))
                #     else:
                #         logging.error('not checked!!!')
                # elif args[1] == u'收益法':
                #     func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[2]').click()
                #     if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[2]').get_attribute(
                #             'checked') == 'true':
                #         currenttxtList.append(func.driver.find_element_by_xpath(
                #             '//*[@id="field_valuationmethods"]/input[2]').get_attribute('value'))
                #     else:
                #         logging.error('not checked!!!')
                # elif args[1] == u'成本法':
                #     func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[3]').click()
                #     if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[3]').get_attribute(
                #             'checked') == 'true':
                #         currenttxtList.append(func.driver.find_element_by_xpath(
                #             '//*[@id="field_valuationmethods"]/input[3]').get_attribute('value'))
                #     else:
                #         logging.error('not checked!!!')
                # elif args[1] == u'假设开发法':
                #     func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[4]').click()
                #     if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[4]').get_attribute(
                #             'checked') == 'true':
                #         currenttxtList.append(func.driver.find_element_by_xpath(
                #             '//*[@id="field_valuationmethods"]/input[4]').get_attribute('value'))
                #     else:
                #         logging.error('not checked!!!')
                # elif args[1] == u'基准地价修正法':
                #     func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[5]').click()
                #     if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[5]').get_attribute(
                #             'checked') == 'true':
                #         currenttxtList.append(func.driver.find_element_by_xpath(
                #             '//*[@id="field_valuationmethods"]/input[5]').get_attribute('value'))
                #     else:
                #         logging.error('not checked!!!')
                # elif args[1] == u'路线价法':
                #     func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[6]').click()
                #     if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[6]').get_attribute(
                #             'checked') == 'true':
                #         currenttxtList.append(func.driver.find_element_by_xpath(
                #             '//*[@id="field_valuationmethods"]/input[6]').get_attribute('value'))
                #     else:
                #         logging.error('not checked!!!')
                # elif args[1] == u'长期趋势法':
                #     func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[7]').click()
                #     if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[7]').get_attribute(
                #             'checked') == 'true':
                #         currenttxtList.append(func.driver.find_element_by_xpath(
                #             '//*[@id="field_valuationmethods"]/input[7]').get_attribute('value'))
                #     else:
                #         logging.error('not checked!!!')
                # # if args[1] == u'比较法':
                # #
                # #     func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[1]').click()
                # #     sleep(5)
                # #     currenttxtList.append(u'比较法')
                # # elif args[1] == u'收益法':
                # #     func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[2]').click()
                # # elif args[1] == u'成本法':
                # #     func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[3]').click()
                # # elif args[1] == u'假设开发法':
                # #     func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[4]').click()
                # # elif args[1] == u'基准地价修正法':
                # #     func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[5]').click()
                # # elif args[1] == u'路线价法':
                # #     func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[6]').click()
                # # elif args[1] == u'长期趋势法':
                # #     func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[7]').click()
        elif idatatype.strip()==u'城市':
            ddata=args[1].split(' ')
            el.getFunctionName('RPdataDetail')
            for i in range(len(ddata)):
                if i==0:
                    el.get_element('Province')
                elif i==1:
                    el.get_element('city')
                elif i==2:
                    el.get_element('area')
                elif i==3:
                    el.get_element('subarea')
                else:
                    logging.info(u'输入的数据不对')
                    exit()
                self.select_elementdata(el,ddata[i])

        else:
            for j in range(1, len(a)):
                b = EL.get_el_dict(a[0], a[j], cg.path)
                if b.get('name').strip() == idatatype.strip():
                    el.getFunctionName(a[0])
                    el.get_element(a[j])
                    sleep(1)
                    if b.get('elementType') == 'select':
                        currentscttext = Select(el.get()).all_selected_options[0].text
                        if args[1] == None:
                            if u'请选择' in currentscttext:
                                rdmod = random.randint(1, len(Select(el.get()).options) - 1)
                                Select(el.get()).select_by_index(rdmod)
                                logging.info(Select(el.get()).all_selected_options[0].text)
                            else:
                                selOption = Select(el.get()).all_selected_options
                                allOptions = Select(el.get()).options
                                stime=time.time()
                                if selOption[0] in allOptions:
                                    index = allOptions.index(selOption[0])
                                    while True:
                                        rd = random.randint(1, len(allOptions) - 1)

                                        if index != rd:
                                            Select(el.get()).select_by_index(rd)
                                            break
                                        if time.time()-stime>10:
                                            logging.error(str(len(allOptions))+',not other data')
                                            break
                        elif args[1] in currentscttext and u'请选择' not in currentscttext:
                            pass
                        else:
                            allOptions = Select(el.get()).options
                            for selem in allOptions:
                                if args[1].strip() == selem.text.strip():
                                    index = allOptions.index(selem)
                                    Select(el.get()).select_by_index(index)
                                    break
                            else:
                                logging.error(u'未找到此选项：' + args[1])
        
                        currenttxtList.append(args[1])
                    elif b.get('elementType') == 'input' or b.get('elementType') == 'textarea':
                        if args[0].strip()==u'完成时间':
                            func.driver.execute_script(
                                "var setDate=function $(id){ return document.getElementById(id); };setDate('field_completedate').removeAttribute('readonly');")
                        # elif args[0].strip()==u'评估总面积':
                        #     func.driver.execute_script("var setDate=function $(id){ return document.getElementById(id); };setDate('field_querytotalarea').removeAttribute('readonly');")
                            #el.get().clear()
                            #nowtime = time.strftime('%Y-%m-%d', time.localtime())
                            #l.get().send_keys(args[1])

                        el.get().clear()
                        el.get().send_keys(args[1])
                        currenttxtList.append(args[1])
                    elif b.get('elementType') == 'button':

                        """
                        if idatatype == u'查勘员':
                            ra.reportAdd().choices_Auser(func, el, 'Ctan1')
                            # self.bSwithcfrname(el, key)
                            try:
                                xf = func.driver.find_element_by_xpath(
                                    '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
                            except:
                                xf = func.driver.find_element_by_xpath(
                                    '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
                            func.driver.switch_to.frame(xf)

                        else:

                            if idatatype == u'报告撰写辅助人':
                                ra.reportAdd().choices_Auser(func, el, 'Mtan1')
                            elif idatatype == u'归档资料负责人':
                                ra.reportAdd().choices_Auser(func, el, 'Gtan1')
                            else:
                                ra.reportAdd().choices_Auser(func, el, 'Atan1')

                            #if args[1]!=None:
                                #self.choices_Quser(func,el,args[1])
                            """
                        if idatatype==u'添加估价师':
                            js = "var q=document.documentElement.scrollTop=10100"
                            func.driver.execute_script(js)
                            sleep(2)
                            ActionChains(el.getDriver()).move_to_element(el.get()).perform()
                            el.get_element('appraisersType')
                            el.gets()[0].click()
                            userdata=list(args)
                            userdata.pop(0)

                            self.choices_Auser(func, el,userdata)
                        else:
                            el.get().click()
                            self.choices_Muser(func,el,args[1])
                        self.bSwithcfrname(el, key)

                        el.getFunctionName(a[0])
                        el.get_element(a[j])
                        currenttxtList.append(args[1])
                    elif b.get('elementType') == 'checkbox':
                        el.get().click()
                        currenttxtList.append(args[1])
                    elif b.get('elementType') == 'readonly':
                        func.driver.execute_script(
                            "var setDate=function $(id){ return document.getElementById(id); };setDate(\"" + b.get(
                                'path') + "\").removeAttribute('readonly');")
                        el.get().clear()
                        el.get().send_keys(args[1])
                        currenttxtList.append(el.get().text)
                    else:
                        el.get().clear()
                        el.get().send_keys(args[1])
                        currenttxtList.append(el.get().text)
                    logging.info(args[0] +u':' +str(args[1:]))
                    break
        if idatatype==u'分支机构' or idatatype==u'委托类型':

            el.get_element(u'department')
            try:
                departmenttext = Select(el.get()).all_selected_options[0].text
            except Exception as e:
                logging.info(e)

            if u'请选择' in departmenttext:
                rdmod = random.randint(2, len(Select(el.get()).options) - 1)
                Select(el.get()).select_by_index(rdmod)
                logging.info(Select(el.get()).all_selected_options[0].text)


            el.get_element(u'technicalteam')
            try:
                currentscttext = Select(el.get()).all_selected_options[0].text
            except Exception as e:
                logging.info(e)
            if u'请选择' in currentscttext:
                rdmod = random.randint(2, len(Select(el.get()).options) - 1)
                Select(el.get()).select_by_index(rdmod)
                logging.info(Select(el.get()).all_selected_options[0].text)
        el.getFunctionName(dataDetail[0])
        if sub==u'正式报告':
            #完成时间
            el.get_element('completedate')
            if el.get().get_attribute('value')=='':
                func.driver.execute_script(
                    "var setDate=function $(id){ return document.getElementById(id); };setDate('field_completedate').removeAttribute('readonly');")
                el.get().clear()
                nowtime=time.strftime('%Y-%m-%d', time.localtime())
                el.get().send_keys(nowtime)

            #报告完成编号
            el.get_element('reportno')
            if el.get().get_attribute('value')=='':
                el.get_element('getNumber')
                el.get().click()

        # 业务部门
        el.get_element('department')
        if Select(el.get()).all_selected_options[0].text.strip() == u'请选择':
            rd = random.randint(1, len(Select(el.get()).options) - 1)
            Select(el.get()).select_by_index(rd)
        #技术团队
        el.get_element('technicalteam')
        if Select(el.get()).all_selected_options[0].text.strip()==u'请选择':
            rd=random.randint(1,len(Select(el.get()).options)-1)
            Select(el.get()).select_by_index(rd)
        time.sleep(1)
        func.driver.find_element_by_id('btnSave').click()
        if sub==u'业务登记':
            func.driver.switch_to.default_content()
            func.driver.find_element_by_xpath(u'//*[@value="确定"]').click()
        return dataId
    def choices_Auser(self,func,el,user='tan1'):
        self.switcthToDefault(func)
        el.getFunctionName(reportFrame[0])
        el.get_element('AbusinessUser')
        xf=el.get()
        func.driver.switch_to.frame(xf)
        sleep(1)
        currentUrl=func.driver.current_url
        logging.info(currentUrl)
        if 'Edit.aspx' in currentUrl:
            self.switcthToDefault(func)
            el.getFunctionName(reportFrame[0])
            el.get_element('dDetail')
            xf = el.get()
            func.driver.switch_to.frame(xf)
            currentUrl = func.driver.current_url
            logging.info(currentUrl)
        """
        el.getFunctionName(User[0])
        #el.get_element('sinput')
        #el.get().send_keys('ta')
        #el.get().send_keys(Keys.ENTER)
        #print user
        if type(user) is list:
            for i in user:
                el.get_element('sinput')
                el.get().clear()
                el.get().send_keys(i)
                el.get().send_keys(Keys.ENTER)
                el.get_element(i)
                el.get().click()
        else:
            el.get_element(user)
            el.get().click()
        """
        el.getFunctionName(User[0])
        el.get_element('sinput')
        if type(user) is list:
            for j in user:
                time.sleep(1.5)
                el.get().clear()
                el.get().send_keys(j)
                el.get().send_keys(Keys.ENTER)
                js = True
                i = 1
                utime=time.time()
                while js:
                    try:
                        txt = func.driver.find_element_by_id('userchkTree_' + str(i) + '_span').text.split(']')[1]

                        if txt.strip() == j.strip():
                            sleep(1)
                            func.driver.find_element_by_id('userchkTree_' + str(i) + '_check').click()
                            js = False
                            logging.info('Found user :'+j)
                    except:
                        pass
                    finally:
                        if time.time()-utime>240:
                            logging.error(u'Not found appraisers:'+j)
                            break
                        i += 1
        else:
            el.get().clear()
            el.get().send_keys(user)
            el.get().send_keys(Keys.ENTER)
            js = True
            i = 1
            utime = time.time()
            while js:
                try:
                    txt = func.driver.find_element_by_id('userchkTree_' + str(i) + '_span').text.split(']')[1]
                    if txt == user:

                        func.driver.find_element_by_id('userchkTree_' + str(i) + '_check').click()
                        js = False
                        logging.info('Found user :' + user)
                        break
                except:
                    pass
                finally:
                    if time.time() - utime > 240:
                        logging.error(u'Not found user:' + user)
                        exit()
                    i += 1

        el.get_element('btnOk')
        el.get().click()
    def chose_data(self, el,idNum=None,sub=None,data=None):
        """
        选择指定数据
        :param el:
        :param idNum:
        :param sub:
        :return:
        """
        dListID = []
        el.getFunctionName(tabledate[0])
        el.get_element(tabledate[1])
        dlist = el.gets()
        tabdataindex=None
        if idNum==None:

            if u'报告撰写辅助人' in data:
                for i in range(len(el.gets())):
                    if dlist[i].find_element_by_xpath(reportwriter).text==CFG.SessionUserName:
                        tabdataindex=i
                        dID = el.gets()[i].find_element_by_xpath(tableid).text
            else:
                rd=random.randint(0,len(dlist)-1)
                dID = el.gets()[rd].find_element_by_xpath(tableid).text
                tabdataindex=rd
        else:
            sleep(3)
            for i in range(len(el.gets())):
                idList=el.gets()[i].find_element_by_xpath(tableid).text
                if u'已完成' in el.gets()[i].find_element_by_xpath(tablink).text:
                    continue
                if idList.strip()==idNum:
                    tabdataindex=i
                    dID=idNum
                    break
            else:
                logging.error(u'no data')
                exit()
        logging.info(u'业务编号: '+str(dID))
        sleep(3)
        ActionChains(el.getDriver()).double_click(el.gets()[tabdataindex].find_element_by_xpath(tableid)).perform()
        return dID
    def choices_Muser(self,func,el,user):
        """
        选择用户
        :param func:
        :param el:
        :param user:
        :return:
        """
        self.switcthToDefault(func)
        el.getFunctionName(reportFrame[0])
        el.get_element('AbusinessUser')
        xf = el.get()
        func.driver.switch_to.frame(xf)
        sleep(3)
        currentUrl = func.driver.current_url
        logging.info(currentUrl)
        ststart=time.time()
        while  'Edit.aspx' in currentUrl:
            self.switcthToDefault(func)
            el.getFunctionName(reportFrame[0])
            el.get_element('dDetail')
            xf = el.get()
            func.driver.switch_to.frame(xf)
            currentUrl = func.driver.current_url
            logging.info(currentUrl)
            if time.time()-ststart>10:
                logging.error('not element,please check!')
                break

        el.getFunctionName(User[0])
        el.get_element('sinput')
        el.get().send_keys(user)
        el.get().send_keys(Keys.ENTER)
        js = True
        i = 1
        utime=time.time()
        while js:
            try:
                txt = func.driver.find_element_by_id('userchkTree_' + str(i) + '_span').text.split(']')[1]

                if txt == user:
                    func.driver.find_element_by_id('userchkTree_' + str(i) + '_check').click()
                    js = False
            except:
                pass
            finally:
                if time.time()-utime>10:
                    logging.error(u'Not found user:'+user)
                    break
                i += 1

        el.get_element('btnOk')
        el.get().click()
    def updtaObject(self,func,el,sub,**kwargs):
        self.reportTab(func, el, sub)
        dataId = self.chose_data(el)
        cn.switchToDetailUI(func, el)
        self.chkTab(el)
        el.getFunctionName(dataDetail[0])
        el.get_element('biztype')
        field_areaid = Select(el.get()).all_selected_options[0].text
        if u'请选择' in field_areaid:
            rdX = random.randint(2, len(Select(el.get()).options) - 1)
            Select(el.get()).select_by_index(rdX)
            XZQtxt = Select(el.get()).all_selected_options[0].text
            logging.info(XZQtxt)
        else:
            logging.info(field_areaid)

        el.get_element('addObject')
        ActionChains(el.getDriver()).move_to_element(el.get()).perform()
        el.get_element('addObjectType')
        el.gets()[0].click()
        logging.info(u'进入委估对象界面')
        sleep(3)
        func.driver.switch_to.default_content()
        # self.duserSwitchFrame(el)
        xf = el.getDriver().find_element_by_xpath(
            '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
        el.getDriver().switch_to.frame(xf)
        txt = 'http://gjb.fxtchina.com/Reports/ReportEdit.aspx?reportid=0&callback=search&dotype=putong'
        cuturl = func.driver.current_url

        if cuturl == txt:
            func.driver.switch_to.default_content()
            xf = el.getDriver().find_element_by_xpath(
                '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
            el.getDriver().switch_to.frame(xf)
            newurl = func.driver.current_url

        sleep(2)
        self.chkTab(el)
        a = EL.get_el_list('EntrustObject', cg.path)
        el.getFunctionName('EntrustObject')

        # 行政区
        el.get_element('xingzhengqu')
        field_areaid = Select(el.get()).all_selected_options[0].text
        if u'请选择' in field_areaid:
            rdX = random.randint(2, len(Select(el.get()).options) - 1)
            Select(el.get()).select_by_index(rdX)
            XZQtxt = Select(el.get()).all_selected_options[0].text
            el.get_element('quyu')
            if len(Select(el.get()).options) > 2:
                rdQ = random.randint(2, len(Select(el.get()).options) - 1)
                Select(el.get()).select_by_index(rdQ)
                QYtxt = Select(el.get()).all_selected_options[0].text
            else:
                QYtxt = ''
            logging.info(u'行政区：' + XZQtxt + QYtxt)
            # 委估对象全称
            el.get_element('weiguduixiangquancheng')
            el.get().send_keys('weiguduixiangquancheng')
            logging.info(u'委估对象名称:')
            # 建筑面积
            el.get_element('jianzhumianji')
            logging.info(u'建筑面积:')
            el.get().send_keys('100')

        if kwargs == {}:
            DataE = EjsonData
        else:
            DataE = kwargs

        for i in DataE.keys():

            for j in range(1, len(a)):
                b = EL.get_el_dict(a[0], a[j], cg.path)
                if b.get('name') == i:
                    el.getFunctionName(a[0])
                    # el.get_element(a[j])
                    # el.get()
                    # break
                    dictFunction = EL.get_el_dict(a[0], a[j], cg.path)
                    el.get_element(a[j])
                    if 'elementType' in dictFunction:
                        if dictFunction['elementType'] == 'select':
                            field_areaid = Select(el.get()).all_selected_options[0].text
                            '''
                            if u'请选择' in field_areaid:
                                rdX = random.randint(2, len(Select(el.get()).options) - 1)
                                Select(el.get()).select_by_index(rdX)
                                XZQtxt = Select(el.get()).all_selected_options[0].text
                            '''
                            if field_areaid == DataE[i]:
                                pass
                            else:
                                txtcontent = Select(el.get()).options
                                for x in range(len(txtcontent)):

                                    if txtcontent[x].text == DataE[i]:
                                        Select(el.get()).select_by_index(x)
                        elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                            el.get().send_keys(DataE[i])
                        else:
                            pass

        el.get_element('btnSave')
        el.get().click()
class ModificationCheck(Modification):
    def check_updateGeneral(self, func, el, sub, *args):
        dataId=Modification().updateGeneral(func, el, sub, *args)
        sleep(3)
        self.mswitchfrname(func,el,sub)
        self.chose_data(el,dataId,data=args)
        # if args[0] == u'评估方法':
        #     currenttxtList = []
        #     if type(args[1]) == list:
        #         pass
        #     else:
        #         if args[1].strip() == u'比较法':
        #             if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[1]').get_attribute(
        #                     'checked') == 'true':
        #                 currenttxtList.append(func.driver.find_element_by_xpath(
        #                     '//*[@id="field_valuationmethods"]/input[1]').get_attribute('value'))
        #                 return True
        #             else:
        #                 logging.error('not checked!!!')
        #                 return False
        #         elif args[1] == u'收益法':
        #             func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[2]').click()
        #             if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[2]').get_attribute(
        #                     'checked') == 'true':
        #                 currenttxtList.append(func.driver.find_element_by_xpath(
        #                     '//*[@id="field_valuationmethods"]/input[2]').get_attribute('value'))
        #                 return True
        #             else:
        #                 logging.error('not checked!!!')
        #                 return False
        #         elif args[1] == u'成本法':
        #             func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[3]').click()
        #             if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[3]').get_attribute(
        #                     'checked') == 'true':
        #                 currenttxtList.append(func.driver.find_element_by_xpath(
        #                     '//*[@id="field_valuationmethods"]/input[3]').get_attribute('value'))
        #                 return True
        #             else:
        #                 logging.error('not checked!!!')
        #                 return False
        #         elif args[1] == u'假设开发法':
        #             func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[4]').click()
        #             if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[4]').get_attribute(
        #                     'checked') == 'true':
        #                 currenttxtList.append(func.driver.find_element_by_xpath(
        #                     '//*[@id="field_valuationmethods"]/input[4]').get_attribute('value'))
        #                 return True
        #             else:
        #                 logging.error('not checked!!!')
        #                 return False
        #         elif args[1] == u'基准地价修正法':
        #             func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[5]').click()
        #             if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[5]').get_attribute(
        #                     'checked') == 'true':
        #                 currenttxtList.append(func.driver.find_element_by_xpath(
        #                     '//*[@id="field_valuationmethods"]/input[5]').get_attribute('value'))
        #                 return True
        #             else:
        #                 logging.error('not checked!!!')
        #                 return False
        #         elif args[1] == u'路线价法':
        #             func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[6]').click()
        #             if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[6]').get_attribute(
        #                     'checked') == 'true':
        #                 currenttxtList.append(func.driver.find_element_by_xpath(
        #                     '//*[@id="field_valuationmethods"]/input[6]').get_attribute('value'))
        #                 return True
        #             else:
        #                 logging.error('not checked!!!')
        #                 return False
        #         elif args[1] == u'长期趋势法':
        #             func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[7]').click()
        #             if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[7]').get_attribute(
        #                     'checked') == 'true':
        #                 currenttxtList.append(func.driver.find_element_by_xpath(
        #                     '//*[@id="field_valuationmethods"]/input[7]').get_attribute('value'))
        #                 return True
        #             else:
        #                 logging.error('not checked!!!')
        #                 return False
        #         else:
        #             logging.error(u'没有此评估方法，请确认')
        #             exit(u'没有此评估方法，请确认')
        #         # delist = func.driver.find_elements_by_xpath('//*[@id="field_valuationmethods"]/input')
        #         # txtlist = func.driver.find_elements_by_xpath('//*[@id="field_valuationmethods"]/input')
        #         # for i in range(len(delist)):
        #         #     try:
        #         #         if delist[i].get_attribute('checked') == 'checked':
        #         #             return True
        #         #
        #         #     except:
        #         #         continue
        #         # else:
        #         #     logging.error(u'没有此评估方法，请确认')
        #         #     exit(u'没有此评估方法，请确认')
        #
        #
        # else:
        # elType=''
        # a= EL.get_el_list('RPdataDetail', cg.path)
        # for j in range(1, len(a)):
        #     b = EL.get_el_dict(a[0], a[j], cg.path)
        #
        #     if b.get('name').strip() == args[0].strip():
        #         elname=a[j]
        #         elType=b.get('elementType')
        #         break
        # else:
        #     logging.error('not found element name !')
        #     exit()

        cn.switchToDetailUI(func, el)
        self.chkTab(el)
        if args[0] == u'评估方法':
            currenttxtList = []
            if type(args[1]) == list:
                pass
            else:
                if args[1].strip() == u'比较法':
                    if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[1]').get_attribute(
                            'checked') == 'true':
                        currenttxtList.append(func.driver.find_element_by_xpath(
                            '//*[@id="field_valuationmethods"]/input[1]').get_attribute('value'))
                        return True
                    else:
                        logging.error('not checked!!!')
                        return False
                elif args[1] == u'收益法':
                    func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[2]').click()
                    if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[2]').get_attribute(
                            'checked') == 'true':
                        currenttxtList.append(func.driver.find_element_by_xpath(
                            '//*[@id="field_valuationmethods"]/input[2]').get_attribute('value'))
                        return True
                    else:
                        logging.error('not checked!!!')
                        return False
                elif args[1] == u'成本法':
                    func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[3]').click()
                    if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[3]').get_attribute(
                            'checked') == 'true':
                        currenttxtList.append(func.driver.find_element_by_xpath(
                            '//*[@id="field_valuationmethods"]/input[3]').get_attribute('value'))
                        return True
                    else:
                        logging.error('not checked!!!')
                        return False
                elif args[1] == u'假设开发法':
                    func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[4]').click()
                    if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[4]').get_attribute(
                            'checked') == 'true':
                        currenttxtList.append(func.driver.find_element_by_xpath(
                            '//*[@id="field_valuationmethods"]/input[4]').get_attribute('value'))
                        return True
                    else:
                        logging.error('not checked!!!')
                        return False
                elif args[1] == u'基准地价修正法':
                    func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[5]').click()
                    if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[5]').get_attribute(
                            'checked') == 'true':
                        currenttxtList.append(func.driver.find_element_by_xpath(
                            '//*[@id="field_valuationmethods"]/input[5]').get_attribute('value'))
                        return True
                    else:
                        logging.error('not checked!!!')
                        return False
                elif args[1] == u'路线价法':
                    func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[6]').click()
                    if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[6]').get_attribute(
                            'checked') == 'true':
                        currenttxtList.append(func.driver.find_element_by_xpath(
                            '//*[@id="field_valuationmethods"]/input[6]').get_attribute('value'))
                        return True
                    else:
                        logging.error('not checked!!!')
                        return False
                elif args[1] == u'长期趋势法':
                    func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[7]').click()
                    if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[7]').get_attribute(
                            'checked') == 'true':
                        currenttxtList.append(func.driver.find_element_by_xpath(
                            '//*[@id="field_valuationmethods"]/input[7]').get_attribute('value'))
                        return True
                    else:
                        logging.error('not checked!!!')
                        return False
                else:
                    logging.error(u'没有此评估方法，请确认')
                    exit(u'没有此评估方法，请确认')
        else:
            elType = ''
            a = EL.get_el_list('RPdataDetail', cg.path)
            for j in range(1, len(a)):
                b = EL.get_el_dict(a[0], a[j], cg.path)

                if b.get('name').strip() == args[0].strip():
                    elname = a[j]
                    elType = b.get('elementType')
                    break
            else:
                logging.error('not found element name !')
                exit()

        if elType=='button':
            if args[0] == u'添加估价师':
                el.getFunctionName(dataDetail[0])
                el.get_element('appraisersTable')
                CAtables = el.gets()
                atabledata=args[1:]
                if len(atabledata)<2:
                    if len(CAtables) > 2:
                        if CAtables[2].find_elements_by_xpath('td')[1].text ==atabledata[0]:
                            return True
                else:
                    for i in range(2,len(CAtables)):#判断是否已添加估价师
                        logging.info(u'估价师：'+CAtables[i].find_elements_by_xpath('td')[1].text)
                        if CAtables[i].find_elements_by_xpath('td')[1].text not in atabledata:
                            return False
                    else:
                        return True

                return False

            b = EL.get_el_list(Usertxt[0], cg.path)
            for j in range(1, len(b)):
                c = EL.get_el_dict(b[0], b[j], cg.path)

                if c.get('name').strip() == args[0].strip():
                    if sub==u'业务登记'and args[0]==u'业务员':
                        elnametxt='BusinessUserName'
                        break
                    elnametxt = b[j]
                    break
            else:
                logging.error('not found!')
                exit()
            rname=cn.GetDetail(func,el,Usertxt,elnametxt)
        else:
            if args[0]==u'城市':
                resultlist=[]
                ddata=args[1].split(' ')
                el.getFunctionName('RPdataDetail')
                for i in range(len(ddata)):
                    if i==0:
                        elname='Province'
                    elif i==1:
                        elname='city'
                    elif i==2:
                        el.get_element('area')
                    elif i==3:
                        elname='subarea'
                    else:
                        logging.info(u'输入的数据不对')
                        exit()
                    resultlist.append(cn.GetDetail(func, el, dataDetail, elname))
                if ddata==resultlist:
                     return True
                else:
                     return False

            rname=cn.GetDetail(func,el,dataDetail,elname)
        if args[1]==None:
            return True
        else:
            if rname.strip()==args[1].strip():
                return True
        return False




