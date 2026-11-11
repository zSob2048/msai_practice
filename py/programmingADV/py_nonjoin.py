from zsobDBManager import ZsobDBM


# def get2(self, pageNo, searchTxt):
    # try:
con, cur = ZsobDBM.op("MSAIuser/2048@195.168.9.238:1521/xe")
        # searchTxt = "%" + searchTxt + "%"
        # pageNo = int(pageNo)
        # start = (pageNo - 1) * self.productPerPage + 1
        # end = pageNo * self.productPerPage

        # sql =  "SELECT * "
        # sql += "FROM ( "
        # sql += "    SELECT rownum AS rn, p_no, p_name, p_price, p_cate, s_name, s_addr, s_birthday "
        # sql += "    FROM ( "
        # sql += "        SELECT p_no, p_name, p_price, p_cate, s_name, s_addr, s_birthday "
        # sql += "        FROM nov11_seller, nov11_product "
        # sql += "        WHERE s_no = p_s_no "
        # # sql += "            AND (p_name LIKE '%s' OR p_cate LIKE '%s') " % (searchTxt, searchTxt)
        # sql += "        ORDER BY p_name, p_price "
        # sql += "    ) "
        # sql += ") "
        # # sql += "WHERE rn >= %d AND rn <= %d" % (start, end)
        # sql += "WHERE rn >= 4 AND rn <= 6"
sql = "SELECT * FROM (SELECT rownum AS rn, p_no, p_name, p_price, p_cate, p_s_no " \
"FROM ( SELECT * FROM product_1111 ORDER BY p_name, p_price ) ) WHERE rn >= 4 AND rn <= 6"
cur.execute(sql)

products = []
for _, p_no, p_name, p_price, p_cate, p_s_no in cur:
    p = [p_no, p_name, p_price, p_cate, p_s_no]
    products.append(p)
        
for p in products:
    sql = "SELECT s_name, s_addr, s_bday FROM seller_1111 WHERE s_no = '%s'" % p[4]
    cur.execute(sql)
    for s_name, s_addr, s_bday in cur:
        p.append(s_name)
        p.append(s_addr)
        p.append(s_bday)
    print(p)

# print(products)

        # products = []
        # for _, no, name, price, cate, s_name, s_addr, s_birthday in cur:
            # p = Product2(no, name, price, cate, s_name, s_addr, s_birthday)
            # products.append(p)
        # return products
    # except Exception as e:
    #     print(e)
    #     return None
    # finally:
ZsobDBM.ed(con, cur)