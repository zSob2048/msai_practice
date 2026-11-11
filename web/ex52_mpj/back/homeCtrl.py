from fastapi import FastAPI
from fastapi.responses import JSONResponse

from memoDAO import memoDAO


app = FastAPI()
mDAO = memoDAO()

@app.get("/main.reg")
def mainMreg(contant):
    result = mDAO.main_reg(contant)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/reply.reg")
def replyMreg(contant,mNum):
    result = mDAO.reply_reg(contant,mNum)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/mainmemo.get")
def mainMget(p,search,dI, dF):
    result = mDAO.get(p,search,dI, dF)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/memodetail.get")
def mainMgetNum(no):
    result = mDAO.numS(no)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/mainmemo.get")
def mainMget(p,search,dI, dF):
    result = mDAO.get(p,search,dI, dF)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/mainmemo.get")
def mainMget(p,search,dI, dF):
    result = mDAO.get(p,search,dI, dF)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)



