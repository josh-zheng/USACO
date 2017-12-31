"""
ID: joshjq91
LANG: PYTHON3
TASK: friday

Dec 31, 2017
"""
def isLeap(y):
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
        return True
    return False


with open('friday.in','r') as fin:
    N = int(fin.readline())

months = [31,31,28,31,30,31,30,31,31,30,31,30]  # starts with december
result = [0]*7  # starts with saturday

day = 4     # 1899.12.13 Wed

for year in range(1900, 1900+N):
        for m in range(12):
            if isLeap(year) and m == 2:
                day = (day + 1) % 7
            else:
                day = (day + months[m]) % 7
            result[day] += 1

with open('friday.out','w') as fout:
    result = list(map(str, result))
    fout.write(' '.join(result) + '\n')


# err: leap year condition; months rellocation; result rellocation
