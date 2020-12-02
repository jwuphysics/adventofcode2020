import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

a = np.array(lines, dtype=int)

b = a[a < 2020-min(a)]

for i in b: 
    for j in b[b > i]: 
        if i+j == 2020: 
            print(i*j)