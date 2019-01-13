# import threading
# import time
import sqlomp
import requests
import json
import jsonpath
class ZLZPSearch(object):
    def __init__(self):
        zlurl="https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=785&workExperience=-1&education=-1&" \
              "companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BF%90%E7%BB%B4&kt=3&_v=0.36566866" \
              "&x-zp-page-request-id=d466571403cb46fdaf13754944b7cbc5-1546252426460-171808"
        self.html_zl=requests.get(zlurl)
    def getinfo(self):
        self.html_zl.encoding='utf8'
        htmltext_zlzp=self.html_zl.text
        zlzp_json=json.loads(htmltext_zlzp)
        companyname=jsonpath.jsonpath(zlzp_json,"$..company[name]") #公司名称
        companytype=jsonpath.jsonpath(zlzp_json,"$..company[type][name]") #公司性质
        companysize=jsonpath.jsonpath(zlzp_json,"$..company[size][name]") #公司规模
        jobname=jsonpath.jsonpath(zlzp_json,"$..jobName") #岗位名称
        postdescurl=jsonpath.jsonpath(zlzp_json,"$..positionURL") #岗位url
        jobcity=jsonpath.jsonpath(zlzp_json,"$..city[display]") #工作所在地
        update=jsonpath.jsonpath(zlzp_json,"$..updateDate") #发布时间
        salary=jsonpath.jsonpath(zlzp_json,"$..salary") #工资
        welfare=jsonpath.jsonpath(zlzp_json,"$..welfare") #公司福利
        workexp=jsonpath.jsonpath(zlzp_json,"$..workingExp[name]") #工作年限要求
        sql=sqlomp.SQLOMP()
        # insdata={"companyname":companyname[0],"companytype":companytype[0],
        #          "companysize":companysize[0],"postioname":jobname[0],
        #          "postdescurl":postdescurl[0],"workexp":workexp[0],
        #          "worklocation":jobcity[0],"wagemoney":salary[0],
        #          }
        # sql.instosql("zlzpdb",**insdata)
        # print(len(companyname))

        for i in range(90):
            print("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n"%(companyname[i],companytype[i],companysize[i],jobname[i],postdescurl[i],
                                                              jobcity[i],update[i],salary[i],welfare[i],workexp[i]))
            insdata={"companyname":companyname[i],"companytype":companytype[i],
                 "companysize":companysize[i],"postioname":jobname[i],
                 "postdescurl":postdescurl[i],"workexp":workexp[i],
                 "worklocation":jobcity[i],"wagemoney":salary[i],
                 "updates":update[i],"walfare":str(welfare[i])}
            sql.instosql("zlzpdb","yw_zljobinfo",**insdata)
        # print("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n"%(companyname,companytype,companysize,jobname,postdescurl,jobcity,update,salary,welfare,workexp))

# t1=time.time()
# a =ZLZPSearch()
# a.getinfo()
# # t=threading.Thread(target=a.getinfo)
# # t.start()
# # print(threading.activeCount())
# t2=time.time()
# print(t2-t1)

