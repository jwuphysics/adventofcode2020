correct = 0

with open('input1.txt') as f:
    lines = f.readlines()    
    for l in lines:
        n1_n2, token, password = l.split(' ')
        n1, n2 = n1_n2.split('-')
        token = token[:-1]

        if (token == password[int(n1)-1]) ^ (token == password[int(n2)-1]):
            correct += 1

print(correct)