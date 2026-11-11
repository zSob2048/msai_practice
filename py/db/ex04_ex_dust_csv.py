# csv파일> hadoop이 db연동이안됨... 

from datetime import datetime
from oracledb import connect

f = open("C:/MS_AI_25/practice/py/seoul_dust.txt", "a", encoding="utf-8")

con = connect("MSAIuser/2048@195.168.9.238:1521/xe")

sql = "SELECT * FROM seoul_dust"

cur = con.cursor()
cur.execute(sql)

for date, msrrgn_nm, msrste_nm, pm10, pm25, idex_nm in cur:
    date = datetime.strftime(date, "%Y,%m,%d,%H,%M")
    # print("%s,%s,%s,%d,%d,%s\n" %(date, msrrgn_nm, msrste_nm, pm10, pm25, idex_nm))
    f.write("%s,%s,%s,%d,%d,%s\n" %(date, msrrgn_nm, msrste_nm, pm10, pm25, idex_nm))

    # (datetime.datetime(2025, 11, 10, 11, 13, 4), '동남권', '송파구', 19, 3, '좋음')



