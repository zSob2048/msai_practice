import datetime
from http.client import HTTPConnection
from json import loads
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

fontF = "C:\Windows\Fonts\gulim.ttc"
fontN = fm.FontProperties(fname=fontF, size= 10).get_name()
plt.rc("font", family=fontN)
plt.rcParams["axes.unicode_minus"]=False

# print(plt.colormaps) # 색상확인용
# hc = HTTPConnection("openapi.seoul.go.kr:8088")
# hc.request("GET","/YOUR_SEOUL_API_KEY/json/RealtimeCityAir/1/25/")
# res = hc.getresponse()
# resBody = res.read()
# hc.close()

# dustData = loads(resBody)
# df = pd.DataFrame((dustData["RealtimeCityAir"]["row"]))

subDf = pd.read_csv("C:\MS_AI_25\practice\py/bd\subpayfree.csv",names=["ym","line","station","on_o","on_x","off_o","off_x"])
# sns.lineplot(df)
# sns.barplot(df, x="MSRSTN_NM",y="PM", palette="Grays", hue="SAREA_NM")
# sns.barplot(df, x="SAREA_NM",y="PM", palette="Grays", hue="SAREA_NM") # 기본 신뢰 95%구간
# sns.barplot(df, x="SAREA_NM",y="PM", palette="Grays", hue="SAREA_NM", errorbar="sd") # 표준편차

# sns.countplot(df,x="SAREA_NM", palette="Grays", hue="SAREA_NM")

# def ftn(t):
#     day = "%d%02d%02d" %(t["y"], t["m"], t["d"])
#     day = datetime.strptime(day,"%Y%m%d")
#     day = datetime.strftime(day,"%a")
#     return day

# subDf["o_addd"] = subDf["on_o"]+subDf["off_o"]
# subDf["col"] = subDf.apply(ftn, axis=1)

sns.scatterplot(subDf, x="on_o", y="on_x", palette="Grays", hue="line",size=1)

# sns.barplot(subDf,x= "line",y = "o_addd")

plt.show()


