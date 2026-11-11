# pip install pymongo

from unittest import result
from pymongo import ASCENDING, DESCENDING, MongoClient


con = MongoClient("195.168.9.238") # 서버주소(:포트번호)
# print(con)
db = con.product
# print(db)

name = input("이름: ")
age = int(input("나이: "))

# db.studunt_1114.insert_one({"s_name":name,"s_age":age});
result = db.student_1114.insert_one({"s_name":name,"s_age":age});
if result.acknowledged:
    print("등록성공")

result = db.student_1114.find();

for s in result:
    print(s["s_name"])
    print(s["s_age"])

# 정렬 : list 안에 tuple 형태로, ASCENDING : 오름차순(=1) / DESCENDING : 내림차순(=-1)
result = db.student_1114.find().sort([("s_name",ASCENDING),("s_age",DESCENDING)])

con.close()
