# 1 2 3 --- 1 2 ... 10 --- 1 3 5 7 9 9 7 5 3 1

from random import randint


for i in range(1, 4):
    print(i)
# 그냥 프린트 3개 다는게 더 효율적일 수 있음...

print("--")

for i in range(1, 11):
    print(i)

print("--")

for i in range(5):  # range(1,10,2) ; i
    print(2 * i + 1)

print("--")

for i in range(5):  # range(9,0,-2) ; i
    print(9 - 2 * i)

print("--")

# 1+2+ ...+10
sum = 0
for i in range(10):
    sum += i + 1
print(sum)

print("--")

# 1+3+5+...+19
sum = 0
for i in range(10):
    sum += 2 * i + 1
print(sum)

# 변수의 기본값 << 언어마다 다름 (0, 쓰레기값, err(없음), ...)
# ; python의 경우 변수'만' 정의가 불가능

# 구구단
# 2단
for i in range(1, 10):
    print(" 2 x %d = %d" % (i, 2 * i))

# 2단~ 9단
for i in range(2, 10):
    for j in range(1, 10):
        print(" %d x %d = %d" % (i, j, i * j))

# 배열정렬
for j in range(1, 10):
    for i in range(2, 10):
        print(" %d x %d = %d" % (i, j, i * j), end="\t")
    print()

# 별찍기...; 반복문 연습용
# ㅋㅋㅋㅋㅋ *5

for i in range(5):
    for j in range(5):
        print("a%d%d" % (i + 1, j + 1), end=" ")
    print()
# 와 행렬!

print("--")

for i in range(5):
    for j in range(i + 1):
        print("ㅋ", end="")
    print()

print("--")

for i in range(5):
    for j in range(5 - i):
        print("ㅋ", end="")
    print()

print("--")

for i in range(5):
    print(i * "  " + "ㅋ")

for i in range(5):
    for j in range(i):
        print("  ", end="")
    print("ㅋ")

print("--")

# for i in range(5):
#     for j in range(2*i + 1):
#         if i % 2 == 0: # 연산량 多
#             print("ㅋ", end="")
#         else:
#             print("ㅎ", end="")
#     print()
s=""
for i in range(5):
    if i % 2 == 0:
        s="ㅋ"
    else:
        s="ㅎ"
    for j in range(2*i + 1):
        print(s, end="")
    print()

print("--")

for i in range(5):
    if i % 2 == 0:
        print("ㅋ"*(2*i+1))
    else:
        print("ㅎ"*(2*i+1))

print("--")

for i in range(5):
    for j in range(i + 1):
        if (i + j) % 2 == 0:
            print("ㅋ", end="")
        else:
            print("ㅎ", end="")
    print()

print("--")

# 1+2+ ... +20
sum_=0
for i in range(20):
    sum_ += i+1
print(sum_)

print("--")


# 반복 조건
# 1+2+...+?>100
# while 조건식:
#     조건식 만족시 실행

# 랜덤
# for i in range(10):
#     print(randint(1,10))

r= randint(1,10)
print(r)
while r!=4:
    r = randint(1,10)
    print(r)

# 정수 입력받아서 출력
n=int(input("숫자: "))
print(n)
while n!=5:
    n=int(input("숫자: "))
    print(n)

#################################################

# 반복문 제어
# break: 반복문 종료 (for while 안가림)
# 1 4 7 10
for i in range(34):
    if (3 * i + 1) % 10 == 0:
        break
    print(3 * i + 1)

# contimue: 강제 반복 / 턴 종료
for i in range(1, 101, 3):
    if i % 10 == 0:
        continue
    print(i)

# 멘트 입력>출력
# while True:
#     comm_ = input("나: ")
#     print(comm_)
#     if comm_ == "나가":
#         break

for i in range(3):
    for j in range(3):
        for k in range(3):
            if k == 1:
                break
            print(i, j, k)
# >> for k 깨짐
#   i까지 완전히 break 하려면...


print("--")

ibreak = False
for i in range(3):
    if ibreak:
        break
    for j in range(3):
        if ibreak:
            break
        for k in range(3):
            if k == 1:
                ibreak = True
                break
            print(i, j, k)
 # == True 생략 가능
 # == False >> not A (==True)
print("--")
