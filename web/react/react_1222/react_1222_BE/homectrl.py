from fastapi import FastAPI

from lDAO import LDAO


app = FastAPI()
i = LDAO()

@app.get("/c.a")
def tst(id,pw):
    return i.reg(id,pw)

@app.get("/c.b")
def tst(jwt):
    return i.decodd(jwt)

@app.get("/c.d")
def tet(jwt):
    return i.udateexp(jwt)