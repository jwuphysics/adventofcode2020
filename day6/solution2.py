with open('input.txt') as f:
    lines = f.readlines()

count = 0
for answers in ''.join(lines).split('\n\n'):
    n = len(answers.split('\n'))
    for questions in set(''.join(answers.split('\n'))):
        if answers.count(questions) == n:
            count += 1
print(count)
