#-*- coding:utf-8 -*-
import os
import random
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
User=cg.reportUser
tabledate=cg.tableData
tabchk=cg.reportTabchk
dataDetail=cg.reportDataDetail
reportFrame=cg.reportFrame
EjsonData=cg.EjsonData
key=u'新增'
class reportAdd(reportBase):
    def report(self,func,el,sub):
        """
        进入新增界面
        :param func:
        :param el:
        :param sub: 模块类型
        :return:
        """
        self.clickFunction(func, el, sub, key)
        sleep(5)
        self.bSwithcfrname(el, key)
        self.tabcheck(el)
        sleep(1)
    def reportadd(self,func,el,sub,button=None,**args):
        oldIDlist=self.clickFunction(func,el,sub,key)
        sleep(3)
        self.bSwithcfrname(el,key)
        self.tabcheck(el)
        RPdataDetail = EL.get_el_list('RPdataDetail', cg.path)
        currenttxtList=[]
        self.checkKeys(func, el, key,sub)

        #通过字典类型来判断数据类型，通过字典的值来填写数据
        if  u'委托客户' in args.keys():
            if u'委托客户分行' in args.keys() and len(args.keys())>=3:
                wtkh=[u'委托客户',u'委托客户分行',u'委托客户支行']
            else:
                wtkh=args.keys()
            for i in wtkh:
                for j in range(1, len(RPdataDetail)):
                    RPdataDetaildict = EL.get_el_dict(RPdataDetail[0], RPdataDetail[j], cg.path)
                    if RPdataDetaildict.get('name').strip() == i.strip():
                        el.getFunctionName(RPdataDetail[0])
                        el.get_element(RPdataDetail[j])
                        currentscttext = Select(el.get()).all_selected_options[0].text
                        if args[i] == None:
                            if u'请选择' in currentscttext:
                                rdmod = random.randint(1, len(Select(el.get()).options) - 1)
                                Select(el.get()).select_by_index(rdmod)
                                logging.info(Select(el.get()).all_selected_options[0].text)
                            else:
                                selOption = Select(el.get()).all_selected_options
                                allOptions = Select(el.get()).options

                                if selOption[0] in allOptions:
                                    index = allOptions.index(selOption[0])
                                    while True:
                                        rd = random.randint(1, len(allOptions) - 1)
                                        if index != rd:
                                            Select(el.get()).select_by_index(rd)
                        elif args[i] in currentscttext and u'请选择' not in currentscttext:
                            pass
                        else:
                            allOptions = Select(el.get()).options
                            for selem in allOptions:
                                if args[i].strip() == selem.text.strip():
                                    index = allOptions.index(selem)
                                    Select(el.get()).select_by_index(index)
                                    sleep(1)
                                    break
                            else:
                                logging.error(u'未找到此选项：' + args[i])
                                exit(u'未找到此选项：' + args[i])
                        currenttxtList.append(args[i])
                        break
                else:
                    logging.error(u'not found:' + i)
                    currenttxtList.append('false')
        else:
            for i in args.keys():
                if i.strip() == u'评估方法':
                    if type(args[i]) == list:
                        pass
                    else:
                        if args[i]==u'比较法':
                            if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[1]').get_attribute('checked')!='true':
                                func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[1]').click()
                            currenttxtList.append(u'比较法')
                        elif args[i]==u'收益法':
                            if func.driver.find_element_by_xpath(
                                    '//*[@id="field_valuationmethods"]/input[2]').get_attribute('checked') != 'true':
                                func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[2]').click()
                            currenttxtList.append(u'收益法')
                        elif args[i]==u'成本法':
                            if func.driver.find_element_by_xpath(
                                    '//*[@id="field_valuationmethods"]/input[3]').get_attribute('checked') != 'true':
                                func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[3]').click()
                            currenttxtList.append(u'成本法')
                        elif args[i]==u'假设开发法':
                            if func.driver.find_element_by_xpath(
                                    '//*[@id="field_valuationmethods"]/input[4]').get_attribute('checked') != 'true':
                                func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[4]').click()
                            currenttxtList.append(u'假设开发法')
                        elif args[i]==u'基准地价修正法':
                            if func.driver.find_element_by_xpath(
                                    '//*[@id="field_valuationmethods"]/input[5]').get_attribute('checked') != 'true':
                                func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[5]').click()
                            currenttxtList.append(u'基准地价修正法')
                        elif args[i]==u'路线价法':
                            if func.driver.find_element_by_xpath(
                                    '//*[@id="field_valuationmethods"]/input[6]').get_attribute('checked') != 'true':
                                func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[6]').click()
                            currenttxtList.append(u'路线价法')
                        elif args[i]==u'长期趋势法':
                            if func.driver.find_element_by_xpath(
                                    '//*[@id="field_valuationmethods"]/input[7]').get_attribute('checked') != 'true':
                                func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[7]').click()
                            currenttxtList.append(u'长期趋势法')
                else:
                    for j in range(1, len(RPdataDetail)):
                        RPdataDetaildict=EL.get_el_dict(RPdataDetail[0], RPdataDetail[j], cg.path)
                        if  RPdataDetaildict.get('name').strip()==i.strip():
                            el.getFunctionName(RPdataDetail[0])
                            el.get_element(RPdataDetail[j])
                            if RPdataDetaildict.get('elementType')== 'select':
                                try:
                                    currentscttext = Select(el.get()).all_selected_options[0].text
                                except:
                                    logging.error(u'请确实是否有此字段')
                                    exit(u'请确实是否有此字段')
                                if args[i] == None or args[i]=='None':
                                    if u'请选择' in currentscttext:
                                        rdmod = random.randint(1, len(Select(el.get()).options) - 1)
                                        Select(el.get()).select_by_index(rdmod)
                                        logging.info(Select(el.get()).all_selected_options[0].text)
                                    else:
                                        selOption = Select(el.get()).all_selected_options
                                        allOptions = Select(el.get()).options
                                        if selOption[0] in allOptions:
                                            index = allOptions.index(selOption[0])
                                            while True:
                                                rd = random.randint(1, len(allOptions) - 1)
                                                if index != rd:
                                                    Select(el.get()).select_by_index(rd)
                                elif args[i] in currentscttext and u'请选择' not in currentscttext:
                                    pass
                                else:
                                    allOptions = Select(el.get()).options
                                    for selem in allOptions:
                                        if args[i].strip() == selem.text.strip():
                                            index = allOptions.index(selem)
                                            Select(el.get()).select_by_index(index)
                                            break
                                    else:
                                        logging.error(u'未找到此选项：' + args[i])
                                        exit(u'未找到此选项：' + args[i])
                                currenttxtList.append(args[i])


                                #currenttxtList.append(Select(el.get()).all_selected_options[0].text)
                            elif RPdataDetaildict.get('elementType')== 'input' or RPdataDetaildict.get('elementType')== 'textarea':
                                el.get().clear()
                                el.get().send_keys(args[i])
                                currenttxtList.append(args[i])

                                #currenttxtList.append(el.get().get_attribute('value'))
                            elif RPdataDetaildict.get('elementType')== 'button':
                                el.get().click()
                                if i==u'查勘员':
                                    self.choices_Auser(func, el, 'tan1')

                                    try:
                                        xf=func.driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
                                    except:
                                        xf = func.driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
                                    func.driver.switch_to.frame(xf)

                                else:
                                    if i==u'报告撰写辅助人':
                                        self.choices_Auser(func, el, 'tan1')
                                    elif i==u'归档资料负责人':
                                        self.choices_Auser(func, el, 'tan1')
                                    else:
                                        self.choices_Auser(func,el,'tan1')
                                    self.bSwithcfrname(el, key)
                                el.getFunctionName(RPdataDetail[0])
                                el.get_element(RPdataDetail[j])
                                currenttxtList.append(args[i])
                            elif RPdataDetaildict.get('elementType') == 'checkbox':
                                el.get().click()
                                currenttxtList.append(args[i])
                            elif RPdataDetaildict.get('elementType')== 'readonly':
                                func.driver.execute_script("var setDate=function $(id){ return document.getElementById(id); };setDate(\"" + RPdataDetaildict.get('path') + "\").removeAttribute('readonly');")
                                el.get().clear()
                                el.get().send_keys(args[i])
                                currenttxtList.append(el.get().text)
                            else:
                                el.get().clear()
                                el.get().send_keys(args[i])
                                currenttxtList.append( el.get().text)
                            logging.info(i+':'+args[i])
                            if i == u'分支机构':
                                # 技术团队
                                el.get_element('technicalteam')
                                rd = random.randint(1, len(Select(el.get()).options) - 1)
                                Select(el.get()).select_by_index(rd)
                                logging.info(u'技术团队：' + Select(el.get()).all_selected_options[0].text)
                                #业务部门
                                el.get_element('department')
                                rd = random.randint(1, len(Select(el.get()).options) - 1)
                                Select(el.get()).select_by_index(rd)
                                logging.info(u'业务部门：' + Select(el.get()).all_selected_options[0].text)
                            elif i == u'委托类型':
                                # 技术团队
                                el.get_element('technicalteam')
                                rd = random.randint(1, len(Select(el.get()).options) - 1)
                                Select(el.get()).select_by_index(rd)
                                logging.info(u'技术团队：' + Select(el.get()).all_selected_options[0].text)

                            break
                    else:
                        logging.error(u'not found,'+i)
                        currenttxtList.append('false')
                    '''
                    elif i.strip() == u'评估方法':
                        el.getFunctionName(RPdataDetail[0])
                        el.get_element(RPdataDetail[j])
                        if type(args[i])==list:
                            pass
                        else:
    
                            if RPdataDetaildict.get('name').strip()==args[i].strip():
                                el.get().click()
                    '''

        el.getFunctionName('RPdataDetail')
        if button==None:
            pass
        else:
            for j in range(1, len(RPdataDetail)):
                RPdataDetaildict = EL.get_el_dict(RPdataDetail[0], RPdataDetail[j], cg.path)
                if RPdataDetaildict.get('name') ==button:
                    el.getFunctionName(RPdataDetail[0])
                    el.get_element(RPdataDetail[j])
                    el.get().click()

                    func.driver.switch_to.default_content()
                    xf = func.driver.find_element_by_xpath(
                        '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
                    func.driver.switch_to.frame(xf)
                    urltxt = func.driver.current_url



                    if 'create.aspx' not in urltxt:
                        func.driver.switch_to.default_content()
                        xf = func.driver.find_element_by_xpath(
                            '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
                        func.driver.switch_to.frame(xf)
                        #print func.driver.current_url


                    if button==u'生成报告':
                        if sub==u'正式报告':
                            elrd=func.driver.find_elements_by_xpath('//*[@id="table"]/table/tbody/tr[3]/td[2]/label')
                            rd=random.randint(0,len(elrd)-1)
                            elrd[rd].click()
                            # TODO 进行工具测试
                            # elrd[2].click()
                    else:
                        pass
                        '''
                        func.driver.switch_to.default_content()
                        xf = func.driver.find_element_by_xpath(
                            '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
                        func.driver.switch_to.frame(xf)
                        urltxt = func.driver.current_url
                        print urltxt
                        if 'create.aspx' not in urltxt:
                            func.driver.switch_to.default_content()
                            xf = func.driver.find_element_by_xpath(
                                '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
                            func.driver.switch_to.frame(xf)
                            print func.driver.current_url
                        '''
                    func.driver.find_element_by_id('complt').click()
                    mdl = func.driver.find_elements_by_xpath('/html/body/div[2]/div/table/tbody/tr')

                    rds = random.randint(0, len(mdl) - 1)
                    mdl[rds].click()
                    #TODO 进行工具测试
                    # for i in range(len(mdl)):
                    #     #print mdl[i].find_element_by_tag_name('td').get_attribute('text')==u'TEST测试模板'
                    #     if mdl[i].find_element_by_tag_name('td').get_attribute('text').strip()==u'TEST测试模板':
                    #         mdl[i].find_element_by_tag_name('td').click()
                    #         break
                    # else:
                    #     print u'没发现模板'
                    #     exit()

                    func.driver.find_element_by_id('btnCreateReport').click()
                    #TODO 单独自动化测试
                    # pngnum=str(time.time())
                    # print pngnum
                    # save_fn=r'D:\\img/'+pngnum+'.png'
                    # func.driver.find_element_by_id('btnCreateReport').click()
                    # func.driver.save_screenshot(save_fn)



                    func.driver.switch_to.default_content()
                    xf = func.driver.find_element_by_xpath(
                        '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
                    func.driver.switch_to.frame(xf)
                    urltxt = func.driver.current_url
                    #print urltxt
                    if 'EditReportFromTemplate' not in urltxt:
                        func.driver.switch_to.default_content()
                        xf = func.driver.find_element_by_xpath(
                            '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
                        func.driver.switch_to.frame(xf)
                        #print func.driver.current_url
                    btsave=func.driver.find_element_by_id('btnCreate')
                    while not btsave.is_enabled():
                        sleep(2)

                    btsave.click()
                    func.driver.switch_to.alert.accept()
                    return
        if sub==u'业务登记':
            el.get_element('btnSubmit')
            el.get().click()
            func.driver.switch_to.default_content()
            sleep(1)
            func.driver.find_element_by_xpath(u'//*[@value="直接提交"]').click()
            sleep(0.5)
            func.driver.find_element_by_xpath(u'//*[@value="确定"]').click()
        else:
            el.get_element('btnsave')
            el.get().click()

        return currenttxtList
    def tabcheck(self,el):
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
            #if 'checked' in tabatb:
            if tabatb=='true':
                logging.info(u'不勾选Tab')
                el.get_element('tabchkbox')
                el.get().click()
        except:
            logging.info(u'Tab未被勾选')
    def checkKeys(self,func,el,key,sub=u'正式报告'):
        """
        检查必填项
        :param func:
        :param el:
        :param key:
        :return:
        """

        if sub==u'业务登记':
            pass
        else:
            el.getFunctionName('RPdataDetail')
            el.get_element('SelectUser')
            el.get().click()
            self.choices_Auser(func,el,'tan1')
            self.duserSwitchFrame(el)
        el.getFunctionName('RPdataDetail')

        #委托类型
        el.get_element('biztype')
        bizS=Select(el.get())
        if bizS.all_selected_options[0].text.strip()==u'请选择':
            rdB=random.randint(1,len(Select(el.get()).options)-1)
            Select(el.get()).select_by_index(rdB)

        sleep(1)
        #技术团队
        el.get_element('technicalteam')
        rd = random.randint(1, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rd)
        logging.info(u'技术团队：' + Select(el.get()).all_selected_options[0].text)

        # 报告类型
        el.get_element('reporttypecode')
        #bizS = Select(el.get())
        # if bizS.all_selected_options[0].text.strip() == u'请选择':
        #     rdR = random.randint(1, len(Select(el.get()).options) - 1)
        #     Select(el.get()).select_by_index(rdR)
        # logging.info(u'报告类型：' + Select(el.get()).all_selected_options[0].text)
        #TODO 自动化单独测试或指定报告类型
        sleep(1)
        selels=Select(el.get()).options
        for i in range(len(selels)):
            if selels[i].text.strip()==u'房地产评估':
                Select(el.get()).select_by_index(i)
                break
        else:
            logging.info(u'没找到房地产评估')

        logging.info(u'报告类型：' + Select(el.get()).all_selected_options[0].text)

        if sub==u'正式报告':
            el.get_element('completedate')
            nowtime=time.strftime('%Y-%m-%d %X',time.localtime())
            logging.info(u'输入完成时间：'+nowtime)
            el.get().send_keys(nowtime)

            logging.info(u'点击获取报告编号')
            el.get_element('getNumber')
            el.get().click()
    def choices_Auser(self,func,el,user='tan1'):
        """

        :param func:
        :param el:
        :param user:
        :return:
        """
        self.switcthToDefault(func)
        el.getFunctionName(reportFrame[0])
        el.get_element('AbusinessUser')
        xf=el.get()
        func.driver.switch_to.frame(xf)
        sleep(3)
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
                            logging.error(u'Not found user:'+user)
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
                    #print func.driver.find_element_by_id('userchkTree_' + str(i) + '_span').text
                    txt = func.driver.find_element_by_id('userchkTree_' + str(i) + '_span').text.split(']')[1]
                    #print txt,i,js
                    if txt == user:
                        #print 111
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
    def duserSwitchFrame(self,el):
        sleep(1)
        try:
            xf = el.getDriver().find_element_by_xpath(
                '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
        except:
            xf = el.getDriver().find_element_by_xpath(
                '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
        el.getDriver().switch_to.frame(xf)
    def get_tabledData(self,func,el,sub,**kwargs):
        """

        :param func:
        :param el:
        :param sub:
        :param kwargs:
        :return:
        """
        sleep(3)
        self.mswitchfrname(func,el,sub)
        el.getFunctionName(tabledate[0])
        el.get_element(tabledate[1])
        sleep(3)
        logging.info(el.gets()[0].find_element_by_xpath('td[2]/div').text)
        ActionChains(el.getDriver()).double_click(el.gets()[0].find_element_by_xpath('td[2]/div')).perform()
        #sleep(5)
        self.bSwithcfrname(el,u'新增')
        currenttxtList = []
        a = EL.get_el_list('RPdataDetail', cg.path)
        for i in kwargs.keys():
            if i.strip() == u'评估方法':
                if type(kwargs[i]) == list:
                    pass
                else:
                    if kwargs[i].strip()==u'比较法':
                        if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[1]').get_attribute('checked')=='true':
                            currenttxtList.append(func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[1]').get_attribute('value'))
                        else:
                           logging.error('not checked!!!')
                    elif kwargs[i]==u'收益法':
                        func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[2]').click()
                        if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[2]').get_attribute('checked')=='true':
                            currenttxtList.append(func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[2]').get_attribute('value'))
                        else:
                           logging.error('not checked!!!')
                    elif kwargs[i]==u'成本法':
                        func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[3]').click()
                        if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[3]').get_attribute('checked')=='true':
                            currenttxtList.append(func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[3]').get_attribute('value'))
                        else:
                           logging.error('not checked!!!')
                    elif kwargs[i]==u'假设开发法':
                        func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[4]').click()
                        if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[4]').get_attribute('checked')=='true':
                            currenttxtList.append(func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[4]').get_attribute('value'))
                        else:
                           logging.error('not checked!!!')
                    elif kwargs[i]==u'基准地价修正法':
                        func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[5]').click()
                        if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[5]').get_attribute('checked')=='true':
                            currenttxtList.append(func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[5]').get_attribute('value'))
                        else:
                           logging.error('not checked!!!')
                    elif kwargs[i]==u'路线价法':
                        func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[6]').click()
                        if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[6]').get_attribute('checked')=='true':
                            currenttxtList.append(func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[6]').get_attribute('value'))
                        else:
                           logging.error('not checked!!!')
                    elif kwargs[i]==u'长期趋势法':
                        func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[7]').click()
                        if func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[7]').get_attribute('checked')=='true':
                            currenttxtList.append(func.driver.find_element_by_xpath('//*[@id="field_valuationmethods"]/input[7]').get_attribute('value'))
                        else:
                           logging.error('not checked!!!')

            else:
                for j in range(1, len(a)):
                    b = EL.get_el_dict(a[0], a[j], cg.path)
                    if b.get('name').strip()==i.strip():
                        el.getFunctionName(a[0])
                        el.get_element(a[j])
                        if b.get('elementType') == 'select':
                            sleep(3)
                            currentscttext = Select(el.get()).all_selected_options[0].text.strip()
                            currenttxtList.append(currentscttext)
                        elif b.get('elementType') == 'input' or b.get('elementType') == 'textarea':
                            #try:
                            currenttxtList.append(el.get().get_attribute('value'))
                            #except:
                                #exit()
                        elif b.get('elementType')=='button':
                            currenttxtList.append('tan1')
                        elif b.get('elementType') == 'checkbox':
                            if b.get('name')==u'是否月结':
                                currenttxtList.append(u'是')
                        else:
                            currenttxtList.append(el.get().text)
        return currenttxtList
    def roundColumn(self, func, el, sub, **kwargs):
        """

        :param func:
        :param el:
        :param sub:
        :param kwargs:
        :return:
        """
        #key = u'新增'
        self.clickFunction(func, el, sub, key)
        sleep(5)
        self.bSwithcfrname(el, key)
        self.tabcheck(el)
        a = EL.get_el_list('RPdataDetail', cg.path)
        currenttxtList = []
        sEl=None
        eEl=None
        for i in kwargs.keys():
            for j in range(1, len(a)):
                b = EL.get_el_dict(a[0], a[j], cg.path)
                el.getFunctionName(a[0])
                el.get_element(a[j])
                if b.get('name').strip() == i.strip():
                    sEl=el.get()
                    sElId=el.path
                if b.get('name').strip()==(i+kwargs[i]).strip():
                    eEl=el.get()

            for x,y in enumerate([100,101,104,105,140,150,1400,1500,14000,15000]):#[100.4,100.5,104,105,140,150,1400,1500,14000,15000]
                #TODO 无法输入float数据
                sEl.clear()
                sEl.send_keys(str(y))
                '''
                func.driver.execute_script(
                    "var setDate=function $(id){ return document.getElementById(id); };setDate(\"" + sElId + "\").value=\"" + str(y) + "\",")
                print sEl.get_attribute('value')
                '''
                Select(eEl).select_by_index(x/2+1)
                currenttxtList.append(sEl.get_attribute('value').replace(',',''))
        return currenttxtList
    def autoCalculate(self, func, el, Ldata, sub):
        """

        :param func:
        :param el:
        :param Ldata:
        :param sub:
        :return:
        """
        #key = u'新增'
        self.clickFunction(func, el, sub, key)
        sleep(5)
        self.bSwithcfrname(el, key)
        self.tabcheck(el)
        a= EL.get_el_list('RPdataDetail', cg.path)
        aEl=None
        bEl=None
        el.getFunctionName(a[0])
        for j in range(1, len(a)):
            b = EL.get_el_dict(a[0], a[j], cg.path)
            if Ldata[0].keys()[0]==b.get('name').strip():
                el.get_element(a[j])
                aEl = el.get()
                continue

            if Ldata[1].keys()[0]==b.get('name').strip():
                el.get_element(a[j])
                bEl = el.get()
                continue

            if len(Ldata)>2:
                for i in range(len(Ldata[2])):
                    if Ldata[2].keys()[i]==b.get('name').strip():
                        el.get_element(a[j])
                        el.get().send_keys(Ldata[2].values()[0])
            if len(Ldata)>3:
                for i in range(len(Ldata[3])):
                    if Ldata[3].keys()[i]==b.get('name').strip():
                        el.get_element(a[j])
                        el.get().send_keys(Ldata[3].values()[0])


        aEl.send_keys(Ldata[0].values()[0])
        currentTxt=bEl.get_attribute('lastvalue')
        #print currentTxt
        return currentTxt
    def add_Appraisers(self,func,el,users,sub):
        """
        新增估价师
        :param func:
        :param el:
        :param users:
        :param sub:
        :return:
        """
        self.clickFunction(func, el, sub, key)
        sleep(5)
        self.bSwithcfrname(el, key)
        self.tabcheck(el)
        js = "var q=document.documentElement.scrollTop=10000"
        func.driver.execute_script(js)
        sleep(1)
        el.getFunctionName(dataDetail[0])
        el.get_element('appraisers')
        ActionChains(el.getDriver()).move_to_element(el.get()).perform()
        el.get_element('appraisersType')
        el.gets()[0].click()

        self.choices_Auser(func,el,users)

        """
        if users==None:
            self.choices_Auser(func,el,'GAtan1')
        else:
            a = EL.get_el_list('RPuser', cg.path)
            uList=[]
            #for i in a:
                #if 'GA' in i:
            for j in range(1, len(a)):
                b = EL.get_el_dict(a[0], a[j], cg.path)
                if b.get('name').strip() in users and 'GA' in a[j]:
                    uList.append(a[j])
                    continue
            self.choices_Auser(func,el,uList)
        """
    def add_Att(self,func,el,sub):
        self.clickFunction(func, el, sub, key)
        sleep(5)
        self.bSwithcfrname(el, key)
        self.tabcheck(el)
        el.getFunctionName('RPdataDetail')
        el.get_element('filetypecode')
        # selSC=Select(el.get()).all_selected_options[0].text
        # if u'请选择' in selSC:
        rdSC1 = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdSC1)
        SCtxt1 = Select(el.get()).all_selected_options[0].text
        logging.info(SCtxt1)
        time.sleep(0.5)
        el.get_element('filetypesubcode')
        rdSC2 = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdSC2)
        SCtxt2 = Select(el.get()).all_selected_options[0].text
        logging.info(SCtxt2)
        time.sleep(1)
        # 上传
        """
        js='''function dispatch(el, type)
                {
                    try{
                        var evt = document.createEvent('Event');
                        evt.initEvent(type,true,true);
                        el.dispatchEvent(evt);
                        }
                        catch(e)
                            {
                        alert(e)
                            };
                }
                var q=document.getElementById('SWFUpload_upload');
                dispatch(q,'click')
           '''
        #self.driver.
        self.driver.execute_script(js)
        """
        el.get_element('SWFUpload')
        ActionChains(func.driver).click(el.get()).perform()

        time.sleep(1)
        # 调用第三方工具文件
        fp = os.path.join(CFG.prjDir, 'ExtraTools/testDir.exe')
        time.sleep(1)
        os.popen(fp)
        time.sleep(5)
    def SubmitApproval(self,func,el,sub):
        self.clickFunction(func,el,sub,key)
        sleep(5)
        self.bSwithcfrname(el, key)
        self.tabcheck(el)
        a = EL.get_el_list('RPdataDetail', cg.path)
        self.checkKeys(func, el, key,sub)
        el.getFunctionName(a[0])
        el.get_element('selWorkFlow')
        currentscttext = Select(el.get()).all_selected_options[0].text

        if u'请选择' in currentscttext:
            rdmod = random.randint(2, len(Select(el.get()).options) - 1)
            Select(el.get()).select_by_index(rdmod)
            logging.info(Select(el.get()).all_selected_options[0].text)
        else:
            selOption = Select(el.get()).all_selected_options
            allOptions = Select(el.get()).options
            if selOption[0] in allOptions:
                index = allOptions.index(selOption[0])
                while True:
                    rd = random.randint(1, len(allOptions) - 1)
                    if index != rd:
                        Select(el.get()).select_by_index(rd)
        el.get_element('SubmitApproval')
        el.get().click()
        func.driver.switch_to.default_content()
        sleep(2)
        #print func.driver.current_url
        txtT=func.driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[1]/td/div/div[1]').text
        if txtT==u'新增报告':
            txtT=func.driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[1]/td/div/div[1]').text
        #print txtT
        if txtT==u'从默认审批人中指定':
            func.driver.find_elements_by_xpath('//*[@id="field_status"]')[0].find_element_by_xpath('input').click()
        else:
            self.choices_Auser(func,el)
    def upload_Object(self,func,el,sub):
        self.clickFunction(func, el, sub, key)
        sleep(5)
        self.bSwithcfrname(el, key)
        self.tabcheck(el)
        sleep(1)
        el.getFunctionName(dataDetail[0])
        el.get_element('importObject')
        ActionChains(el.getDriver()).click(el.get()).perform()
        self.PswitchToFrame(func,'ObjectImport.aspx')

        ''''
        func.driver.switch_to.default_content()
        xf=func.driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
        func.driver.switch_to.frame(xf)
        logging.info(func.driver.current_url)
        sleep(3)
        '''
        el.get_element('SWFUpload')
        ActionChains(func.driver).click(el.get()).perform()
        time.sleep(1)
        # 调用第三方工具文件
        fp = os.path.join(CFG.prjDir, 'ExtraTools/wgdx.exe')
        os.popen(fp)
        time.sleep(5)
        func.driver.find_element_by_id('btnImportObject').click()
    def add_Object(self,func,el,sub,**kwargs):
        """增加委估对象"""
        self.report(func,el,sub)
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
        print func.driver.current_url,867
        el.get_element('addObject')
        ActionChains(el.getDriver()).move_to_element(el.get()).perform()
        el.get_element('addObjectType')
        el.gets()[0].click()
        logging.info(u'进入委估对象界面')
        sleep(5)
        func.driver.switch_to.default_content()

        xf = el.getDriver().find_element_by_xpath(
            '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
        el.getDriver().switch_to.frame(xf)
        txt='EntrustObjectEdit.aspx'
        #chrome浏览器需要为43版本
        cuturl=func.driver.current_url
        logging.info(cuturl)
        while txt not in cuturl:
            sleep(3)
            func.driver.switch_to.default_content()
            xf = el.getDriver().find_element_by_xpath(
                '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
            el.getDriver().switch_to.frame(xf)
            cuturl=func.driver.current_url
            logging.info(cuturl)
        sleep(2)
        self.tabcheck(el)
        #委托对象类型
        EntrustObject = EL.get_el_list('EntrustObject', cg.path)
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
            logging.info(u'委估对象名称: weiguduixiangquancheng')
            # 建筑面积
            el.get_element('jianzhumianji')
            logging.info(u'建筑面积: 100')
            el.get().send_keys('100')

        #通过json文件来增加委估对象
        if kwargs=={}:
            DataE=EjsonData
        else:
            DataE=kwargs

        for i in DataE.keys():

            for j in range(1, len(EntrustObject)):
                b = EL.get_el_dict(EntrustObject[0], EntrustObject[j], cg.path)
                if b.get('name') == i:
                    el.getFunctionName(EntrustObject[0])
                    # el.get_element(EntrustObject[j])
                    # el.get()
                    # break
                    dictFunction = EL.get_el_dict(EntrustObject[0], EntrustObject[j], cg.path)
                    el.get_element(EntrustObject[j])
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
                    logging.info(i + ':' + DataE[i])

        el.get_element('btnSave')
        el.get().click()
class reportAddCheck(reportAdd):
    def check_add(self,func,el,sub=u'正式报告',**kwargs):
        oldtext=self.reportadd(func,el,sub,**kwargs)
        updatatext=self.get_tabledData(func,el,sub,**kwargs)
        if oldtext[0]==None or oldtext[0]=='None':
            return True
        else:
            if len(oldtext) == len(updatatext):
                for i in oldtext:
                    logging.info(i)
                    if i not in updatatext:
                        return False
                else:
                    return True
            return False
    def check_roundColumn(self, func, el, sub=u'正式报告', **kwargs):
        OdataList=self.roundColumn(func, el, sub, **kwargs)
        CdataList=[100,101,100,110,100,200,1000,2000,10000,20000]
        Breport=[]
        #print OdataList,CdataList
        if len(OdataList)==len(CdataList):
            for i in range(len(OdataList)):

                if OdataList[i]!=str(CdataList[i]):
                    logging.error(str(OdataList[i])+'---'+str(CdataList[i]))
                    Breport.append(False)
                else:
                    Breport.append(True)
            if False in Breport:
                logging.info(Breport)
                return False
            else:
                return True
        else:
            return False
    def check_autoCalculate(self,func,el,Ldata,sub=u'正式报告'):
        rt=self.autoCalculate(func,el,Ldata,sub)
        ort=Ldata[1].values()[0]
        if rt==str(ort):
            return True
        logging.error(rt+'---'+str(ort))
        return False
    def check_appraisers(self,func,el,users=None,sub=u'正式报告'):
        self.add_Appraisers(func,el,users,sub)
        func.driver.switch_to.default_content()
        self.duserSwitchFrame(el)
        el.getFunctionName(dataDetail[0])
        el.get_element('appraisersTable')
        CAtables=el.gets()
        if users==None:
            if len(CAtables)>2:
                if CAtables[2].find_elements_by_xpath('td')[1].text=='tan1':
                    return True
        else:
            for i in range(2,len(CAtables)):

                if CAtables[i].find_elements_by_xpath('td')[1].text not in users:
                    return False
            else:
                return True

        return False
    def check_Att(self,func,el,sub=u'正式报告'):
        self.add_Att(func,el,sub)
        el.get_element('attTable')
        if len(el.gets())>=3:
            return True
        return False
    def check_submitApproval(self,func,el,sub):
        self.SubmitApproval(func,el,sub)
        func.driver.switch_to.default_content()
        sleep(5)
        logging.info(func.driver.current_url)
        try:
            rtText=func.driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/font').text
        except:
            rtText = func.driver.find_element_by_xpath(
                '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/font').text
        #print rtText
        if rtText==u'提交审批成功。':
            return True
        return False
    def check_uploadObject(self,func,el,sub=u'正式报告'):
        self.upload_Object(func,el,sub)
        func.driver.switch_to.default_content()
        self.duserSwitchFrame(el)
        numObject=func.driver.find_elements_by_xpath('//*[@id="gridEvaluateObjce"]/tbody/tr')
        if numObject>4:
            return True
        return False
    def check_addObject(self,func,el,sub,**kwargs):
        self.add_Object(func,el,sub,**kwargs)
        func.driver.switch_to.default_content()
        txtrt = func.driver.find_element_by_xpath(
            '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/font').text
        if u'添加成功'in txtrt:
            return True
        return False
    def check_button(self,func,el,button,sub=u'正式报告'):
        self.reportadd(func,el,sub,button)
        func.driver.switch_to.default_content()
        self.duserSwitchFrame(el)

        el.getFunctionName(dataDetail[0])
        el.get_element('attTable')
        if len(el.gets()) >= 3:
            return True
        return False



