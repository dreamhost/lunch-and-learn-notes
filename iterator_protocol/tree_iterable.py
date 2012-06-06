class Tree(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.traversal = []

    def __str__(self):
        return self.data

    def __iter__(self):
        inorder(self, self.traversal.append)
        return self

    def next(self):
        if self.traversal:
            return self.traversal.pop(0)
        raise StopIteration()


def inorder(t, f):
    """Call f with tree.data value using inorder traversal.
    """
    if t.left:
        inorder(t.left, f)
    f(t.data)
    if t.right:
        inorder(t.right, f)


if __name__ == '__main__':
    root = Tree('root',
                Tree('left', Tree('L1'), Tree('L2')),
                Tree('right', Tree('R1'), Tree('R2')),
                )
    for node in root:
        print node
