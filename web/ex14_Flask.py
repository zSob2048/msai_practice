# Web Server
#   HTML을 올려놓으면 클라이언트가 요청했을때 HTML 응답
# WAS(Web Application Server)
#   Web Server + 프로그램 실행되는 


# Flask
#   Python WAS 라이브러리
# cmd
# pip install flask

# HTTP통신 : 클라이언트가 서버에 요청하면 서버가 응답
# get  > 주소 직접 쳐서 접속,  <a>
# 변수가 주소에
# post > <form action method="post"> + input + button 
# : action에 써놓은 쪽으로 input값 넣어서 요청 날림
# 또는 프로그램을 통해서만
# 변수가 내부적으로 전달됨(주소에 ㄴㄴ >보안성 높음) : 로그인같은때

# 일반적으로 get방식(웹기준)



from flask import Flask, request


app = Flask(__name__)

# 요청
@app.get("/te.st") 
def test():
    return "abcd"

@app.get("/html.test")
def html_test():
    html = "<html><head><meta charset='utf-8'></head><body>"
    html += "내용내용내용내용"
    html += "</body></html>"
    return html

@app.get("/det.calculate")
def xplusy():
    x=int(request.args.get("x"))
    y=int(request.args.get("y"))
    html = "<html><head><meta charset='utf-8'></head><body>"
    html += "%d" %(x+y)
    html += "</body></html>"
    return html

@app.post("/post.calculate")
def xplusy():
    x=int(request.form["x"])
    y=int(request.form["y"])
    html = "<html><head><meta charset='utf-8'></head><body>"
    html += "%d" %(x+y)
    html += "</body></html>"
    return html


if __name__ == "__main__":
    # 접속 허용 주소(특정IP > 이 IP만 접속 가능/0.0.0.0 > 전부다)
    # 포트번호 : WAS마다 부여가능 (지금은 맘대로, 이 포트로 접속하면 flask하러 접속한다는 의미 > 실전에선 80)
    # 디버그모드(로그출력, 설정변경시 자동 재시작) 여부(True> 로그찍히고 자동재시작됨)
    app.run("0.0.0.0", 2048, True)

