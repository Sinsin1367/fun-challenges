import time

def timeit(method):
    def wrapper(*args, **kwargs):
        start = time.time() * 1000
        result = method(*args, **kwargs)
        end = time.time() * 1000
        print('The method {} with args: {}, {}, ran for {} msec' \
              .format(method.__name__, args, kwargs, end-start))
        return result
    return wrapper

@timeit
def t1(s, d, j, a=22):
    time.sleep(.05)

@timeit
def t2(k, l, m, bb= 'sina', aa = 'sasa'):
    print (bb)
    time.sleep(2)

if __name__ == '__main__':
    t1(1, 2, 3, 6)
    t2(7, 8, 9)