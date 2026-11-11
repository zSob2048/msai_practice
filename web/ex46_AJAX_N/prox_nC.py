

from fastapi import FastAPI, Response

from web.ex46_AJAX_N.prox_nDAO import NShopDAO


app = FastAPI()
nsD = NShopDAO()

@app.get("/n.shop")
def nsd(q:str):
    h = {"Access-Control-Allow-Origin":"*"}
    return Response(nsD.nShopData(q), media_type="application/xml", headers=h)
    