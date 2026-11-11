import numpy as np

a = np.random.randint(1,101,[3,5])
b = np.random.randint(1,101,[3,5])
print(a)
print(b)
print("---")
print(np.concatenate([a,b])) # 6*5
print(np.concatenate([a,b],axis=1)) # 3*10
print(np.append(a,b)) # 1차원
print("---")
print(np.array_split(a,2))
print(np.split(a,3)) # n빵아니고 열빵이라 5개 안되는데
print("---")
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b)) # A○B
print(np.divide(a,b)) # 요소별
print(np.mod(a,b)) # 요소별
print(np.power(a,b)) # 요소별
print(np.less_equal(a,b)) # 요소별
## 

c = np.random.rand(2,3)
print(c)
print(np.rint(c)) # 가장 가까운 정수값
print(np.round(c, 1)) # 자리수 지정 반올림

d = np.array([1, np.nan, np.inf])
print(d)
print(np.isnan(d))
print(np.isinf(d))

e = np.random.randint(-5,6,[2,3])
print(e)
print(np.abs(e))
print(np.sqrt(e))

f = np.random.randn(2,3)
print(f)
print(np.sum(f))
print(np.mean(f))
print(np.max(f))
print(np.max(f, axis=1))
print(np.argmax(f)) # 값의 index
print(np.argmax(f, axis=1)) # 값의 index


g = np.random.randint(1,11,[3,5])
h = np.random.randint(1,11,[3,5])
print(g)
print(h)
print("---")
print(np.intersect1d(g,h)) # ∧
print(np.union1d(g,h)) # ∨
print(np.setdiff1d(g,h)) # -
print(np.setxor1d(g,h)) # 대칭차집합

print(np.unique(g)) # 중복제거

print("---")
# sort
i = np.random.randint(1, 101, [10])
print(i)
print(i[::-1]) # 역순
print(np.sort(i)) # 오름차순

j = np.random.randint(1, 101, [3,5])
print(j)
print("---")
print(np.sort(j)) # 기본 행별 정렬 (axis=1)
print("-")
print(np.sort(j)[:, ::-1])
print("-")
print(np.sort(j, axis=0))
print("-")
print(np.sort(j, axis=0)[::-1]) 
print("-")

# upd
k = np.random.randint(1,11,[5])


