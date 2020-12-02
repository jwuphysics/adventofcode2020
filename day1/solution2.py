import numpy as np

with open('input.txt') as f:
    lines = f.readlines()

a = np.array(lines, dtype=int)
b = a[a < (2020-min(a))]
c = b[b < (2020-min(b))]

for i in c: 
    for j in c[c > i]: 
        for k in c[c > j]: 
            if i+j+k == 2020: 
                print(i*j*k)