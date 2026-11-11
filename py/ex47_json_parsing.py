# 데이터를 특정 형식으로 표현..
# HTML모양으로 > XML
# JavaScript모양으로> JSON

# JSON(JavaScript Object Notation)
# 요즘 대부분... 
# 가독성은 xml이 좀 더 나을지도... (각종 설정파일은 여전히 xml이 쓰임)
# but 나머지는 json이 굿

# JavaScript객체 : { 멤버변수명: 값. 멤버변수명: 값, ...} >> Python dict
# JavaScript배열 : [값, 값, ...] >> Python list

# https://api.openweathermap.org/data/2.5/weather
# ?
# 주소에 설명 떠있음 좌표적어주시술? 하는것
# lat={lat}
# &lon={lon}
# 대신 q=도시
# &appid={API key}
# baff8f3c6cbc28a4024e336599de28c4
# >> https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4


from http.client import HTTPSConnection
from json import loads


hc = HTTPSConnection("api.openweathermap.org")
hc.request("GET", "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4")
res_body = hc.getresponse().read()
# print(res_body.decode())
hc.close()

weather_data= loads(res_body) # JSON > Python 컬렉션으로
# weather_data["coord"]["lon"]
