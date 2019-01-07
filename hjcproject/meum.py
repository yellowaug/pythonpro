import os
import win32api
class MEUN(object):
    def __init__(self):
        print("="*50)
        print("1:测试项目1  ")
        print("2:测试项目2  ")
        print("3:测试项目3  ")
        print("4:测试项目4  ")
        print("5:测试项目5  ")
        print("0:退出程序")
    def change(self):
        selectchar=input("请输入项目编号（按回车确定）：\n")

        if(selectchar=="1"and len(selectchar)==1):
            print("111")
        elif(selectchar=="2"and  len(selectchar)==1):
            print("222")
        else:
            print("请输入正确的项目编号")
        os.system("pause")
        os.system("cls")
        re=MEUN()
        re.change()
        win32api.FindFiles()
a =MEUN()
a.change()