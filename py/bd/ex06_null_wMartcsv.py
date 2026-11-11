import pandas as pd

df = pd.read_csv("C:\MS_AI_25\practice\py/bd\lnps 1.csv", names=["마트", "품명", "가격","날짜","종류","구"])
df = df.set_index(df["마트"])
df = df.sort_index()

print(df.loc["통인시장"])

print(df["품명"].isnull()) # TF로 출력
print(df[df["품명"].isnull()])

df["품명"] = df["품명"].fillna("NaN")

# pandas엔 null이 없음
import numpy as np

df["품명"] = df["품명"].replace("NaN", np.nan)
# df["품명"] = df["품명"].replace("NaN", None) # 보통 npnan으로 많이 씀(왜죠...)

print(df[df["마트"].str.contains("가락",na=False)])
print(df[df["품명"].str.contains("사과",na=False)][["마트","품명"]])

print(df.sort_values(["품명","가격"],ascending=[True,False]))

print(df[df["가격"]>=30000][["품명","가격"]])

# for i, v in enumerate(df[df["구"]=="종로구"].index):
#     print(df[df["구"]=="종로구"].iloc[i])

print(df["가격"].max())
print(df["가격"].min())
print(df["가격"].median()) # 중앙값
print(df["가격"].mode()) # 최빈값 : Series로 나옴(앞쪽 0은 index)
print(df["가격"].sum())
print(df["가격"].count())
print(df["가격"].var())
print(df["가격"].std())
print(df["가격"].describe()) # 이거저거 요약(위에거거의다)

print(df.groupby("종류")["가격"].mean())
print(df.groupby(["구","종류"])["가격"].mean())

# df.replace("전통시장","시장") # 필드 구분 X
df["종류"] = df["종류"].replace("전통시장","시장") # 필드 지정

# 다중수정
df["구"] = df["구"].replace(["강남구", "송파구"],["강남","송파"])
df["구"] = df["구"].replace({"강남":"강남구","송파":"송파구"})
df["구"] = df["구"].replace(["강남구", "송파구"],"서울")

# 필드명 수정
df = df.rename(columns={"마트":"마트명","품명":"품목명"})





#huggingface/ollama