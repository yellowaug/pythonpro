from pymysql import connect
# from hjctool import check_net
class Sql_manager(object):
    def __init__(self):
        # net_code=check_net()
        # if net_code==1:
        host = "192.168.15.251"
        user = "root"
        pw = "zzq"
        # sql_com="select * from ip_mac"
        db="ipdata"
        self.sql=connect(host,user,pw,db)
        self.cur=self.sql.cursor()
        # cur.execute(sql_com)
        # table_info=cur.fetchall()
        print("连接成功。")
        # elif net_code==0:
        print("连接失败，请检查网络")
    def omp_sql(self,table_name="account_list"):
        #coum_name，value_name 两个变量使用数组或者列表的形式进行填充
        # sql_com="use %s"%db_name
        # self.cur.execute(sql_com)
        sql_com="select * from %s"%table_name
        self.cur.execute(sql_com)
        self.info =self.cur.fetchall()
        sql_com="desc %s"%table_name
        self.cur.execute(sql_com)
        self.info_desc=self.cur.fetchall()
        self.cur.close()
    def ins_sql(self,v_device=None,v_ip=None,v_acc=None,v_pass=None,v_note=None): #插入account_list表
        sql_com1="insert into account_list(device,ip_addr,accuont,password,note) VALUES (%s,%s,%s,%s,%s)"
        values=(v_device,v_ip,v_acc,v_pass,v_note)
        self.cur.execute(sql_com1,values)
        sql_com1="select * from account_list"
        self.cur.execute(sql_com1)
        self.sql.commit()
        self.info_seclect = self.cur.fetchall()
        self.cur.close()
    def ins_computer_info_sql(self,sys_name=None,cpu_info=None,board_info=None,disk_info=None,mem_info=None,grap_info=None,note=None,upload_time=None):
    # def ins_computer_info_sql(self, sys_name=None, cpu_info=None,): #测试用的方法
        sql_com1="insert into computer_info(computer_name,cpu_info,board_info,disk_info,mem_info,grap_card,note,upload_time) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        # sql_com1 = "insert into computer_info(computer_name,cpu_info) VALUES (%s,%s)" #测试用的方法
        values = (sys_name, cpu_info, board_info, disk_info, mem_info, grap_info, note,upload_time)
        # values = (sys_name, cpu_info)
        # sql_com2="select * from computer_info"
        self.sql.commit()
        self.cur.execute(sql_com1, values)
        # self.cur.execute(sql_com2)
        self.sql.commit()
        # self.info_seclect = self.cur.fetchall()
        self.cur.close()
    def update_sql(self,cou_name=None,new_values=None,cou_limit=None,limit_key=None):
        #定义修改数据的功能，以及变量
        #SQL语句用的参数用.format拼接，SQL语句的值用%s拼接，这样才不会报错
        #功能已经完成
        try:
            sql_com1="update {t_name} set {coume_name}=%s where {coume_limit}=%s"\
                .format(t_name="account_list",coume_name=cou_name,coume_limit=cou_limit)
            var=(new_values,limit_key)
            self.cur.execute(sql_com1,var)
            self.sql.commit()
        except Exception as e:
            self.sql.rollback()
            print(e)
        self.cur.close()

