import requests
from bs4 import BeautifulSoup

class Serach(object):
    def __init__(self,keyword,page):
        url="http://s.gxrc.com/sJob?schType=1&workProperty=&keyword={postkeyword}&page={num}".format(postkeyword=keyword,num=page)
        # zlurl="https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=785&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BF%90%E7%BB%B4&kt=3&_v=0.36566866&x-zp-page-request-id=d466571403cb46fdaf13754944b7cbc5-1546252426460-171808"
        self.html=requests.get(url)

        # self.html_zl=requests.get(zlurl)
    def selectinfo_gxcr(self):
        # postinfolist = []
        self.postion_url=[] #职位详情描述url
        self.postnamelist=[] #职位名称列表
        self.companynamelist=[] #公司名称列表
        self.wagemoneylist=[] #工资列表
        self.worklocatiolist=[] #工作地点列表
        self.pushdatelist=[] #更新日期列表
        self.companyinfolist=[] #公司信息列表url
        htmltxt=self.html.text
        # print(htmltxt)
        classall=BeautifulSoup(htmltxt,features='lxml')
        classtext = classall.find_all('div',{"class":"rlOne"})
        for text in classtext:
            # print(text.get_text())
            url=text.h3.a['href']
            self.postion_url.append(url)
            postname=text.h3.a.get_text()
            self.postnamelist.append(postname)
            companynames=text.find_all('li',{"class":"w2"}) #获取公司名称
            wagemoneys=text.find_all('li',{"class":"w3"}) #获取工资信息
            worklocatios=text.find_all('li',{"class":"w4"}) #获取工作地点
            pushdates=text.find_all('li',{"class":"w5"}) #获取发布日期
            # print("%s\t%s\n"%(url,postname))
            for money in wagemoneys:
                w_money=money.get_text()
                self.wagemoneylist.append(w_money)
            for location in worklocatios:
                w_location=location.get_text()
                self.worklocatiolist.append(w_location)
            for date in pushdates:
                p_date=date.get_text()
                self.pushdatelist.append(p_date)
            for companyname in companynames:
                c_name=companyname.get_text()
                self.companynamelist.append(c_name)
                companyinfo=companyname.a['href']
                self.companyinfolist.append(companyinfo)
                # print(companyinfo)
                # ins_data={"companyname":c_name,
                #           "wagemoney":w_money,
                #           "worklocation":w_location,
                #           "pushdate":p_date}
                # SQLOMP.instosql(self,"gxrcdb","jobinfo",**ins_data)
                # print("%s\t%s\n%s\t%s\n%s\t%s\t%s\n"%(c_name,companyinfo,postname,url,w_money,w_location,p_date))
        # postinfolist.append(postion_url)
        # postinfolist.append(postnamelist)
        # postinfolist.append(companynamelist)
        # postinfolist.append(companyinfolist)
        # postinfolist.append(wagemoneylist)
        # postinfolist.append(worklocatiolist)
        # postinfolist.append(pushdatelist)
        # return postinfolist
    # def selectinfo_zlzp(self):
    #     self.html_zl.encoding='utf8'
    #     htmltext_zlzp=self.html_zl.text
    #     zlzp_json=json.loads(htmltext_zlzp)
    #     a=jsonpath.jsonpath(zlzp_json,"$..code")
    #     print(a)
# a=Serach(1)
# c=a.selectinfo_gxcr()
# for d in c[2]:
#     print(d)
