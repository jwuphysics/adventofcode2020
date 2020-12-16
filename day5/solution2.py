mapping = {'B':1, 'F':0, 'R':1, 'L':0}

def map_func(x):
    b = ''.join([str(mapping[char]) for char in x.strip('\n')])
    code = int(f'0b{b[:-3]}', 2) * 8 + int(f'0b{b[-3:]}', 2)
    return code

with open('input.txt') as f:
    codes = list(sorted(map(map_func, f.readlines())))

for i in range(len(codes) - 1):
    if codes[i] + 2 == codes[i + 1]:
        print(codes[i]+1)
