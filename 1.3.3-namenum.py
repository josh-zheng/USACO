"""
ID: joshjq91
LANG: PYTHON3
TASK: namenum

Jan 1, 2018
"""

def toNum(c):
    if ord(c) < ord('Q'):
        return str((ord(c)-65)//3 + 2)
    else:
        return str((ord(c)-66)//3 + 2)

with open('dict.txt','r') as fin:
    names = fin.read().split('\n')

serials = [''.join(list(map(toNum, name))) for name in names]

with open('namenum.in','r') as fin:
    serial = fin.read()[:-1]

i = -1
o = ''
while serial in serials[i+1:]:
    i = serials.index(serial,i+1)
    o += names[i] + '\n'

if not o:
    o = 'NONE\n'

with open('namenum.out','w') as fout:
    fout.write(o)
