from fastapi.responses import JSONResponse


class Calculator:
    def operatee(self, x, y):
        h = {"Access-Control-Allow-Origin":"*"}
        return JSONResponse({"add": x + y, "sub": x - y, "multi": x * y, "div": x / y},headers=h)
    
    def operateupg(self, x, y):
        h = {"Access-Control-Allow-Origin":"http://localhost:5173",
             "Access-Control-Allow-Credentials":"true"}
        return JSONResponse({"add": x + y, "sub": x - y, "multi": x * y, "div": x / y},headers=h)
    

# IP주소:
# localhost = 본인 IP = 127.0.0.1 인데
# "Access-Control-Allow-Origin":"http://localhost:5173" 라고 적었을 경우
# 127.0.0.1:5173으로 접속시 불가능