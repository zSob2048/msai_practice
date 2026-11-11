from fastapi import FastAPI, Form, UploadFile
from fastapi.responses import JSONResponse

from member.memberDAO import MemberDAO

app=FastAPI()
mDAO=MemberDAO()
hAll = {"Access-Control-Allow-Origin":"*"}
hLocal = {"Access-Control-Allow-Origin":"http://localhost:5173", "Access-Control-Allow-Credentials":"true"}


@app.get("/member.idcheck")
def idCheck(id):
    return JSONResponse(mDAO.idCheck(id),headers=hAll)

@app.post("/member.sign.up")
async def signUp(
    photo:UploadFile, 
    id:str=Form(), 
    pw:str=Form(), 
    name:str=Form(), 
    addr:str=Form(), 
    bday:str=Form(), 
    tel:str=Form()
    ):
    result = await  mDAO.signUp(photo,id, pw,name,addr,bday,tel)
    return JSONResponse( result , headers=hLocal)

@app.post("/member.signup")
def signUpNp(
    id:str=Form(), 
    pw:str=Form(), 
    name:str=Form(), 
    addr:str=Form(), 
    bday:str=Form(), 
    tel:str=Form()
    ):
    return  JSONResponse( mDAO.signUpNp(id, pw,name,addr,bday,tel) , headers=hLocal)

@app.post("/member.login")
def login(id:str=Form(),pw:str=Form()):
    return JSONResponse( mDAO.login(id,pw), headers=hLocal)

@app.get("/member.info")
def infoGet(memberInfo):
    return JSONResponse(mDAO.memberInfoGet(memberInfo),headers=hAll)

@app.get("/member.info.r")
def infoGetR(memberInfo):
    return  JSONResponse(mDAO.memberInfoGetR(memberInfo),headers=hAll)

@app.get("/member.photo")
def photoGet(photo):
    return mDAO.photoGet(photo)
