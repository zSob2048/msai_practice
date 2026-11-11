from fastapi import FastAPI, Form, UploadFile

from fileeee.fileupp import FileUpSimul


app=FastAPI()
s = FileUpSimul()

@app.post("/fi.le")
async def fileUpp(img: UploadFile,title:str=Form()):
    return await s.uppppp(img,title)

@app.get("/fi.leb")
def fileB(fileN):
    return s.backkk(fileN)

###########################################

@app.post("/ipi.up")
async def regg(img: UploadFile,id:str=Form(),pw:str=Form(),txt:str=Form()):
    return await s.regDB(id,pw,txt,img)

@app.get("/get.pim")
def rPimg(imgn):
    return s.rPimg(imgn)

@app.get("/get.post")
def gett(page,txt):
    return s.getDB(page,txt)

@app.get("/delete.post")
def dell(id,imgn):
    return s.delete(id,imgn)