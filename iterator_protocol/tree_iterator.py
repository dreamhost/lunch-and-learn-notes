class TreeIterator(object):

    def __init__(self, root, traversal='in'):
        self.root = root
        traversal_method = getattr(self, '_%s_order' % traversal)
        self.traversal = traversal_method(root)

    def __iter__(self):
        return self

    def next(self):
        return self.traversal.next()

    @staticmethod
    def _in_order(tree):
        if tree.left is not None:
            for l in tree.left:
                yield l
        yield tree.data
        if tree.right is not None:
            for r in tree.right:
                yield r

    @staticmethod
    def _pre_order(tree):
        yield tree.data
        if tree.left is not None:
            for l in tree.left:
                yield l
        if tree.right is not None:
            for r in tree.right:
                yield r

    @staticmethod
    def _post_order(tree):
        if tree.left is not None:
            for l in tree.left:
                yield l
        if tree.right is not None:
            for r in tree.right:
                yield r
        yield tree.data


class Tree(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return self.data

    def __iter__(self):
        return TreeIterator(self)


if __name__ == '__main__':
    root = Tree('root',
                Tree('left', Tree('L1'), Tree('L2')),
                Tree('right', Tree('R1'), Tree('R2')),
                )
    iterators = [TreeIterator(root, 'in'),
                 TreeIterator(root, 'pre'),
                 TreeIterator(root, 'post'),
                 ]
    print 'In     Pre    Post'
    print '-----  -----  -----'
    for _in, pre, post in zip(*iterators):
        print '%-6s %-6s %s' % (_in, pre, post)
