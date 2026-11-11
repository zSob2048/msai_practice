# 숫자 1개 넣으면 홀수인지 아닌지를 출력해주는 함수

from time import sleep


def odd_print(n):
    print(n % 2 == 1)


# 만든 함수로 13이 홀수인지

odd_print(13)


# 숫자 1개 넣으면 홀수인지 아닌지를 구해주는 함수
def odd_sol(n):
    return n % 2 == 1


# 함수를 사용해 10이 홀수 맞는지 출력

print(odd_sol(10))


# 숫자 1개 넣으면 2배값 구하
def times2(x=0):
    return 2 * x


print(times2(3))

# sleep(times2(5)) # 프로그램 진행 멈춤


# 숫자 2개 넣으면 합
def sum_(x=0, y=0):
    return x + y


# sleep(sum_(1,4))


# 숫자 2개 넣으면 사칙연산 통틀어...
def operate_(x, y):
    # return {"add": x + y, "sub": x - y, "multi": x * y, "div": x / y}
    return x + y, x - y, x * y, x / y # >> brackat 생략한 tuple

# ... 방정식은 아니고 함수임 >> return이 여러개일수는 없음 >> 어차피 매개변수로 나타낸 벡터값 취급하면 되는거 아닌가?
#   end랑 같은 역할도 함(이거쓰면 함수 끝)

# print(operate_(10, 5)["add"])
# add_, sub_, multi_, div_ = operate_(10, 5)
add_, sub_, _, div_ = operate_(10, 5) # 필요하지 않은 변수의 경우 _로 생략 ; 
