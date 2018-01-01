"""
ID: joshjq91
LANG: PYTHON3
TASK: milk2

Jan 1, 2018
"""

r = set()

with open('milk2.in','r') as fin:
    N = int(fin.readline())
    for i in range(N):
        s, e = map(int, fin.readline().split())
        r.update(range(s,e))
        #print(len(r))

s, e = min(r), max(r)
l = [int(i in r) for i in range(s,e+1)]

s = ''.join(list(map(str, l)))
#print(len(s))

milk = len(max(s.split('0'), key = len))
idle = len(max(s.split('1'), key = len))

with open('milk2.out','w') as fout:
    fout.write(str(milk) + ' ' + str(idle) + '\n')
