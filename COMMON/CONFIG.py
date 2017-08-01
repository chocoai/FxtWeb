#coding:utf-8
import os,os.path
import configparser
import codecs
import zipfile
#global configfile_path
#项目根路径
prjDir = os.path.abspath(os.path.join(os.path.split(os.path.realpath(__file__))[0],os.pardir))
#下载路径
downloadDir=os.path.join(prjDir,"Download")
#Cookies标识变量
Cookies=None
#登陆账户标识变量
SessionUserName=None
currentpath=os.getcwd()
class ReadConfig:
    def __init__(self,filepath=''):
        filefig=os.path.join(filepath,'config.ini')
        fd=open(filefig)
        data = fd.read()
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(filefig, "w")
            file.write(data)
            file.close()
        fd.close()
        self.cf = configparser.ConfigParser()
        self.cf.read(filefig)
    def getConfigValue(self, name):
        """
        获取cofing的对应值
        :param name:
        :return:
        """
        value = self.cf.get("config", name)
        return value
    def getEmailValue(self, name):
        """
        获取ini文件中Email项对应的值
        :param name:
        :return:
        """
        value = self.cf.get("email", name)
        return value
    def getEmail(self):
        """获取config中邮件配置信息
        :return:返回字典类型
        """
        listValues={}
        sections=self.cf.sections()
        for i in range(len(sections)):
            if sections[i]=='email':
                for j in self.cf.options(sections[i]):
                    listValues[j]=self.cf.get('email',j)
        return listValues
    def getEmailAttPath(self,attpath):
        """
        获取附件路径
        :param attpath: 文件夹路径
        :return: 路径
        """
        self.attPath=self.zipDir(attpath,(attpath+'.zip'))
        return self.attPath
    def zipDir(self,dirname,zipfilename):
        """
        压缩文件，返回路径
        :param dirname: 文件夹路径
        :param zipfilename: 压缩文件路径
        :return: 返回压缩文件路径
        """
        filelist=[]
        if os.path.isfile(dirname):
            filelist.append(dirname)
        else:
            for root,dirs,files in os.walk(dirname):
                for name in files:
                    filelist.append(os.path.join(root,name))
        zf=zipfile.ZipFile(zipfilename,'w',zipfile.zlib.DEFLATED)
        for tar in filelist:
            arcname=tar[len(dirname):]
            zf.write(tar,arcname)
        zf.close()
        return zipfilename








