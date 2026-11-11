from zsob.zsobDBManager import ZsobDBM


class studentDAO:
    def __init__(self):
        pass

    def reg(self,student):
        try:
            con, cur = ZsobDBM.op("MSAIuser/2048@195.168.9.238:1521/xe")
            sql = "INSERT INTO student_mpj values(student_mpj_seq.nextval, '%s', '%s' )" %(student.name, student._class)
            cur.execute(sql)
            con.commit()
            sql = "SELECT s_no FROM student_mpj WHERE s_name = '%s'" % student.name
            cur.execute(sql)
            for result in cur:
                student.no = result[0]
                print("%s 학생 학번: %s" % (student.name,student.no))
            # self.all_num += 1
            return "성공"

        except Exception as e :
            print(e)
            return "실패"
        

        finally:
            ZsobDBM.ed(con,cur)