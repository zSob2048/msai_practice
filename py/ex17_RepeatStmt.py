# 반복문
# 횟수> for > python에 없음(엥)
# 컬렉션 탐색용> for-each (생긴건 비슷)

a = [1, 1, 2, 3, 5, 8, 13]
for i in a:
    print(i)

for i in range(0, 5):
    print(i)

for i in range(1, 6):
    print(2 * i)

times = 1
for i in range(1, 6):
    times *= i
print(times)

#

list_ = ["가", "나", "다", "라"]
for i in range(len(list_)):
    print(list_[i])

for i, j in enumerate(list_):  # (인덱스, 값) (tuple로 돌리다...)
    print(i)
    print(j)

d = {"색": "깜장", "가격": 500}
for i in d:
    print(i)  # > 키를 출력함
for i, j in d.items():  # (키, 값) tuple
    print(i)
    print(j)


value = int(input("매장 특성: "))
source_ = ["wifi\t", "24h\t", "흡연실\t", "주차장\t"]

for i in range(len(source_)):
    if (value // 2**i) % 2 == 1:
        print(source_[i])

for i, j in enumerate(source_):
    if (value // 2**i) % 2 == 1:
        print(j)

# 비슷한거같은데

for i in range(len(source_) - 1, -1, -1):
    if value >= (1 << i):
        print(source_[i])
        value -= 1 << i

