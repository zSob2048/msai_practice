from http.client import HTTPConnection
from json import loads
import pandas as pd

a = pd.Series([1,2,3,4])
print(a)

b = pd.DataFrame()
b["indexA"] = ["A1","A2"]
b["index0"] = [1,2]
b = b.set_index(b["indexA"])
print(b)
print(b.loc["A1"])
# indexA    A1
# index0     1
# Name: A1, dtype: object
print(b.iloc[1])
# indexA    A2
# index0     2
# Name: A2, dtype: object


import numpy as np

a["index0"] = np.array([1, 2])

b = [["A1", 1],["A2",2]]
b = pd.DataFrame(b, columns=["indexA","index0"])
print(b)

c = {"indexA": ["A1","A2"],
     "index0": [1, 2]}
c = pd.DataFrame(c)
print(c)

d = [{"indexA":"A1","index0":1},
    {"indexA":"A2","index0":2},]
d = pd.DataFrame(d)
print(d)

# hc = HTTPConnection("openapi.seoul.go.kr:8088")
# hc.request("GET","/YOUR_SEOUL_API_KEY/json/RealtimeCityAir/1/25/")
# res = hc.getresponse()
# resBody = res.read()
# hc.close()

# dustData = loads(resBody)
# dustDF = pd.DataFrame((dustData["RealtimeCityAir"]["row"]))
# print(dustDF)

# subDataCsv = pd.read_csv("py/bd/subway.csv", names = ["y","m","d","line","station","up","down"]) # sep="??" : 데이터 구분 기호(기본 csv , 기준)

e = pd.Series(["A3",3], index= ["indexA","index0"])
# append 불가
e = pd.DataFrame([e])
d =pd.concat([d,e])
print(d)
