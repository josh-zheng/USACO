"""
ID: joshjq91
LANG: PYTHON3
TASK: skidesign

Jan 4, 2018
"""

with open('skidesign.in', 'r') as fin:
    N = int(fin.readline())
    le = []  # list of the elevation of hills
    for i in range(N):
        le.append(int(fin.readline()))

le.sort()

"""
1 2 3 20 24
4 4 4 20 21 3 2 1 3 23
3 3 3 20 20 2 1 0 4 21
"""

lp = []   # list of possible prices
for s in range(min(le), max(le) - 17):  # s: start of the height range (17)
    e = s + 17                          # e: end of the height range
    p = 0   # price for the change

    # add the square of height differences to the price
    for mt in le:
        if mt < s:
            p += (mt-s)**2
        elif mt > e:
            p += (mt-e)**2

    lp.append(p)

lp = [0] if not lp else lp  # if does not require changes

result = min(lp)

with open('skidesign.out', 'w') as fout:
    fout.write(str(result) + '\n')
