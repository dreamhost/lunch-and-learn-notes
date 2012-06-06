import random


def random_integers(min, max):
    r = random.Random()
    while True:
        yield r.randint(min, max)


for i, j in zip(xrange(3), random_integers(1, 100)):
    print i, j
