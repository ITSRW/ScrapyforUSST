from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
import time,os,xlwt

class scrapyclass():
    options = Options()
    base_url = "https://yjsxt.webvpn2.usst.edu.cn/wsxk/jsp/T_PYGL_KWGL_WSXK_KKBJ.jsp"
    datalist = []

    def getCourseData(self,info,savepath):
         try:
            templist = []
            self.options = Options()
            self.options.add_argument("--headless")
            info.append('正在启动...')
            self.driver = webdriver.Chrome(options=self.options)
            self.driver.get(self.base_url)

            info.append('进行初始化，登录中...')
            WebDriverWait(self.driver,60).until(lambda x:x.find_element_by_id("username"))
            WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_id("password"))

            if self.driver.find_element_by_id('username').is_displayed():
                self.driver.find_element_by_id('username').send_keys('192560922')
                self.driver.find_element_by_id('password').send_keys('IVANLIN~|!y#!')
                self.driver.find_element_by_id('password').send_keys(Keys.ENTER)

            if self.driver.find_element_by_id('IDToken1').is_displayed():
                self.driver.find_element_by_id('IDToken1').send_keys('192560922')
                self.driver.find_element_by_id('IDToken2').send_keys('IVANLIN~|!y#!')
                self.driver.find_element_by_name('Login.Submit').click()
            if self.driver.find_element_by_id('KCDM').is_displayed():
                info.append('登陆成功！')
            for index in [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17]:#
                info.append('正在爬取'+str(index)+'号学院开课数据...')
                WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_id("YXDM"))
                WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_id("KCDM"))
                s=self.driver.find_element_by_id('YXDM')
                Select(s).select_by_index(index)
                s.click()
                self.driver.find_element_by_id('KCDM').clear()
                self.driver.find_element_by_id('KCDM').send_keys('%')
                time.sleep(2)

                self.driver.find_element_by_id('KCDM').send_keys(Keys.ENTER)
                WebDriverWait(self.driver, 60).until(lambda x: x.find_element_by_id("table_5"))

                info.append(str(index)+'号学院课程数据组爬取完毕，正在准备初步数据清洗...')
                array=self.driver.find_element_by_id('table_5').text.split('\n')#将各个学院的数据进行拆分

                info.append('清洗策略启动，正在初步清洗...')
                del array[0:2]#删去每个学院数据的表头
                if array[len(array)-1]==' ':#如果有，则删除每一行末尾的空格
                    del array[len(array)-1]
                point=len(array)-1
                while point>-1:
                    if(('专业课' in array[point])
                            or('跨选课' in array[point])
                            or('基础课' in array[point])
                            or('补修课' in array[point])
                            or('必修课' in array[point])):
                        del array[point]
                    elif ('周' in array[point] and '星期' in array[point]) \
                        and \
                        ('周' in array[point] and '星期' in array[point-1]):
                        array[point-1]+=";"+array[point]
                        del array[point]
                    point-=1

                for elements in array:
                    templist.append(elements)#合并至二维列表
                info.append('初步清洗完成！')
                time.sleep(2)#休眠等待
            self.driver.close()
            os.system("taskkill /f /im chromedriver.exe")
            os.system("taskkill /f /im chrome.exe")

            '''抓取结束，进入到数据处理阶段'''

            modboxhead=0
            box = []
            info.append('开始进行全体数据精加工！补全缺省值...')
            while modboxhead + 7 < len(templist):
                box.append(templist[modboxhead])
                cur=0
                for point in range(1,7):
                    if not(
                            (templist[modboxhead+point].strip().isdigit())
                           and
                            (len(templist[modboxhead+point].strip())==8)
                    ):  # 不是为8位数字
                        box.append(templist[modboxhead+point])
                        cur+=1
                    else:
                        for times in range(0,7-point):
                            box.append('缺省数据')
                        break

                modboxhead = modboxhead + cur+1  # 移动到下一个mod7周期
                self.datalist.append(box)
                box=[]#清空
            info.append('数据清洗完成！')
            info.append("正在存入指定位置...")
            self.toExcel(savepath,info)
            info.append("已成功存入"+savepath+"!")
         except:
             self.driver.close()
             os.system("taskkill /f /im chromedriver.exe")
             os.system("taskkill /f /im chrome.exe")
             info.append("爬取出错！")

        # 将查询结果写入到excel
    def toExcel(self,savepath,info):
        info.append('正在写入Excel...')
        workbook = xlwt.Workbook()
        table = ['课程代码', '课程详情', '学时', '任课教师', '开课学院', '开课校区', '时间地点']
        # 创建一个新的sheet
        sheet = workbook.add_sheet('最新学期开课信息爬取', cell_overwrite_ok=True)
        # 将表的字段名写入excel
        for column in range(0, len(['课程代码', '课程详情', '学时', '任课教师', '开课学院', '开课校区', '时间地点'])):
            sheet.write(0, column, table[column])
        for row in range(1, len(self.datalist)):
            for column in range(0, len(self.datalist[row])):
                sheet.write(row, column, self.datalist[row][column])
        workbook.save(savepath)
        info.append('写入Excel成功！正在打开...')
        os.startfile(str(savepath))

