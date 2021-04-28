import sys
from collections import Counter

n = int(sys.stdin.readline())

array = []

for i in range(n):
    array.append(int(sys.stdin.readline()))

def average(ar):
    return round(sum(ar) / n)

def mid(ar):
    ar.sort()
    return ar[n//2]
    
def mode(ar):
    mod = Counter(ar).most_common()
    if len(ar) > 1:
        if mod[0][1] == mod[1][1]:
            return mod[1][0]
        else:
            return mod[0][0]
    else:
        return ar[0]

def ran(ar):
    ar.sort()
    size = ar[n - 1] - ar[0]
    return size

print(average(array))
print(mid(array))
print(mode(array))
print(ran(array))