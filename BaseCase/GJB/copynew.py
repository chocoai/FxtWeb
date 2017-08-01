#coding:utf-8
import COMMON.ELEMNET as EL
import os
import time
import random
import logging
from selenium.webdriver.support.ui import Select
from BaseCase.GJB import commond
from COMMON import CONFIG as CFG
xmlpath=os.path.join(CFG.prjDir,'BaseCase/GJB')
dataDetail=EL.get_el_name('DetailData',xmlpath)
MsgBtn=EL.get_el_name('MsgBtnKey',xmlpath)
MulMsgBtn=EL.get_el_name('MulMsgBtnKey',xmlpath)
MsgFrm=EL.get_el_name('MsgFrame',xmlpath)
dataCopyNew=EL.get_el_name('Fuzhixinzeng',xmlpath)

def NewData(self,el,ButtonKey=None,Num=1,Inquiry=None):

    """
    选择数据进行复制新增（从第一条开始）
    :param self:
    :param el:
    :param ButtonKey:
    :param num:
    :return:
    """
    num=Num
    if Inquiry==None:
        commond.Duantao(self,el)
    else:
        commond.OtherXujia(self,el,Inquiry)
    commond.ChkData(el,num)
    el.getFunctionName(dataCopyNew[0])
    el.get_element(dataCopyNew[1])
    el.get().click()
    self.driver.switch_to.default_content()
    if num > 1:
        el.get_element('multext')
        text=el.get().text
        el.get_element('mulOK')
        el.get().click()
        return text
    el.getFunctionName(MsgFrm[0])
    el.get_element(MsgFrm[1])
    xf=el.get()
    self.driver.switch_to.frame(xf)
    if ButtonKey not in MsgBtn or ButtonKey==None:
        ButtonKey='save'
    if Inquiry!=None:
        time.sleep(3)#10 fixed to 3
        el.getFunctionName(MulMsgBtn[0])
        el.get_element(ButtonKey)
    else:
        el.getFunctionName(MsgBtn[0])
        el.get_element(ButtonKey)
    el.get().click()
    self.driver.switch_to.default_content()

def NewCopyMold(self,el,num,link=None,Inquiry=None,ButtonKey=None):
    """
    复制新增数据
    :param self: 类的默认参数
    :param el: Element类对象
    :param num: 数目
    :param link: 环节
    :param Inquiry: 询价类型
    :param ButtonKey: 按钮
    :return: 环节编号
    """
    if Inquiry == None:
        commond.Duantao(self, el)
    else:
        commond.OtherXujia(self, el, Inquiry)
    idNum=commond.LinkDate(el,num,link)
    el.getFunctionName(dataCopyNew[0])
    el.get_element(dataCopyNew[1])
    el.get().click()
    self.driver.switch_to.default_content()
    if num > 1:
        el.get_element('multext')
        text = el.get().text
        el.get_element('mulOK')
        el.get().click()
        return text

    el.getFunctionName(MsgFrm[0])
    el.get_element(MsgFrm[1])
    xf = el.get()
    self.driver.switch_to.frame(xf)

    #需要加入对必填项检查的代码
    el.getFunctionName(dataDetail[0])
    el.get_element('jishutuandui')
    currentseltext=Select(el.get()).all_selected_options[0].text
    logging.info(u'当前技术团队项为：'+currentseltext)
    if u'请选择' in currentseltext:
        logging.info(len(Select(el.get()).options))
        rd = random.randint(1, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rd)
        seltext=Select(el.get()).all_selected_options[0].text
        logging.info(u'选择技术团队项为：'+seltext)


    if ButtonKey not in MsgBtn or ButtonKey == None:
        ButtonKey = 'save'
    if Inquiry != None:
        time.sleep(3)#10s fixed to 3
        el.getFunctionName(MulMsgBtn[0])
        #el.get_element(ButtonKey)
    else:
        el.getFunctionName(MsgBtn[0])
    el.get_element(ButtonKey)
    el.get().click()

    self.driver.switch_to.default_content()
    return idNum

def NewCopyDetail(self,el,args=None,ButtonKey=None,Inquiry=None):
    """
    复制新增功能
    :param self:
    :param el: Element类对象
    :param args: 参数组，
    :param ButtonKey: 操作的按钮，默认为保存
    :param Inquiry: 询价方式
    :return:
    """
    if Inquiry == None:
        commond.Duantao(self, el)
    else:
        commond.OtherXujia(self, el, Inquiry)

    commond.LinkDate(el)

    el.getFunctionName(dataCopyNew[0])
    el.get_element(dataCopyNew[1])
    el.get().click()

    self.driver.switch_to.default_content()
    el.getFunctionName(MsgFrm[0])
    el.get_element(MsgFrm[1])
    xf = el.get()
    self.driver.switch_to.frame(xf)

    el.getFunctionName(dataDetail[0])
    el.get_element('jishutuandui')

    '''
    #当前技术团队项为
    currentseltext = Select(el.get()).all_selected_options[0].text
    print currentseltext
    if u'请选择' in currentseltext:
        rd = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rd)
        #Select(el.get()).all_selected_options[0].text
    '''

    # 技术团队
    #el.get_element('jishutuandui')
    if len(Select(el.get()).options) < 2:
        el.get_element('weituoleixing')
        selOption = Select(el.get()).all_selected_options
        allOptions = Select(el.get()).options
        print allOptions

        if selOption[0] in allOptions:
            index = allOptions.index(selOption[0])
            while True:
                rd = random.randint(1, len(allOptions) - 1)
                if index != rd:
                    Select(el.get()).select_by_index(rd)
                    break
    # 当前技术团队项
    el.get_element('jishutuandui')
    currentseltext = Select(el.get()).all_selected_options[0].text
    if u'请选择' in currentseltext:
        rd = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rd)
        logging.info(u'技术团队：' + Select(el.get()).all_selected_options[0].text)


    el.get_element('shenfen')
    selProvince=Select(el.get()).all_selected_options[0].text
    if u'请选择'in selProvince:
        rdP = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdP)
        el.get_element('chengshi')
        rdC = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdC)
        el.get_element('xingzhengqu')
        rdX = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdX)
        el.get_element('quyu')
        rdQ = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdQ)

    el.get_element('chengshi')
    field_cityid=Select(el.get()).all_selected_options[0].text
    if u'请选择' in field_cityid:
        rdC = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdC)
        el.get_element('xingzhengqu')
        rdX = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdX)
        el.get_element('quyu')
        rdQ = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdQ)

    el.get_element('xingzhengqu')
    field_areaid=Select(el.get()).all_selected_options[0].text
    if u'请选择' in field_areaid:
        rdX = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdX)
        el.get_element('quyu')
        rdQ = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdQ)

    #el.get_element('quyu')
    #field_subareaid=Select(el.get()).all_selected_options[0].text
    #if u'请选择' in field_subareaid:
        #rdQ = random.randint(2, len(Select(el.get()).options) - 1)
        #Select(el.get()).select_by_index(rdQ)


    firstText=commond.NewDataDetial(el,args)

    if ButtonKey not in MsgBtn or ButtonKey == None:
        ButtonKey = 'save'
    if Inquiry != None:
        time.sleep(5)# 10s fixed 3s
        el.getFunctionName(MulMsgBtn[0])
        # el.get_element(ButtonKey)
    else:
        el.getFunctionName(MsgBtn[0])
    el.get_element(ButtonKey)
    el.get().click()
    self.driver.switch_to.default_content()
    time.sleep(3)
    commond.Switchto_Frame(self,Inquiry)
    commond.SelectFirstData(self,el)

    self.driver.switch_to.default_content()
    el.getFunctionName(MsgFrm[0])
    el.get_element(MsgFrm[1])
    xf = el.get()
    self.driver.switch_to.frame(xf)

    secondText = commond.NewDataDetial(el, args)

    if firstText[0]==''or firstText[0]==None:
        firstTXT=u'未填写'
    else:
        firstTXT=firstText[0]

    if secondText[0]==None or secondText[0]=='':
        secondTXT=u'未填写'
    else:
        secondTXT=secondText[0]

    #logging.info(firstText[1]+u' 复制前：'+firstTXT+u'-- 复制后：'+secondTXT)
    if firstText[0]==secondText[0]:
        return True
    else:
        return False

def PropertyRightMessage(self,el,args,ButtonKey=None,Inquiry=None):
    """
    产权信息（只能检查第一条信息）
    :param self:
    :param el:
    :param args:
    :param ButtonKey:
    :param Inquiry:
    :return:
    """

    if Inquiry == None:
        commond.Duantao(self, el)
    else:
        commond.OtherXujia(self, el, Inquiry)

    commond.LinkDate(el)

    el.getFunctionName(dataCopyNew[0])
    el.get_element(dataCopyNew[1])
    el.get().click()

    self.driver.switch_to.default_content()
    el.getFunctionName(MsgFrm[0])
    el.get_element(MsgFrm[1])
    xf = el.get()
    self.driver.switch_to.frame(xf)

    el.getFunctionName(dataDetail[0])
    el.get_element('chanquanleixing')
    proRig=Select(el.get()).all_selected_options[0].text
    logging.info(proRig)

    el.get_element('chanquanxinxi')
    if len(el.gets()) > 2:
        print args
        el.get_element(args)
        firstText=el.get().get_attribute('value')
        logging.info(el.get().get_attribute('tagname') + firstText)
    else:
        firstText=''
        logging.info(u'没有产权信息')

    el.get_element('jishutuandui')

    # 当前技术团队项为
    currentseltext = Select(el.get()).all_selected_options[0].text
    if u'请选择' in currentseltext:
        rd = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rd)
        # Select(el.get()).all_selected_options[0].text

    el.get_element('shenfen')
    selProvince = Select(el.get()).all_selected_options[0].text
    if u'请选择' in selProvince:
        rdP = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdP)
        el.get_element('chengshi')
        rdC = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdC)
        el.get_element('xingzhengqu')
        rdX = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdX)
        el.get_element('quyu')
        rdQ = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdQ)

    el.get_element('chengshi')
    field_cityid = Select(el.get()).all_selected_options[0].text
    if u'请选择' in field_cityid:
        rdC = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdC)
        el.get_element('xingzhengqu')
        rdX = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdX)
        el.get_element('quyu')
        rdQ = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdQ)

    el.get_element('xingzhengqu')
    field_areaid = Select(el.get()).all_selected_options[0].text
    if u'请选择' in field_areaid:
        rdX = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdX)
        el.get_element('quyu')
        rdQ = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdQ)



     #保存操作
    if ButtonKey not in MsgBtn or ButtonKey == None:
        ButtonKey = 'save'
    if Inquiry != None:
        time.sleep(3)#10 fixed to 3
        el.getFunctionName(MulMsgBtn[0])
    else:
        el.getFunctionName(MsgBtn[0])
    el.get_element(ButtonKey)
    el.get().click()
    self.driver.switch_to.default_content()
    time.sleep(3)
    commond.Switchto_Frame(self, Inquiry)
    commond.SelectFirstData(self, el)

    self.driver.switch_to.default_content()
    el.getFunctionName(MsgFrm[0])
    el.get_element(MsgFrm[1])
    xf = el.get()
    self.driver.switch_to.frame(xf)

    el.getFunctionName(dataDetail[0])
    el.get_element('chanquanxinxi')
    if len(el.gets()) > 2:
        el.get_element(args)
        secondText = el.get().get_attribute('value')
        logging.info(u'复制后：'+el.get().get_attribute('tagname') +secondText)
    else:
        secondText = ''
        logging.info(u'复制后没有产权信息')
        exit(' no ')

    if firstText==''and secondText=='':
        return False
    elif firstText!=secondText:
        return False
    else:
        return

def SubHouse(self,el,args,ButtonKey=None,Inquiry=None):
    """
    附属房屋添加操作
    :param self:
    :param el:
    :param args:
    :param ButtonKey:
    :param Inquiry:
    :return:
    """
    if Inquiry == None:
        commond.Duantao(self, el)
    else:
        commond.OtherXujia(self, el, Inquiry)

    commond.LinkDate(el)

    el.getFunctionName(dataCopyNew[0])
    el.get_element(dataCopyNew[1])
    el.get().click()

    self.driver.switch_to.default_content()
    el.getFunctionName(MsgFrm[0])
    el.get_element(MsgFrm[1])
    xf = el.get()
    self.driver.switch_to.frame(xf)

    el.getFunctionName(dataDetail[0])

    el.get_element('fuzhufangwuxinxi')
    if len(el.gets()) > 2:
        el.get_element(args)
        firstText = el.get().text
        logging.info( u'复制前：'+firstText)
    else:
        firstText = ''
        logging.info(u'没有附属房屋信息')

    # 当前技术团队项为
    el.get_element('jishutuandui')
    currentseltext = Select(el.get()).all_selected_options[0].text
    if u'请选择' in currentseltext:
        rd = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rd)
        # Select(el.get()).all_selected_options[0].text

    el.get_element('shenfen')
    selProvince = Select(el.get()).all_selected_options[0].text
    if u'请选择' in selProvince:
        rdP = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdP)
        el.get_element('chengshi')
        rdC = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdC)
        el.get_element('xingzhengqu')
        rdX = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdX)
        el.get_element('quyu')
        rdQ = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdQ)

    el.get_element('chengshi')
    field_cityid = Select(el.get()).all_selected_options[0].text
    if u'请选择' in field_cityid:
        rdC = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdC)
        el.get_element('xingzhengqu')
        rdX = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdX)
        el.get_element('quyu')
        rdQ = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdQ)

    el.get_element('xingzhengqu')
    field_areaid = Select(el.get()).all_selected_options[0].text
    if u'请选择' in field_areaid:
        rdX = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdX)
        el.get_element('quyu')
        rdQ = random.randint(2, len(Select(el.get()).options) - 1)
        Select(el.get()).select_by_index(rdQ)

    # 保存操作
    if ButtonKey not in MsgBtn or ButtonKey == None:
        ButtonKey = 'save'

    if Inquiry != None:
        time.sleep(3)#10 fixed to 3
        el.getFunctionName(MulMsgBtn[0])
    else:
        el.getFunctionName(MsgBtn[0])
    el.get_element(ButtonKey)
    el.get().click()
    self.driver.switch_to.default_content()
    time.sleep(3)
    commond.Switchto_Frame(self, Inquiry)
    commond.SelectFirstData(self, el)

    self.driver.switch_to.default_content()
    el.getFunctionName(MsgFrm[0])
    el.get_element(MsgFrm[1])
    xf = el.get()
    self.driver.switch_to.frame(xf)

    el.getFunctionName(dataDetail[0])
    el.get_element('fuzhufangwuxinxi')

    if len(el.gets()) > 2:
        el.get_element(args)
        secondText = el.get().text
        logging.info(u'复制后：' + secondText)
    else:
        secondText = ''
        logging.info(u'复制后没有附属房屋信息')
        exit()

    if firstText == '' and secondText == '':
        return False
    elif firstText=='0' or secondText=='0':
        return True
    elif firstText != secondText and firstText!='0':
        return False
    else:
        return True













