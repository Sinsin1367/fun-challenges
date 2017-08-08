print('sina is good')

from math import inf
from collections import defaultdict

import sys
sys.setrecursionlimit(1000000)
#print(sys.getrecursionlimit())

d = dict()  #######map to store the sub problem asnwers (dynamic programming)


def Problematic(N):
    if N < 4:
        return float('inf')

    if N in d:
        return d[N]

    strn = str(N)
    dig = len(strn)
    valid = set()
    valid.add('4')
    valid.add('5')
    # print (valid)
    for ind, let in enumerate(strn):
        if let in valid:
            if ind != dig - 1:
                continue
            else:
                return 1
        else:
            break

    allprob = [4, 5]

    ind = 0
    level = 1
    while True:
        for _ in range(2 ** (level - 1)):
            next = allprob[ind] + 4 * 10 ** level
            if next >= N:
                break
            allprob.append(next)
            next = allprob[ind] + 5 * 10 ** level
            if next >= N:
                break
            allprob.append(next)
            ind += 1
            next = allprob[ind] + 4 * 10 ** level
            if next >= N:
                break
            allprob.append(next)
            next = allprob[ind] + 5 * 10 ** level
            if next >= N:
                break
            allprob.append(next)
            ind += 1


        level += 1
        if next >= N:
            break

    # print (allprob)
    minpos = min(list(map(Problematic, [(N - num) for num in allprob if num < N]))) + 1
    print(N, '----', minpos, allprob)
    # print('hi there thi is minpos : {}'.format(minpos))
    d[N] = minpos

    return minpos

    # print(lastdig)

dd = {}
def Problematic2(N):
    prob = problem(N)
    print(prob)
    for pr in prob:
        dd[pr] = 1
    for num in range(1, N+1):
        if num in prob:
            continue
        try:
            dd[num] = min([dd[num - val] for val in prob if (num-val) in dd]) + 1
            #print(num, '----', dd[num])
        except ValueError as e:
            print('{0} Not Possible!!! {1}'.format(num, e))

    if N not in dd:
        return -1
    return dd[N]

def problem(N):
    prob = [[4, 5]]
    while prob[-1][-1] < N:
        prob.append([])
        for item in prob[-2]:
            new = int(str(4) + str(item))
            if  new > N:
                break
            prob[-1].append(new)

        for item in prob[-2]:
            new = int(str(5) + str(item))
            if  new > N:
                break
            prob[-1].append(new)

        if new > N:
            break

    sum_ = list()
    for item in prob:
        sum_ += item
    return sum_

lst = []
T = int(input())
for _ in range(T):
    N = int(input())

    out_ = Problematic2(N)
    lst.append(out_)

for item in lst:
    print(item)
#this was fun