from http.client import HTTPConnection
from json import loads
import pandas as pd


hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET","/YOUR_SEOUL_API_KEY/json/RealtimeCityAir/1/25/")
res = hc.getresponse()
resBody = res.read()
hc.close()

dustData = loads(resBody)
dustDF = pd.DataFrame((dustData["RealtimeCityAir"]["row"]))
# print(dustDF)

dustDF["PM_AVG"] = (dustDF["PM"]+dustDF["FPM"])/2

print(dustDF[["MSRSTN_NM","PM_AVG"]])

