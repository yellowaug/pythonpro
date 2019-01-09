import os
class STARTUP(object):
    def __init__(self):
        path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
        os.chdir(path)

    def generatefile(self,remotohost,username,password,*shellconnect):
        cmddshell=["echo off\n",r"net use \\{host} {pwd} /user:{user}".format(host=remotohost,pwd=password,user=username),"\n","pause\n"]
        file=open("test.bat","w+",encoding="utf-8")
        print(os.getcwd()+file.name)
        file.writelines(cmddshell)
        file.seek(0,2)
        file.writelines(shellconnect)
        # for shell in shellconnect:
        #     file.seek(0,2)
        #     file.write(shell)
        file.flush()
        file.close()


a = STARTUP()
host="192.168.13.167"
user="02342045"
passw="1"
shell=["net use \\\%s\project\n"%host,"net use \\\%s\project\n"%host,"net use \\\%s\project\n"%host]
a.generatefile(host,user,passw,*shell)

