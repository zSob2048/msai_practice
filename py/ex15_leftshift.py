value = int(input("매장 특성: "))

# wifi   2^0
# 24h    2^1
# 흡연실 2^2
# 주차장 2^3

# if (value // 1) % 2 == 1:
#     result += "wifi\t"
# if (value // 2) % 2 == 1:
#     result += "24h\t"
# if (value // 4) % 2 == 1:
#     result += "흡연실\t"
# if (value // 8) % 2 == 1:
#     result += "주차장\t"

# result = ""
source_ = ["wifi\t", "24h\t", "흡연실\t", "주차장\t"]
for i in range(4):
    if (value // 2**i) % 2 == 1:
        print(source_[i])
        # result += source_[i]
# print(result)

# ###

# wifi   1 << 0
# 24h    1 << 1
# 흡연실 1 << 2
# 주차장 1 << 3

# if value >= (1<<3):
#     print("주차장")
#     value-=(1<<3)
# if value >= (1<<2):
#     print("흡연실")
#     value-=(1<<2)
# if value >= (1<<1):
#     print("24시간")
#     value-=(1<<1)
# if value >= (1<<0):
#     print("와이파이")
#     value-=(1<<0)

source_ = ["wifi\t", "24h\t", "흡연실\t", "주차장\t"]
for i in range(3,-1, -1):       # range(3,-1,-1) ; (3,2,1,0)
    if value >= (1 << i):
        print(source_[i])
        value -= (1 << i)
