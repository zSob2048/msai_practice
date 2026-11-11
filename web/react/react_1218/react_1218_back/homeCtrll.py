from fastapi import FastAPI, Form

from calculator.calculator import Calculator


app=FastAPI()
c=Calculator()

@app.get("/get.asmd")
def calcultateg(x:int,y:int):
    return c.operatee(x,y)

@app.post("/post.asmd")
def calcultatep(x:int=Form(),y:int=Form()):
    return c.operatee(x,y)

@app.post("/upgpost.asmd")
def calcultatepu(x:int=Form(),y:int=Form()):
    return c.operateupg(x,y)