class Tree(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return self.data

    def __iter__(self):
        if self.left is not None:
            for l in self.left:
                yield l
        yield self.data
        if self.right is not None:
            for r in self.right:
                yield r


if __name__ == '__main__':
    root = Tree('root',
                Tree('left', Tree('L1'), Tree('L2')),
                Tree('right', Tree('R1'), Tree('R2')),
                )
    for node in root:
        print node
