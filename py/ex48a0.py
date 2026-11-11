# http://openapi.seoul.go.kr:8088/YOUR_SEOUL_API_KEY/json/CardBusStatisticsServiceNew/1/5/20151101/

from http.client import HTTPConnection
from json import loads

yy = 2015
f = open("C:/MS_AI_25/practice/py/busdata%d.csv"%yy,"a",encoding="utf=8")

hc = HTTPConnection("openapi.seoul.go.kr:8088")


for mm in range(1,13):
    for dd in range(1,32):
        for start in range (1, 41002,1000):
            t = "%d/%d/%d%d%d"%(start,start+999,yy,mm,dd)
            hc.request("GET","/YOUR_SEOUL_API_KEY/json/CardBusStatisticsServiceNew/"+t)
            res_body = hc.getresponse().read()

            data_raw = loads(res_body)
            if "CardBusStatisticsServiceNew" in data_raw:
                cbssn= data_raw["CardBusStatisticsServiceNew"]
                stations = cbssn["row"]
                for s in stations:
                    y,m,d = s["USE_YMD"][0:4],s["USE_YMD"][4:6],s["USE_YMD"][6,8] # 2015, 11, 01 형태로
                    rn = s["RTE_NM"].replace(",",".") # , 제거
                    ssn = s["SBWY_STNS_NM"].replace(",",".") # , 제거
                    gont = s["GTON_TNOPE"] # 소숫점 절삭
                    gofft = s["GTOFF_TNOPE"] # 소숫점 절삭
                    data = "%s,%s,%s,%s,%s,%.0f,%.0f\n" %(y,m,d,rn,ssn,gont,gofft)
                    f.write(data)
                

hc.close()
f.close()