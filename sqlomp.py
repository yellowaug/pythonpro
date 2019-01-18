from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

class SQLOMP(object):
    def instosql(self,db,table,**kwargs):
        engine = create_engine("mysql+pymysql://root:zzq@192.168.15.251/{dbname}?charset=utf8".format(dbname=db), encoding='utf-8', echo=True)
        metadata = MetaData(engine)
        con_table=Table(table,metadata,autoload=True)
        ins = con_table.insert()
        conn=engine.connect()
        # result=conn.execute(ins,[{"companyname":"test1",
        #                           "companytype":"test2",
        #                           "companysize":"test3",
        #                           "postioname":"test4"}])
        conn.execute(ins,kwargs)
    # def readtosql(self):
