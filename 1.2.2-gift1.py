"""
ID: joshjq91
LANG: PYTHON3
TASK: gift1

Dec 31, 2017
"""
from collections import OrderedDict

accounts = OrderedDict()

with open('gift1.in', 'r') as fin:
    NP = int(fin.readline())

    for i in range(NP):
        accounts[fin.readline()] = 0

    while True:
        giver = fin.readline()
        if not giver: break

        money, NG = map(int, fin.readline()[:-1].split())

        if not NG:
            continue

        for j in range(NG):
            recipient = fin.readline()
            accounts[recipient] += money // NG

        accounts[giver] += -money + money%NG


with open('gift1.out','w') as fout:
    for name, net in accounts.items():
        fout.write(name[:-1] + ' ' + str(net) + '\n')


# err 1: dict did not maintain the fixed order
    # OrderedDict()

# solution: struct in C
