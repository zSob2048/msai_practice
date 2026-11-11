# Django > 클래식 웹에 적합

##
# 클래식 웹(Java>Spring , Python>Django)
#   back-end(FastAPI)
#       프로그램 작업 전부 > 서버에 부담
#       HTML+CSS+JS 만들어서 응답 > 작업 불편
#   front-end(JavaScript)
#       유효성검사 + 약간의 효과

# 신형 웹
#   back-end(FastAPI)
#       DB관련작업만 (JS와 연동 불가한부분만) > XML/JSON
#   front-end(JavaScript)
#       프로그램 작업을 여기서 > 서버 부담 감소 > AJAX

# 결과를 HTML모양으로 보내주자>XML
# 어차피 활용하는건 JS인데?> JSON

from fastapi import FastAPI, Response


app = FastAPI()

@app.get("/xmll.testt")
def xmlTest():
    xml = '<?xml version="1.0" encoding="UTF-8"?>' \
    '<snacks>' \
    '<snack>' \
    '<s_name>초코파이</s_name>' \
    '<s_price>5000</s_price>' \
    '</snack>' \
    '<snack>' \
    '<s_name>마이쮸</s_name>' \
    '<s_price>500</s_price>' \
    '</snack>' \
    '</snacks>'
    return Response(xml, media_type="application/xml")

@app.get("/jsonn.testt")
def jsonTest():
    json = [
        {"s_name":"초코파이","s_price":"5000"},
        {"s_name":"마이쮸","s_price":"500"}
    ]
    return json