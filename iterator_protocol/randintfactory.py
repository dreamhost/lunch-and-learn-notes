import random


class RandomIntegerFactory(object):

    def __init__(self, min, max, seed=None, step=1):
        self.rand = random.SystemRandom(seed)
        self.seed = seed
        self.min = min
        self.max = max
        self.step = step

    def get_number(self):
        return self.rand.randrange(self.min, self.max, self.step)


if __name__ == '__main__':
    r = RandomIntegerFactory(1, 100)
    for i in xrange(3):
        print i, r.get_number()
