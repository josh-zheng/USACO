"""
ID: joshjq91
LANG: PYTHON3
TASK: palsquare

Jan 2, 2018
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


with open('palsquare.in','r') as fin:
    B = int(fin.readline())

with open('palsquare.out','w') as fout:
    for n in range(1,301):
        #print('n', n, 'bn', toBase(n,B))

        bsq = toBase(n**2, B)
        if bsq[::-1] == bsq:
            bn = toBase(n, B)
            fout.write(bn + ' ' + bsq + '\n')

"""
def bAddOne(s, b):
    s = s[::-1]
    i = 0

    s[0] = str(int(s[0]) + 1)

    while s[i] >= b and i < len(s):
        s[i] = '0'
        s[i+1] = str(int(s[i+1]) + 1)
        i += 1

    if i == len(s):
        s[-1] = '0'
        s =
"""
