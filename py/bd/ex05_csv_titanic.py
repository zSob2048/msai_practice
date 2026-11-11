from http.client import HTTPConnection
import pandas as pd


tt = pd.read_csv("C:\MS_AI_25\practice\py/bd/titanic.csv")
# print(tt)
# print(tt.shape)
# print(tt.columns)
# print(tt.head())
# print(tt.tail(3))

# print(tt["Name"])
# print(tt.Name)
# print(tt[["Name","Age"]])

# print(tt.iloc[1])
# print(tt.iloc[1:5])

# ttN = tt.set_index(tt["Name"]) # 지정값이 없는 경우 0~N
# print(ttN)
# print(ttN.loc["Behr, Mr. Karl Howell"]) # 얘도 범위조회 가능(왜...)

# print(ttN.loc["Behr, Mr. Karl Howell", "Age"])
# print(ttN.loc["Behr, Mr. Karl Howell"][["Age","Ticket"]])
# print(ttN.loc["Behr, Mr. Karl Howell", ["Age","Ticket"]])
# print(ttN[ (ttN["Age"]>=20) & (ttN["Age"]<30)][ "Age"])

# print(ttN[ttN["Name"].str.contains("Mr")])

# ttN = ttN.sort_values(by=["Pclass","Age"], ascending=[False, True])

# hc = HTTPConnection("openapi.seoul.go.kr:8088")
# hc.request("GET","/YOUR_SEOUL_API_KEY/xml/ListNecessariesPriceService/1/25/")
# res = hc.getresponse()
# resBody = res.read()
# hc.close()

# tt = tt[["Name", "Sex"]]
tt["Sex"] = tt["Sex"].replace({"male":"남","female":"여"})
tt["Name"] = tt["Name"].apply(lambda n :n.replace("Mr.","미스터"))
tt["Name"] = tt["Name"].apply(lambda n :n.split(", ")[0])

# tt["Age"] = tt["Age"].apply(lambda n :"%.0f0대" %(n/10))
# tt["Age"] = tt["Age"].apply(lambda n :"%.0f0대" %(n//10))
# tt["Age"] = tt["Age"].replace({"nan0대":"미상"})

# delete
# tt = tt.drop("Survived", axis=1)
# tt = tt.drop(["Pclass","Fare"], axis=1)
# tt = tt[["Age","Name"]]

# tt = tt.drop(889) # index 기준
# tt = tt[tt["Age"]<30]

print(tt.groupby("Pclass")["Fare"].mean())
print(tt.groupby(["Pclass","Survived"])["PassengerId"].count())
print(tt["Cabin"].unique()) # 중복제거
print(tt["Cabin"].nunique()) # 중복제거>count
print(tt["Cabin"].value_counts()) # 중복 타이틀 당 값 count


print(tt)


# marge
# pd.concat([df1,df2]) : 단순 합성(df1 뒤 df2 이어서) / row 추가
# pd.concat([df1,df2],axis=1) : column 추가
# pd.marge(df1, df2) : 겹치는 필드 기준
# pd.marge(df1, df2, on="filed") : 겹치는 필드 2개이상인경우 지정
# pd.marge(df1, df2, left_on="filedLeft", right_on="filedRight") : 다른 필드명을 가진경우 각각

