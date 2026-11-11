from fastapi import FastAPI

from snack.snackDAO import SnackDAO


app = FastAPI()
sDAO = SnackDAO

@app.get("/snackk.regg")
def snackReg(n:str,p:int):
    sDAO.reg(n,p)

@app.get("/snackk.gett")
def snackGet():
    sDAO.get()