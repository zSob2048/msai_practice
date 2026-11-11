from datetime import datetime, timedelta, timezone
from os import remove

from fastapi.responses import FileResponse
import jwt
from lib.zDBM import zDB
from lib.zFileM import zFile


class MemberDAO:
    def __init__(self):
        self.photoPath = "./member/photo/"
        self.jKey = "zKey2048"
        self.jAlgorithm = "HS256"

    def idCheck(self,id):
        try:
            con, cur =zDB.op("MSAIuser/2048@195.168.9.10:1521/xe")
            sql = "SELECT count(*) FROM sitemember WHERE id = '%s'" %id
            cur.execute(sql)

            for c in cur:
                if c[0] == 1:
                    return { "result":False }
            return{ "result":True }
        except:
            return {"result" : False }
        finally:
            zDB.ed(con,cur)

    async def signUp(self, photo,id, pw,name,addr,bday,tel):
        photoN = await zFile.op(self.photoPath, photo, "uuid" , 3000)
        if photoN == "fail":
            return {"result": "이미지 용량 초과"}
            
        try: 
            con, cur =zDB.op("MSAIuser/2048@195.168.9.10:1521/xe")
            sql = "INSERT INTO sitemember values(" \
            "'%s','%s','%s','%s',to_date('%s','yyyymmdd'),'%s','%s')" %(id, pw,name,addr,bday,tel,photoN)
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return {"result": "가입 성공"}
            raise
        except:
            remove(self.photoPath+photoN)
            return {"result": "가입 실패"}
        finally:
            zDB.ed(con,cur)

    def signUpNp(self, id, pw,name,addr,bday,tel):
        try: 
            con, cur =zDB.op("MSAIuser/2048@195.168.9.10:1521/xe")
            sql = "INSERT INTO sitemember values(" \
            "'%s','%s','%s','%s',to_date('%s','yyyymmdd'),'%s','')" %(id, pw,name,addr,bday,tel)
            cur.execute(sql)

            if cur.rowcount == 1:
                con.commit()
                return {"result": "가입 성공"}
            raise
        except:
            return {"result": "가입 실패"}
        finally:
            zDB.ed(con,cur)

    def login(self,idI,pwI):
        try: 
            con, cur =zDB.op("MSAIuser/2048@195.168.9.10:1521/xe")
            sql = "SELECT * FROM sitemember WHERE id = '%s'" %idI
            cur.execute(sql)
            count = 0
            for id, pw, name, addr, bday, tel, photo in cur:
                count += 1
                if pwI == pw:
                    memberData = {
                        "id" : id,
                        "pw" : pw,
                        "name" : name,
                        "addr" : addr,
                        "bday" : datetime.strftime(bday, "%Y%m%d") if bday is not None else "N/A",
                        "tel" : tel,
                        "photo" : photo,
                        "exp" : datetime.now(timezone.utc)+timedelta(seconds=300)
                    }
                    memberData = jwt.encode(memberData, self.jKey, self.jAlgorithm)
                    return {"result": "로그인 성공" , "memberInfo": memberData}
                else:
                   return {"result": "PW오류"}
            if count ==0:
                return{"result": "ID 정보 없음"}
            raise
        except Exception as e :
            print(e)
            return {"result": "DB오류"}
        finally:
            zDB.ed(con,cur)

    def memberInfoGet(self, memberInfo):
        try:
            memberInfo = jwt.decode(memberInfo, self.jKey,self.jAlgorithm)
            memberInfo = {
                "id" : memberInfo["id"],
                "pw" : memberInfo["pw"],
                "name" : memberInfo["name"],
                "addr" : memberInfo["addr"],
                "bday" : memberInfo["bday"],
                "tel" : memberInfo["tel"],
                "photo" : memberInfo["photo"]
            }
            return {"result":"조회 성공","memberInfo":memberInfo}
        except jwt.ExpiredSignatureError:
            return {"result": "만료"}
        except jwt.DecodeError:
            return {"result": "정보 없음"}
        
    def memberInfoGetR(self, memberInfo):
        try:
            memberInfo = jwt.decode(memberInfo, self.jKey,self.jAlgorithm)
            memberInfo = {
                "id" : memberInfo["id"],
                "pw" : memberInfo["pw"],
                "name" : memberInfo["name"],
                "addr" : memberInfo["addr"],
                "bday" : memberInfo["bday"],
                "tel" : memberInfo["tel"],
                "photo" : memberInfo["photo"],
                "exp" : datetime.now(timezone.utc)+timedelta(seconds=300)
            }
            memberInfo = jwt.encode(memberInfo, self.jKey, self.jAlgorithm)
            return {"result":"갱신","memberInfo":memberInfo}
        except jwt.ExpiredSignatureError:
            return {"result": "만료"}
        except jwt.DecodeError:
            return {"result": "정보 없음"}



    def photoGet(self,photo):
        if photo == None or photo== "" or photo=="null":
            photo = "default.png"
        return FileResponse(self.photoPath+photo, filename=photo)
    
    