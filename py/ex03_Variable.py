# variable 변수; 데이터를 임시로 저장하는 공간
# 변수 명 = 데이터 형태로 정의


#  a=10 #8byte byte를 따지면 정렬이 필요하지 않지만 pc의 성능 증가로 별 차이 없음
a = 10  # 12byte

print("a")
print(a)
# "aaaa" : 글자 데이터
# aaaa: python 문법

# 변수명으로
#     기존 문법명 사용 불가
#     숫자로 시작 불가
#     특수문자불가(일부제외) ; 언더바 가능> 언더바로 시작하는 변수 가능
# 통상적으로 한글 자제 / 뜻은 통하게(길어도 됨, 최대한 상세하게) / 대문자 시작 자제

# 변수 국룰
# restaurantTableCount ; 낙타체 (띄어쓰기 위치에 대문자)
# restaurant_table_count ; 뱀체 (띄어쓰기 위치에 언더바) : Python에서 선호


# 정수형 데이터
# 식당 테이블 수 10이라는 데이터
rest_table_tot = 10
# 출력
print(rest_table_tot)

# 실수형 데이터
# 식당 별점이 4.3이라는 데이터
rest_star = 4.3
print(rest_star)

# 글자 데이터
# 식당 이른이 김밥천국종로점 이라는 데이터
rest_name = "김밥천국종로점"
print(rest_name)

# 논리형 데이터 (T/F)
# 식당 영업중(T)
rest_open = True # or False
print(rest_open)

#################################################
# Data type

# 자료형 data type
#   str     : 문자
#   int     : 정수
#   float   : 실수
#   bool    : 논리
#       > 기본 자료형 4종
#           >>python의 경우 자동 분류 but 언어에 따라 직접 지정해줘야함 (ex. java의 경우 int a = 10, float b = 2.3 ... )

# 핸드폰 모델명
# 폰 번호
# 폰 가격
# 폰 화면크기
# 폰 충전상태(100?)

phone_model = "S23FE"
phone_num = "010-5851-3840"
phone_price = 800000
phone_display = 163.1
phone_energy = False

print(type(phone_model))
print(type(phone_num))
print(type(phone_price))
print(type(phone_display))
print(type(phone_energy))

# >> 터미널
# <class 'str'>
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>

# 과자 이름이 다이제 미니
# 자료형
# 과자이름 출력

# 과자 가격이 5000원
# 자료형
# 과자가격 출력

#################################################
# Memory

cookie_name = "다이제미니"
cookie_price = 5000

print(id(cookie_name)) # id: 메모리 위치
print(type(cookie_name))
print(cookie_name)

print("--")

print(id(cookie_price))
print(type(cookie_price))
print(cookie_price)
