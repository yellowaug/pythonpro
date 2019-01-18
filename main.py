from runspide import Spider
from zlzp_search import ZLZPSearch
import schedule
import time
def runspide():
    for i in range(10):
        run = Spider("运维", i+1)
        exitcote = run.rungxrc()
        print(exitcote)
    for i in range(10):
        run = Spider("JAVA", i + 1)
        exitcote = run.rungxrc()
        print(exitcote)
    zlzp = ZLZPSearch()
    zlzp.getinfo()
# def rungxzr_java():
#     for i in range(10):
#         run = Spider("JAVA", i+1)
#         exitcote = run.rungxrc()
#         print(exitcote)
# def runzlzp():
#     zlzp = ZLZPSearch()
#     zlzp.getinfo()

if __name__=="__main__":
    # runspide()
    schedule.every().day.at("18:30").do(runspide)
    while True:
        schedule.run_pending()
        time.sleep(1)
