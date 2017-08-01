#coding:utf-8
import os,sys
import xlrd
import json
from xml.etree import ElementTree as elementTree
import CONFIG as readConfig
#import DRIVER as DR


global fHost, dKey, dValue
xmlNodePath = os.path.join(readConfig.prjDir, 'config', 'node.xml')
def get_xls(sheetname,casetar='username',path='',rowsindex=7):
    """
    获取xlsx表格
    :param sheetname:表单名
    :param casetar: 第一行第一列名
    :param path: 文件所在路径
    :param rowsindex:行数索引，确定需要排除的项
    :return: 以列表返回数据
    """
    cls=[]
    if path=='':
        path=os.getcwd()
    #xlsPath = os.path.join(path, 'TestCase.xlsx')
    xlsPath=path
    data=xlrd.open_workbook(xlsPath)
    table=data.sheet_by_name(sheetname)
    nrows=table.nrows

    for i in range(nrows):
        if table.row_values(i)[0]!=casetar and table.row_values(i)[rowsindex]!=0:
            cls.append(table.row_values(i))
    print u'%s的测试用例数共为:%d 条'%(sheetname,len(cls))
    return cls
def get_xls_dict(sheetname,path=None):
    """
    获取xlsx表格中的数据，并返回每一条数据存入字典
    :param sheetname:表单页名
    :param path:文件路径
    :return:返回字典的列表集
    """
    res=[]
    if path == None:
        path = os.getcwd()
    xlsPath = os.path.join(path, 'TestCase.xlsx')
    data = xlrd.open_workbook(xlsPath)
    table = data.sheet_by_name(sheetname)
    nrows = table.nrows
    for i in range(1,nrows):
        cls = {}
        for j in range(table.ncols):
            cls[table.row_values(0)[j]]=table.row_values(i)[j]
        res.append(cls)
    return res
def get_xml_grid():
    """
    获取IP，浏览器
    :param projectPath:当前项目配置文件路径
    :return: 字典
    """
    fHost = {}
    if len(fHost) == 0:
        per = elementTree.parse(xmlNodePath)
        all_element = per.findall('node')

        for firstElement in all_element:

            for secondElement in firstElement.getchildren():
                #print secondElement
                if secondElement.tag == 'host':
                    dkey = secondElement.text
                if secondElement.tag == 'browser':
                    dValue = secondElement.text
                    fHost[dkey] = dValue
    return fHost
def get_xml_girdParam():
    """
    获取机器IP与浏览器
    :return: 列表
    """
    fList = []
    if len(fList)==0:
        per=elementTree.parse(xmlNodePath)
        nodeElement=per.findall('node')
        for subNode in nodeElement:
            subdict={}
            for subElement in subNode.getchildren():
                if subElement.tag=='host':
                    subdict['host']=subElement.text
                if subElement.tag=='browser':
                    subdict['browser']=subElement.text
                if subElement.tag=='index':
                    subdict['index']=subElement.text
            fList.append(subdict)
    return fList
def get_xls_sql(filename,dataPath):
    """
    读取excel文件
    :param filename:文件名称
    :return:
    """
    cls = []
    path = dataPath
    xlsPath = os.path.join(path, filename)
    data = xlrd.open_workbook(xlsPath)
    #table = data.sheet_by_name(sheetname)
    sheets=data.sheets()
    for sheet in sheets:
        nrows = sheet.nrows
        #print sheet.name
        for i in range(2,nrows):

            line=sheet.row_values(i)
            line.append(sheet.name)
            #print line
            '''
            params = line[7].strip('\n') if line[7] != 'None' else ''
            #trans for " to '
            if "\"" in params:
                params = params.replace("\"","\'")
            if '\n' in params:
                params = params.replace("\n","")
            if '  ' in params:
                params = params.replace("  ","")
            params.strip('\n')
            #print type(params),params

            line[7]=params
            '''
            cls.append(line)
    return cls


def get_girdDriver(index):
    """
    获取启动客户机IP，执行浏览器信息
    :param index: 标识
    :return: 返回IP，浏览器信息
    """
    listdriver=get_xml_girdParam()
    for dr in listdriver:
        if dr['index']==index:
            host=dr['host']
            browser=dr['browser']
            driver=DR.MyDriver.get_gridDriver(host,browser)
            return driver
def get_module():
    """
    获取当前模块名
    :return: 模块名
    """
    def main_module_name():
        mod = sys.modules['__main__']
        file = getattr(mod, '__file__', None)
        return file and os.path.splitext(os.path.basename(file))[0]

    def modname(fvars):

        file, name = fvars.get('__file__'), fvars.get('__name__')
        if file is None or name is None:
            return None

        if name == '__main__':
            name = main_module_name()
        return name

    module_name = modname(globals())
    return module_name
def get_json_value(key,path):
    """
    通过key,获取value
    :param key: 关键字
    :param path: json文件路径
    :return:
    """
    fj=open(path,'r')
    jsn=json.load(fj)
    fj.close()
    return jsn[key]
def get_json(path):
    """
    读取json文件
    :param path: 文件路径
    :return:
    """
    fj=open(path)
    jsn=json.load(fj)
    fj.close()
    return jsn


