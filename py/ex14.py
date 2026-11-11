# 비만도 검사 프로그램
# 이름: (입력)
# 키: (입력)
# 몸무게: (입력)
# ---
# BMI:
# (이름) 은 (상태)


from time import sleep


name_ = input("이름       :")
print(" ** 아래 입력 시 단위 제외 숫자만 입력해주세요. ** ")
hight_ = float(input("키    (cm) :"))
mass_ = float(input("몸무게(kg) :"))
print("---")
bmi_ = mass_ / (hight_ / 100) ** 2
print("BMI(kg/m²): %.2f" % bmi_)

# # 소스 길다> 프로그램 용량 증가> HDD 사용량 증가
if bmi_ >= 39:
    print("%s씨는 고도 비만" % name_)
elif bmi_ >= 32:
    print("%s씨는 중도 비만" % name_)
elif bmi_ >= 30:
    print("%s씨는 경도 비만" % name_)
elif bmi_ >= 24:
    print("%s씨는 과체중" % name_)
elif bmi_ >= 10:
    print("%s씨는 정상" % name_)
else:
    print("%s씨는 저체중" % name_)

# # # 변수 할당> RAM 사용량 증가
# result_ = "저체중"
# if bmi_ >= 39:
#     result_="고도 비만"
# elif bmi_ >= 32:
#     result_="중도 비만"
# elif bmi_ >= 30:
#     result_="경도 비만"
# elif bmi_ >= 24:
#     result_="과체중"
# elif bmi_ >= 10:
#     result_="정상"
#     # else로 끝날 필요 X( if에 else는 필수가 아님 )

# print("%s씨는 %s" % (name_,result_))

sleep(10)

# 실행파일...
#    .bat : cmd 명령어 써놓는 파일, 메모장에도 상관 X
#    pyinstaller : 추후 확인