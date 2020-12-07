with open('input.txt') as file:
    lines = file.readlines()

# reformat so all passports are on a single line and space-delimited
lines = ''.join(lines).replace('\n\n', '\t').replace('\n', ' ').split('\t') 

# a passport must have these 7 fields
necessary_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

valid = 0
for line in lines:
    kvs = line.split()

    fields = set([kv.split(':')[0] for kv in kvs])
    if necessary_fields.issubset(fields):
        valid += 1

print(valid)