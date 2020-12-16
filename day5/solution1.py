mapping = {'B':1, 'F':0, 'R':1, 'L':0}

largest = 0
with open('input.txt') as f:
    for line in f.readlines():
        b = ''.join([str(mapping[char]) for char in line.strip('\n')])
        code = int(f'0b{b[:-3]}', 2) * 8 + int(f'0b{b[-3:]}', 2)
        largest = max(largest, code)

print(largest)