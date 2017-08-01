#coding:utf-8
import os
import time
import random
import logging
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from BaseCase.GJB import commond
from BaseCase.GJB import addnew
from COMMON import CONFIG as CFG
import COMMON.ELEMNET as EL

xmlpath=os.path.join(CFG.prjDir,'BaseCase/GJB')
ExamineModif=EL.get_el_name('ExamineModif', xmlpath)
MsgBtn=EL.get_el_name('MsgBtnKey',xmlpath)
MsgFrm=EL.get_el_name('MsgFrame',xmlpath)
chkElementlist=EL.get_el_name('Checkbox',xmlpath)

def QueryData(self,el,msgmode=None,data=None,link=None,submode=None,button=None,Inquiry=None):
    """
    查看数据的正确性
    :param self:
    :param el:
    :param msgmode:xml文件中元素定位名称
    :param data:输入的数据
    :param link:环节
    :param submode:单套询价的询价类型
    :param button:数据详细界面的按钮
    :param Inquiry:询价类型,如多套，单套
    :return:
    """
    if Inquiry==None:
        commond.Duantao(self,el,submode)
        listid=QueryClickLinkData(el,msgmode,link,functionName='Querylist')
        #listid=commond.ClickLinkData(el,msgmode,link,functionName='Querylist')
        #commond.Switchto_Frame(self,Inquiry)
        currentuser=commond.sessionName
        valuer=commond.Valuer

        '''
        self.driver.switch_to.default_content()
        el.getFunctionName(MsgFrm[0])
        el.get_element(MsgFrm[1])
        xf = el.get()
        self.driver.switch_to.frame(xf)
        time.sleep(5)
        '''
        commond.switchToDetailUI(self,el)
        if button==1:
            el.getFunctionName(ExamineModif[0])
            el.get_element('keybutton')
            for i in range(len(el.gets())):
                keyvalue=el.gets()[i].get_attribute('value')
                if msgmode==keyvalue:
                    return keyvalue
            else:
                logging.error(u'没有此按钮，请确认！')
                exit(u'退出测试')
        else:
            addnew.checkTab(el)
            el.getFunctionName(ExamineModif[0])
            el.get_element(msgmode)
            dictFunction = EL.get_el_dict(ExamineModif[0], msgmode, xmlpath)
            try:
                tagname = el.get().get_attribute('tagname')
            except:
                tagname='Element not exist'
            if tagname == None:
                tagname = ''
            currenttext = u'没有类型'
            if tagname!='Element not exist':
                if 'elementType' in dictFunction:
                    if dictFunction['elementType'] == 'select':
                        if dictFunction['type']=='xpath':
                            ellen=len(el.gets())
                            if ellen>1:
                                currenttext=''
                                for i in range(ellen):
                                    currenttext+=Select(el.gets()[i]).all_selected_options[0].text
                                if msgmode=='weituokehu':
                                    currenttext=currenttext[1:]
                            else:
                                currenttext=Select(el.gets()[0]).all_selected_options[0].text
                        else:
                            currenttext = Select(el.get()).all_selected_options[0].text
                    elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                        currenttext = el.get().get_attribute('value').strip()

                    else:
                        currenttext = el.get().text.strip()
            else:
                currenttext =''
            logging.info(tagname + u'：' + currenttext.rstrip(u'请选择'))

            #结果为数字
            if currenttext.replace(',','').replace('.','').isdigit():
                if currenttext.find(',')>0:
                    currentvalue=currenttext.replace(',','')
                else:
                    currentvalue=float(currenttext)

                if msgmode=='pingguzongjia' or msgmode=='jingzhi':
                    return round(float(currentvalue)/10000,2)==float(listid)

                return float(currentvalue)==float(listid)

            if currenttext==''or currenttext=='0' and float(listid)==0:
                return True

            return (currenttext.rstrip(u'请选择').strip()==listid)
    else:
        commond.OtherXujia(self,el,Inquiry)

def modification_lookData(self,el,dataId,inquiry=None):
    """
    询价界面选择数据
    :param self:
    :param el:
    :param dataId:数据的询价编号
    :param inquiry:询价类型
    :return:
    """
    commond.Switchto_Frame(self, inquiry)
    el.getFunctionName(chkElementlist[0])
    el.get_element(chkElementlist[1])

    idList = []
    idtext = None
    time.sleep(1)
    for i in range(15):
        # 询价编号
        idtext = el.gets()[i].find_element_by_xpath('td[3]/div').text
        linktext = el.gets()[i].find_element_by_xpath('td[7]/div').text
        if idtext == dataId:
            Valuer = el.gets()[i].find_element_by_xpath('td[23]/div').text  # 获取选择数据的估价师
            idList.append(idtext)
            logging.info(u'找到数据，编号：' + idtext + u',环节：' + linktext)
            break
    else:
        logging.error(u'没有找到此编号数据！')
        exit(u'没有找到此编号数据，退出此用例！')
    ActionChains(el.getDriver()).double_click(el.gets()[i].find_element_by_xpath('td[3]/div')).perform()
    commond.switchToDetailUI(self,el)
    addnew.checkTab(el)
    return linktext

def ModificationData(self,el,msgmode=None,data=None,link=None,submode=None,button=None,Inquiry=None):
    """
    修改数据验证
    :param self:
    :param el:
    :param msgmode:元素在xml的名称
    :param data: 输入数据
    :param link: 环节
    :param submode: 单套询价类型
    :param button: 按钮
    :param Inquiry: 询价类型
    :return:
    """
    if Inquiry == None:
        commond.Duantao(self, el, submode)
        # commond.Switchto_Frame(self, Inquiry)
        # currentuser = commond.sessionName
        # valuer = commond.Valuer
        dataId=ModificationClickLinkData(el,link=link)
        commond.switchToDetailUI(self, el)

        '''
        if button == 'writePreviews':
            el.getFunctionName(ExamineModif[0])
            el.get_element(msgmode)
            el.get().click()
        '''


        addnew.checkTab(el)#查看是否Tab显示
        el.getFunctionName(ExamineModif[0])
        el.get_element(msgmode)
        commond.GetDetail(self, el, ExamineModif, msgmode)
        if msgmode != None:
                currenttext=''
                el.get_element(msgmode)
                dictFunction = EL.get_el_dict(ExamineModif[0], msgmode, xmlpath)
                try:
                    el.get().get_attribute('tagname')
                except:
                    raise (u'未找元素，请确认')
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
                            allOptions = Select(el.get()).options
                            for selem in allOptions:
                                if data == selem.text:
                                    index = allOptions.index(selem)
                                    Select(el.get()).select_by_index(index)
                                    break
                            else:
                                logging.info(u'选项中没有输入的项，请确认！')
                                exit(u'选项中没有输入的项，请确认！')
                        currenttext=Select(el.get()).all_selected_options[0].text

                    elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                        el.get().clear()
                        el.get().send_keys(data)
                        currenttext = el.get().get_attribute('value')
                    else:
                        el.get().clear()
                        el.get().send_keys(data)
                        currenttext = el.get().text
                logging.info(u'输入:'+currenttext)

        el.getFunctionName(MsgBtn[0])
        el.get_element('save')
        el.get().click()
        self.driver.switch_to.default_content()
        time.sleep(1)
        '''
        el.get_element('close')
        el.get().click()
        '''
        modification_lookData(self,el,dataId,Inquiry)
        commond.switchToDetailUI(self,el)
        newtext=commond.GetDetail(self, el, ExamineModif, msgmode)
        return data==newtext

    else:
        commond.OtherXujia(self, el, Inquiry)

def JudgeTOBData(el,link=None):
    """
    获取数据需要的数据
    :param el:
    :param link:
    :return:
    """
    sessionName = commond.sessionName
    el.getFunctionName(chkElementlist[0])
    el.get_element(chkElementlist[1])
    idList = []
    idtext = None
    #if link != None:
    for i in range(15):
        idtext = el.gets()[i].find_element_by_xpath('td[3]/div').text # 询价编号
        linktext = el.gets()[i].find_element_by_xpath('td[7]/div').text #环节
        datamode = el.gets()[i].find_element_by_xpath('td[2]/div/img').get_attribute('src')#来源
        opeartor = el.gets()[i].find_element_by_xpath('td[8]/div').text #当前处理人
        businessId=el.gets()[i].find_element_by_xpath('td[4]/div').text #业务编号
        if businessId=='':
            el.gets()[i].find_element_by_xpath('td/div/input').click()
            idList.append(idtext)
            logging.info(u'第 ' + str(i + 1) + u' 条数据')
            logging.info(u'选择编号：' + idtext + u',环节：' + linktext)
            break
    else:
        logging.error(u'没有找到数据！')
        exit(u'没有找到数据，退出此用例！')
    #ActionChains(el.getDriver()).double_click(el.gets()[i].find_element_by_xpath('td[3]/div')).perform()
    return idtext

def TransferOfBusiness(self,el,msgElement=None,data=None,link=None,submode=None,Inquiry=None):
    """
    转业务功能
    :param self:
    :param el:
    :param msgElement:
    :param data:
    :param link:
    :param submode:
    :param Inquiry:
    :return:
    """
    if Inquiry == None:
        commond.Duantao(self, el, submode)
        dataId=JudgeTOBData(el,link)
        #commond.switchToDetailUI(self, el)
        #print self.driver.current_url
        #time.sleep(3)
        el.getFunctionName(ExamineModif[0])
        el.get_element('transferOfBusiness')
        el.get().click()
        time.sleep(1)

        self.driver.switch_to.default_content()
        el.get_element('transferOfBusinessiframe')
        self.driver.switch_to.frame(el.get())
        #print self.driver.current_url

        el.getFunctionName(ExamineModif[0])
        # 查看是否Tab显示
        el.get_element('TOBtabshowdiv')
        tabatb = el.get().get_attribute('class')
        logging.info(u'查看是否为Tab方式')
        if 'chked' in tabatb:
            el.get_element('tabchkbox')
            el.get().click()

        if msgElement!='jishutuandui':
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

        if msgElement!='yewubumen':
            ##业务部门
            el.get_element('yewubumen')
            currentseltext = Select(el.get()).all_selected_options[0].text
            if u'请选择' in currentseltext:
                rd = random.randint(1, len(Select(el.get()).options) - 1)
                Select(el.get()).select_by_index(rd)
                logging.info(u'业务部门：' + Select(el.get()).all_selected_options[0].text)

        if msgElement!='baogaoleixing':
            ##报告类型
            el.get_element('baogaoleixing')
            currentseltext = Select(el.get()).all_selected_options[0].text
            if u'请选择' in currentseltext:
                rd = random.randint(1, len(Select(el.get()).options) - 1)
                Select(el.get()).select_by_index(rd)
                logging.info(u'报告类型：' + Select(el.get()).all_selected_options[0].text)
        #time.sleep(5)

        #if msgElement !=None:
            #.get_element(msgElement)

        if msgElement != None:
                currenttext=''
                el.get_element(msgElement)
                dictFunction = EL.get_el_dict(ExamineModif[0], msgElement, xmlpath)
                try:
                    el.get().get_attribute('tagname')
                except:
                    raise (u'未找元素，请确认')
                if 'elementType' in dictFunction:
                    if dictFunction['elementType'] == 'select':
                        currentscttext = Select(el.get()).all_selected_options[0].text
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
                            allOptions = Select(el.get()).options
                            for selem in allOptions:
                                if data == selem.text:
                                    index = allOptions.index(selem)
                                    Select(el.get()).select_by_index(index)
                                    break
                            else:
                                logging.info(u'选项中没有输入的项，请确认！')
                                exit(u'选项中没有输入的项，请确认！')
                        currenttext=Select(el.get()).all_selected_options[0].text

                    elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                        el.get().clear()
                        el.get().send_keys(data)
                        currenttext = el.get().get_attribute('value')
                    else:
                        el.get().clear()
                        el.get().send_keys(data)
                        currenttext = el.get().text
                logging.info(u'输入:'+currenttext)

        el.get_element('submitBusiness')
        el.get().click()
        time.sleep(5)
        self.driver.switch_to.default_content()
        time.sleep(1)
        el.get_element('nowSubmit')
        el.get().click()
        el.get_element('sureOK')
        el.get().click()



        modification_lookData(self,el,dataId,Inquiry)
        #commond.switchToDetailUI(self,el)
        #newtext=commond.GetDetail(self,el,ExamineModif,msgElement)
        #return data==newtext
    else:
        commond.OtherXujia(self, el, Inquiry)

def WritePreviews(self,el,msgElement=None,data=None,link=None,submode=None,Inquiry=None):
    if Inquiry == None:
        commond.Duantao(self, el, submode)
        dataId=JudgeTOBData(el,link)
        #commond.switchToDetailUI(self, el)
        el.getFunctionName(ExamineModif[0])
        el.get_element('writePreviews')
        el.get().click()
        time.sleep(1)

        self.driver.switch_to.default_content()
        el.get_element('transferOfBusinessiframe')
        self.driver.switch_to.frame(el.get())


        el.getFunctionName(ExamineModif[0])
        # 查看是否Tab显示
        el.get_element('pReevaluateTab')
        tabatb = el.get().get_attribute('class')
        logging.info(u'查看是否为Tab方式')
        if 'chked' in tabatb:
            el.get_element('tabchkbox')
            el.get().click()
        time.sleep(1)
        if msgElement!='jishutuandui':
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

        if msgElement!='yewubumen':
            ##业务部门
            el.get_element('yewubumen')
            currentseltext = Select(el.get()).all_selected_options[0].text
            if u'请选择' in currentseltext:
                rd = random.randint(1, len(Select(el.get()).options) - 1)
                Select(el.get()).select_by_index(rd)
                logging.info(u'业务部门：' + Select(el.get()).all_selected_options[0].text)

        if msgElement!='baogaoleixing':
            ##报告类型
            el.get_element('baogaoleixing')
            currentseltext = Select(el.get()).all_selected_options[0].text
            if u'请选择' in currentseltext:
                rd = random.randint(1, len(Select(el.get()).options) - 1)
                Select(el.get()).select_by_index(rd)
                logging.info(u'报告类型：' + Select(el.get()).all_selected_options[0].text)
        #time.sleep(5)

        #if msgElement !=None:
            #.get_element(msgElement)

        if msgElement != None:
                currenttext=''
                el.get_element(msgElement)
                dictFunction = EL.get_el_dict(ExamineModif[0], msgElement, xmlpath)
                try:
                    el.get().get_attribute('tagname')
                except:
                    raise (u'未找元素，请确认')
                if 'elementType' in dictFunction:
                    if dictFunction['elementType'] == 'select':
                        currentscttext = Select(el.get()).all_selected_options[0].text
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
                            allOptions = Select(el.get()).options
                            for selem in allOptions:
                                if data == selem.text:
                                    index = allOptions.index(selem)
                                    Select(el.get()).select_by_index(index)
                                    break
                            else:
                                logging.info(u'选项中没有输入的项，请确认！')
                                exit(u'选项中没有输入的项，请确认！')
                        currenttext=Select(el.get()).all_selected_options[0].text

                    elif dictFunction['elementType'] == 'input' or dictFunction['elementType'] == 'textarea':
                        el.get().clear()
                        el.get().send_keys(data)
                        currenttext = el.get().get_attribute('value')
                    else:
                        el.get().clear()
                        el.get().send_keys(data)
                        currenttext = el.get().text
                logging.info(u'输入:'+currenttext)
        time.sleep(1)
        el.get_element('pReevaluateSave')
        el.get().click()

        self.driver.switch_to.default_content()
        time.sleep(1)
        el.get_element('pReevaluateOk')
        el.get().click()
        '''
        el.get_element('sureOK')
        el.get().click()
        '''
        linkText=modification_lookData(self,el,dataId,Inquiry)
        if linkText==u'撰写预评中':
            return True
        #commond.switchToDetailUI(self,el)
        #newtext=commond.GetDetail(self,el,ExamineModif,msgElement)
        #return data==newtext

    else:
        commond.OtherXujia(self, el, Inquiry)

def QueryClickLinkData(el,msgmod=None,link=None,functionName=None):
    """
    点击数据并获取指定项的数据,并判断账户与估价是否一致
    :param el:
    :param msgmod:
    :param link:根据环节选择数据
    :param functionName:
    :return:
    """
    global Valuer
    sessionName = commond.sessionName
    time.sleep(1)
    el.getFunctionName(chkElementlist[0])
    try:
        msgnum = EL.get_el_value(functionName, msgmod, xmlpath)
        el.get_element('checkboxtitle')
        el.getDriver().implicitly_wait(30)
        msgnumll=int(msgnum)-1
        if msgnum>9:
        #js = "var q=document.documentElement.scrollTop=10000"
        #js="scroll(document.body.scrollWidth,0);"
        #el.getDriver().execute_script(js)
        #time.sleep(10)

            ll = el.get().find_elements_by_xpath('th')
            aa = ll[msgnumll]
            el.getDriver().execute_script("arguments[0].scrollIntoView();", aa)
            time.sleep(3)

        title = el.get().find_element_by_xpath('th['+msgnum+']/div').text
    except:
        msgnum=0
        title='not find'

    ''''
    for i in range(len(ll)):

        #js = "var q=document.documentElement.scrollLeft=10000"
        #js="scroll(10000,0);"
        #el.getDriver().execute_script(js)
        #time.sleep(10)

        #以下解决不在显示区的元素读取
        aa=ll[i]
        el.getDriver().execute_script("arguments[0].scrollIntoView();",aa)
        time.sleep(3)
        ActionChains(el.getDriver()).move_to_element(ll[i].find_element_by_xpath('div')).perform()

        print ll[i].find_element_by_xpath('div').text,ll[i].find_element_by_xpath('div').get_attribute('style')
    '''
    el.get_element(chkElementlist[1])
    idList = []
    try:
        len(el.gets())
    except:
        logging.error(u'没有数据请确认')
        tishitext = el.getDriver().find_element_by_xpath('/html/body/div/div[2]/div/div[5]/table/tbody/tr/td').text
        logging.info(tishitext)
        exit()
    if link != None:
        for i in range(15):
            # 询价编号
            idtext = el.gets()[i].find_element_by_xpath('td[3]/div').text
            linktext = el.gets()[i].find_element_by_xpath('td[7]/div').text
            Valuer=el.gets()[i].find_element_by_xpath('td[23]/div').text
            if linktext == link:
                if sessionName!=Valuer and Valuer!="":
                    continue
                el.gets()[i].find_element_by_xpath('td/div/input').click()
                idList.append(idtext)
                logging.info(u'选择编号：' + idtext + u',环节：' + linktext + u'的数据')
                break
        else:
            logging.error(u'没有找到此环节数据，或账号与估价师不一致！')
            exit(u'没有找到此环节数据')
        ActionChains(el.getDriver()).double_click(el.gets()[i].find_element_by_xpath('td[3]/div')).perform()
        return idtext
    else:
        rd = random.randint(0, 14)
        #rd=0
        logging.info(u'第 ' + str(rd + 1) + u' 条数据')
        idtext = el.gets()[rd].find_element_by_xpath('td[3]/div').text
        linktext = el.gets()[rd].find_element_by_xpath('td[7]/div').text
        if title == u'询价时间':
            resutltext = el.gets()[rd].find_element_by_xpath('td[' + str(msgnum) + ']/div').text.split()[0]
        else:
            resutltext = el.gets()[rd].find_element_by_xpath('td[' + str(msgnum) + ']/div').text
        logging.info(u'编号：' + idtext + u',环节：' + linktext)
        el.gets()[rd].find_element_by_xpath('td/div/input').click()
        ActionChains(el.getDriver()).double_click(el.gets()[rd].find_element_by_xpath('td[3]/div')).perform()

        logging.info(title+u'：'+resutltext)
        return resutltext

def ModificationClickLinkData(el,link=None,button=None):
    """
    点击数据并获取指定项的数据,并判断账户与估价是否一致
    :param el:
    :param msgmod:
    :param link:
    :param functionName:
    :return:
    """
    sessionName = commond.sessionName
    el.getFunctionName(chkElementlist[0])
    el.get_element(chkElementlist[1])
    idList = []
    idtext = None
    try:
        len(el.gets())
    except:
        logging.error(u'没有数据请确认')
        tishitext = el.getDriver().find_element_by_xpath('/html/body/div/div[2]/div/div[5]/table/tbody/tr/td').text
        logging.info(tishitext)
        exit()
    if link != None:
        for i in range(15):
            # 询价编号
            idtext = el.gets()[i].find_element_by_xpath('td[3]/div').text
            linktext = el.gets()[i].find_element_by_xpath('td[7]/div').text
            datamode=el.gets()[i].find_element_by_xpath('td[2]/div/img').get_attribute('src')
            opeartor=el.gets()[i].find_element_by_xpath('td[8]/div').text
            if linktext in link :
                #logging.info(sessionName+':'+opeartor)
                if sessionName==opeartor and (button==None or button=='save'):
                    #Valuer = el.gets()[i].find_element_by_xpath('td[23]/div').text  # 获取选择数据的估价师
                    el.gets()[i].find_element_by_xpath('td/div/input').click()
                    idList.append(idtext)
                    logging.info(u'第 '+str(i+1)+u' 条数据')
                    logging.info(u'选择编号：' + idtext + u',环节：' + linktext )
                    break
        else:
            logging.error(u'没有找到数据！')
            exit(u'没有找到数据，退出此用例！')
        ActionChains(el.getDriver()).double_click(el.gets()[i].find_element_by_xpath('td[3]/div')).perform()
        return idtext
    else:
        rd = random.randint(0, 14)
        # rd=0
        logging.info(u'第 ' + str(rd + 1) + u' 条数据')
        idtext = el.gets()[rd].find_element_by_xpath('td[3]/div').text
        linktext = el.gets()[rd].find_element_by_xpath('td[7]/div').text
        logging.info(u'编号：' + idtext + u',环节：' + linktext)
        #el.gets()[rd].find_element_by_xpath('td/div/input').click()
        ActionChains(el.getDriver()).double_click(el.gets()[rd].find_element_by_xpath('td[3]/div')).perform()
        return idtext
