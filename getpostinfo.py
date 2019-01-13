import requests
from bs4 import BeautifulSoup
from searchjob import Serach
class GETpostinfo(Serach):
    # def __init__(self,url):
    def getpostinfo(self,url):
        self.htmltext = requests.get(url)
        htmltext=self.htmltext.text
        # postdesclist=[]
        self.postwelfarelist=[] #公司福利待遇
        self.companytypelist=[] #公司类型
        self.companytotalpeoplelist=[] #公司总人数
        self.companyindustrylist=[] #公司介绍
        classall=BeautifulSoup(htmltext,features='lxml')
        classinfo=classall.find_all('table',{"class":"gs_zp_table"})
        for info in classinfo:
            welfare=info.td.find_next(attrs={"id":"welfare_td"}).get_text() #公司福利
            welfare="".join(welfare.split())#去除获取内容中的空格段落
            self.postwelfarelist.append(welfare)
            # print("公司福利：%s"%welfare)
        classinfo_1=classall.find_all('div',{"class":"fl"})
        for info_1 in classinfo_1:
            company_type = info_1.ul.find('li').get_text()
            self.companytypelist.append(company_type)
            company_total_people = info_1.ul.find('li').find_next('li').get_text()
            self.companytotalpeoplelist.append(company_total_people)
            company_industry = info_1.ul.find('li').find_next('li').find_next('li').get_text()
            self.companyindustrylist.append(company_industry)
            # print("%s\t%s\t%s\n"%(company_type,company_total_people,company_industry))
        # postdesclist.append(postwelfarelist)
        # postdesclist.append(companytypelist)
        # postdesclist.append(companytotalpeoplelist)
        # postdesclist.append(companyindustrylist)
        # return postdesclist
    def getworkcontent(self):
        self.workconnetlist = [] #工作内容
        htmltext=self.htmltext.text
        classall=BeautifulSoup(htmltext,"lxml")
        classinfo=classall.find_all('div',{"class":"gsR_con_txt"})
        for info in classinfo:
            w_content =info.find_next("div",{"class":"gz_info_txt"})
            w_contenttext = w_content.p.get_text()
            w_contenttext="".join(w_contenttext.split())#去除获取内容中的空格段落
            self.workconnetlist.append(w_contenttext)
            # print(w_contenttext)
        # return workconnetlist

