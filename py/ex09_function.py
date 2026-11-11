# 함수다!!!


# 1) 함수 정의
#    def f(x,y,...):
#       들여쓰기_내용...return값 ; python의 경우 : 이후 정의 영역이 들여쓰기로만 정해지니 주의
#       return 값 ;  y = f(x,y, ...)


def schrodinersKatze(n):
    print("슈뢰딩거의고양이")
    print("슈뢰딩완전고양이")
    print("슈뢰딩%d%%고양이" % n)


# 2) 함수 호출
#    f()
schrodinersKatze(95)


def test():
    pass  # 영역 내용이 정해지지 않은 경우 비워둘 때


print("졸려")


# 숫자 2개 넣으면 그 합을 출력하는 fn
def print_plus(x, y):
    print(x, y, x + y)


print_plus(20, 15)


# 숫자 3개 넣으면 그 합을 출력하는 fn
def print_plus(x, y, z=0):
    print(x, y, z, x + y + z)

# 들어가는 변수 상태(갯수, 자료형 등...)가 다르면 함수명이 같아도 됨
# >> 일부러 같은 함수명을 사용 : overloading 

print_plus(45, 86) # >> overloading의 효력이 저하 (어떤 함수인지 구별 불가)... 근데 기본값이 되면 항등원을 기본값에 넣으면 되는거 아닌가?
print_plus(241, 5, 35)


# 숫자 2개 넣으면 그 합을 출력하는 fn
def print_plus_str(x, y="ㅋ"):  # y에 기본값(ㅋ) 지정 가능 , python에서만가능...
    print(x + y)


print_plus_str("바", "보")
print_plus_str("바")
print_plus_str(y="바", x="보")  # 변수 지정 가능 , python에서만...

# overriding <> overloading ; 

