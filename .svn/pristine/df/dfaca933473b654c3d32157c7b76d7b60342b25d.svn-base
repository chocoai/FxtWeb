# coding:utf-8
from selenium import webdriver
from selenium.webdriver import Remote
import os
import CONFIG as FIG
import COMMON as CM
Distributed=FIG.ReadConfig().getConfigValue('Distributed')
Browser=FIG.ReadConfig().getConfigValue('Browser')

class MyDriver(object):
    @classmethod
    def getDriver(self):
        """启动驱动"""
        if Distributed == 'ON':
            driver = MyDriver.get_gridNode()
        else:
            driver = MyDriver.get_driver(Browser)
        driver.maximize_window()
        return driver
    @classmethod
    def get_driver(self,browsers='IE'):
        """普通driver
        get selenium driver
        :param browsers:
        :return:
        """
        try:
            if browsers == 'IE':
                #prefs = {"download.default_directory": "D:\driver"}
                driver = webdriver.Ie()
            elif browsers == 'Chrome':
                downloadpath = FIG.downloadDir
                chromeOptions = webdriver.ChromeOptions()
                prefs = {"download.default_directory": downloadpath}
                chromeOptions.add_experimental_option("prefs", prefs)
                chromeOptions.add_argument('--always-authorize-plugins=true')
                chromeOptions.add_argument('test-type')
                driver = webdriver.Chrome(chrome_options=chromeOptions)

            elif browsers == 'Firefox':

                driver = webdriver.Firefox()
            elif browsers=='PhantomJS':
                driver=webdriver.PhantomJS()
            else:
                #print U'请输入IE，Chrome,FireFox'
                return
        except Exception as e:
            raise e

        return driver
    @classmethod
    def get_gridNode(self):
        """
        获取机器或节点
        :return:
        """
        filepath = os.getcwd()
        fig = FIG.ReadConfig(filepath)
        Host = fig.getConfigValue('Host')
        driver = CM.get_girdDriver(Host)
        return driver
    @classmethod
    def get_gridDriver(self, host, browser):
        """
        通过代理IP，浏览器驱动来运行
        :param host: IP
        :param browser: 浏览器
        :return:
        """
        try:

            dr = Remote(command_executor=host,
                        desired_capabilities={'platform': 'ANY',
                                              'browserName': browser,
                                              'version': '',
                                              'javascriptEnabled': True
                                              })
            return dr
        except Exception:
            raise (u'请启动selenium Gird 服务')
            # drivers.append(dr)
            # return drivers

