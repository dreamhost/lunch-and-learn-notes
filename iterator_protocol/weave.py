

def weave(*args):
    inputs = [iter(a) for a in args]
    while True:
        for i in inputs:
            yield i.next()


if __name__ == '__main__':
    print list(weave('abc', '123'))
    print list(weave('abc', '12'))
    print list(weave('ab', '123'))
