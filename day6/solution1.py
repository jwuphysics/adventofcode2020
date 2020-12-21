with open('input.txt') as f:
    lines = f.readlines()

groups = [set(''.join(g.split('\n'))) for g in ''.join(lines).split('\n\n')]
print(sum(len(g) for g in groups))