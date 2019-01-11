from getpostinfo import GETpostinfo
class Spider(GETpostinfo):
    def rungxrc(self):
        posttotallist = []
        p_infolist =self.selectinfo_gxcr()
        # print(p_infolist)
        # print(len(p_infolist))

        # for i in range(len(p_infolist)):
        #     postinfo=p_infolist[i]
            # print(postinfo)
            # if(i==0):
            #     for posturl in postinfo:
            #         postlist = GETpostinfo.getpostinfo(self, posturl)
            #         workcontlist = GETpostinfo.getworkcontent(self)
            #         print(postlist)
            #         print(workcontlist)
            #     print(p_infolist[i])
            # for j in range(len(p_infolist[i])):
            #     print(p_infolist[i][j])
        for posturl in p_infolist[0]:
            # print(posturl)
            postlist = GETpostinfo.getpostinfo(self,posturl)
            workcontlist=GETpostinfo.getworkcontent(self)
            # posttotallist.append(postlist)
            # posttotallist.append(workcontlist)
            # print(postlist)
            # print(workcontlist)
            # print(len(postlist))
        print(p_infolist)
        print(posttotallist)
if __name__=="__main__":
    run=Spider(1)
    run.rungxrc()