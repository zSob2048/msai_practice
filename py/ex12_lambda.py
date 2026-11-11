# lambda 함수 : 무명의 1회용 함수
# (lambda param변수명, param변수명, ... : 내용)(값)
# 람다대수의 그거...? 익명함수...?


# 자기 이름 출력하는 함수
# 사용
# 일반함수 ver.
def name_print(n):
    print(n)


name_print("자기이름")

# 람다함수 ver.
(lambda n: print(n))("자기이름")


# 숫자 3개 넣으면 그 평균값...
# 일반함수 ver.
def min_triple(a=0, b=0, c=0):
    return (a + b + c) / 3


print(min_triple(10, 20, 55))

# 람다함수 ver.
print((lambda a, b, c: (a + b + c) / 3)(10, 20, 55))
