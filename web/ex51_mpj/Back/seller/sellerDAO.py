from datetime import datetime
from zsob.zDBM import zDB


class SellerDAO:
    def __init__(self):
        self.inPage_num = 5
        self.seller_all()

    def seller_all(self):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "SELECT count(*) FROM company_1203"
            cur.execute(sql)

            for c in cur:
                self.allseller_num = c[0]

        except Exception as e:
            print(e)
        finally:
            zDB.ed(con,cur)

    def reg(self, name, bday, addr):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "INSERT INTO company_1203 values(company_1203_seq.nextval,  '%s','%s',to_date('%s','yyyymmdd'))" %(name,addr,bday)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allseller_num += 1
                return {"result" : name + " 등록 성공"}
            return {"result" : name + " 등록 실패"}

        except:
            return {"result" : name + " 등록 실패"}
        finally:
            zDB.ed(con,cur)

    def get(self,pg,searchkey):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            searchkey = "%" + searchkey + "%"
            sql = sql = "SELECT * FROM (" \
            "SELECT rownum AS rn , c_no, c_ceo, c_loc, c_bday FROM(" \
            "SELECT * FROM company_1203 WHERE (c_ceo LIKE '%s' OR c_loc LIKE '%s') ORDER BY c_no) )" \
            "WHERE rn>%d AND rn<=%d" % ( searchkey, searchkey ,self.inPage_num * (int(pg) - 1) , self.inPage_num * int(pg))
            cur.execute(sql)

            sellers = []
            for _, no, name, addr, bday in cur:
                bday = datetime.strftime(bday, "%Y/%m/%d")
                sellers.append({"no":no, "name":name,"bday":bday, "addr":addr})
            return sellers

        except Exception as e:
            print(e)
            return {"result" : "err" }
        finally:
            zDB.ed(con,cur)

    def NumS(self,no):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "SELECT * FROM company_1203 WHERE c_no = %s" %no
            cur.execute(sql)

            for no, name, addr, bday in cur:
                bday = datetime.strftime(bday, "%Y/%m/%d")
                seller = {"no":no, "name":name,"bday":bday, "addr":addr}
            return seller

        except Exception as e:
            print(e)
        finally:
            zDB.ed(con,cur)

    def update(self, no, name, addr):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "UPDATE company_1203 SET c_ceo = '%s' , c_loc = '%s' WHERE c_no = %s" %(name,addr,no)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return {"result" : name + " 수정 성공"}
            return {"result" : name + " 수정 실패"}

        except:
            return {"result" : name + " 수정 실패"}
        finally:
            zDB.ed(con,cur)

    def delete(self, no):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "DELETE FROM company_1203 WHERE c_no = %s" % no
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allseller_num -= 1
                return {"result" : " 삭제 성공"}
            return {"result" : " 삭제 실패"} # 이미 삭제된 게시글의 경우

        except:
            return {"result" : " 삭제 실패"}
        finally:
            zDB.ed(con,cur)