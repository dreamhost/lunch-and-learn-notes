from randint_iterable import RandomIntegerFactory

r = RandomIntegerFactory(1, 100)
for i, r1 in zip(xrange(3), r):
    print i, r1,
    for j, r2 in zip(xrange(3), r):
        print r2,
    print
