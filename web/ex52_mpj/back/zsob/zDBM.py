from oracledb import connect


class zDB:
    @staticmethod
    def op(info):
        con = connect(info)
        cur = con.cursor()
        return con, cur
    
    @staticmethod
    # def ed(sql, con, cur):
    def ed(con, cur):
        # cur.execute(sql)
        # if sql.startswith("SELECT") != True :
        #     if cur.rowcount == 1:
        #         print("등록 성공")
        #         con.commit()
        #     else:
        #         print("등록 실패")

        cur.close()
        con.close()

    
