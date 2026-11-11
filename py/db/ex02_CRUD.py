from oracledb import connect 

con = connect("MSAIuser/2048@195.168.9.238:1521/xe")


# ###############################################
# # insert
# name = input("이름 :")
# addr = input("주소 :")
# ceo = input("사장 :")
# emp = int(input("직원수 :"))

# sql = "INSERT INTO company_1107 values('%s', '%s', '%s',%d)" %(name,addr,ceo,emp)

# ###############################################
# # delete
# name = input("이름 :")

# sql = "DELETE FROM company_1107 WHERE c_name = '%s'" %name

# ###############################################
# # update
# name = input("이름 :")
# addr = input("수정할 주소 :")

# sql = "UPDATE company_1107 SET c_add = '%s' WHERE c_name = '%s'" %(name,addr)

# ###############################################

# # db 관련 작업들 총괄해주는 매니저 객체 겸 결과
cur = con.cursor()

# # str로 써둔 sql을 db서버로 전송 + 원격실행 + 결과 받아오기
# cur.execute(sql)


# # commit(DB서버에 반영) <> rollback(롤백)
# # > DBeaver가 자동commit

# # 실행 결과
# # CUD   : 영향받은 데이터 수
# # R     : 데이터
# if cur.rowcount == 1:
#     print("등록 성공")
#     con.commit()
# else:
#     print("등록 실패")

###############################################
# select

sql = "SELECT avg(s_price) FROM snack_1107"
cur.execute(sql)

for result in cur: # cur > tuple형태
    print(result[0])
    print("---")


###############################################

cur.close()

con.close
