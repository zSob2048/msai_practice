# deprecated
# 너무얫날에만들어서지금은정상작동을안함
# 담버전갈때다시만들예정이든업그레이드를하든삭제를하든할테니까남겨두긴했는데쓰디마~

from datetime import datetime


now = datetime.today() # now()
print(now)

# 패키지명: 업듬(하든말든)
# 모듈명: datetime.py (from ~ )
# 클래스명: datetime (import ~ )
# today()의 정체: static메소드
# >> class datetime: @staticmethod def today() 으쩌그...
print(now.year)
print(now.month)
print(now.day)

d = datetime(2000,1,1)
print(d)

# 날짜 yyyy/mm/dd 로 받고 dattetime으로
# d2 = input("yyyy/mm/dd : ")
# yyyy ,mm ,dd = int(d2.split("/")[0]),int(d2.split("/")[1]),int(d2.split("/")[2])
# d2 = datetime(yyyy,mm,dd)
# print(d2)

d3 = "2000/04/15"
d3 = datetime.strptime(d3,"%Y/%m/%d")
print(d3)

d4 = datetime.today()
d4 = datetime.strftime(d4,"%Y.%m.%d %H:%M:%S")
help(datetime)
print(d4)