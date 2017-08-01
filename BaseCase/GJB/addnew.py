#coding:utf-8
import COMMON.ELEMNET as EL
import os
import time
import random
import logging
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from BaseCase.GJB import commond
from COMMON import CONFIG as CFG
#autoitPath=os.path.join(CFG.prjDir,'ExtraTools/gjbfxtchinaUploadIE.exe')
autoitPath=os.path.join(CFG.prjDir,'ExtraTools/testDir.exe')
xmlpath=os.path.join(CFG.prjDir,'BaseCase/GJB')

dataDetail=EL.get_el_name('DetailData',xmlpath)
MsgBtn=EL.get_el_name('MsgBtnKey',xmlpath)
MulMsgBtn=EL.get_el_name('MulMsgBtnKey',xmlpath)
MsgFrm=EL.get_el_name('MsgFrame',xmlpath)
TooltipAddnew=EL.get_el_name('AddNewTooltip',xmlpath)
AddNewDetail=EL.get_el_name('AddNewDetail',xmlpath)
AddNewEquitiesResult=EL.get_el_name('chanquanxinxijieguo',xmlpath)
elAddNew=EL.get_el_name('xinzengxujia',xmlpath)
AddNewOutbuidingResult=EL.get_el_name('fuzhufangwuxinxijieguo',xmlpath)
MultiAddNew=EL.get_el_name('MultiAddNew',xmlpath)

Browser=CFG.ReadConfig().getConfigValue('Browser')

AddNewMutil=EL.get_el_name('Duotao',xmlpath)

def addnewMust(self,el,msgmode=None):
    """
    根据msgmod是否填写必填项
    :param self:
    :param el:
    :param msgmode:
    :return:
    """
    WGtxt = 'autotest'
    MJnum = 1230
    if msgmode != None:
        WGtxt = msgmode
    '''
    commond.Duantao(self, el, submode)
    el.getFunctionName(elAddNew[0])
    el.get_element('dantaoxinzeng')
    ActionChains(self.driver).move_to_element(el.get()).perform()
    if submode == None:
        el.get_element('zhuzhai')
    else:
        el.get_element(submode)
    el.get().click()
    '''
    self.driver.switch_to.default_content()
    el.getFunctionName(MsgFrm[0])
    el.get_element(MsgFrm[1])
    xf = el.get()
    self.driver.switch_to.frame(xf)
    time.sleep(5)

    el.getFunctionName(AddNewDetail[0])
    # 判断是否为Tab方式
    el.get_element('tabshowdiv')
    tabatb = el.get().get_attribute('class')
    logging.info(u'查看是否为Tab方式')
    if 'chked' in tabatb:
        el.get_element('tabchkbox')
        el.get().click()

    if msgmode != None:
        currenttext = ''
        # 技术团队
        el.get_element('jishutuandui')
        if len(Select(el.get()).options) < 2:
            el.get_element('weituoleixing')
            selOption = Select(el.get()).all_selected_options
            allOptions = Select(el.get()).options
            if selOption[0] in allOptions:
                index = allOptions.index(selOption[0])
                while True:
                    rd = random.randint(1, len(allOptions) - 1)
                    if index != rd:
                        Select(el.get()).select_by_index(rd)
                        break
            time.sleep(1)
            el.get_element('jishutuandui')
        currentseltext = Select(el.get()).all_selected_options[0].text
        if u'请选择' in currentseltext:
            rd = random.randint(1, len(Select(el.get()).options) - 1)
            Select(el.get()).select_by_index(rd)
            logging.info(u'技术团队：' + Select(el.get()).all_selected_options[0].text)


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
            el.get().send_keys(WGtxt)
            logging.info(u'委估对象名称:' + WGtxt)
            # 建筑面积
            el.get_element('jianzhumianji')
            logging.info(u'建筑面积:' + str(MJnum))
            el.get().send_keys(MJnum)

def addnewData(self,el,msgmode=None,data=None,submode=None,button=None,Inquiry=None,valuation=None):
    """
    新增信息功能
    :param self:
    :param el:
    :param mode: 信息类型
    :param data: 填写数据
    :param submode: 单套询价类型
    :param Inquiry:询价类型
    :param button: 操作
    :return: 返回新增的数据添加的结果
    """

    WGtxt = 'autotest'
    MJnum = 1230 #面积
    WTFtxt = 'test1' #委托方
    XMMCtxt = 'aaaaaaa'#项目名称
    if msgmode != None and msgmode.strip():
        WGtxt = msgmode

    if Inquiry == None:

        commond.Duantao(self, el,submode)

        el.getFunctionName(elAddNew[0])
        el.get_element('dantaoxinzeng')
        ActionChains(self.driver).move_to_element(el.get()).perform()
        if submode==None:
            el.get_element('zhuzhai')
        else:
            el.get_element(submode)
        el.get().click()

        self.driver.switch_to.default_content()
        el.getFunctionName(MsgFrm[0])
        el.get_element(MsgFrm[1])
        xf = el.get()
        self.driver.switch_to.frame(xf)
        #time.sleep(5)
        self.driver.implicitly_wait(3)

        el.getFunctionName(AddNewDetail[0])

        addnewMust(self,el,msgmode)
        if msgmode != None:

                if msgmode == u'必填':
                    pass
                else:
                    currenttext=''
                    el.get_element(msgmode)
                    dictFunction = EL.get_el_dict(AddNewDetail[0], msgmode, xmlpath)
                    try:
                        el.get().get_attribute('tagname')
                    except:
                        raise (u'no find element')
                    if 'elementType' in dictFunction:
                        if dictFunction['elementType'] == 'select':
                            currentscttext = Select(el.get()).all_selected_options[0].text
                            # logging.info(currenttext)
                            if data == None:
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
                            elif data in currentscttext and  u'请选择' not in currentscttext:
                                pass
                            else:
                                # selOption = Select(el.get()).all_selected_options
                                allOptions = Select(el.get()).options
                                for selem in allOptions:
                                    if data == selem.text:
                                        index = allOptions.index(selem)
                                        Select(el.get()).select_by_index(index)
                                        break
                                else:
                                    logging.error(u'未找到此选项：'+data)
                                    exit()
                            currenttext=Select(el.get()).all_selected_options[0].text

                        elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                            el.get().clear()
                            el.get().send_keys(data)
                            currenttext = el.get().get_attribute('value')
                        else:
                            el.get().clear()
                            el.get().send_keys(data)
                            currenttext = el.get().text
                    logging.info(u'选择或输入:'+currenttext)

        #填写单价
        if button == 'tijiaohuijia':
            el.get_element('danjia')
            el.get().send_keys(1234)
            logging.info(u'选择单价：1234')
            el.get_element('huijiashenpiliucheng')
            if 'select disabled' not in el.get().get_attribute('class'):
                allOpt=Select(el.get()).options
                #print allOpt
                for i in range(len(allOpt)):
                    if u'无需审批' in i.text:
                        Select(el.get()).select_by_index(rdmod)
                        break
                else:
                    logging.info(u'not  Approval')
                logging.info(u'选择回价审批流程：'+Select(el.get()).all_selected_options[0].text)

        el.getFunctionName(MsgBtn[0])
        #print button
        if button==None :
            el.get_element('save')
        else:
            el.get_element(button)
        el.get().click()
        if msgmode==None:
            self.driver.switch_to.default_content()
            time.sleep(1)
            #print self.driver.current_url
            el.getFunctionName(TooltipAddnew[0])
            el.get_element('xinzengtishikuang')
            result=el.get().text
            logging.info(result)
            return result
        self.driver.switch_to.default_content()
        time.sleep(1)
        if button=='tijiaohuijia':
            el.getFunctionName(AddNewDetail[0])
            el.get_element('huijiaOK')
            el.get().click()
        time.sleep(1)
        commond.Switchto_Frame(self, Inquiry)
        if data!=None:
            commond.SelectFirstData(self, self.el)
            result = commond.GetDetail(self, self.el, AddNewDetail,msgmode)
            return result
        #commond.SelectFirstData(self, el)

    else:
        commond.OtherXujia(self, el, Inquiry)
        MultiAdd=EL.get_el_name(Inquiry,xmlpath)
        el.getFunctionName(MultiAdd[0])
        el.get_element('xinzeng')
        el.get().click()

        self.driver.switch_to.default_content()
        el.getFunctionName(MultiAddNew[0])
        el.get_element('frame')
        xf=el.get()
        self.driver.switch_to.frame(xf)
        time.sleep(8)

        # 判断是否为Tab方式
        el.getFunctionName(AddNewDetail[0])
        el.get_element('tabshowdiv')
        tabatb = el.get().get_attribute('class')
        logging.info(u'查看Tab是否勾选')
        if 'chked' in tabatb:
            el.get_element('tabchkbox')
            el.get().click()

        #必填项
        el.getFunctionName(MultiAddNew[0])
        #项目名称
        if msgmode!='xiangmumingcheng':
            el.get_element('xiangmumingcheng')
            el.get().send_keys('123456')

        #委托方
        if msgmode!='weituofang':
            el.get_element('weituofang')
            el.get().send_keys(WTFtxt)

        #el.get_element('weituofanglianxiren')
        #el.get().send_keys(XMMCtxt)

        if valuation !=True:
            el.get_element(msgmode)
            dictFunction = EL.get_el_dict(MultiAddNew[0], msgmode, xmlpath)
            try:
                tagtxt=el.get().get_attribute('tagname')
            except:
                raise (u'未找元素，请确认')
            if tagtxt==None:
                tagtxt=msgmode
            currenttext=u'no data'
            if 'elementType' in dictFunction:
                if dictFunction['elementType'] == 'select':
                    currentscttext = Select(el.get()).all_selected_options[0].text
                    logging.info(tagtxt+u',默认为：'+currentscttext)
                    if data == None:
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

                    elif data == currentscttext and  u'请选择' not in currentscttext:
                        pass
                    else:
                        allOptions = Select(el.get()).options
                        for selem in allOptions:
                            if data.strip() == selem.text.strip():
                                index = allOptions.index(selem)
                                Select(el.get()).select_by_index(index)
                                break
                        else:
                            logging.error(u'没有选项'+data+u',请确认')
                            exit()
                    currenttext = Select(el.get()).all_selected_options[0].text

                elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                    el.get().clear()
                    el.get().send_keys(data)
                    currenttext = el.get().get_attribute('value')
                else:
                    el.get().clear()
                    el.get().send_keys(data)
                    currenttext = el.get().text
            logging.info(tagtxt+':'+currenttext)


        time.sleep(1)
        #谷歌浏览器不支持
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)
        #self.driver.execute_script(js)#chrome需要执行两次


        #time.sleep(10)
        el.get_element('tianjiaweiguduixiang')
        ActionChains(self.driver).move_to_element(el.get()).perform()
        if submode==None:
            el.get_element('zhuzhai')
        else:
            el.get_element(submode)
        el.get().click()
        time.sleep(1)

        #self.driver.implicitly_wait(3)
        self.driver.switch_to.default_content()
        time.sleep(3)
        el.getFunctionName(MultiAddNew[0])
        el.get_element('weiguduixiangframe')
        xf = el.get()
        text=self.driver.find_element_by_xpath('/html/body/div[2]/table').get_attribute('class')
        if 'ui_state_focus' not in text:
            xf=self.driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
        self.driver.switch_to.frame(xf)
        #print self.driver.current_url
        time.sleep(1)
        el.getFunctionName(AddNewDetail[0])
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
        el.get().send_keys(WGtxt)
        logging.info(u'委估对象名称:'+WGtxt )
        # 建筑面积
        el.get_element('jianzhumianji')
        logging.info(u'建筑面积:'+str(MJnum))
        el.get().send_keys(MJnum)
        currenttext = ''
        el.getFunctionName(MultiAddNew[0])

        el.get_element(msgmode)

        if valuation==True:
            dictFunction = EL.get_el_dict(MultiAddNew[0], msgmode, xmlpath)
            try:
                tagtxt=el.get().get_attribute('tagname')
            except:
                raise (u'未找元素，请确认')
            if tagtxt==None:
                tagtxt=msgmode
            if 'elementType' in dictFunction:
                if dictFunction['elementType'] == 'select':
                    currentscttext = Select(el.get()).all_selected_options[0].text
                    # logging.info(currenttext)
                    if data == None:
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
                    elif data in currentscttext and u'请选择' not in currentscttext:
                        pass
                    else:
                        # selOption = Select(el.get()).all_selected_options
                        allOptions = Select(el.get()).options
                        for selem in allOptions:
                            logging.info(u'选项：'+selem.text)
                            if data == selem.text:
                                index = allOptions.index(selem)
                                Select(el.get()).select_by_index(index)
                                break
                        else:
                            logging.error(u'没有选项'+data+u'，请确认！')
                            exit()
                    currenttext = Select(el.get()).all_selected_options[0].text

                elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                    el.get().clear()
                    el.get().send_keys(data)
                    currenttext = el.get().get_attribute('value')
                else:
                    el.get().clear()
                    el.get().send_keys(data)
                    currenttext = el.get().text
            logging.info(tagtxt+':'+currenttext)

        #点击委估对象保存按钮
        el.get_element('save')
        el.get().click()

        self.driver.switch_to.default_content()
        #print self.driver.current_url
        self.driver.implicitly_wait(2)
        el.get_element('buxuyao')
        el.get().click()

        el.getFunctionName(MultiAddNew[0])
        el.get_element('weiguduixiangframe')
        xf1 = el.get()
        if 'ui_state_focus' not in text:

            if Browser=='Firefox':
                pass
                #xf1 = self.driver.find_element_by_xpath( '/html/body/div[2]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
            else:
                xf1 = self.driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/iframe')
        self.driver.switch_to.frame(xf1)
        time.sleep(2)
        print self.driver.current_url
        el.get_element('save')
        el.get().click()

        #已回价提示框
        if msgmode=='danjia'or msgmode=='zongjia':
            self.driver.switch_to.default_content()
            time.sleep(1)
            el.get_element('danjiaOK')
            el.get().click()

        commond.Switchto_Frame(self, Inquiry)

        if data != None and valuation!=True:
            time.sleep(1)
            commond.SelectFirstData(self, self.el)
            result = commond.GetDetail(self, self.el, MultiAddNew, msgmode).strip()
        else:
            time.sleep(1)
            commond.SelectFirstData(self, self.el)
            commond.switchToDetailUI(self,el)
            time.sleep(1)

            # 判断是否为Tab方式
            el.getFunctionName(AddNewDetail[0])
            el.get_element('tabshowdiv')
            tabatb = el.get().get_attribute('class')
            logging.info(u'查看Tab是否勾选')
            if 'chked' in tabatb:
                el.get_element('tabchkbox')
                el.get().click()

            # 谷歌浏览器不支持
            js = "var q=document.documentElement.scrollTop=10000"
            self.driver.execute_script(js)

            el.getFunctionName(MultiAddNew[0])
            if msgmode == 'danjia' or msgmode == 'zongjia':
                el.get_element('weiguhuijiashuju')
            else:
                el.get_element('weigushuju')
            el.get().click()

            self.driver.switch_to.default_content()
            el.getFunctionName(MultiAddNew[0])
            el.get_element('frame')
            xf=el.get()
            self.driver.switch_to.frame(xf)
            el.get_element(msgmode)
            dictFunction = EL.get_el_dict(MultiAddNew[0], msgmode, xmlpath)
            tagname=None
            try:
                tagname = el.get().get_attribute('tagname')
            except:
                pass
            if tagname == None:
                tagname = ''
            currenttext = u'没有类型'
            if 'elementType' in dictFunction:
                if dictFunction['elementType'] == 'select':
                    currenttext = Select(el.get()).all_selected_options[0].text
                elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                    currenttext = el.get().get_attribute('value').strip()
                else:
                    currenttext = el.get().text.strip().replace(',','')
            result=currenttext
            logging.info(tagname + ':' + currenttext)

        return result

def addnewAtt(self,el,data,key=None,submode=None,subDanTao=None,Inquiry=None):
    """
    附件上传功能
    :param self:
    :param el:
    :param data:
    :param key:
    :param submode:
    :param subDanTao:
    :param Inquiry:
    :return:
    """
    WGtxt = 'test2'
    MJnum = 123
    if Inquiry == None:
        commond.Duantao(self, el, subDanTao)
    else:
        commond.OtherXujia(self, el, Inquiry)

    time.sleep(1)
    el.getFunctionName(elAddNew[0])
    el.get_element('dantaoxinzeng')
    time.sleep(3)
    ActionChains(self.driver).move_to_element(el.get()).perform()
    if submode == None:
        el.get_element('zhuzhai')
    else:
        el.get_element(submode)

    #新增按钮悬停操作
    el.get().click()
    #ActionChains(self.driver).move_to_element(el.get()).perform()
    '''
    mouseHoverjs="var var evObj = document.createEvent('MouseEvents');"\
    "evObj.initMouseEvent(mouseover,true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);"\
    " js.executeScript(mouseHoverjs, targetElement);"
    self.driver.execute_script(mouseHoverjs,el.get())
    '''
    #ActionChains(self.driver).click(el.get()).perform()


    self.driver.switch_to.default_content()
    el.getFunctionName(MsgFrm[0])
    el.get_element(MsgFrm[1])
    xf = el.get()
    self.driver.switch_to.frame(xf)
    time.sleep(5)

    el.getFunctionName(AddNewDetail[0])
    #判断是否为Tab方式
    el.get_element('tabshowdiv')
    tabatb=el.get().get_attribute('class')
    logging.info(tabatb)
    if 'chked' in tabatb:
        el.get_element('tabchkbox')
        el.get().click()

    if data != None:
        if data == u'必填':
            # 技术团队
            el.get_element('jishutuandui')
            if len(Select(el.get()).options) < 2:
                el.get_element('weituoleixing')
                selOption = Select(el.get()).all_selected_options
                allOptions = Select(el.get()).options
                if selOption[0] in allOptions:
                    index = allOptions.index(selOption[0])
                    while True:
                        rd = random.randint(1, len(allOptions) - 1)
                        if index != rd:
                            Select(el.get()).select_by_index(rd)
                            logging.info(Select(el.get()).all_selected_options[0].text)
                            break
            # 当前技术团队项
            el.get_element('jishutuandui')
            currentseltext = Select(el.get()).all_selected_options[0].text
            if u'请选择' in currentseltext:
                logging.info(len(Select(el.get()).options))
                rd = random.randint(2, len(Select(el.get()).options) - 1)
                Select(el.get()).select_by_index(rd)
                logging.info(u'技术团队：' + Select(el.get()).all_selected_options[0].text)

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
            el.get().send_keys(WGtxt)
            logging.info(u'委估对象名称:' + WGtxt)
            # 建筑面积
            el.get_element('jianzhumianji')
            logging.info(u'建筑面积:' + str(MJnum))
            el.get().send_keys(MJnum)
    ''
    #附件
    el.get_element('fujianleixing1')
    #selSC=Select(el.get()).all_selected_options[0].text
    #if u'请选择' in selSC:
    rdSC1 = random.randint(2, len(Select(el.get()).options) - 1)
    Select(el.get()).select_by_index(rdSC1)
    SCtxt1 = Select(el.get()).all_selected_options[0].text
    logging.info(SCtxt1)
    time.sleep(0.5)
    el.get_element('fujianleixing2')
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

    el.get_element('shangchuan')
    ActionChains(self.driver).click(el.get()).perform()

    time.sleep(1)
    #调用第三方工具文件
    os.popen(autoitPath)
    time.sleep(10)

    if key!=None:
        el.get_element('attdel')
        el.get().click()
        logging.info(u'删除附件成功')
        self.driver.switch_to.default_content
        time.sleep(3)
        #print self.driver.current_url
        el.get_element('attsuredel')
        #el.get().click()
        #commond.Switchto_Frame()

        el.getFunctionName(MsgFrm[0])
        el.get_element(MsgFrm[1])
        xf = el.get()
        self.driver.switch_to.frame(xf)
        time.sleep(3)


    #点击保存
    #self.driver.find_element_by_id('btnTempSave').click()

    el.getFunctionName(MsgBtn[0])
    el.get_element('save')
    logging.info(u'点击保存')
    el.get().click()

    logging.info(u'新增成功')
    if data == None:
        self.driver.switch_to.default_content()
        el.getFunctionName(TooltipAddnew[0])
        el.get_element('xinzengtishikuang')
        result = el.get().text
        logging.info(result)
        return result
    #self.driver.switch_to.default_content()
    #time.sleep(3)
    #logging.info(1111)
    commond.Switchto_Frame(self, Inquiry)
    report=commond.SelectFirstData(self, el)
    return report

    #logging.info(u'结束')

def addnewEquities(self,el,msgmode=None,data=None,equities=None,submode=None,Inquiry=None,button=None):
    """
    添加产权人信息
    :param self:
    :param el:
    :param msgmode: 产权人信息项
    :param data: 输入的数据
    :param equities: 产权类型
    :param submode: 单套询价类型，
    :param Inquiry: 询价类型
    :param button: 点击的按钮
    :return:
    """
    if Inquiry == None:
        commond.Duantao(self, el, submode)
        el.getFunctionName(elAddNew[0])
        el.get_element('dantaoxinzeng')
        ActionChains(self.driver).move_to_element(el.get()).perform()
        if submode == None:
            el.get_element('zhuzhai')
        else:
            el.get_element(submode)
        el.get().click()

        addnewMust(self, el, msgmode)


        el.get_element('chanquanleixing')
        equitiestxt = Select(el.get()).all_selected_options[0].text
        logging.info(u'默认产权类型：'+equitiestxt)
        if equities==None or equities==u'个人':
            if equitiestxt==u'个人':
                pass
            else:
                Select(el.get()).select_by_value(u'20010502')
        else:
            Select(el.get()).select_by_value('20010501')
            '''
                allOptions = Select(el.get()).options
                if equitiestxt[0] in allOptions:
                    index = allOptions.index(equitiestxt[0])
                    while True:
                        rd = random.randint(1, len(allOptions) - 1)
                        if index != rd:
                            Select(el.get()).select_by_index(rd)
            '''

        equitiestxt2 = Select(el.get()).all_selected_options[0].text
        logging.info(u'选择后的产权类型：' + equitiestxt2)
        el.get_element('zengjiachanquanren')
        el.get().click()

        if msgmode!='chanquanrenxingming':
            el.get_element('chanquanrenxingming')
            el.get().send_keys(equities)
            logging.info(u'输入的产权人姓名：'+equities)

        if msgmode!=None and msgmode!=u'必填':
            el.get_element(msgmode)
            dictFunction = EL.get_el_dict(AddNewDetail[0], msgmode, xmlpath)
            if dictFunction['elementType'] == 'select':
                Select(el.get()).select_by_value(data)
            else:
                el.get().send_keys(data)


        # 提交回价
        if button == 'tijiaohuijia':
            el.get_element('danjia')
            el.get().send_keys(1234)

        el.getFunctionName(MsgBtn[0])
        if button == None:
            el.get_element('save')
        else:
            el.get_element(button)
        el.get().click()
        if msgmode == None:
            self.driver.switch_to.default_content()
            time.sleep(3)
            el.getFunctionName(TooltipAddnew[0])
            el.get_element('xinzengtishikuang')
            result = el.get().text
            logging.info(result)
            return result
        self.driver.switch_to.default_content()
        time.sleep(3)
        if button == 'tijiaohuijiao':
            el.getFunctionName(AddNewDetail[0])
            el.get_element('huijiaOK')
            el.get().click()
        time.sleep(3)
        commond.Switchto_Frame(self, Inquiry)
        if msgmode != None:
            if msgmode==u'必填':
                msgmode='chanquanrenxingming'
            commond.SelectFirstData(self, self.el)
            result = commond.GetDetail(self, self.el, AddNewEquitiesResult, msgmode)
            return result

    else:
        commond.OtherXujia(self, el, Inquiry)

def addnewOutbuilding(self,el,msgmode=None,data=None,submode=None,Inquiry=None,button=None,valuation=None):
    """
    多套询价附属房屋信息增加
    :param self:
    :param el:
    :param msgmode:
    :param data:
    :param submode:
    :param Inquiry:
    :param button:
    :param valuation:
    :return:
    """
    WGtxt = 'autotest'
    MJnum = 1230  # 面积
    WTFtxt = 'test1'  # 委托方
    XMMCtxt = 'aaaaaaa'  # 项目名称
    if Inquiry == None:
        commond.Duantao(self, el, submode)

        el.getFunctionName(elAddNew[0])
        el.get_element('dantaoxinzeng')
        ActionChains(self.driver).move_to_element(el.get()).perform()
        if submode == None:
            el.get_element('zhuzhai')
        else:
            el.get_element(submode)
        el.get().click()
        addnewMust(self, el, msgmode)

        el.get_element('tianjiafuzhufangwu')
        el.get().click()

        self.driver.switch_to.default_content()
        el.get_element('fuzhufangwuiframe')
        xf=el.get()
        self.driver.switch_to.frame(xf)
        time.sleep(1)
        '''
        if msgmode != None:
            print msgmode
            if msgmode == u'必填':
                el.get_element('fuzhufangwuleixing')
                rdmod = random.randint(2, len(Select(el.get()).options) - 1)
                Select(el.get()).select_by_index(rdmod)
                logging.info(Select(el.get()).all_selected_options[0].text)
            else:
                currenttext = ''
                el.get_element(msgmode)
                dictFunction = EL.get_el_dict(AddNewDetail[0], msgmode, path)
                try:
                    el.get().get_attribute('tagname')
                except:
                    pass
                    #raise (u'未找元素，请确认')
                if 'elementType' in dictFunction:
                    if dictFunction['elementType'] == 'select':
                        currentscttext = Select(el.get()).all_selected_options[0].text
                        # logging.info(currenttext)
                        if data == None:
                            if u'请选择' in currentscttext:
                                #print 1111
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
                        elif data in currentscttext or u'请选择' not in currentscttext:
                            pass
                        else:
                            # selOption = Select(el.get()).all_selected_options
                            allOptions = Select(el.get()).options
                            for selem in allOptions:
                                if data == selem.text:
                                    index = allOptions.index(selem)
                                    Select(el.get()).select_by_index(index)
                                    break
                        currenttext = Select(el.get()).all_selected_options[0].text

                    elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                        el.get().clear()
                        el.get().send_keys(data)
                        currenttext = el.get().get_attribute('value')
                    else:
                        el.get().clear()
                        el.get().send_keys(data)
                        currenttext = el.get().text

                logging.info(u'选择或输入:' + currenttext)
        '''

        """
        if msgmode != 'fuzhufangwuleixing' or msgmode==None:
                el.get_element('fuzhufangwuleixing')
                #if data == None:
                rd=random.randint(2,len(Select(el.get()).options))
                Select(el.get()).select_by_index(rd)
                #logging.info(u'附属房屋类型：' + Select(el.get()).all_selected_options[0].text)
                '''
                else:
                    listop = Select(el.get()).options
                    for i in range(len(listop)):
                        if listop[i].text == data:
                            Select(el.get()).select_by_index(i)
                '''
                logging.info(u'附属房屋类型：' + Select(el.get()).all_selected_options[0].text)
            """

        if msgmode != 'fuzhufangwuleixing':
            el.get_element('fuzhufangwuleixing')
            #print self.driver.current_url
            if data == None:
                rd = random.randint(2, len(Select(el.get()).options))
                Select(el.get()).select_by_index(rd)
            else:
                if msgmode == u'必填' or msgmode == None:
                    listop = Select(el.get()).options
                    for i in range(len(listop)):
                        if listop[i].text == data:
                            Select(el.get()).select_by_index(i)
                else:
                    rd = random.randint(1, len(Select(el.get()).options))
                    Select(el.get()).select_by_index(rd)

        if msgmode != None and msgmode!=u'必填' :
            el.get_element(msgmode)
            dictFunction = EL.get_el_dict(AddNewDetail[0], msgmode, xmlpath)
            if dictFunction['elementType'] == 'select':
                if Select(el.get()).all_selected_options[0]!=data:
                    listop=Select(el.get()).options
                    for i in range(len(listop)):
                        if listop[i].text==data:
                            Select(el.get()).select_by_index(i)
            else:
                el.get().send_keys(data)

        el.get_element('fuzhufangwuSave')
        el.get().click()

        self.driver.switch_to.default_content()
        time.sleep(1)
        print self.driver.current_url
        el.get_element('xiangxixinxiIframe')
        self.driver.switch_to.frame(el.get())




        # 提交回价
        if button == 'tijiaohuijia':
            el.get_element('danjia')
            el.get().send_keys(1234)

        el.getFunctionName(MsgBtn[0])
        if button == None:
            el.get_element('save')
        else:
            el.get_element(button)
        el.get().click()
        if msgmode == None:
            self.driver.switch_to.default_content()
            time.sleep(3)
            el.getFunctionName(TooltipAddnew[0])
            el.get_element('xinzengtishikuang')
            result = el.get().text
            logging.info(result)
            return result
        self.driver.switch_to.default_content()
        time.sleep(3)
        if button == 'tijiaohuijiao':
            el.getFunctionName(AddNewDetail[0])
            el.get_element('huijiaOK')
            el.get().click()
        time.sleep(3)

        commond.Switchto_Frame(self, Inquiry)
        if msgmode != None:
            if msgmode == u'必填':
                msgmode = 'fuzhufangwuleixing'
            commond.SelectFirstData(self, self.el)
            result = commond.GetDetail(self, self.el,AddNewOutbuidingResult,msgmode)
            return result

    ###不适用于Chrome浏览器
    else:
        #commond.OtherXujia(self, el, Inquiry)
        #el.getFunctionName(Inquiry[0])
        #el.get_element('xinzeng')
        #el.get().click()

        commond.OtherXujia(self, el, Inquiry)
        MultiAdd = EL.get_el_name(Inquiry, xmlpath)
        el.getFunctionName(MultiAdd[0])
        el.get_element('xinzeng')
        el.get().click()

        self.driver.switch_to.default_content()
        el.getFunctionName(MultiAddNew[0])
        el.get_element('frame')
        xf = el.get()
        self.driver.switch_to.frame(xf)
        time.sleep(5)

        # 判断是否为Tab方式
        el.getFunctionName(AddNewDetail[0])
        el.get_element('tabshowdiv')
        tabatb = el.get().get_attribute('class')
        logging.info(u'查看Tab是否勾选')
        if 'chked' in tabatb:
            el.get_element('tabchkbox')
            el.get().click()

        # 必填项
        el.getFunctionName(MultiAddNew[0])
        # 项目名称
        if msgmode != 'xiangmumingcheng':
            el.get_element('xiangmumingcheng')
            el.get().send_keys('123456')

        # 委托方
        if msgmode != 'weituofang':
            el.get_element('weituofang')
            el.get().send_keys(WTFtxt)

        # el.get_element('weituofanglianxiren')
        # el.get().send_keys(XMMCtxt)

        if valuation != True:
            el.get_element(msgmode)
            dictFunction = EL.get_el_dict(MultiAddNew[0], msgmode, xmlpath)
            try:
                tagtxt = el.get().get_attribute('tagname')
            except:
                raise (u'未找元素，请确认')
            if tagtxt == None:
                tagtxt = msgmode
            if 'elementType' in dictFunction:
                if dictFunction['elementType'] == 'select':
                    currentscttext = Select(el.get()).all_selected_options[0].text
                    logging.info(tagtxt + u',默认为：' + currentscttext)
                    if data == None:
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
                    elif data == currentscttext and u'请选择' not in currentscttext:
                        pass
                    else:
                        allOptions = Select(el.get()).options
                        for selem in allOptions:
                            if data.strip() == selem.text.strip():
                                index = allOptions.index(selem)
                                Select(el.get()).select_by_index(index)
                                break
                    currenttext = Select(el.get()).all_selected_options[0].text

                elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                    el.get().clear()
                    el.get().send_keys(data)
                    currenttext = el.get().get_attribute('value')
                else:
                    el.get().clear()
                    el.get().send_keys(data)
                    currenttext = el.get().text
            logging.info(tagtxt + ':' + currenttext)

        time.sleep(3)
        # 谷歌浏览器不支持
        js = "var q=document.documentElement.scrollTop=10000"
        self.driver.execute_script(js)

        # time.sleep(10)
        el.get_element('tianjiaweiguduixiang')
        ActionChains(self.driver).move_to_element(el.get()).perform()
        if submode == None:
            el.get_element('zhuzhai')
        else:
            el.get_element(submode)
        el.get().click()
        time.sleep(5)

        self.driver.switch_to.default_content()
        el.getFunctionName(MultiAddNew[0])
        el.get_element('weiguduixiangframe')
        xf = el.get()
        self.driver.switch_to.frame(xf)

        time.sleep(1)
        el.getFunctionName(AddNewDetail[0])
        # 行政区
        #el.get_element('xingzhengqu')
        #field_areaid = Select(el.get()).all_selected_options[0].text

        el.get_element('xingzhengqu')
        field_areaid = Select(el.get()).all_selected_options[0].text
        print field_areaid

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
        el.get().send_keys(WGtxt)
        logging.info(u'委估对象名称:' + WGtxt)
        # 建筑面积
        el.get_element('jianzhumianji')
        logging.info(u'建筑面积:' + str(MJnum))
        el.get().send_keys(MJnum)
        currenttext = ''
        el.getFunctionName(MultiAddNew[0])

        #el.get_element(msgmode)
        if valuation == True:
            '''
            dictFunction = EL.get_el_dict(MultiAddNew[0], msgmode, path)
            try:
                tagtxt = el.get().get_attribute('tagname')
            except:
                raise (u'未找元素，请确认')
            if tagtxt == None:
                tagtxt = msgmode
            if 'elementType' in dictFunction:
                if dictFunction['elementType'] == 'select':
                    currentscttext = Select(el.get()).all_selected_options[0].text
                    # logging.info(currenttext)
                    if data == None:
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
                    elif data in currentscttext and u'请选择' not in currentscttext:
                        pass
                    else:
                        # selOption = Select(el.get()).all_selected_options
                        allOptions = Select(el.get()).options
                        for selem in allOptions:
                            if data == selem.text:
                                index = allOptions.index(selem)
                                Select(el.get()).select_by_index(index)
                                break
                    currenttext = Select(el.get()).all_selected_options[0].text

                elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                    el.get().clear()
                    el.get().send_keys(data)
                    currenttext = el.get().get_attribute('value')
                else:
                    el.get().clear()
                    el.get().send_keys(data)
                    currenttext = el.get().text
            logging.info(tagtxt + ':' + currenttext)
            '''
            el.get_element('tianjiafuzhufangwu')
            el.get().click()
            logging.info(u'点击添加附属房屋')

            self.driver.switch_to.default_content()
            el.get_element('fuzhufangwuiframe')
            xf = el.get()
            self.driver.switch_to.frame(xf)
            time.sleep(3)
            if msgmode != 'fuzhufangwuleixing':
                el.get_element('fuzhufangwuleixing')
                if data == None :
                    rd = random.randint(2, len(Select(el.get()).options))
                    Select(el.get()).select_by_index(rd)
                else:
                    if msgmode==u'必填'or msgmode==None:
                        listop = Select(el.get()).options
                        for i in range(len(listop)):
                            if listop[i].text == data:
                                Select(el.get()).select_by_index(i)
                    else:
                        rd = random.randint(2, len(Select(el.get()).options))
                        Select(el.get()).select_by_index(rd)


                logging.info(u'附属房屋类型：' + Select(el.get()).all_selected_options[0].text)

            if msgmode != None and msgmode !=u'必填':
                el.get_element(msgmode)
                dictFunction = EL.get_el_dict(AddNewDetail[0], msgmode, xmlpath)
                if dictFunction['elementType'] == 'select':
                    if Select(el.get()).all_selected_options[0] != data:
                        listop = Select(el.get()).options
                        #print listop[i].text
                        for i in range(len(listop)):
                            if listop[i].text == data:
                                Select(el.get()).select_by_index(i)
                else:
                    el.get().send_keys(data)

            el.get_element('fuzhufangwuSave')
            el.get().click()
            #self.driver.switch_to.default_content()
            # print self.driver.current_url
            #el.get_element('xiangxixinxiIframe')
            #self.driver.switch_to.frame(el.get())
            # print self.driver.current_url

        self.driver.switch_to.default_content()
        el.getFunctionName(MultiAddNew[0])
        el.get_element('fuzhuweiguframe')
        xf = el.get()
        self.driver.switch_to.frame(xf)
        #time.sleep(10)
        self.driver.execute_script('scroll(250, 0)')
        #print self.driver.current_url

        # 点击委估对象保存按钮
        el.get_element('save')
        el.get().click()
        time.sleep(2)

        self.driver.switch_to.default_content()
        el.get_element('buxuyao')
        el.get().click()
        time.sleep(3)

        el.getFunctionName(MultiAddNew[0])
        el.get_element('weiguduixiangframe')
        xf1 = el.get()
        self.driver.switch_to.frame(xf1)
        time.sleep(5)

        el.get_element('save')
        el.get().click()

        if msgmode == 'danjia' or msgmode == 'zongjia':
            self.driver.switch_to.default_content()
            time.sleep(1)
            el.get_element('danjiaOK')
            el.get().click()



        commond.Switchto_Frame(self, Inquiry)

        if data != None and valuation != True:
            time.sleep(1)
            commond.SelectFirstData(self, self.el)
            result = commond.GetDetail(self, self.el, MultiAddNew, msgmode).strip()
            return result
        else:
            time.sleep(1)
            commond.SelectFirstData(self, self.el)
            commond.switchToDetailUI(self, el)
            time.sleep(1)

            # 判断是否为Tab方式
            el.getFunctionName(AddNewDetail[0])
            el.get_element('tabshowdiv')
            tabatb = el.get().get_attribute('class')
            #logging.info(u'查看Tab是否勾选')
            if 'chked' in tabatb:
                el.get_element('tabchkbox')
                el.get().click()

            # 谷歌浏览器不支持
            js = "var q=document.documentElement.scrollTop=10000"
            self.driver.execute_script(js)

            #点击客户信息界面委估对象信息
            el.getFunctionName(MultiAddNew[0])
            if msgmode == 'danjia' or msgmode == 'zongjia':
                el.get_element('weiguhuijiashuju')
            else:
                el.get_element('weigushuju')
            el.get().click()



            self.driver.switch_to.default_content()
            el.getFunctionName(MultiAddNew[0])

            # 不屏蔽新增可用
            el.get_element('frame')

            #不新增可用
            #el.get_element('weiguduixiangframe')

            xf = el.get()
            self.driver.switch_to.frame(xf)
            time.sleep(5)



            el.get_element('resfuzhufangwu')
            el.get().click()

            self.driver.switch_to.default_content()
            el.get_element('fuzhuweiguframe2')
            xfres=el.get()

            self.driver.switch_to.frame(xfres)
            time.sleep(3)

            if msgmode==u'必填' or msgmode==None:
                el.get_element('fuzhufangwuleixing')
                dictFunction = EL.get_el_dict(MultiAddNew[0], 'fuzhufangwuleixing', xmlpath)
            else:
                el.get_element(msgmode)
                dictFunction = EL.get_el_dict(MultiAddNew[0], msgmode, xmlpath)
            tagname = None
            try:
                tagname = el.get().get_attribute('tagname')
            except:
                pass
            if tagname == None:
                tagname = ''
            currenttext = u'没有类型'

            if 'elementType' in dictFunction:
                if dictFunction['elementType'] == 'select':
                    currenttext = Select(el.get()).all_selected_options[0].text
                elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                    currenttext = el.get().get_attribute('value').strip()
                else:
                    currenttext = el.get().text.strip()
            result = currenttext
            logging.info(tagname + ':' + currenttext)
            return result

def checkTab(el):
    el.getFunctionName(AddNewDetail[0])
    # 判断是否为Tab方式
    el.get_element('tabshowdiv')
    tabatb = el.get().get_attribute('class')
    logging.info(u'查看是否为Tab方式')
    if 'chked' in tabatb:
        el.get_element('tabchkbox')
        el.get().click()




