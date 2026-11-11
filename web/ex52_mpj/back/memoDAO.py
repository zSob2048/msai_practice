from datetime import datetime
from zsob.zDBM import zDB


class memoDAO:
    def __init__(self):
        self.inPageN = 5
        
    def main_reg(self, cont):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "INSERT INTO MAINMEMO1203 values(memo1203_seq.nextval,  '%s', 0, sysdate)" %(cont)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allseller_num += 1
                return {"result" : " 등록 성공"}
            return {"result" : " 등록 실패"}

        except:
            return {"result" : " 등록 실패"}
        finally:
            zDB.ed(con,cur)

    def reply_reg(self, cont, m_no):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "INSERT INTO REPLYMEMO1203 values(memo1203_seq.nextval,  %s, '%s', sysdate)" %(m_no, cont)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allseller_num += 1
                return {"result" : " 등록 성공"}
            return {"result" : " 등록 실패"}

        except:
            return {"result" : " 등록 실패"}
        finally:
            zDB.ed(con,cur)

    def get(self,pg,searchkey,dateI, dateF):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            searchkey = "%" + searchkey + "%"
            if dateI == "":
                dateI = "2000-01-01"
            if dateF == "":
                dateF = datetime.strftime(datetime.today(),"%Y-%m-%d")

            sql = sql = "SELECT * FROM (" \
            "SELECT rownum AS rn , m_no, m_content, m_correct, m_uplodedate FROM(" \
            "SELECT * FROM mainmemo1203 WHERE (m_content LIKE '%s') AND " \
            "(m_uplodedate between to_date('%s','YYYY-MM-DD') and to_date('%s','YYYY-MM-DD')) " \
            "ORDER BY m_uplodedate) )" \
            "WHERE rn>%d AND rn<=%d" % ( searchkey, dateI, dateF ,self.inPageN * (int(pg) - 1) , self.inPageN * int(pg))
            cur.execute(sql)

            memos = []
            for _, no, cont, corr, uday in cur:
                uday = datetime.strftime(uday, "%Y-%m-%d")
                memos.append({"no":no, "cont":cont,"uday":uday, "corr":corr})
            return memos

        except Exception as e:
            return {"result" : str(e) }
        finally:
            zDB.ed(con,cur)

    def numS(self,no):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "SELECT * FROM mainmemo1203 WHERE m_no = %s" %no
            cur.execute(sql)

            for no, cont, corr, uday in cur:
                uday = datetime.strftime(uday, "%Y-%m-%d")
                mainmemo = {"no":no, "contant":cont,"uploadday":uday, "corr":corr}
            

            sql = "SELECT * FROM replymemo1203 WHERE r_m_no = %s" %no
            cur.execute(sql)

            replys = []
            for no, _, cont, uday in cur:
                uday = datetime.strftime(uday, "%Y-%m-%d")
                replys.append({"no":no, "contant":cont,"uploadday":uday})
            return {"mainM" : mainmemo, "replM" : replys}

        except Exception as e:
            return {"result" : str(e) }
        finally:
            zDB.ed(con,cur)

    def update(self, no, cont):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "UPDATE mainmemo1203 SET m_content = '%s' , m_correct = 1 WHERE m_no = %s" %(cont,no)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return {"result" : " 수정 성공"}
            return {"result" : " 수정 실패"}

        except :
            return {"result" : " 수정 실패"}
        finally:
            zDB.ed(con,cur)

    def deleteM(self, no):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "DELETE FROM mainmemo1203 WHERE m_no = %s" % no
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allseller_num -= 1
                return {"result" : " 삭제 성공"}
            return {"result" : " 삭제 실패"}

        except :
            return {"result" : " 삭제 실패"}
        finally:
            zDB.ed(con,cur)
    
    def deleteR(self, no):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "DELETE FROM replymemo1203 WHERE r_no = %s" % no
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allseller_num -= 1
                return {"result" : " 삭제 성공"}
            return {"result" : " 삭제 실패"}

        except :
            return {"result" : " 삭제 실패"}
        finally:
            zDB.ed(con,cur)