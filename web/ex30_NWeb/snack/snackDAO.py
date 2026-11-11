from zsob.zDBM import ZsobDBM


class SnackDAO:
    def reg(self, nn, pp):
        # DB에 등록 + 결과가 JSON으로
        try: 
            con,cur = ZsobDBM.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "insert into snack_1125 values('%s',%d)" %(nn,pp)
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return{"result": nn+" 등록 성공"}
            return{"result": nn+" 등록 실패"}
        except Exception as e:
            print(e)
            return{"result": nn+" 등록 실패"}
        finally:
            ZsobDBM.ed(con,cur)

    def get(self):
        # DB에 등록 + 결과가 JSON으로
        try: 
            con,cur = ZsobDBM.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "select * from snack_1125 order by s_name"
            cur.execute(sql)

            snacks = []
            for name,price in cur:
                snacks.append({"s_name":name,"s_price":price})
            return snacks

        except Exception as e:
            print(e)
            return None

        finally:
            ZsobDBM.ed(con,cur)

# /snack.search?page=2&search=칩