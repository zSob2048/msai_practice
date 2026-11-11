# server : 서비스를 제공하는 콤퓨타
# client : 서비스를 이용하는 콤퓨타

# Socket 통신 : 실시간(카톡 등)
#   Socket 서버 - Node.js :웹소켓서버구현특화
#   Socket 클라이언트 - JavaScript/React
# HTTP 통신 : 안실시간(페이지로있는...)
#   HTTP 서버 - Flask/FastAPI
#   HTTP 클라이언트 - ... 받아와서 훈련용 데이터로... (py) // AI 결과 받아 웹에 띄우자... (JavaScript/React)

# protocol 프로토콜(통신방식)
# ip주소 (어느 주소로 걸고받을지...)
# Domain namw (ip대신 알아볼수있게... www.어쩌고)
# port 번호 (서비스 구분 번호)

# 기상청에서... 하단의 RSS
# http://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20251030.xml 
# https://www.kma.go.kr/repositary/xml/fct/mon/img/fct_mon1rss_108_20251030.xml

# HTTP 통신
#   protocol : http or https(요즘쓴는거, 좀더보안이ㄱㅊ은버전.)
#   ip : ??
#   domain : www.kma.go.kr
#   port번호 : 기본번호면 생략가능, 기본아니면 : # 식으로 마지막에...
#           http  - 80번이 기본
#           https - 443번이 기본
#   뒷부분은...? : >> 폴더명/파일명임

# python에서 http통신방법은 다양함... 그중1나
from http.client import HTTPSConnection


hc = HTTPSConnection("www.kma.go.kr") # (ip주소or도메인 , port번호(기본값생략댐))

hc.request("GET","/repositary/xml/fct/mon/img/fct_mon1rss_108_20251030.xml") # 통신 요청(GET/POST), 주소 남은부분
res = hc.getresponse() # 응답
res_main = res.read() # 응답내용(핵심부분)
print(res_main.decode()) # .decode() >> 한글처리

hc.close() # 접속끊기 ; 안해도되지만 해주는게좋음

# 국제 표준 데이터 형식
# XML  : 데이터를 HTML모양으로 표현
# JSON : 데이터를 JavaScript모양으로 표현
# Python에 가공기능 있듬!!

# parsing : 데이터에서 필요없는 부분을 날리고 필여한부분만 추출