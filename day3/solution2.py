with open('input.txt') as f:
    lines = f.readlines()

length = len(lines[0].strip('\n'))

prod_trees = 1
for (r,d) in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
    n_trees = 0
    for i, l in enumerate(lines[::d]):

        idx = r*i % length
        if l[idx] == '#':
            n_trees += 1

        # c = 'X' if l[idx] == '#' else 'O'
        # print(l[:idx] + c + l[idx+1:], end='')
    # print('\n' + str(n_trees) + '\n')

    prod_trees *= n_trees

print(prod_trees)
