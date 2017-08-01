#-*- coding:utf-8 -*-
import sys
import commond as cm
import config as cg
import COMMON.ELEMNET as EL
import logging
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random
import time
from time import sleep
from COMMON import COMMON as cn

reportTitle=cg.report
reportCheck=cg.reportCheck
reportFrame=cg.reportFrame
reportTabweb=cg.reportTabweb
reportButton=cg.reportButton
xmlpath=cg.path
chkdata=cg.jsndatapath
tabledate=cg.tableData
tabchk=cg.reportTabchk
requestInfo=cg.reportRequestInfo
reportInfo=cg.reportReportInfo
dataButton=cg.reportDataButton
tooltip=cg.reportTooltip
User=cg.reportUser
tableid='td[3]/div'
class reportBase(object):
    def loginReport(self,func,el,sub):
        '''
        进入模块
        :param func:
        :param el:
        :param sub:
        :return:
        '''
        cm.TitleHand(func, el, u'报告')
        sleep(2)
        el.getFunctionName(reportTitle[0])
        if sub==u'正式报告':
            emsub=reportTitle[1]
        elif sub==u'业务登记':
            emsub=reportTitle[3]
        elif sub==u'预评报告':
            emsub=reportTitle[2]
        el.get_element(emsub)
        el.get().click()
    def reportTab(self, func, el, sub, tab=u'全部'):
        '''
        点击tab页
        :param func:
        :param el:
        :param sub:
        :param tab:
        :return:
        '''
        self.loginReport(func,el,sub)
        self.mswitchfrname(func, el, sub)
        '''
        el.getFunctionName(reportFrame[0])
        if sub==u'正式报告':
            xf=reportFrame[1]
        elif sub==u'业务登记':
            xf=reportFrame[2]
        elif sub==u'预评报告':
            xf=reportFrame[3]
        else:
            exit('args sub is error')

        eldict = EL.get_el_dict(reportFrame[0], xf, GJBpath)
        if eldict['type'] == 'ID' or eldict['type'] == 'id':
            path = eldict['path']
        elif eldict['type'].upper() == 'ID':
            el.get_element(xf)
            path = el.get()
        else:
            raise logging.error('not found iframe!')
        func.driver.switch_to.frame(path)
        '''

        el.getFunctionName(reportTabweb[0])
        chkem=sub+tab
        if  u'全部' in chkem:
            sleep(1)
            em=reportTabweb[1]
        elif  chkem in [u'正式报告我要撰写的',u'业务登记我的业务',u'预评报告我要撰写的'] :
            em=reportTabweb[2]
        elif chkem == u'业务登记待我分配的':
            em=reportTabweb[3]
        elif chkem in [u'业务登记我已分配的',u'正式报告待我审的',u'预评报告转交待我确认的']:
            em=reportTabweb[4]
        elif chkem in [u'业务登记微信个人业务',u'正式报告我已审的',u'预评报告已转交他人的']:
            em=reportTabweb[5]
        elif chkem in [u'正式报告我已完成的',u'预评报告我提审的']:
            em=reportTabweb[6]
        elif chkem in [u'正式报告我提审的',u'预评报告待我审的']:
            em=reportTabweb[7]
        elif chkem in [u'预评报告我已审的',u'正式报告转交待我确认的']:
            em=reportTabweb[8]
        elif chkem in [u'预评报告我已完成的',u'正式报告已转交他人的']:
            em=reportTabweb[9]
        elif chkem in [u'正式报告待我分配的']:
            em=reportTabweb[10]
        elif chkem in [u'正式报告我已分配的']:
            em=reportTabweb[11]
        else:
            logging.error( 'not found mode!')
            exit()
        el.get_element(em)
        el.get().click()
        sleep(2)
    def clickFunction(self,func,el,sub,key,tab=u'全部',state=0):
        """
        点击功能按键
        :param func:
        :param el:
        :param sub:
        :param key:
        :param tab:
        :param state:
        :return:
        """

        self.reportTab(func, el, sub,tab)
        drList=[]
        if key==u'新增':
            emkey=reportButton[1]
        else:
            if key==u'复制':
                emkey =reportButton[2]
            elif key==u'删除':
                if sub==u'业务登记':
                    emkey=reportButton[8]
                else:
                    emkey=reportButton[3]
            elif key==u'转交'and tab==u'我要撰写的':
                emkey=reportButton[4]
            elif key==u'分配':
                emkey=reportButton[5]
            elif key==u'转交' and tab==u'待我审的':
                emkey=reportButton[6]
            elif key==u'确认' and tab==u'转交待我确认的':
                emkey=reportButton[7]
            elif key==u'导出数据':
                emkey=reportButton[9]
            if state==0:
                pass
            else:
                drList=self.select_tableData(func, el, state,tab,sub)
        el.getFunctionName(reportButton[0])
        el.get_element(emkey)
        el.get().click()

        return drList
    def select_tableData(self,func,el,state,tab,sub):
        """
        选择Tab项
        :param func:
        :param el:
        :param state:
        :param tab:
        :param sub:
        :return:
        """
        dListID = []
        el.getFunctionName(tabledate[0])
        el.get_element(tabledate[1])
        dlist=el.gets()
        try:
            if tab==u'我要撰写的':
                if state == 1:
                    for i in range(15):
                        if sub==u'正式报告':
                            dLink = dlist[i].find_element_by_xpath('td[14]/div').text
                        elif sub==u'预评报告':
                            dLink = dlist[i].find_element_by_xpath('td[11]/div').text
                        logging.info(u'环节为：%s'%dLink)
                        if dLink==u'撰写中':
                            dID = dlist[i].find_element_by_xpath('td[3]/div').text
                            dlist[i].find_element_by_xpath('td/div/input').click()
                            dListID.append(dID)
                            break
                    else:
                        logging.error('data not exist!')
                elif state > 1:
                    startj = 0
                    for i in range(state):
                        for j in range(startj,15):
                            if sub == u'正式报告':
                                dLink = dlist[j].find_element_by_xpath('td[14]/div').text
                            elif sub == u'预评报告':
                                dLink = dlist[j].find_element_by_xpath('td[11]/div').text
                            if dLink!=u'已转交,待确认':
                                dID = el.gets()[j].find_element_by_xpath('td[3]/div').text
                                el.gets()[j].find_element_by_xpath('td/div/input').click()
                                dListID.append(dID)
                                startj=j+1
                                break

                else:
                    logging.error('choose the data cannot be negative!')
                    exit('choose the data cannot be negative!')
            else:
                if state==1:
                    dID = dlist[0].find_element_by_xpath('td[3]/div').text
                    dlist[0].find_element_by_xpath('td/div/input').click()
                    dListID.append(dID)
                elif state>1:
                    for i in range(state):
                        # el.get_element(chkElementlist[1])
                        dID = el.gets()[i].find_element_by_xpath('td[3]/div').text
                        el.gets()[i].find_element_by_xpath('td/div/input').click()
                        dListID.append(dID)
                else:
                    logging.error( 'choose the data cannot be negative!')
                    exit('choose the data cannot be negative!')
            return dListID
        except:
            txt=func.driver.find_element_by_xpath('/html/body/div/div[2]/div/div[5]/table/tbody/tr/td').text
            logging.info(txt)
            exit(txt)
    def mswitchfrname(self,func,el,sub):
        """
        切换到列表的iframe
        :param func:
        :param el:
        :param sub:
        :return:
        """
        #print func.driver.current_url
        el.getFunctionName(reportFrame[0])
        if sub == u'正式报告':
            xf = reportFrame[1]
            #print 1111
        elif sub == u'业务登记':
            xf = reportFrame[2]
        elif sub == u'预评报告':
            xf = reportFrame[3]
            logging.info(' PreealuateList frame!')
        else:
            exit('args sub is error')
        eldict = EL.get_el_dict(reportFrame[0], xf, xmlpath)
        #if eldict['type'] == 'ID' or eldict['type'] == 'id':
            #path = eldict['path']
        if eldict['type'].upper() == 'ID':
            el.get_element(xf)
            path = el.get()
        else:
            raise logging.error('not found iframe!')

        func.driver.switch_to.frame(path)
    def bSwithcfrname(self, el, key=None):
        """

        :param el:
        :param key:
        :return:
        """
        el.getDriver().switch_to.default_content()
        el.getFunctionName(reportFrame[0])
        fem=reportFrame[4]
        el.get_element(fem)

        xf = el.get()
        if xf==None:
            fem=reportFrame[5]
            el.get_element(fem)
            xf=el.get()
        el.getDriver().switch_to.frame(xf)
        logging.info(el.getDriver().current_url)
    def swithcfrname(self,el):
        """
        切换iframe
        :param el:
        :return:
        """

        el.getFunctionName(reportFrame[0])
        try:
            el.getDriver().switch_to.default_content()
            fem = reportFrame[4]
            el.get_element(fem)
            xf = el.get()
            el.getDriver().switch_to.frame(xf)
        except:
            el.getDriver().switch_to.default_content()
            fem = reportFrame[5]
            el.get_element(fem)
            xf = el.get()
            el.getDriver().switch_to.frame(xf)
    def change_dTab(self,el):
        el.getFunctionName(tabchk[0])
        # 判断是否为Tab方式
        try:
            el.get_element('tabshowdiv')
            tabatb = el.get().get_attribute('class')
        except:
            try:
                el.get_element('Mtabshowdiv')
                tabatb = el.get().get_attribute('class')
            except:
                el.get_element('Ytabshowdiv')
                tabatb = el.get().get_attribute('class')
        logging.info(u'查看是否为Tab方式')
        time.sleep(3)
        if 'chked' in tabatb:
            el.get_element('tabchkbox')
            el.get().click()
    def mandatoryField(self,el,sub):
        el.getFunctionName(requestInfo[0])
        el.get_element('technicalTeam')
        currentseltext = Select(el.get()).all_selected_options[0].text
        if u'请选择' in currentseltext:
            rd = random.randint(1, len(Select(el.get()).options) - 1)
            Select(el.get()).select_by_index(rd)
            logging.info(u'技术团队：' + Select(el.get()).all_selected_options[0].text)
        if sub==u'正式报告':
            el.getFunctionName(reportInfo[0])
            el.get_element('completedate')
            el.get().send_keys('2016-11-16')
            el.get_element('getnumber')
            el.get().click()
    def get_tabledataId(self,el):
        """
        获取列表中所有数据的ID
        :param el:
        :return:
        """
        dListID = []
        try:
            el.getFunctionName(tabledate[0])
            el.get_element(tabledate[1])
            dlist = el.gets()
            for i in range(len(dlist)):
                dID = el.gets()[i].find_element_by_xpath('td[2]/div').text
                dListID.append(dID)
            return dListID
        except:
            txt=el.getDriver().find_element_by_xpath('/html/body/div/div[2]/div/div[5]/table/tbody/tr/td').text
            logging.error(txt)
            exit(txt)
    def choices_user(self,func,el,key,user='luyb'):
        """
        选择用户
        :param func:
        :param el:
        :param key:
        :param user:
        :return:
        """
        '''
        if len(sys.argv) >= 2:
            if sys.argv[1] == '10':
                user = 'luyoubiao'
        '''
        if cg.url=='gjb.yungujia.com':
            user='luyoubiao'
        self.switcthToDefault(func)
        sleep(1)
        self.bSwithcfrname(el, key)
        sleep(3)
        el.getFunctionName(User[0])
        el.get_element('sinput')
        el.get().send_keys(user)
        js = True
        i = 1
        utime = time.time()
        while js:
            try:
                txt = func.driver.find_element_by_id('userchkTree_' + str(i) + '_span').text.split(']')[1].split('(')[0]
                print txt,user
                if txt == user:
                    func.driver.find_element_by_id('userchkTree_' + str(i) + '_check').click()
                    js = False
            except:
                pass
            finally:
                if time.time() - utime > 30:
                    logging.error(u'Not found user:' + user)
                    break
                i += 1

        el.get_element('btnOk')
        el.get().click()
    def choices_reassign_user(self,func,el,key,user='luyb'):

        if 'gjb.yungujia.com' in cg.url:
            user='tan1'
        self.switcthToDefault(func)
        sleep(1)
        self.bSwithcfrname(el, key)
        sleep(3)
        el.getFunctionName(User[0])
        el.get_element('sinput')
        el.get().send_keys(user)



        js = True
        i = 1

        utime = time.time()
        while js:
            try:
                txt = func.driver.find_element_by_id('userchkTree_' + str(i) + '_span').text.split(']')[1].split('(')[0]
                print txt,user
                if txt == user:
                    func.driver.find_element_by_id('userchkTree_' + str(i) + '_check').click()
                    js = False
            except:
                pass
            finally:
                if time.time() - utime > 30:
                    logging.error(u'Not found user:' + user)
                    break
                i += 1


        """
        #print func.driver.current_url
        el.getFunctionName(User[0])
        el.get_element('sinput')
        el.get().send_keys('tan1')
        el.get().send_keys(Keys.ENTER)
        el.get_element(user)
        el.get().click()
        """
        el.get_element('btnOk')
        el.get().click()
    def switcthToDefault(self,func):
        func.driver.switch_to.default_content()
    def get_reassign_tableadataId(self,el):
        """

        :param el:
        :return:
        """

        dListID = []
        el.getFunctionName(tabledate[0])
        el.get_element(tabledate[1])
        dlist = el.gets()
        try:
            for i in range(len(dlist)):
                    dLink=el.gets()[i].find_element_by_xpath('td[13]/div').text
                    if dLink==u'已转交,待确认':
                        continue
                    dID = el.gets()[i].find_element_by_xpath('td[2]/div').text
                    dListID.append(dID)
        except:
            logging.info(el.getDriver().find_elment_by_xpath('/html/body/div/div[2]/div/div[5]/table/tbody/tr/td').text)
        return dListID
    def chkTab(self,el):
        """
        检查数据详细界面的Tab页是否勾选
        :param el:
        :return:
        """
        el.getFunctionName(tabchk[0])
        el.get_element('tabshow')
        logging.info(u'查看Tab是否勾选')
        sleep(1)
        try:
            tabatb = el.get().get_attribute('checked')

            if tabatb == 'true':
                logging.info(u'不勾选Tab')
                el.get_element('tabchkbox')
                el.get().click()
            else:
                logging.info(u'Tab未被勾选')
        except:
            logging.info(u'Tab元素未找到')
    def PswitchToFrame(self,func,txthtml):
        """

        :param func: webdriver
        :param txthtml: 判断的html
        :return:
        """
        func.driver.switch_to.default_content()
        xf = func.driver.find_element_by_xpath(
            '/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
        func.driver.switch_to.frame(xf)
        txt = txthtml
        cuturl = func.driver.current_url
        logging.info(cuturl)
        Count=0
        while txt not in cuturl:
            Count+=1
            sleep(3)
            func.driver.switch_to.default_content()
            xf = func.driver.find_element_by_xpath(
                '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
            func.driver.switch_to.frame(xf)
            cuturl = func.driver.current_url
            logging.info(cuturl)
            if Count>10:
                logging.info('not found frame!')
                exit('not found frame')

    def importData(self,func,el,sub,tab,state,num):
        """
        导出数据功能
        :param func:
        :param el:
        :param sub:
        :param tab:
        :param state:
                --0:自由导出
                --1：导出自己的模块
                --2：删除模板
                --3：建立模板导出
        :return:
        """
        key=u'导出数据'
        self.clickFunction(func,el,sub,key,tab)
        self.swithcfrname(el)
        sleep(3)
        if state==3:
            driversLi2=func.driver.find_elements_by_xpath('//*[@id="linkTab2"]/ul/li')
            driversLi3=func.driver.find_elements_by_xpath('//*[@id="linkTab"]/ul/li')
            for i in range(len(driversLi2)):
                driversLi2[i].click()
                driversLi3[i].click()
                driversLi = func.driver.find_elements_by_xpath('//*[@id="selection"]/li')
                if num<len(driversLi):
                    dnum=num
                else:
                    dnum=len(driversLi)
                clknum=0
                for j in range(dnum):
                    clknum=clknum+j
                    while True:
                        if driversLi[clknum].get_attribute('style').strip()=='display: list-item;':
                            break
                        else:
                            clknum = clknum + 1
                    ActionChains(func.driver).double_click(driversLi[clknum]).perform()


            try:
                chktxt=func.driver.find_element_by_id('ckNewTemplate').get_attribute('checked')
                if chktxt.strip()!='checked':
                    func.driver.find_element_by_id('ckNewTemplate').click()
            except:
                func.driver.find_element_by_id('ckNewTemplate').click()
            sleep(1)
            tpName = time.strftime('%Y%m%d%H%M%S', time.localtime())
            func.driver.find_element_by_id('templateName').send_keys(tpName)

        else:
            if state==0:
                pass
            elif state==1 :
                func.driver.find_element_by_id('ckbself').click()
            else:
                pass
            sleep(1)
            selectdirver = Select(func.driver.find_element_by_id('selTemplate'))
            rd = random.randint(1, len(selectdirver.options) - 1)
            selectdirver.select_by_index(rd)
            logging.info(Select(func.driver.find_element_by_id('selTemplate')).all_selected_options[0].text)

        if state==2:
            txt=Select(func.driver.find_element_by_id('selTemplate')).all_selected_options[0].text
            func.driver.find_element_by_id('delTemplate').click()
            func.driver.switch_to.default_content()
            sleep(1)
            func.driver.find_element_by_xpath('//*[@value="确定"]').click()
            sleep(1)
            func.driver.find_element_by_xpath('//*[@value="确定"]').click()
            return txt

        else:
            func.driver.find_element_by_id('btnSave').click()
            bt=True
            stime = time.time()
            while bt:
                sleep(1)
                expDow = func.driver.find_element_by_id('exportDow').get_attribute('style')
                if 'display: none' not in expDow:
                    bt=False
                if time.time()-stime>240:
                    logging.error('timesout !')
                    exit('Timesout')
            return True


class reportTest(reportBase):
    def check_reportTilte(self,func,el,sub):
        '''
        检查点击模块全，是否为模块的Tab页
        :param func: unittest的基类
        :param el: element类对象
        :param sub:
        :return:
        '''
        self.loginReport(func,el,sub)
        el.getFunctionName(reportCheck[0])
        if sub==u'正式报告':
            el.get_element(reportCheck[1])
        elif sub==u'业务登记':
            el.get_element(reportCheck[2])
        elif sub==u'预评报告':
            el.get_element(reportCheck[3])
        if sub==el.get().text:
            return True
        logging.info(el.get().text)
        return False
    def check_Tab(self,func,el,sub,tab):
        '''
        检查模块的Tab项是否缺失
        :param func:
        :param el:
        :param sub: 模块
        :param tab: tab页
        :return: bool
        '''
        self.reportTab(func, el, sub, tab)
        el.getFunctionName(reportCheck[0])
        el.get_element(reportCheck[4])
        emlist=el.gets()
        tbs=cn.get_json_value(sub,chkdata)
        #print tbs
        etbs=[]
        for i in emlist:
             r=i.find_element_by_tag_name('a').text
             etbs.append(r)
        if etbs==tbs:
            return True
        logging.info(etbs)
        logging.info(tbs)
        return False
    def check_addBtn(self,func,el,sub,):
        self.clickFunction(func,el,sub,u'新增',u'全部')
        self.bSwithcfrname(el, u'新增')
        self.change_dTab(el)
    def check_copyBtn(self,func,el,sub,state=0):
        key=u'复制'
        sourceID=self.clickFunction(func,el,sub,key,u'全部',state)
        if state!=1:
            func.driver.switch_to.default_content()
            el.getFunctionName(tooltip[0])
            el.get_element('tip1')
            rtText = el.get().text
            logging.info(rtText)
            if state==0:
                if rtText==u'请选择要操作的项':
                    return True
            else:
                if rtText == u'只能选择一条进行复制':
                    return True
            return False

        else:
            self.bSwithcfrname(el, key)
            print func.driver.current_url
            self.change_dTab(el)
            self.mandatoryField(el,sub)
            el.getFunctionName(dataButton[0])
            if sub==u'业务登记':
                el.get_element('btnSubmit')
                el.get().click()
                func.driver.switch_to.default_content()
                func.driver.find_element_by_xpath(u"//*[@value='直接提交']").click()
                sleep(3)
                func.driver.find_element_by_xpath(u"//*[@value='确定']").click()
            else:
                el.get_element('save')
                el.get().click()

            func.driver.switch_to.default_content()
            self.mswitchfrname(func,el,sub)
            sleep(3)
            newID=self.get_tabledataId(el)[0]
            print newID,sourceID
            if newID not in sourceID:
                return True
            return False
    def check_deleteBtn(self,func,el,sub,state=0):
        """
        删除数据
        :param func:
        :param el:
        :param sub:
        :param state:
        :return:
        """
        key=u'删除'
        sourceID=self.clickFunction(func,el,sub,key,state=state)
        func.driver.switch_to.default_content()
        el.getFunctionName(tooltip[0])
        if state==0:
            el.get_element('tip1')
            rtText = el.get().text
            if rtText==u'请选择要操作的项':
                return True
        else:
            el.get_element('tip2')
            el.get().click()
            sleep(3)
            self.mswitchfrname(func,el,sub)
            newID=self.get_tabledataId(el)
            rtbool=[]
            for i in sourceID:
                if i not in newID:
                    rtbool.append(True)
            if len(rtbool)==len(sourceID):
                return True
        return False
    def check_reassignBtn(self,func,el,sub,tab,state=0):
        """

        :param func:
        :param el:
        :param sub:
        :param tab:
        :param state:
        :return:
        """
        key=u'转交'
        sourceID=self.clickFunction(func,el,sub,key,tab,state)
        func.driver.switch_to.default_content()
        el.getFunctionName(tooltip[0])
        if state == 0:
            el.get_element('tip1')
            rtText = el.get().text
            if rtText == u'请选择要操作的项':
                return True
        else:
            self.choices_reassign_user(func,el,key)
            #self.choices_user(func,el,key)#TODO 此方法已无法使用
            self.switcthToDefault(func)
            if tab==u'我要撰写的':
                el.getFunctionName(tooltip[0])
                el.get_element('tip2')
                el.get().click()
            sleep(3)
            self.mswitchfrname(func, el, sub)
            #TODO newID = self.get_tabledataId(el)#需要关闭了，转交待确认
            newID=self.get_reassign_tableadataId(el)
            rtbool = []

            for i in sourceID:
                if i not in newID:
                    rtbool.append(True)
                if sub==u'预评报告':
                    if i in newID:
                        rtbool.append(True)

            if len(rtbool) == len(sourceID):
                return True
        return False
    def check_OKBtn(self,func,el,sub,state):
        key=u'确认'
        tab=u'转交待我确认的'
        sourceID=self.clickFunction(func,el,sub,key,tab,state)
        func.driver.switch_to.default_content()
        el.getFunctionName(tooltip[0])
        if state == 0:
            el.get_element('tip1')
            rtText = el.get().text
            if rtText == u'请选择要操作的项':
                return True
        else:
            el.get_element('tip2')
            el.get().click()
            sleep(3)
            self.mswitchfrname(func, el, sub)
            newID = self.get_tabledataId(el)
            rtbool = []
            for i in sourceID:
                if i not in newID:
                    rtbool.append(True)
            if len(rtbool) == len(sourceID):
                return True
        return False
    def check_assignButton(self,func,el,sub,state):
        """
        分配转交功能
        :param func:
        :param el:
        :param sub:
        :param state:
        :return:
        """
        key=u'分配'
        tab=u'待我分配的'
        sourceID=self.clickFunction(func,el,sub,key,tab,state)
        func.driver.switch_to.default_content()
        el.getFunctionName(tooltip[0])
        if state == 0:
            el.get_element('tip1')
            rtText = el.get().text
            if rtText == u'请选择要操作的项':
                return True
        else:
            self.choices_user(func,el,key)
            self.switcthToDefault(func)
            el.getFunctionName(tooltip[0])
            el.get_element('tip2')
            el.get().click()
            sleep(3)
            self.mswitchfrname(func, el, sub)
            newID = self.get_tabledataId(el)
            rtbool = []
            for i in sourceID:
                if i not in newID:
                    rtbool.append(True)
            if len(rtbool) == len(sourceID):
                return True
        return False
    def check_importData(self,func,el,sub,tab,state,num=5):
        rt=self.importData(func,el,sub,tab,state,num)
        if state==2:
            fr=func.driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
            func.driver.switch_to.frame(fr)
            print func.driver.current_url
            selectdirver = Select(func.driver.find_element_by_id('selTemplate'))
            for i in selectdirver.options:
                if i.text==rt:
                    return False
            else:
                return True
        else:
            return rt


















