# lotto

from random import randint


lotto_s= {randint(1,45),randint(1,45),randint(1,45),randint(1,45),randint(1,45),randint(1,45)}
while len(lotto_s)!=6:
    lotto_s.add(randint(1,45))
print(lotto_s)

def num_out():
    num_ = randint(1, 45)
    if num_ in lotto_l :
        # print(num_)
        return num_out()
    return num_


lotto_l = [0, 0, 0, 0, 0, 0]
for i in range(6):
    lotto_l[i] = num_out()
    print("%d번 숫자는 %d" % (i+1, lotto_l[i]))

print(" 총 번호 :", lotto_l)

def pick(i,lotto):
    l=randint(1,45)
    for j in range(i):
        if l == lotto[j]:
            return pick(i, lotto)
    return l     

lotto = []
for i in range(6):
    l=pick(i,lotto)
    lotto.append(l)

print(lotto)

