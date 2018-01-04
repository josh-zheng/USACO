"""
ID: joshjq91
LANG: PYTHON3
TASK: combo

Jan 4, 2018
"""
def reg(n):
    """
    Returns: the number n regulated so that it fits within the lock.
    """
    if n <= 0:
        return N+n
    elif n > N:
        return n-N
    else:
        return n

with open('combo.in', 'r') as fin:
    N = int(fin.readline())

    f = list(map(int, fin.readline().split()))
    m = list(map(int, fin.readline().split()))

nr = set(range(1,N+1))  # set of all dials
d = []

for i in range(3):
    fr = set(map(reg, range(f[i]-2, f[i]+3))) & nr  # set of dials near farmer's key
    mr = set(map(reg, range(m[i]-2, m[i]+3))) & nr  # set of dials near master's key
    d.append(len(fr & mr))  # number of dials that suit both patterns

result = 2*(min(N,5)**3) - d[0]*d[1]*d[2]
# min(N,5): the number of legal dials around a key
# 2*(min(N,5)**3): number of possible combinations near key of farmer together with master
# d[0]*d[1]*d[2]: number of possible combinations near key of both farmer and master

with open('combo.out', 'w') as fout:
    fout.write(str(result)+'\n')
