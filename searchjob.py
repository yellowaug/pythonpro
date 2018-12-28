import requests
import lxml
from bs4 import BeautifulSoup
import re
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
            print(text.get_text())



a=Serach()
a.selectinfo()