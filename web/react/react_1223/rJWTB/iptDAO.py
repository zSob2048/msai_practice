from fastapi.responses import JSONResponse
from datetime import datetime, timedelta, timezone
import jwt

class IptDAO:
    def __init__(self):
        self.jkey = "keyy"
        self.jAlgorithm = "HS256"

    def reg(self,ip1,ip2):
        h={"Access-Control-Allow-Origin":"*"}
        ipdata = {"ipt1":ip1,"ipt2":ip2,"exp":datetime.now(timezone.utc)+timedelta(seconds=600)}
        jwtt = jwt.encode(ipdata,"keyy","HS256")
        return JSONResponse({"jwtresult":jwtt},headers=h)
    
    def decodd(self,jwtt):
        h={"Access-Control-Allow-Origin":"*"}
        try:
            jwtD = jwt.decode(jwtt,self.jkey,self.jAlgorithm)
            jwtD = {"result": "성공","ipt1":jwtD["ipt1"],"ipt2":jwtD["ipt2"]}
        except jwt.ExpiredSignatureError:
            jwtD = {"result": "시간만료"}
        except jwt.DecodeError:
            jwtD = {"result": "존재하지않는DATA"}
        
        print(jwtD)
        return JSONResponse(jwtD,headers=h)