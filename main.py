from runspide import Spider
from zlzp_search import ZLZPSearch
import schedule
import time
def rungxzr_yw():
    for i in range(10):
        run = Spider("运维", i+1)
        exitcote = run.rungxrc()
        print(exitcote)
def rungxzr_java():
    for i in range(10):
        run = Spider("JAVA", i+1)
        exitcote = run.rungxrc()
        print(exitcote)
def runzlzp():
    zlzp = ZLZPSearch()
    zlzp.getinfo()

if __name__=="__main__":
    # rungxzr_yw()
    # runzlzp()
    # rungxzr_java()
    schedule.every().day.at("18:30").do(rungxzr_yw)
    schedule.every().day.at("18:00").do(rungxzr_java)
    schedule.every().day.at("18:10").do(runzlzp)
    while True:
        schedule.run_pending()
        time.sleep(1)
