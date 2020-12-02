correct = 0

with open('input1.txt') as f:
    lines = f.readlines()    
    for l in lines:
        num_range, token, password = l.split(' ')
        lo, hi = num_range.split('-')
        token = token[:-1]
        num = password.count(token)
        if (num >= int(lo)) and (num <= int(hi)):
            correct += 1

print(correct)