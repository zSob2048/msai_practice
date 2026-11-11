from datetime import datetime
from http.client import HTTPConnection
from time import strftime
from xml.etree.ElementTree import fromstring
from oracledb import connect 
 
hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET", "/YOUR_SEOUL_API_KEY/xml/RealtimeCityAir/1/25/")
res = hc.getresponse()
resBody = res.read()
hc.close()
#######################
con = connect("MSAIuser/2048@195.168.9.238:1521/xe")

seoulDustDataa = fromstring(resBody)
rowsss = seoulDustDataa.iter("row")
for r in rowsss:
    msrrgn_nm = r.find("SAREA_NM").text
    msrste_nm = r.find("MSRSTN_NM").text
    pm10 = r.find("PM").text
    pm25 = r.find("FPM").text
    idex_nm = r.find("CAI_GRD").text
    
    sql = "insert into seoul_dust values(sysdate, '%s', '%s', '%s', '%s', '%s')" % ( msrrgn_nm, msrste_nm, pm10, pm25, idex_nm)
    
    cur = con.cursor() # 이거 1회용임 = for 안에 넣어두기
    cur.execute(sql)
    con.commit()
    cur.close()

con.close()


 
