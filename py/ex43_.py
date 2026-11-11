# 미세먼지
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring


hc = HTTPConnection("openapi.seoul.go.kr:8088")
hc.request("GET","/YOUR_SEOUL_API_KEY/xml/RealtimeCityAir/1/5/")
# 사이트에 메뉴얼 있음 (주소 맨 뒷부분이 권역, 1~25)
res = hc.getresponse()
resBody = res.read()
# print(resBody.decode())
hc.close()

# XML(eXtended Markup Language)
# : 데이터를 HTML모양으로 표현해둠
# DOM(Document Object Model)객체
#   <tag_name attribute="value"> text </tag_name>
#    start tag                          end tag          

seoul_dust_data = fromstring(resBody)
rows = seoul_dust_data.iter("row")  # <row> 단위로... 여러개 찾을때
for r in rows:
    r.find("MSRRGN_NM") # 1개 찾을땐 find

## 1103-1  59:43 

# #############################################

# # 실행하면 실시간 서울 미세먼지를 csv에 저장
# # 2025,11,03,10,52,도심권,중구,10,5,좋음
# # 2025,11,03,10,52,도심권,종로구,20,3,좋음
# # ...
# from datetime import datetime
# from http.client import HTTPConnection
# from time import strftime
# from xml.etree.ElementTree import fromstring
 
# hc = HTTPConnection("openapi.seoul.go.kr:8088")
# hc.request("GET", "/YOUR_SEOUL_API_KEY/xml/RealtimeCityAir/1/25/")
# res = hc.getresponse()
# resBody = res.read()
# hc.close()
# #######################
# now = datetime.today()
# now = datetime.strftime(now, "%Y,%m,%d,%H,%M")
 
# f = open("C:/Kwon/seoulDust.csv", "a", encoding="utf-8")
# seoulDustDataa = fromstring(resBody)
# rowsss = seoulDustDataa.iter("row")
# for r in rowsss:
#     msrrgn_nm = r.find("MSRRGN_NM").text
#     msrste_nm = r.find("MSRSTE_NM").text
#     pm10 = r.find("PM10").text
#     pm25 = r.find("PM25").text
#     idex_nm = r.find("IDEX_NM").text
#     data = "%s,%s,%s,%s,%s,%s\n" % (now, msrrgn_nm, msrste_nm, pm10, pm25, idex_nm)
#     f.write(data)
 
# f.close()