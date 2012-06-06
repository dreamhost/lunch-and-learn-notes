import itertools


class TreeTraversal(object):

    def __init__(self, root):
        self.root = root
        self.traversal = self._make_iterator()

    def _make_iterator(self):
        raise NotImplementedError('override me!')

    def __iter__(self):
        return self

    def next(self):
        return self.traversal.next()


class InOrder(TreeTraversal):

    def _make_iterator(self):
        return itertools.chain(
            iter(self.root.left) if self.root.left else [],
            [self.root.data],
            iter(self.root.right) if self.root.right else [],
            )


class PreOrder(TreeTraversal):

    def _make_iterator(self):
        return itertools.chain(
            [self.root.data],
            iter(self.root.left) if self.root.left else [],
            iter(self.root.right) if self.root.right else [],
            )


class PostOrder(TreeTraversal):

    def _make_iterator(self):
        return itertools.chain(
            iter(self.root.left) if self.root.left else [],
            iter(self.root.right) if self.root.right else [],
            [self.root.data],
            )


class Tree(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return self.data

    def __iter__(self):
        return InOrder(self)


if __name__ == '__main__':
    root = Tree('root',
                Tree('left', Tree('L1'), Tree('L2')),
                Tree('right', Tree('R1'), Tree('R2')),
                )
    print 'In     Pre    Post'
    print '-----  -----  -----'
    for _in, pre, post in zip(InOrder(root), PreOrder(root), PostOrder(root)):
        print '%-6s %-6s %s' % (_in, pre, post)
