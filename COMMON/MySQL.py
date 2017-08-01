# -*- coding: UTF-8 -*-
import MySQLdb
import logging
class MySql(object):
    def __init__(self):
        self.conn= MySQLdb.connect(
                host='192.168.2.32',
                port = 3306,
                user='root',
                passwd='fxt_2017',
                db='test',
                )

        self.cur = self.conn.cursor()
        self.conn.set_character_set('utf8')
        self.cur.execute('SET NAMES utf8;')
        self.cur.execute('SET CHARACTER SET utf8;')
        self.cur.execute('SET character_set_connection=utf8;')
    def insert_data(self,table,data):
        dCount = self.cur.execute("select TCNO from %s" % table)
        dDatas = self.cur.fetchmany(dCount)
        i=0
        while i <len(data):
            for j in dDatas:
                if data[i][0] in j[0]:
                    data.pop(i)
                    i-=1
                    break
            i+=1
        sqli = "insert into "+table+" (TCNO,InterfaceName,URL,Method,Introduce,Priorty,Flag,Parameter,`Expected Result`,TestResult,Comment)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        x=self.cur.executemany(sqli,data)
        logging.info(u'插入'+str(x)+u'条数据')
        self.cur.close()
        self.conn.commit()
        self.conn.close()
    def insert_all_data(self,table,data):
        """
        批量插入数据
        :param table:
        :param data:
        :return:
        """
        dCount = self.cur.execute("select TCNO from %s" % table)
        dDatas = self.cur.fetchmany(dCount)
        i=0
        while i <len(data):
            for j in dDatas:
                if data[i][0] in j[0]:
                    data.pop(i)
                    i-=1
                    break
            i+=1
        sqli = "insert into "+table+" (TCNO,description,sub,data,submode,Inquiry,substate,Flag,function,testmodename)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        x=self.cur.executemany(sqli,data)
        print x
        logging.info(u'插入'+str(x)+u'条数据')
        self.cur.close()
        self.conn.commit()
        self.conn.close()


    def get_data(self,table,cell=None):
        """
        获取数据
        :param table:
        :param cell:
        :return:
        """
        resultlist = []
        if cell==None:
            dCount=self.cur.execute("select * from %s"%table)
        else:
            dCount=self.cur.execute("select * from %s where interfaceId='%s' "%(table,cell))
        dDatas=self.cur.fetchmany(dCount)
        for i in dDatas:
            resultlist.append(list(i))
        return resultlist
    def update_data(self,table,data,interfaceid,TCNO):
        Sqlit=self.cur.execute("update %s set Parameter='%s' where interfaceId='%s' and TCNO=%d" %(table,data,interfaceid,TCNO))
        self.cur.close()
        self.conn.commit()
        self.conn.close()
# for i in MySql().get_data('vq_testcase','Login'):
#     print i
# MySql().get_data('VQ_login')
# print aa
# for i in aa:
#     for j in i:
#         print j
import CONFIG as CFG
import COMMON as cn
import os
dataPath=os.path.join(CFG.prjDir,'BaseCase','GJB','data','10')
b=cn.get_xls_sql('testData.xlsx',dataPath)
for i in b:
    print i



