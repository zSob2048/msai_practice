
from math import ceil
from py_object import product, seller
from zsobDBManager import ZsobDBM


class sellerDAO:
    def __init__(self):
        self.count_all()
        self.pagein = 3


    def reg(self,seller):
        try:
            con, cur = ZsobDBM.op("MSAIuser/2048@195.168.9.238:1521/xe")
            sql = "INSERT INTO seller_1111 VALUES(seller_1111_seq.nextval,'%s','%s',to_date('%s','yyyymmdd'))" %(seller.name, seller.addr, seller.bday)
            cur.execute(sql)
            con.commit()
            sql = "SELECT s_no FROM seller_1111 WHERE s_name = '%s'" % seller.name
            cur.execute(sql)
            for result in cur:
                seller.no = result[0]
                print("당신의 판매자 번호는 '%s'번 입니다." % seller.no)
            self.all_num += 1
            return "성공"
        except Exception as e :
            print(e)
            return "실패"
        
        finally:
            ZsobDBM.ed(con,cur)

    def count_all(self):
        try:
            con, cur = ZsobDBM.op("MSAIuser/2048@195.168.9.238:1521/xe")
            sql = "SELECT count(*) FROM seller_1111"
            cur.execute(sql)
            for result in cur:
                self.all_num = result[0]
        except Exception as e :
            print(e)
            return None
        finally:
            ZsobDBM.ed(con,cur)

    def count_page(self):
        return ceil(self.all_num / self.pagein)
    
    def all_list_page(self, page):
        page = int(page)
        try:
            con, cur = ZsobDBM.op("MSAIuser/2048@195.168.9.238:1521/xe")
            sql = "SELECT * FROM (SELECT rownum AS rn , s_no, s_name, s_addr, s_bday FROM(SELECT * FROM seller_1111 ORDER BY s_name) )WHERE rn>=%d AND rn<=%d" % (self.pagein * (page - 1) , self.pagein * page)
            cur.execute(sql)
            sellerlist = []
            for _, no, name, addr, bday in cur:
                s = seller(no, name, addr, bday)
                sellerlist.append(s)
            return sellerlist
        except Exception as e :
            print(e)
            return None
        finally:
            ZsobDBM.ed(con,cur)      
    
    # self.pagein * (page - 1) ~ self.pagein * page





class productDAO:
    def __init__(self):
        self.count_all()
        self.pagein = 3

    def reg(self, product):
        try:
            con, cur = ZsobDBM.op("MSAIuser/2048@195.168.9.238:1521/xe")
            sql = "INSERT INTO product_1111 VALUES(product_1111_seq.nextval,'%s',%s,'%s',%s)" % (product.name,product.price,product.cate,product.s_no)
            
            cur.execute(sql)
            con.commit()
            return "성공"
        except Exception as e :
            print(e)
            return "실패"
        finally:
            ZsobDBM.ed(con,cur)

    def count_all(self):
        try:
            con, cur = ZsobDBM.op("MSAIuser/2048@195.168.9.238:1521/xe")
            sql = "SELECT count(*) FROM product_1111"
            cur.execute(sql)
            for result in cur:
                self.all_num = result[0]
        except Exception as e :
            print(e)
            return None
        finally:
            ZsobDBM.ed(con,cur)

    def count_page(self):
        return ceil(self.all_num / self.pagein)
    
    def all_list_page(self, page):
        page = int(page)
        try:
            con, cur = ZsobDBM.op("MSAIuser/2048@195.168.9.238:1521/xe")
            sql = "SELECT * FROM (SELECT rownum AS rn , s_no, s_name, s_price, s_cate, s_no FROM(SELECT * FROM product_1111 ORDER BY s_name) )WHERE rn>=%d AND rn<=%d" % (self.pagein * (page - 1) , self.pagein * page)
            cur.execute(sql)
            productlist = []
            for _, no, name, price, cate, s_no in cur:
                s = product(no, name, price, cate, s_no)
                productlist.append(s)
            return productlist
        except Exception as e :
            print(e)
            return None
        finally:
            ZsobDBM.ed(con,cur)      

    
