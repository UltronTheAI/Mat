import random

i = 0
lis = ['x', '-', '+', '/']

for qus in range(0, 11):
    # i += 1
    n = random.randint(0, 99 + i)
    n1 = random.randint(90, 260)
    n2 = random.randint(0, 3)
    try:
        pi = 0
        print(f'{n} {lis[n2]} {n1} = ')
        ans = int(input())
        if n2 == 0:
            pi = n * n1
        if n2 == 1:
            pi = n - n1
        if n2 == 2:
            pi = n + n1
        if n2 == 3:
            pi = n / n1
        else:
            pass
        if ans == pi:
            pass
        else:
            print('Wrong Ans... Ans IS '+pi)

    except:
        pass
