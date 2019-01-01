import searchjob
import getpostinfo
import zlzp_search
import time
import threading
def gxrc():
    for num in range(1):
        jobresult=searchjob.Serach(num+1)
        post_urllist = jobresult.selectinfo_gxcr()
        for url in post_urllist:
            postdesc=getpostinfo.GETpostinfo(url)
            postdesc.getpostinfo()
            postdesc.getworkcontent()
def zlzp():
    zl = zlzp_search.ZLZPSearch()
    zl.getinfo()

if __name__=="__main__":
    threads=[]
    th1=threading.Thread(target=gxrc)
    threads.append(th1)
    th2=threading.Thread(target=zlzp)
    threads.append(th2)
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

