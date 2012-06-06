import itertools


def weave(*args):
    return itertools.imap(next, itertools.cycle(iter(a) for a in args))


if __name__ == '__main__':
    print list(weave('abc', '123'))
    print list(weave('abc', '12'))
    print list(weave('ab', '123'))
