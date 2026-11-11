from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from pymongo import MongoClient

# get으로 데이터가 안나올때(웹들어감 보여주긴 하는데 ret은안됨)
# selenium ; Python HTML 파싱 라이브러리 인데 웹브라우저 매크로도 지원함
# >> 크롬 연동용 드라이버가 필요했.... 었는데 이제 ㄱㅊ

driver = webdriver.Chrome()
driver.get("https://www.melon.com/chart/index.htm")

# driver.execute_script("JavaScript소스") 로 이거저거 할 수 있음
_as = driver.find_elements(By.CSS_SELECTOR,".rank01 span a")

for a in _as:
    print(a.text)

# con = MongoClient("195.168.9.155")
# db = con.product

# chart_data = BeautifulSoup(res,"html.parser", from_encoding="utf-8")
# chart = chart_data.select(".wrap")
# for r in chart:
#     # db.neverchart.insert_one({"txt":r.text})
#     print(r)

# # con.close()