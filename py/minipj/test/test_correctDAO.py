from zsob.zsobDBManager import ZsobDBM


class test_correctDAO:
    def __init__(self):
        # self.count_all()
        # self.pagein = 3
        pass

    def reg(self,test):
        try:
            con, cur = ZsobDBM.op("MSAIuser/2048@195.168.9.238:1521/xe")
            sql = "INSERT INTO test_correct_mpj values(%s,%s,%s,%s,%s,%s)" % (test.c_no,test.q1,test.q2,test.q3,test.q4,test.q5)
            
            cur.execute(sql)
            con.commit()
            return "성공"

        except Exception as e :
            print(e)
            return "실패"
        
        finally:
            ZsobDBM.ed(con,cur)