# 숫자 넣으면 Σ k
def serise(k):
    if k == 1:
        return 1
    else:
        return serise(k - 1) + k


print(serise(10))

# 오오 점화식
# 재귀적 호출 recursive call


# 점화식 이어서


# !
def factorial(n):
    if n == 1:
        return 1
    # else:
    # return factorial(n - 1) * n
    return factorial(n - 1) * n  # ; return이 함수 종료> 1인경우 #7줄을 연산하지 않음


print(factorial(10))


# a_n= a_n-1 + a_n-2
def fibonacci_r(n):
    if n <= 2:
        return 1
    return fibonacci_r(n - 2) + fibonacci_r(n - 1)


def fibonacci_g(n):
    return (((1 + 5 ** (1 / 2)) / 2) ** n - ((1 - 5 ** (1 / 2)) / 2) ** n) / 5 ** (
        1 / 2
    )


# print(fibonacci_r(50)) ## 숫자가 커지면 = 반복이 늘어나면... 연산속도 현저히 저하
print(fibonacci_g(50))

# 재귀가 아니더라도 ...  함수를 사용시 속도 저하(점프연산)
# 계산문제는 반복문이 더 빠르다...

# 짝수 : (입력)
# ---
# 입력한 짝수는 2n ; 단, 짝수 이외 입력시 에러 후 **재입력 요청** 
def even_input():
    n = int(input("짝수:"))
    if n % 2 == 0:
        return n
    print(" 짝수를 입력하세요. ")
    return even_input()


print("---\n입력한 숫자는 %d" % even_input())

# >> 속도를 신경쓰는 환경이 아닌/반복이 다수가 아닌 경우 사용

name_ = input("이름       :")
print(" ** 아래 입력 시 단위 제외 숫자만 입력해주세요. ** ")
def hight_():
    h = float(input("키    (cm) :"))
    if h>10:
        return h
    print("단위를 확인하세요.")
    return hight_()
hight_ = hight_()
mass_ = float(input("몸무게(kg) :")) # 정리 일관성을 위해 만들도록
bmi_ = mass_ / (hight_ / 100) ** 2
print("---\nBMI(kg/m²): %.2f" % bmi_)

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
