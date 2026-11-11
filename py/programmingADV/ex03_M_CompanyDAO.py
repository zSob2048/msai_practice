from py.zsob.zDB import ZsobDBM


class CompanyDAO:
    def reg(company):
        con, cur = ZsobDBM.op("MSAIuser/2048@195.168.9.238:1521/xe")
        sql = "insert into company_1107 values('%s','%s','%s',%d)" %(company.name, company.add, company.ceo, company.emp )
        cur.execute(sql)
        if cur.rowcount == 1:
            con.commit()
            ZsobDBM.ed(con, cur)
            return "성공"
        else:
            ZsobDBM.ed(con, cur)
            return "실패"
        
