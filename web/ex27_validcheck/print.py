from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()
@app.get("/product.reg")
def productreg(name: str, price: int):
    html = '<html><head><meta charset="utf-8"></head><body>' \
    '<h1>품명 : %s</h1> ' \
    '<h1>가격 : %s</h1> ' \
    '</body></html>' % (name, price)
    return HTMLResponse(html)
    