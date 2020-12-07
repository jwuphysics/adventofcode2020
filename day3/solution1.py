with open('input.txt') as f:
    lines = f.readlines()

n_trees = 0
for i, l in enumerate(lines):
    idx = 3*i % (len(l)-1)
    if l[idx] == '#':
        n_trees += 1

    # c = 'X' if l[idx] == '#' else 'O'
    # print(l[:idx] + c + l[idx+1:])

print(n_trees)