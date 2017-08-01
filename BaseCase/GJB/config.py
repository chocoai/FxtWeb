#coding:utf-8
import os
import sys
import COMMON.ELEMNET as EL
from COMMON import CONFIG as CFG
from COMMON import COMMON as cn

url=CFG.ReadConfig().getConfigValue('Url')
datapath=os.getcwd()
path=os.path.join(CFG.prjDir, 'BaseCase/GJB')
dataDetail=EL.get_el_name('DetailData', path)

TitleMode = EL.get_el_name('Xujia', path)
eldantao=EL.get_el_name('Dantao', path)
elquanbu=EL.get_el_name('Quanbu', path)
elGaizhang=EL.get_el_name('Gaizhang', path)
tableData=EL.get_el_name('Checkbox', path)
elZXYP=EL.get_el_name('Zuanxieyuping', path)
elDateDetail=EL.get_el_name('DetailData', path)
eDaochu=EL.get_el_name('Daochu', path)
Distributed=CFG.ReadConfig().getConfigValue('Distributed')
MsgFrm=EL.get_el_name('MsgFrame', path)
dAddDetail=EL.get_el_name('AddNewDetail',path)
elData=EL.get_el_name('Checkbox',path)
query=EL.get_el_name('Query',path)
ExamineModif=EL.get_el_name('ExamineModif', path)
if len(sys.argv)>=2:
    if sys.argv[1]=='09':
        username = CFG.ReadConfig().getConfigValue('09username')
        password = CFG.ReadConfig().getConfigValue('09password')
    elif sys.argv[1]=='10':
        username = CFG.ReadConfig().getConfigValue('10username')
        password = CFG.ReadConfig().getConfigValue('10password')
    else:
        exit('exit system!')
else:
    username=CFG.ReadConfig().getConfigValue('username')
    password=CFG.ReadConfig().getConfigValue('password')
sessionName=CFG.SessionUserName
Browser=CFG.ReadConfig().getConfigValue('Browser')

entrustObject=EL.get_el_name('EntrustObject',path)
#报告参数
report=EL.get_el_name('RPLeftTilte', path)
reportCheck=EL.get_el_name('RPCheck', path)
reportFrame=EL.get_el_name('RPiframe', path)
reportTabweb=EL.get_el_name('RPtabweb', path)
reportButton=EL.get_el_name('RPbutton',path)
reportdReportTab=EL.get_el_name('RPdTab',path)
reportTabchk=EL.get_el_name('RPtabchk',path)
reportReportInfo=EL.get_el_name('RPreportInfo',path)
reportRequestInfo=EL.get_el_name('RPrequestInfo',path)
reportDataButton=EL.get_el_name('RPdataButton',path)
reportTooltip=EL.get_el_name('RPtoolTip',path)
reportUser=EL.get_el_name('RPuser',path)
reportDataDetail=EL.get_el_name('RPdataDetail',path)
reportQuery=EL.get_el_name('RPquery',path)
reportUserText=EL.get_el_name('RPuserTxet',path)
#报告数据
jsndatapath=os.path.join(path, 'chkdata.json')
jsedatapath=os.path.join(path,'EntrustObject.json')
EjsonData=cn.get_json(jsedatapath)
