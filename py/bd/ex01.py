# anaconda : py+bd/ai용 lib 설치된 가상환경 + Jupyter Notbook이라는 작업 툴
# => 분석 작업에 적합

# MS Azure ML에서 같은 환경 제공

#
import numpy as np

list_normal = [[11, 12, 13], [21, 22, 23]]
list_numpy = np.array([[11, 12, 13], [21, 22, 23]])


print(list_normal, type(list_normal))
print(list_normal[0][1])
print(list_numpy, type(list_numpy))
print(list_numpy[0][1])
print(list_numpy[0, 1])

# list_numpy[1,0:3] = 0 # slicing
print(list_numpy.shape)  # 2,3
print(list_numpy.dtype)  # data type int64
print(len(list_numpy))
print(len(list_numpy))
print(list_numpy.size)  # 6

no = list_normal[0] + list_normal[1]
nu = list_numpy[0] + list_numpy[1]
print(no)  # [11 12 13 21 22 23]
print(nu)  # [32 34 36]

index = np.array(["a", "b", "c"])
x = np.array([10, 15, 10])
y = np.array([30, 15, 10])
z = np.array([10, 20, 40])

avg = (x + y + z) / 3
tf = avg >= 20
print(index[tf])
print((5 < z) & (z < 30))
