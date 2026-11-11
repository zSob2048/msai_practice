# Flask   : 자체 WAS기능 포함 > 단독실행
#           응답형태 자유
# FastAPI : 포함은 되어있으나 주로 uvicorn에서 실행
#           기본 JSON응답

# cmd
# pip install fastapi
# pip install uvicorn[standard]

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get("/a.b")
def test():
    return {"a":"b"}

@app.get("/html.test")
def html_test():
    html = "<html><head><meta charset='utf-8'></head><body>"
    html += "내용내용내용내용"
    html += "</body></html>"
    return HTMLResponse(html)

@app.get("/det.calculate")
def xplusy(x:int,y:int):
    html = "<html><head><meta charset='utf-8'></head><body>"
    html += "%d" %(x+y)
    html += "</body></html>"
    return HTMLResponse(html)

@app.post("/post.calculate")
def xplusy(x:int=Form(),y:int=Form()):
    html = "<html><head><meta charset='utf-8'></head><body>"
    html += "%d" %(x+y)
    html += "</body></html>"
    return HTMLResponse(html)
# >> post방식 reqParam 받으려면
# pip install python-multipart