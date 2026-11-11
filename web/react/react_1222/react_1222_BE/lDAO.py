from datetime import datetime, timedelta, timezone
from fastapi.responses import JSONResponse
import jwt
    
# JWT (JSON Web Token)
# JSON+암호화+시간제(갱신x)

# pip install pyjwt



class LDAO:
    def __init__(self):
        self.jkey = "keyy"
        self.jAlgorithm = "HS256"

    def reg(self, id,pw):
        h={"Access-Control-Allow-Origin":"*"}
        # result = {"id":id,"pw":pw}
        result = {"id":id,"pw":pw, "asdf":"asdf" ,"exp":datetime.now(timezone.utc)+timedelta(seconds=600)} # exp: 시간제한(그 시간까지!)
        jwtR = jwt.encode(result,"keyy","HS256") # HS256: 암호화 알고리즘
        print(jwtR)
        return JSONResponse({"jwtresult":jwtR},headers=h)
    
    def decodd(self,jwtt):
        h={"Access-Control-Allow-Origin":"*"}
        try:
            jwtD = jwt.decode(jwtt,self.jkey,self.jAlgorithm)
            jwtD = {"result": "성공","id":jwtD["id"],"pw":jwtD["pw"]}
        except jwt.ExpiredSignatureError:
            jwtD = {"result": "시간만료"}
        except jwt.DecodeError:
            jwtD = {"result": "존재하지않는DATA"}
        
        print(jwtD)
        return JSONResponse(jwtD,headers=h)
    
    def udateexp(self, jwtt):
        h={"Access-Control-Allow-Origin":"*"}
        try:
            jwtU = jwt.decode(jwtt,self.jkey,self.jAlgorithm)
            print(jwtU)
            jwtU = {"result": "갱신","id":jwtU["id"],"pw":jwtU["pw"], "exp":datetime.now(timezone.utc)+timedelta(seconds=600)}
            print(jwtU)
            jwtU = jwt.encode(jwtU,self.jkey,self.jAlgorithm)
            print(jwtU)
        except jwt.ExpiredSignatureError:
            jwtU = "시간만료"
        except jwt.DecodeError:
            jwtU = "존재하지않는DATA"

        return JSONResponse({"result":jwtU},headers=h)