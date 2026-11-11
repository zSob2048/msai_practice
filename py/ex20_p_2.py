from random import randint

rsp_ = ["가위", "바위", "보"]
wdl_= ["draw","win","lose"]

# s = ""     # 공집합> 메모리공간차지
# s = None   # 다른 언어에선 Null, 정의안함> 메모리공간차지X

def rsp_cpu():
    return randint(0, 2)


def rsp_input():
    rsp_i = input("YOU\t: ")
    if rsp_i in rsp_:
        return rsp_.index(rsp_i)
    print("입력한 값을 확인하세요.( 가위, 바위, 보 )\n---")
    return rsp_input()


def rsp(rsp_input,rsp_cpu ):
    print("CPU\t: %s" % rsp_[rsp_cpu])
    wdl = (rsp_input - rsp_cpu)%3
    print(wdl_[wdl])
    if wdl == 2:
        print("%d연승" % count_w)
    print("---")
    return wdl

count_w = 0
while True:
    rsp_i = rsp_input()
    rsp_c = rsp_cpu()
    wdl = rsp(rsp_i, rsp_c)
    if wdl==2:
        break
    count_w += wdl
