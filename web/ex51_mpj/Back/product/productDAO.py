from zsob.zDBM import zDB


class ProductDAO:
    def __init__(self):
        self.inPage_num = 5
        self.product_all()

    def product_all(self):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "SELECT count(*) FROM product_1203"
            cur.execute(sql)

            for c in cur:
                self.allproduct_num = c[0]

        except Exception as e:
            print(e)
        finally:
            zDB.ed(con,cur)

    def reg(self, name, pric, stoc,c_no):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "INSERT INTO product_1203 values(product_1203_seq.nextval,  '%s', %s,%s,%s)" %(name,pric,stoc,c_no)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allproduct_num +=1
                return {"result" : name + "등록 성공"}
            return {"result" : name + "등록 실패"}

        except Exception as e:
            return {"result" : name + "등록 실패"}                
                
        finally:
            zDB.ed(con,cur)

    def get(self,pg,searchkey):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            searchkey = "%" + searchkey + "%"
            sql = sql = "SELECT * FROM (" \
            "SELECT rownum AS rn , p_no, p_name, p_price, p_stock, p_c_no FROM(" \
            "SELECT * FROM product_1203 WHERE (p_name LIKE '%s') ORDER BY p_no) )" \
            "WHERE rn>%d AND rn<=%d" % ( searchkey, self.inPage_num * (int(pg) - 1) , self.inPage_num * int(pg))
            cur.execute(sql)

            products = []
            for _, no, name, pric, stoc, c_no in cur:
                products.append({"no":no, "name":name,"pric":pric, "stoc":stoc, "c_no" : c_no})
            return products

        except Exception as e:
            print(e)
            return {"result" : "err" }
        finally:
            zDB.ed(con,cur)    


    def NumS(self,no):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "SELECT * FROM product_1203 WHERE p_no = %s" %no
            cur.execute(sql)

            for no, name, pric, stoc, c_no in cur:
                product={"no":no, "name":name,"pric":pric, "stoc":stoc, "c_no" : c_no}
            return product

        except Exception as e:
            print(e)
            
        finally:
            zDB.ed(con,cur)


    def update(self, no, name, pric, stoc):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "UPDATE product_1203 SET p_name = '%s' , p_price = %s, p_stock = %s WHERE p_no = %s" %(name,pric,stoc,no)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return {"result" : name + " 수정 성공"}
            return {"result" : name + " 수정 실패"}

        except Exception as e:
            return {"result" : name + " 수정 실패"}
        finally:
            zDB.ed(con,cur)

    def delete(self, no):
        try:
            con,cur = zDB.op("MSAIuser/2048@195.168.9.194:1521/xe")
            sql = "DELETE FROM product_1203 WHERE p_no = %s" % no
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allseller_num -= 1
                return {"result" : " 삭제 성공"}
            return {"result" : " 삭제 실패"}

        except Exception as e:
            return {"result" : " 삭제 실패"}
        finally:
            zDB.ed(con,cur)
