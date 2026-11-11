# 연산자 Operator

# x ,y: input int
# prt x = , y=
x = int(input("임의의 정수 x:"))
y = int(input("임의의 정수 y:"))

print("---")
print("x=%d, y=%d" % (x, y))

# x = y   #  대입연산자, 우항을 좌항에 대입
#         #  우선순위가 가장 낮음
# x + y   #  사 
# x - y   #  칙
# x * y   #  연
# x / y   #  산
#         #  산술연산자. 못할시할복
# x % y   #  x mod(y)
# x ** y  #  x^y


# x(str) + y(str)   문자열도 덧셈 가능(붙여줌)
# x(int) + y(str)   숫자열+문자열 불가능 (python만 불가능...)
# x(str) + y(int)   문자열*숫자열 가능(반복) (python만 가능...)
# x(int) + y(int)   소숫점 이하까지 계산함(python만, 이외에선 정수계에 닫혀있음)
#                    >> x // y ; 정수계에 닫혀있는 나눗셈 (python 한정)

# 반복/축약형
# a += k # a = a + k
# a -= k # a = a - k
# a *= k # a = a * k
# a /= k # a = a / k
# a %= k # a = a % k

# Python에 없는 추가 축약형
# a++ # a += 1
# a-- # a -= 1

#################################################

# 자전거 ; 앞바퀴 뒷바퀴 사이즈 동일> 바퀴둘레 : (입력)
# 앞 기어 톱니 수 :
# 뒷 기어 톱니 수 :
# 발 구른 횟수 :
# ---
# 총 이동거리 :

print(" ** 아래 입력 시 단위 제외 숫자만 입력해주세요. ** ")
wheel = float(input("자전거 바퀴 둘레(cm) : "))
f_gear = int(input("앞 기어 톱니 수(개) : "))
b_gear = int(input("뒷 기어 톱니 수(개) : "))
rotation = float(input("발 구른 횟수(회) : "))

length_cm = float(wheel * rotation * f_gear / b_gear)
length_m = length_cm / 100

print(" 총 이동거리 : %.2f (cm)" %length_cm)
print(" 총 이동거리 : %.2f (m)" %length_m)

# 구매한 물건 가격 :
# 낸 돈 :
# ----
# 거스름돈 :

price = int(input("물품 가격: "))
price_input = int(input("지불한 가격: "))
print("---")

price_out = price_input - price
print("거스름돈: %s원" % price_out)
price_ = (50000, 10000, 5000, 1000, 500, 100)
for i in price_:
    price_output = price_out // i
    print("%s원 : %d 장" % (i, price_output))
    price_out %= i


#################################################

# << left-shift 연산자
# >> right-shift 연산자
# a를 2진수로 바꾼 뒤 b회 왼/오른쪽으로(빈자리에 0) ( 이후 10진수출력 )

a = 2
b = 3
print(a << b, a >> b)  # 16,0

# 글자 속성 {
#     이텔릭  1<<0
#     볼드    1<<1
#     언더바  1<<2
# }
# 속성 = 5
# 속성 = 3
# 속성 = (1<<0) + (1<<2)
# 속성 = 이텔릭 + 볼드
# ... 등 다중선택의 경우 사용...

# 놀이공원
# 키:
# 나이:
# ---
# 키는 어쩌고, 나이는 뭐시기살

# name = input("이름: ")
# hight = float(input("키(cm): "))
# year = int(input("나이(세): "))
name = "홍길동"
hight = 160
year = 2
# print("키: %.1fcm, 나이: %d세." % (hight, year))

# 논리 연산자 : 결과로 T/F
# 초과> 이상>= 같다== 다르다!= 이하<= 미만<

# a는 키가 130초과 가능
a = hight > 130
# b는 나이가 10살 미만
# c는 키가 120이하
b = year < 10
# b = 10 < year # 상관 없... 지만 그냥 위가 더 커여움
c = hight <= 120
# c = (hight <= 120) # 등호 들어갈때 가독성문제 안해도됨

# d는 나이가 5살이어야만
d = year == 5
# e는 나이가 10살이 아니어야
e = year != 10
# f는 나이가 홀수
f = (year % 2) == 1
# g는 이름이 홍길동
g = name == "홍길동"
# 자바에선 같다가 않됨 외죠 >> stack에 저장안됨 string > 스텍+heap 참조식으로 나옴 >> 연산자의 경우 스택영역이 대상>> 참조안됨...
# >> python에서만 그냥 나옴; python의 경우 모든 데이터가 다 heap이라... 대충 뭐 됨

#            ∧       ∨      ~     xor ( a~=b )
# 다른 언어> &&, &    ||, |   !     ^
# Py>        and, &   or, |   not   ^
# && / &, || / | 차이> A B명제를 둘다 판단하는지(&,|) 스킵하는지(&&,||)

# h는 키가 100 이상이고 나이가 80 이상
# i는 나이가 90이상이거나 키가 80 이상
# j는 i의 반대
# k는 나이가 100 이상 이든지 키가 100 이상이든지 *둘중 하나만*

# h = hight >= 100 and year >= 80
h = (
    year >= 80 and hight >= 100
)  # > 앞쪽을 먼저 연산 > 앞쪽에 F조건을 두면 검사횟수 down > 속도의 차이...
# i = year >= 90 or hight >= 80
i = hight >= 80 or year >= 90  # > 앞쪽에 T조건을 두면 ...
j = not i
# k = year >= 100 != hight >= 100
k = year >= 100 ^ hight >= 100

# l은 나이 20미만 or 나이 80초과
# m은 10<=나이<=30
# n은 나이가 10넘고 50넘고
l = year < 20 or year > 80
m = 10 <= year <= 30 # python 아니면 and써야댐~
n = year >= 50

# 단항연산 : not
# 2항연산 : 나머지대브븐
# 3항연산 : (조건식) ? true일때 값 : False일때 값> 조건따져서 변수값넣을때 3개들어가면 3항
# 근데python에없음
