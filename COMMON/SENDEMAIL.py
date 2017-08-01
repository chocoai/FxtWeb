# coding:utf-8
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import CONFIG as readConfig
import logging
import string

class MyEmail(object):
    def __init__(self,path=''):
        self.rcg = readConfig.ReadConfig(path)

    def  sendEmail(self,attfile) :
        """
        send Email
        :param attfile:Attachment
        :return:
        """

        mailDict=self.rcg.getEmail()
        mailTo=mailDict['mailto']
        mailFrom=mailDict['mailfrom']
        mailHost=mailDict['mailhost']
        mailUser=mailDict['mailuser']
        mailPassword=mailDict['mailpassword']
        mailPostFix=mailDict['mailpostfix']
        mailText=mailDict['mailtext']
        mailTitle=mailDict['mailtitle']
        msg=MIMEMultipart()

        part=MIMEText(mailText,_subtype='plain',_charset='gb2312')
        msg.attach(part)

        # attachment
        att=MIMEText(open(attfile,'rb').read(),'base64','gb2312')
        att['Content-Type']='application/octet-stream'
        att['Content-Disposition']='attachment;filename="report.rar"'
        msg.attach(att)

        fmuser=string.splitfields(mailTo,',')
        #msg['to']=string.splitfields(mailTo,",")
        #msg['to']=mailTo

        msg['from']=mailFrom
        msg['subject']=mailTitle
        #print type(msg['to'])

        server = smtplib.SMTP()
        server.connect(mailHost)
        server.login(mailUser, mailPassword)
        try:
            server.sendmail(msg['from'],fmuser,msg.as_string())#会多个收件人时会报告列表错误
            #server.sendmail(msg['from'],msg['to'],mailText)
            logging.info( u'邮件发送成功')
        except Exception,e:
            if '535' in  str(e):
                logging.error(str(e))
                logging.info(u'请填写邮件地址！')
            print 'email fail!'
            raise e
        finally:
            server.quit()



