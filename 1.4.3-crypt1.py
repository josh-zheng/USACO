"""
ID: joshjq91
LANG: PYTHON3
TASK: crypt1

Jan 4, 2018
"""

with open('crypt1.in', 'r') as fin:
    N  = int(fin.readline())
    ds = fin.readline().split() # read in as strings for later comparison

c = 0
for i in range(100,1000):   # brutal force
    for j in range(10,100):
        try:
            s = str(i)+str(j)   # the two numbers
            p = str(i*j)        # product
            pp1 = str(i*(j%10)) # partial products
            pp2 = str(i*(j//10))
            assert all(d in ds for d in s+p+pp1+pp2)    # all digits are listed
            assert len(pp1) == 3 and len(pp2) == 3 and len(p) == 4  # digits count
            c += 1  # satisties all requirements
        except:
            pass

result = c

with open('crypt1.out', 'w') as fout:
    fout.write(str(result)+'\n')
