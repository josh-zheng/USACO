"""
ID: joshjq91
LANG: PYTHON3
TASK: wormhole

Jan 4, 2018
"""
#import itertools
#import timeit
#start = timeit.default_timer()

# possibility of all pairings:
#   C(N)(2) * C(N-2)(2) * ... * C(2)(2)
# = (N)(N-1)(N-2)...(2)(1) / 2**(N/2)
# = N! / 2**(N/2)


class Cord(object):
    """Instances of the wormhole instances"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.paired = None

    def __repr__(self): # for debugging # may be better to subclass from tuple
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def next(self):
        """
        Returns: the next wormhole the cow will encounter after jumping out of
            the current wormhole.
        """
        for d in cords:
            if d.y == self.y and d.x > self.x:
                return d
        return None


with open('wormhole.in', 'r') as fin:
    N = int(fin.readline()) # N in [2,12], 11! = 0.3M
    cords = []
    for i in range (N):
        x, y = map(int, fin.readline().split())
        cords.append(Cord(x,y))
    cords.sort(key=lambda c: c.x)   # would be easier were it subclass of tuple


def pair(c):
    """Pair the coordinates together.

    Parameter c: a tuple of the two coordinates to be paired together
    """
    c1, c2 = c[0], c[1]
    c1.paired = c2
    c2.paired = c1

"""
def comb(*l):
    r = set(cords)
    for t in l:
        for c in t:
            r |= set(c)
    #print ('r',r)
    return r


cl = list(itertools.combinations(cords, 2))

stop1 = timeit.default_timer()

for l in itertools.combinations(cl, N//2):
    common = False
    s = set()
    s.intersection(*map(set,l))
"""

def pairs(s):
    """Returns: all possible combinations of pairs in given coordinations."""
    l = list(s)
    
    if len(l) == 2:
        return [[(l[0], l[1])]]
    
    result = []
    i = 0
    for j in range(1,len(s)):
        rests = pairs( s - {l[i], l[j]} )
        pair = [ [(l[i],l[j])] + rest for rest in rests ]
        result += pair
    return result

pl = pairs(set(cords))

"""
    a previous bad solution (2.3s run time for N=10)
    pl = [l for l in itertools.combinations(cl, N//2) if all(set(s1).intersection(set(s2))
   is None for (s1,s2) in tuple(itertools.combinations(l,2)))]
 )set(itertools.combination(l,2)).intersection(*list(map(set,l)))]

stop2 = timeit.default_timer()
"""

count = 0   # more substantial name
for pairings in pl:
    for p in pairings:
        pair(p)

    loop = False    # hasLoop for bool
    for c in set(cords):
        route = set()       # list of entrances of wormhole visited

        while True:
            n = c.paired    # exit of wormhole
            if n in route:
                loop = True
                break
            route |= {n}
            if n.next() is None:    # no further wormholes to encounter # if not
                break
            else:
                c = n.next()

        if loop == True:    # if discovered a loop, no need to consider
            break
    if loop == True:
        count += 1

#print (count)

result = str(count)

#stop = timeit.default_timer()

#print (stop1-start)
#print (stop2-stop1)
#print (stop-stop2)

with open('wormhole.out', 'w') as fout:
    fout.write(result+'\n')

