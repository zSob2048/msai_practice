# 셍년월일 yyyy/mm/dd > 요일 나이

from datetime import datetime


day = "2000/04/15"
day = datetime.strptime(day,"%Y/%m/%d")
_yoile = ["월","화","수","목","금","토","일"]
print(_yoile[datetime.weekday(day)])
# help(datetime)
print(datetime.today().year - day.year +1)

birth_y = int(day[0:4])
age = datetime.today().year - birth_y +1
yoil = datetime.strftime(day,"%A") # 요일!
