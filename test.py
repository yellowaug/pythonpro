import requests
import json
import jsonpath
class TEXT(object):
    def __init__(self):
        zlurl="https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=785&workExperience=-1&education=-1&" \
              "companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BF%90%E7%BB%B4&kt=3&_v=0.36566866" \
              "&x-zp-page-request-id=d466571403cb46fdaf13754944b7cbc5-1546252426460-171808"
        self.html_zl=requests.get(zlurl)
    def getinfo(self):
        self.html_zl.encoding='utf8'
        htmltext_zlzp=self.html_zl.text
        zlzp_json=json.loads(htmltext_zlzp)
        companyname=jsonpath.jsonpath(zlzp_json,"$..company[name]")
        companytype=jsonpath.jsonpath(zlzp_json,"$..company[type][name]")
        companysize=jsonpath.jsonpath(zlzp_json,"$..company[size][name]")
        jobname=jsonpath.jsonpath(zlzp_json,"$..jobName")
        postdescurl=jsonpath.jsonpath(zlzp_json,"$..positionURL")
        jobcity=jsonpath.jsonpath(zlzp_json,"$..city[display]")
        update=jsonpath.jsonpath(zlzp_json,"$..updateDate")
        salary=jsonpath.jsonpath(zlzp_json,"$..salary")
        welfare=jsonpath.jsonpath(zlzp_json,"$..welfare")
        workexp=jsonpath.jsonpath(zlzp_json,"$..workingExp[name]")


        print("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n"%(companyname,companytype,companysize,jobname,postdescurl,jobcity,update,salary,welfare,workexp))


a =TEXT()
a.getinfo()