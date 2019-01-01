import requests
from bs4 import BeautifulSoup
class GETpostinfo(object):
    def __init__(self,url):
        self.htmltext = requests.get(url)
    def getpostinfo(self):
        htmltext=self.htmltext.text
        classall=BeautifulSoup(htmltext,features='lxml')
        classinfo=classall.find_all('table',{"class":"gs_zp_table"})
        for info in classinfo:
            welfare=info.td.find_next(attrs={"id":"welfare_td"}).get_text() #公司福利
            welfare="".join(welfare.split())#去除获取内容中的空格段落
            print("公司福利：%s"%welfare)
        classinfo_1=classall.find_all('div',{"class":"fl"})
        for info_1 in classinfo_1:
            company_type = info_1.ul.find('li').get_text()
            company_total_people = info_1.ul.find('li').find_next('li').get_text()
            company_industry = info_1.ul.find('li').find_next('li').find_next('li').get_text()
            print("%s\t%s\t%s\n"%(company_type,company_total_people,company_industry))
    def getworkcontent(self):
        htmltext=self.htmltext.text
        classall=BeautifulSoup(htmltext,"lxml")
        classinfo=classall.find_all('div',{"class":"gsR_con_txt"})
        for info in classinfo:
            w_content =info.find_next("div",{"class":"gz_info_txt"})
            w_contenttext = w_content.p.get_text()
            w_contenttext="".join(w_contenttext.split())#去除获取内容中的空格段落
            print(w_contenttext)
