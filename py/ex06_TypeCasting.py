# type casting 형변환 : 자료형 변환

# 폰 모델명 입력받기
# 출력

phone_model = input("기종을 입력하세요.")
print("기종: %s" % phone_model)

# 변수 주소값
# 변수 자료형
print("주소값: %d, 자료형: %s" % (id(phone_model), type(phone_model)))

print("--")

phone_price = input("가격을 입력해주세요.")
print("가격: %s" % phone_price)  # python의 경우 input 변수는 자동으로 string으로 잡아줌

# 변수 주소값
# 변수 자료형
print("주소값: %d, 자료형: %s" % (id(phone_price), type(phone_price)))

# > 자료형(변수명)으로 작성
phone_price = int(phone_price)
print("주소값: %d, 자료형: %s" % (id(phone_price), type(phone_price)))

# 화면 크기 입력
# 소수점 이하 2자리로 출력
phone_display = input("화면 크기:")
phone_display = float(phone_display)
print("크기: %.2f mm" %phone_display)

# 한번에 작성해 소스 줄이기...
phone_display = float(input("화면 크기:"))
print("크기: %.2f mm" % phone_display)
# 변수 >안쓰는게 이득; 메모리 사용량
# 소스 >짧으면 좋음; 프로그램 용량
