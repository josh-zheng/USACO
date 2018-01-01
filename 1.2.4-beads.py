"""
ID: joshjq91
LANG: PYTHON3
TASK: beads

Jan 1, 2018
"""
with open('beads.in','r') as fin:
    N = int(fin.readline())
    beads = fin.readline()[:-1]

def canCollect(s):
    return not ('r' in s and 'b' in s)

beads = beads*3
max = 0

for p in range(N, N*2):
    i = p-1
    left = []
    while i > 0:
        if canCollect(left + [beads[i]]):
            left.append(beads[i])
            i -= 1
        else:
            break

    i = p
    right = []
    while i < 3*N - 1:
        #print("righti",i-N)
        if canCollect(right + [beads[i]]):
            right.append(beads[i])
            i+=1
        else:
            break

    result = len(left) + len(right)
    if result >= N:
        max = N
        break
    elif result > max:
        max = result

with open('beads.out','w') as fout:
    fout.write(str(max) + '\n')
