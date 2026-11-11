import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm



# C:\Windows\Fonts 에서 cmd > dir로 이름 확인
fontF = "C:\Windows\Fonts\gulim.ttc"
fontN = fm.FontProperties(fname=fontF, size= 10).get_name() # 폰트명
plt.rc("font", family=fontN) # mpl 기본톤프 바꾸기
plt.rcParams["axes.unicode_minus"]=False # - 안깨지게... 

yD = [12, 10, 5 ,22 ,8]
xD = np.array([1,3,5,6,7])

# plt.plot(xD,yD)

plt.xlabel("name of x-axis")
plt.ylabel("name of x-axis")

plt.axis([0,10,-10,30]) # xmin, xmax, ymin, ymax

plt.title("title")
plt.title("title2", loc="left")
plt.title("title3", loc="right", fontdict={"fontsize":20, "fontweight": 900,"color":"#A0CB8C"})

# matplotlib cheat sheet

plt.grid(axis="both")

# plt.xticks(xD,["1틱","3틱","5틱","6틱","7틱"])
# plt.yticks(yD,["12틱","10틱","5틱","22틱","8틱"])
# plt.yticks(np.arange(0,23,5),["a","b","c","d","e"])
# plt.tick_params("x", direction="in", length= 10, pad=20) # out inout
# plt.tick_params("y", color= "#A0CB8C", labelcolor="#A0CB8C", labelsize=15)


yD2 = [3, 10, 21, 21, 8]
# plt.plot(xD,yD2, "r-.")

_, ax1 = plt.subplots()
# p1 = ax1.plot(xD,yD)
# ax2 = ax1.twinx()
# p2 = ax2.plot(xD,yD2)


# plt.legend(["d1","d2"])

# plt.bar(xD,yD,
#         color=["#A0Cb8C","#6F9F68"], width=1,
#         # edgecolor="#6F9F68", linewidth=5
#         )

# plt.bar(xD,yD,width=0.4, align="edge")
# plt.bar(xD-0.4,yD2,width=0.4, align="edge")

plt.bar(xD,yD)
plt.bar(xD,yD2, bottom=yD)


plt.show()