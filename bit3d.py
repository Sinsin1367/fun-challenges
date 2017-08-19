import copy
from collections import defaultdict


class bit3d():
    def __init__(self, n):
        self.size = n
        self._origarr = self.make3d(n)
        self._arr = self.make3d(n)
        # print(self._origarr)

    def make3d(self, n):
        d = defaultdict(int)
        return d

    def process(self, op):
        optype, *args = op.split()
        # print(optype, args)
        if optype.startswith('UPDATE'):
            self.update(*args)
        elif optype.startswith('QUERY'):
            self.query(*args)

    def update(self, *args):
        x, y, z, val = list(map(int, args))
        up = val - self._origarr[x - 1, y - 1, z - 1]
        for xx in self._next(x):
            for yy in self._next(y):
                for zz in self._next(z):
                    self._arr[xx - 1, yy - 1, zz - 1] += up
        self._origarr[x - 1, y - 1, z - 1] = val

        # print('Updated {}, {}, {} to : {}'.format(x, y, z, val))
        # print(self._origarr)
        # print(self._arr)

    def update2(self, x, y, z, val):
        up = val - self._arr[x][y][z]
        xxx = list(self._next(x))
        yyy = list(self._next(y))
        zzz = list(self._next(z))
        for xx in xxx:
            for yy in yyy:
                for zz in zzz:
                    self._arr[xx][yy][zz] += up

    def _next(self, num):
        while (num <= self.size):
            yield num
            num = num + (num & -num)

    def query(self, *args):
        x1, y1, z1, x2, y2, z2 = list(map(int, args))
        x1 -= 1
        y1 -= 1
        z1 -= 1
        sum1 = self._sum(x2, y2, z2) - self._sum(x2, y1, z2) - self._sum(x1, y2, z2) + self._sum(x1, y1, z2)
        sum2 = self._sum(x2, y2, z1) - self._sum(x2, y1, z1) - self._sum(x1, y2, z1) + self._sum(x1, y1, z1)
        print(sum1 - sum2)

    def _sum(self, *args):
        x, y, z = args
        if x == 0 or y == 0 or z == 0:
            return 0
        xxx = list(self._par(x))
        yyy = list(self._par(y))
        zzz = list(self._par(z))
        mysum = 0
        for xx in xxx:
            for yy in yyy:
                for zz in zzz:
                    mysum += self._arr[xx - 1, yy - 1, zz - 1]
        return mysum

    def _par(self, num):
        while num > 0:
            yield num
            num = num - (num & -num)


t = int(input().strip())
for _ in range(t):
    n, m = list(map(int, input().strip().split()))
    mybit = bit3d(n)
    for op in range(m):
        op = input().strip()
        mybit.process(op)