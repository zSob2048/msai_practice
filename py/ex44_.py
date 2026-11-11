

















# #############################################

# # ClientID : YOUR_NAVER_ID
# # ClientSecret: YOUR_NAVER_SECRET

# # https://developers.naver.com/ 로그인
 
# # 애플리케이션 등록
# #   애플리케이션 이름 : 마음대로
# #   사용API : 검색
# #   비로그인... : WEB설정 -> 웹사이트 주소 아는거 아무거나
# # ClientID : YOUR_NAVER_ID
# # ClientSecret: YOUR_NAVER_SECRET
 
# # Documents - 서비스API - 검색
 
# # request parameter
# #   클라이언트가 서버에게 전달하는 정보
# #   주소 뒤에
# # request header
# #   클라이언트가 서버에게 전달하는 정보
# #   내부적으로
 
 
# # 인터넷 주소 체계
# #   프로토콜://서버주소[:포트번호]/폴더/.../파일
# #   ?
# #   변수명=값&변수명=값&변수명=값...
 
# # 인터넷 주소에 한글,특수문자x
# #   ㅋ -> %2A(URL인코딩)
 
# # 실시간 네이버 뉴스를 AI훈련용 데이터로 확보하는 프로그램
# # 1) HTTP통신해서 콘솔출력
# # 2) 파싱 -> title, description -> 콘솔출력
# # 3) 날짜, title, description -> 파일에
# ####################################
# from datetime import datetime
# from http.client import HTTPSConnection
# from urllib.parse import quote
# from xml.etree.ElementTree import fromstring
# from kwon.kwonStringCleaner import KwonStringCleaner
 
# q = "야구"
# q = quote(q)  # ㅋ -> %2A
 
# k = {"X-Naver-Client-Id": "YOUR_NAVER_ID", "X-Naver-Client-Secret": "YOUR_NAVER_SECRET"}
 
# hc = HTTPSConnection("openapi.naver.com")
# hc.request("GET", "/v1/search/news.xml?query=" + q, headers=k)
# res = hc.getresponse()
# resBody = res.read()
# hc.close()
# ###################################
# f = open("C:/Kwon/naverNews.txt", "a", encoding="utf-8")
# newsData = fromstring(resBody)
# news = newsData.iter("item")
# now = datetime.today()
# now = datetime.strftime(now, "%Y\t%m\t%d\t%H\t%M")
 
# for n in news:
#     title = KwonStringCleaner.clean(n.find("title").text)
#     desc = KwonStringCleaner.clean(n.find("description").text)
#     data = "%s\t%s\t%s\n" % (now, title, desc)
#     f.write(data)
 
# f.close()