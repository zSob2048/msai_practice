
# 컴이랑 1~ 10000 사이 랜덤 뽑아서
# 업다운게임
# 횟수만에 정답

from random import randint


# num_ = randint(1, 10000)
# count_ = 0
# while True:
#     n_in = int(input("# :"))
#     count_ += 1
#     if n_in < num_:
#         print("UP")
#         continue
#     elif n_in > num_:
#         print("DOWN")
#         continue
#     print("%d번만에 정답" % count_)
#     break

# num_ = randint(1, 10000)
# count_ = 0
# while True:
#     n_in = int(input("# :"))
#     count_ += 1
#     if n_in < num_:
#         print("UP")
#     elif n_in > num_:
#         print("DOWN")
#     else:
#         print("%d번만에 정답" % count_)
#         break

# num_0 = randint(1, 10000)
# count_ = 0
# while True:
#     num_in = int(input("# :"))
#     if num_in>10000 or num_in<1:
#         print(" 할생각있음? ")
#         continue
#     count_ += 1
#     if num_in == num_0:
#         print("%d번만에 정답" % count_)
#         break
#     print("UP" if num_in < num_0 else "DOWN")



count_ = 0

def num_input():
    num_in = int(input("# :"))
    if 0 < num_in < 10001:
        return num_in
    print(" 할생각있음? ")
    return num_input()


def num_rand():
    return randint(1, 10000)


def conutinue_(num_0, num_in):
    global count_
    count_ += 1
    if num_in == num_0:
        print("%d번만에 정답" % count_)
        return False
    print("UP" if num_in < num_0 else "DOWN")
    return True


num_0 = num_rand()

while True:
    num_in = num_input()
    if not conutinue_(num_0, num_in):
        break
