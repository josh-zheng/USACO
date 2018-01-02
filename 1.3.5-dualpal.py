"""
ID: joshjq91
LANG: PYTHON3
TASK: dualpal

Jan 1, 2018
"""
def toBase(n, b):
    l = 0
    result = []
    while n >= b**l:
        l += 1

    for i in reversed(range(l)):
        d = n // (b**i)
        if d < 10:
            d = str(d)
        else:
            d = chr(ord('A')+d-10)
        result.append(d)
        n %= (b**i)

    return ''.join(result)


with open('dualpal.in','r') as fin:
    N, S = map(int, fin.readline().split())

n = S
r = []

while len(r) < N:
    n += 1
    c = 0

    for b in range(2,11):
        bn = toBase(n, b)

        if bn == bn[::-1]:
            print(n,'s')
            c += 1
        if c == 2:
            r.append(n)
            break

with open('dualpal.out','w') as fout:
    for n in r:
        fout.write(str(n)+'\n')


