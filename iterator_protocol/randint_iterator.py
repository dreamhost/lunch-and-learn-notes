import random


class RandomIntegerIterator(object):

    def __init__(self, factory):
        self.factory = factory

    def next(self):
        return self.factory.get_number()


class RandomIntegerFactory(object):

    def __init__(self, min, max, seed=None, step=1):
        self.rand = random.SystemRandom(seed)
        self.seed = seed
        self.min = min
        self.max = max
        self.step = step

    def get_number(self):
        return self.rand.randrange(self.min, self.max, self.step)

    def __iter__(self):
        return RandomIntegerIterator(self)


if __name__ == '__main__':
    r = RandomIntegerFactory(1, 100)
    for i, j in zip(xrange(3), r):
        print i, j
