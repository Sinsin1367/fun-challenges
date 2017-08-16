import sys
import numpy
import timeit

pl = [[1, 2, 3], [4, 5, 6]]
pl2 = list(pl)
na = numpy.array(pl)
print( na == pl, pl2 == pl, na is pl)

@timeit
def myprint(it):
    for item in it:
        print(item)

myprint(pl)
myprint(na)
