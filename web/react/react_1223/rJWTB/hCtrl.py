from fastapi import FastAPI

from iptDAO import IptDAO


app=FastAPI()
ii = IptDAO()

@app.get("/t.s")
def test(ipt1,ipt2):
    return ii.reg(ipt1,ipt2)

@app.get("/t.e")
def test(jwt):
    return ii.decodd(jwt)