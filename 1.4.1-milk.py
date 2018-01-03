"""
ID: joshjq91
LANG: PYTHON3
TASK: milk

Jan 3, 2018
"""
prices = []

with open('milk.in','r') as fin:
    N, M = map(int, fin.readline().split())
    for i in range(M):
        p, u = map(int, fin.readline().split())
        prices.append((p,u))

prices.sort()
print(prices)

n = N
r = 0
for p in prices:
    if n == 0:
        break
    elif p[1] <= n:
        r += p[0] * p[1]
        n -= p[1]
    else:
        r += p[0] * n
        break

with open('milk.out','w') as fout:
    fout.write(str(r)+'\n')
