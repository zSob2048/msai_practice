# 숫자(x,y,x,...):
# ----------------------
# 합

x=input("# : ").split(",")
# x="ㅋ,x, 1, 2, 6,, 6c".split(",")
k , n = 0 , 0
for i in x:
    try:
        k += int(i)
        n += 1
    except:
        pass

print("합계 : %d\n평균 : %.1f"%(k, k/n))