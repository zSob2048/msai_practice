# 이름이 보드마카
# 가격이 500원

_name = "보드마카"
_price = 500
_length = 15.456
# _color = False
_humidity=40.345

# 이름 자료형/주소값 >지워도됨
print(type(_name))
print(id(_name))

# 이름 줄력
# 가격 출력
print(_name)
print(_price)
# > ,를 사용 : 띄어쓰기로 보여줌
print(_name, _price)  # python에서만 사용

print("품명 :", _name, ", 가격 :", _price, "원")

# 형식을 지정해서 출력
# % 문법
print("품명: %s." % _name)  # %s : str문자 데이터
print("가격: %d원." % _price)  # %d : 정수 데이터(decimal;10진법)
print("가격: %06d원." % _price)  # %0nd : 자릿수 지정 가능(무조건 n자리로)
print("길이: %fcm." % _length)  # %f : 실수 데이터(flot)
print("길이: %.2fcm." % _length)  # %.nf : 소숫점 아래 n자리만(반올림)
# print("색상: %b." % _color,)  # %b : 논리형 데이터 ; python에 존재하지않음......

# printf("품명: %s." , _name) 다른 언어는 ,로 사용

print("품명: %s, 가격: %d원." % (_name, _price))

# 습도는 40.3%입니다.
print("습도는 %.1f%%입니다." % _humidity) # %% = %

