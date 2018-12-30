import requests
from bs4 import BeautifulSoup
class GETpostinfo(object):
    def __init__(self):
        url="http://www.gxrc.com/WebPage/JobDetail.aspx?EnterpriseID=1551525&PositionId=c42f9f49-1003-4c16-8845-a3054426f55a"
        self.htmltext = requests.get(url)
    def getpostinfo(self):
        htmltext=self.htmltext.text
        classall=BeautifulSoup(htmltext,features='lxml')
        classinfo=classall.find_all('table',{"class":"gs_zp_table"})
        # for info1 in classinfo:
        #     infolist=info1.find_all('td')
        #     for i_text in infolist:
        #         print(i_text.get_text())
        #     for info
        for info in classinfo:
            welfare=info.td.find_next(attrs={"id":"welfare_td"}).get_text() #公司福利
            print("公司福利：%s"%welfare)
        classinfo_1=classall.find_all('div',{"class":"fl"})
        for info_1 in classinfo_1:
            company_type = info_1.ul.find('li').get_text()
            company_total_people = info_1.ul.find('li').find_next('li').get_text()
            compant_industry = info_1.ul.find('li').find_next('li').find_next('li').get_text()
            print("%s\t%s\t%s\n"%(company_type,company_total_people,compant_industry))
    def getworkcontent(self):
        htmltext=self.htmltext.text
        classall=BeautifulSoup(htmltext,"lxml")
        classinfo=classall.find_all('div',{"class":"gsR_con_txt"})
        for info in classinfo:
            w_content =info.find_next("div",{"class":"gz_info_txt"})
            print(w_content.p.get_text())
a =GETpostinfo()
a.getpostinfo()
a.getworkcontent()