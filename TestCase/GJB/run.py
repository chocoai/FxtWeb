#!/usr/bin/python
#coding:utf-8
import os
import sys
sys.path.append(os.path.join(os.getcwd(),os.pardir,os.pardir))
#sys.path.append('/root/FxtWeb')
from COMMON import RUN as Rn
from COMMON import CONFIG as CG
from COMMON import CONFIG as readConfig
currentPath=os.getcwd()
cmdput=CG.ReadConfig(currentPath).getConfigValue('CmdLogPut')
t=Rn.MyRun(currentPath,cmdput)
t.start()
mailValue = readConfig.ReadConfig(currentPath).getConfigValue('Email')
if mailValue == 'ON' or mailValue == 'on':
    attfile = t.attFile()
    t.mailSend(attfile)
    

