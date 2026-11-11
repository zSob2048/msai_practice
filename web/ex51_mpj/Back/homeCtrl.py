
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from seller.sellerDAO import SellerDAO
from product.productDAO import ProductDAO


app = FastAPI()
sDAO = SellerDAO()
pDAO = ProductDAO()

@app.get("/seller.reg")
def sellerReg(name,bday,addr):
    result = sDAO.reg(name,bday,addr)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/seller.get")
def sellerGet(page,searchkey):
    result = sDAO.get(page,searchkey)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/seller.ids")
def sellerNumSearch(no):
    result = sDAO.NumS(no)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)


@app.get("/seller.upd")
def sellerUpdate(no,name,addr):
    result = sDAO.update(no,name,addr)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/seller.del")
def sellerDelete(no):
    result = sDAO.delete(no)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)



@app.get("/product.reg")
def productReg(name,price,stock,c_no):
    result = pDAO.reg(name,price,stock,c_no)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/product.get")
def productGet(page,searchkey):
    result = pDAO.get(page,searchkey)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/product.ids")
def productNumSearch(no):
    result = pDAO.NumS(no)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/product.upd")
def productUpdate(no,name,pric,stoc):
    result = pDAO.update(no,name,pric,stoc)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)

@app.get("/product.del")
def productDelete(no):
    result = pDAO.delete(no)
    h = {"Access-Control-Allow-Origin":"*"}
    return JSONResponse(result,headers=h)
