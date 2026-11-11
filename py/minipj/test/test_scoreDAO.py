from zsob.zsobDBManager import ZsobDBM


class test_scoreDAO:
    def __init__(self):
        # self.count_all()
        # self.pagein = 3
        pass

    def reg(self,score):
        try:
            con, cur = ZsobDBM.op("MSAIuser/2048@195.168.9.238:1521/xe")
            
            sql = "SELECT * FROM test_correct_mpj WHERE c_no = %s" % score.t_c_no
            cur.execute(sql)
            for result in cur:
                if score.q1 == str(result[1]) :
                    score._score += 20
                if score.q2 == str(result[2]) :
                    score._score += 20
                if score.q3 == str(result[3]) :
                    score._score += 20
                if score.q4 == str(result[4]) :
                    score._score += 20
                if score.q5 == str(result[5]) :
                    score._score += 20

            
            print(score)
            

            sql = "INSERT INTO test_score_mpj values(%s,%s,%s,%s,%s,%s,%s,%s)" % (score.t_c_no,score.q1,score.q2,score.q3,score.q4,score.q5,score.t_s_no,score._score)
            
            cur.execute(sql)
            con.commit()
            return "성공"            


        except Exception as e :
            print(e)
            return "실패"
        
        finally:
            ZsobDBM.ed(con,cur)