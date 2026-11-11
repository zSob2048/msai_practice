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

hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET","/YOUR_SEOUL_API_KEY/json/RealtimeCityAir/1/25/")
res = hc.getresponse()
resBody = res.read()
hc.close()

dustData = loads(resBody)
dustDF = pd.DataFrame((dustData["RealtimeCityAir"]["row"]))

# sns.histplot(dustDF,x="PM")
# sns.pairplot(dustDF)
# sns.violinplot(dustDF, x="PM", y="SAREA_NM" )
# sns.lmplot(dustDF, x="PM", y="FPM") # 추세선 포함
# sns.jointplot(dustDF, x="PM", y="FPM",kind="reg") # 
# sns.jointplot(dustDF, x="PM", y="FPM",kind="kde") # 등고선
# sns.jointplot(dustDF, x="PM", y="FPM",kind="hex") 

# pt = dustDF.pivot_table(index="SAREA_NM", columns="", values="")
# sns.heatmap(pt)


plt.show()