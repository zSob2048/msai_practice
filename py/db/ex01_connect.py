# python - DB서버 : ? 
# db메이커간 표준화된 통신방식 x 다다름

# cx_Oracle.py(구버전) >> +instantclient
# oracledb.py >> 신버전. instantclient는 없어도 되지만 구버전이랑 호환x

# pip : python 패키지 관리자
# cmd에 pip install (패키지명) >>설치
# pip install oracledb

from oracledb import connect #, init_oracle_client


# init_oracle_client(lib_dir="instantclient 폴더경로") : 구버전 쓴다면 해야됨

con = connect("MSAIuser/2048@195.168.9.238:1521/xe") # sqlplus 그주소

print(con)

con.close
