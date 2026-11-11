import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontF = "C:\Windows\Fonts\gulim.ttc"
fontN = fm.FontProperties(fname=fontF, size= 10).get_name()
plt.rc("font", family=fontN)
plt.rcParams["axes.unicode_minus"]=False

df = pd.read_csv("C:\MS_AI_25\practice\py/bd\subpayfree.csv",names=["ym","line","station","on_o","on_x","off_o","off_x"])

df = df.groupby("line")[["on_o","on_x","off_o","off_x"]].mean()

y1 = df["on_o"].to_numpy()
y2 = df["on_x"].to_numpy()
y3 = df["off_o"].to_numpy()
y4 = df["off_x"].to_numpy()
xLab = df.index.to_numpy()
x = np.arange(len(xLab))

# plt.bar(x-0.4,y1,width=0.4, align="edge")
# plt.bar(x-0.4,y3,width=0.4, align="edge", bottom=y1)
# plt.bar(x,y2,width=0.4, align="edge")
# plt.bar(x,y4,width=0.4, align="edge", bottom=y2)
# plt.xticks(x,xLab, rotation=45)

# pieD = [y1.mean(),y2.mean(),y3.mean(),y4.mean()]
# pieL = ["유임승차","무임승차","유임하차","무임하차"]
# plt.pie(pieD,labels=pieL,autopct="%.1f%%")

plt.scatter(y1,y3,s=(y2+y4)/5000)

plt.title("지하철 유/무임승하차")

plt.show()