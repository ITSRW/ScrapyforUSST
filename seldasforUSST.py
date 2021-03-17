import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time,os,xlwt,copy

class scrapyclass():
    base_url = "http://yjsxt.usst.edu.cn/wsxk/jsp/T_PYGL_KWGL_WSXK_KKBJ.jsp"
    array='<table>'
    table=None
    templist=[]
    datalist=[]
    def getCourseData(self,info,savepath,term):
        info.append('初始化...')
        try:
            self.driver = webdriver.Ie(executable_path="C:\\Program Files\\Internet Explorer\\IEDriverServer.exe")
            self.driver.get(self.base_url)
            info.append('登录中...')
            time.sleep(1)
            if self.isexist('username'):
                self.driver.find_element_by_id('username').send_keys('192560922')
                self.driver.find_element_by_id('password').send_keys('IVANLIN~|!y#!')
                self.driver.find_element_by_id('password').send_keys(Keys.ENTER)

            elif self.isexist('IDToken1'):
                self.driver.find_element_by_id('IDToken1').send_keys('192560922')
                self.driver.find_element_by_id('IDToken2').send_keys('IVANLIN~|!y#!')
                self.driver.find_element_by_id('IDToken2').send_keys(Keys.ENTER)

            info.append('权限验证通过！')
            time.sleep(3)
            self.driver.find_element_by_id('XQDM').send_keys(term)
            for index in [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17]:#
                info.append('正在渗透注入！爬取'+str(index)+'号学院开课信息...')
                WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_id("YXDM"))
                WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_id("KCDM"))
                s=self.driver.find_element_by_id('YXDM')
                Select(s).select_by_index(index)
                s.click()
                self.driver.find_element_by_id('KCDM').clear()
                self.driver.find_element_by_id('KCDM').send_keys('%')
                self.driver.find_element_by_id('KCDM').send_keys(Keys.ENTER)
                time.sleep(5)
                self.array+=self.driver.find_element_by_id("table_5").get_attribute('innerHTML')
                info.append(str(index)+'号学院开课信息爬取成功！')
                time.sleep(1)#休眠等待
            '''抓取结束，进入到数据处理阶段'''
            self.array+= '</table>'
            self.table = pd.read_html(self.array)[0]
            pd.set_option('display.max_rows', None)
            pd.set_option('display.width', None)
            for row in range(0,len(self.table)):
                if ('课程' in self.table.loc[row][1]) and ('课程' in self.table.loc[row][2]):
                    continue
                for col in range(0,len(self.table.loc[row])):
                    self.templist.append(copy.deepcopy(self.table.loc[row][col]))
                self.datalist.append(copy.deepcopy(self.templist))
                self.templist.clear()
            self.toExcel(savepath, info)
            self.driver.close()
            os.system("taskkill /f /im IEDriverServer.exe")
            os.system("taskkill /f /im iexplore.exe")
        except:
            self.driver.close()
            info.append('爬取失败请重试！')
            os.system("taskkill /f /im IEDriverServer.exe")
            os.system("taskkill /f /im iexplore.exe")
 # 将查询结果写入到excel
    def toExcel(self,savepath,info):
        info.append('正在写入Excel...')
        workbook = xlwt.Workbook()
        table = ['课程类型','课程代码', '课程详情', '学时', '任课教师', '开课学院', '开课校区', '时间地点']
        # 创建一个新的sheet
        sheet = workbook.add_sheet('最新学期开课信息爬取', cell_overwrite_ok=True)
        # 将表的字段名写入excel
        for column in range(0, len(['课程类型','课程代码', '课程详情', '学时', '任课教师', '开课学院', '开课校区', '时间地点'])):
            sheet.write(0, column, table[column])
        for row in range(1, len(self.datalist)):
            for column in range(0, len(self.datalist[row])):
                sheet.write(row, column, self.datalist[row][column])
        workbook.save(savepath)
        info.append('写入Excel成功！正在打开...')
        os.startfile(str(savepath))

    def isexist(self,element):
        try:
            flag=self.driver.find_element_by_id(element)
            return True
        except:
            return False

'''
    该项目目前存在的问题：
    1.运行爬虫核心代码的线程无法在执行完代码后自动销毁，必须通过Terminate按钮终止才能停下
    2.按下Terminate后会继续打开Excel（已解决）
    3.无法灵活选择需要爬取的学院
    4.在多个验证机制突然出现时无法绕开（已解决）
'''