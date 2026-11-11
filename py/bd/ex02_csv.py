import numpy as np


f = open("py/bd/subway.csv", "r", encoding="utf-8")
data = np.zeros([3,1])
print(data)
for line in f.readlines():
    line = line.replace("\n","").split(",")
    line = np.array([line[4], line[5], line[6]])[:, np.newaxis]
    data = np.block([data, line])
    print(data)



