
from json import loads
from http.client import HTTPConnection

f = open("C:\MS_AI_25\practice\py/bd/subpayfree.csv", "a", encoding="utf-8")
hc = HTTPConnection("openapi.seoul.go.kr:8088")

for y in range(2015,2026):
    for m in range(1,13):
        ym = "%d%02d" %(y,m)
        hc.request("GET","/YOUR_SEOUL_API_KEY/json/CardSubwayPayFree/1/700/"+ym)
        res = hc.getresponse().read()
        
        for r in loads(res)["CardSubwayPayFree"]["row"]:
            f.write("%s,"%r["USE_MM"])
            f.write("%s,"%r["SBWY_ROUT_LN_NM"])
            f.write("%s,"%r["STTN"])
            f.write("%.0f,"%r["RMIO_GTON_NOPE"])
            f.write("%.0f,"%r["FREECHRG_GTON_NOPE"])
            f.write("%.0f,"%r["RMIO_GTOFF_NOPE"])
            f.write("%.0f\n"%r["FREECHRG_GTOFF_NOPE"])

hc.close()
f.close()