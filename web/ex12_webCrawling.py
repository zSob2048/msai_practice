# web crawling(scraping)
# 넓은 의미 : 걍 웹 데이터 긁어오면 전부
# 좁은 의미 : 웹 사이트에서 HTML파싱



from http.client import HTTPConnection, HTTPSConnection

from bs4 import BeautifulSoup
from pymongo import MongoClient


# hc = HTTPConnection("195.168.9.153")

# hc.request("GET","/review.html")
# res = hc.getresponse().read()

# hc.close()

# data_mine = BeautifulSoup(res,"html.parser", from_encoding="utf-8") # 받아온 데이터, 내장 파서 이름(고정), 인코딩
# data__= data_mine.select(".aReview") # CSS선택자
# for r in data__:
#     print(r.select("td")[3].text)


hc = HTTPSConnection("news.daum.net")
hc.request("GET","/")
res = hc.getresponse().read()
# print(res)
hc.close

con = MongoClient("195.168.9.155")
db = con.product

news_data = BeautifulSoup(res,"html.parser", from_encoding="utf-8")
news = news_data.select(".item_newsheadline2 .tit_txt")
for r in news:
    db.neverNews.insert_one({"txt":r.text})

con.close()