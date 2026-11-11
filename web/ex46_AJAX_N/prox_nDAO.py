from http.client import HTTPSConnection
from urllib.parse import quote

class NShopDAO:
    def nShopData(self,q):# q = "가습기"
        q = quote(q)
        h = {"X-Naver-Client-Id":"","X-Naver-Client-Secret":""}

        huc = HTTPSConnection("openapi.naver.com")
        huc.request("GET","/v1/search/shop.xml?query="+q, headers=h)
        resBody = huc.getresponse().read()
        huc.close()
        return resBody
