from typing import Optional
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse



app = FastAPI()


@app.post("/input.test")
def signUp(id:str=Form(),pw:str=Form(),select1:str=Form(),select2:str=Form()
           ,select3:Optional[list[str]]=Form(None),freeSp:str=Form): # checkbox형 다수선택의 경우 : List로
    # id:str=Form("a") >> a가 기본값
    html = "<html><head><meta charset='utf-8'></head><body>"
    html += "%s, %s," %(id , pw)
    html += "%s, %s" %(select1,select2)
    if select3 != None:
        html += "<h1>3선택지<h1>"
        for s in select3:
            html += s + ", "
        html += "<br>"
    freeSp = freeSp.replace("\r\n","<br>") # html에서 사용시 변환
    html += freeSp + "<br>"
    
    html += "</body></html>"
    return HTMLResponse(html)