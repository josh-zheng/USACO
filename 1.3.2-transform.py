"""
ID: joshjq91
LANG: PYTHON3
TASK: transform

Jan 1, 2018
"""

with open('transform.in','r') as fin:
    N = int(fin.readline())

    bef = []
    for i in range(N):
        bef.append(list(fin.readline()[:-1]))

    aft = []
    for i in range(N):
        aft.append(list(fin.readline()[:-1]))

#print(bef)

def rotated(m):
    result = []
    for r in range(N):
        row = []
        for c in range(N):
            row.append(m[N-c-1][r])
        result.append(row)
    return result


def reflected(m):
    return [x[::-1] for x in m]


buf = bef

for i in range(1,4):
    buf = rotated(buf)
    if buf == aft:
        n = i
        break
else:
    if reflected(bef) == aft:
        n = 4
    else:
        buf = reflected(bef)
        for i in range(3):
            buf = rotated(buf)
            if buf == aft:
                n = 5
                break
        else:
            if bef == aft:
                n = 6
            else:
                n = 7


with open('transform.out','w') as fout:
    fout.write(str(n)+'\n')
