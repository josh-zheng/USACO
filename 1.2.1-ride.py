"""
ID: joshjq91
LANG: PYTHON3
TASK: ride

Dec 31, 2017
"""

fin = open('ride.in','r')
fout = open('ride.out','w')

s1 = fin.readline()[:-1]
s2 = fin.readline()[:-1]

r1 = 1
for ch in s1: r1 *= ord(ch)-64

r2 = 1
for ch in s2: r2 *= ord(ch)-64

if r1%47==r2%47:
    s = "GO\n"
else:
    s = "STAY\n"

fout.write(s)
fout.close

# err 1: no '\n' at the end of output files

"""
Example Code: (Python 2)

with open('ride.in', 'r') as fin:
    comet1 = fin.readline().strip()
    comet2 = fin.readline().strip()
prod1, prod2 = 1, 1
for c in comet1: prod1 *= ord(c) - ord('A') + 1
for c in comet2: prod2 *= ord(c) - ord('A') + 1
with open('ride.out', 'w') as fout:
    if prod1 % 47 == prod2 % 47: fout.write('GO\n')
    else: fout.write('STAY\n')
"""

# use with when reading files
# define multiple variables at the sam time
# control flow within one line
