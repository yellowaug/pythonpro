from getpostinfo import GETpostinfo
from zlzp_search import ZLZPSearch
from sqlomp import SQLOMP
import time
class Spider(GETpostinfo):
    def rungxrc(self):
        n=0
        sql=SQLOMP()
        self.selectinfo_gxcr()
        taday=time.strftime("%y-%m-%d",time.localtime())
        # for j in range(len(self.postion_url)):
        #     self.getpostinfo(self.postion_url[j])
        # print(len(self.postnamelist))
        # print(len(self.companynamelist))
        '''
        self.postion_url=[] #职位详情描述url
        self.postnamelist=[] #职位名称列表
        self.companynamelist=[] #公司名称列表
        self.wagemoneylist=[] #工资列表
        self.worklocatiolist=[] #工作地点列表
        self.pushdatelist=[] #更新日期列表
        self.companyinfolist=[] #公司信息列表url
        self.postwelfarelist=[] #公司福利待遇
        self.companytypelist=[] #公司类型
        self.companytotalpeoplelist=[] #公司总人数
        self.companyindustrylist=[] #公司介绍
        self.workconnetlist = [] #工作内容
        '''
        for i in range(len(self.postnamelist)):
            self.getpostinfo(self.postion_url[i])
            self.getworkcontent()
            # print("%s\t%s\t%s\n%s\t%s\t%s\t%s"%(self.postnamelist[i],self.companynamelist[i],self.postion_url[i],
            #                             self.wagemoneylist[i],self.worklocatiolist[i],self.pushdatelist[i],self.companyinfolist[i]))
            # print("%s\t%s\t%s\t%s"%(self.postwelfarelist,self.companytypelist,self.companytotalpeoplelist,self.workconnetlist))
            # print("%s\t%s\n"%(self.companyindustrylist,self.workconnetlist))
            if(self.pushdatelist[i]=="20"+taday):
            #     return 10
            # else:
                insdata={"companyname":self.companynamelist[i],
                             "companytype":self.companytypelist[0],
                             "companydescurl":self.companyinfolist[i],
                             "companyindustry":self.companyindustrylist[0],
                             "companytotalpeople":self.companytotalpeoplelist[0],
                             "postioname":self.postnamelist[i],
                             "postdesc":self.workconnetlist[0],
                             "postionurl":self.postion_url[i],
                             "walfare":self.postwelfarelist[0],
                             "wagemoney":self.wagemoneylist[i],
                             "worklocation":self.worklocatiolist[i],
                             "pushdate":self.pushdatelist[i]}
                sql.instosql("gxrcdb","yw_jobinfo",**insdata)
            else:
                n=n+1
                if(n==3):
                    return 10
                else:
                    pass
        # print(self.postwelfarelist)
    # def runzlzp(self):
    #     zlzp=ZLZPSearch()
    #     zlzp.getinfo()


# if __name__=="__main__":
    # for i in range(10):
    #     run = Spider("运维", i+1)
    #     exitcote = run.rungxrc()
    #     print(exitcote)
    # for i in range(10):
    #     run1=Spider("JAVA",i+1)
    #     print(run1.rungxrc())
        # run.runzlzp()
    # zlzp = ZLZPSearch()
    # zlzp.getinfo()
