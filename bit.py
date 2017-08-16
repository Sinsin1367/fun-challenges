

class BIT(object):
    def __init__(self, arr=[]):

        self._len = len(arr) + 1
        self._origarr = [0] * (self._len - 1)
        self._arr = [0] * self._len
        for ind in range(self._len - 1):
            print (ind, self._arr)
            self.insert(ind, arr[ind])

    def insert(self, ind, val):
        up = val - self._origarr[ind]
        bitind = ind + 1
        self._arr[bitind] += up
        print('---- ', bitind, up, self._arr[bitind])
        while self._next(bitind):
            bitind = self._next(bitind)
            self._arr[bitind] += up
            print('---- ', bitind, up, self._arr[bitind])

        self._origarr[ind] = val

    def _next(self, bitind):
        lsone = (bitind & -bitind)
        newind = bitind + lsone
        if newind < self._len:
            return newind
        else:
            return None

    def __repr__(self):
        return str(self._arr)


if __name__ == '__main__':
    lst = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
    bit = BIT(lst)
    print('*****', bit)