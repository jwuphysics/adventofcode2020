with open('input.txt') as file:
    lines = file.readlines()

# reformat so all passports are on a single line and space-delimited
lines = ''.join(lines).replace('\n\n', '\t').replace('\n', ' ').split('\t') 

# a passport must have these 7 fields
necessary_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

# validate passports using these functions and helper func
def within(x:int, x1:int, x2:int):
    return (x >= x1) and (x <= x2)

validation_funcs = {
    'byr': lambda x: within(int(x), 1920, 2002),
    'iyr': lambda x: within(int(x), 2010, 2020),
    'eyr': lambda x: within(int(x), 2020, 2030),
    'hgt': lambda x: (len(x) >= 4) and (within(int(x[:-2]), 150, 193) if x[-2:] == 'cm' else within(int(x[:-2]), 59, 76)),
    'hcl': lambda x: (x[0] == '#') and set(x[1:]).issubset('0123456789abcdef'),
    'ecl': lambda x: x in 'amb blu brn gry grn hzl oth'.split(),
    'pid': lambda x: (len(x) == 9) and set(x).issubset('0123456789')
}

num_valid = 0
for line in lines:
    kvs = line.split()
    keys, values = zip(*list(kv.split(':') for kv in kvs))
    
    if not necessary_fields.issubset(keys):
        continue

    valid = True
    for k, v in zip(keys, values):
        if k == 'cid': continue
        f = validation_funcs[k]
        if not f(v): 
            valid = False
    num_valid += valid

print(num_valid)