import requests
from bs4 import BeautifulSoup

class Serach(object):
    def __init__(self):
        url="http://s.gxrc.com/sJob?schType=1&workProperty=&keyword=运维"
        self.html=requests.get(url)

    def selectinfo(self):
        htmltxt=self.html.text
        # print(htmltxt)
        classall=BeautifulSoup(htmltxt,features='lxml')
        classtext = classall.find_all('div',{"class":"rlOne"})
        for text in classtext:
            # print(text.get_text())
            url=text.h3.a['href']
            postname=text.h3.a.get_text()
            companynames=text.find_all('li',{"class":"w2"}) #获取公司名称
            wagemoneys=text.find_all('li',{"class":"w3"}) #获取工资信息
            worklocatios=text.find_all('li',{"class":"w4"}) #获取工作地点
            pushdates=text.find_all('li',{"class":"w5"}) #获取发布日期
            # print("%s\t%s\n"%(url,postname))
            for money in wagemoneys:
                w_money=money.get_text()
            for location in worklocatios:
                w_location=location.get_text()
            for date in pushdates:
                p_date=date.get_text()
            for companyname in companynames:
                c_name=companyname.get_text()
                companyinfo=companyname.a['href']
                # print(companyinfo)
                print("%s\t%s\n%s\t%s\n%s\t%s\t%s\n"%(c_name,companyinfo,postname,url,w_money,w_location,p_date))

                # print(t.get_text())
        # companyinfo=classall.find_all('li',{"class":"w2"})
        # for info in companyinfo:
        #     url = classall.f
        #     print(url[0])
        #     print(info.get_text())



a=Serach()
a.selectinfo()