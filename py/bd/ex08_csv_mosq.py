import pandas as pd

df = pd.read_csv("C:\MS_AI_25\practice\py/bd\mosquito 1.csv", names=["date", "r", "h","p"])
df = df.set_index(df["date"])
print(df)
df = df.replace("noValue",None)
df["r"] = pd.to_numeric(df["r"])
df["h"] = pd.to_numeric(df["h"])
df["p"] = pd.to_numeric(df["p"])
# df = df.astype({"r":"float","h":"float","p":"float"})
df["avg"] = (df["r"]+df["h"]+df["p"])/3
print(df[df["avg"]==df["avg"].max()])
# print(df["avg"])