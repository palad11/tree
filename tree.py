import os

for x in os.walk('.'):
    if x[0] == '.':
        print(x[0])
        continue
    a = x[0].split('\\')
    print('|    ' * (len(a) - 1), f'-{a[-1]}')
    v = f'\n{"|    " * (len(a))}|_'.join(x[2])
    v = f'{"|    " * (len(a))}|_{v}'
    print(v)
