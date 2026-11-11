import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm



fontF = "C:\Windows\Fonts\gulim.ttc"
fontN = fm.FontProperties(fname=fontF, size= 10).get_name()
plt.rc("font", family=fontN)
plt.rcParams["axes.unicode_minus"]=False


data = [28, 1, 10]
labell = ["901", "902", "903"]
e = [0,0,0.3]
w = {"width":0.7, "edgecolor":"#A0CB8C","linewidth":2}

plt.pie(data, labels=labell)
plt.pie(data, labels=labell, autopct="%.1f%%", startangle=90, explode=e, wedgeprops=w)
plt.show()
