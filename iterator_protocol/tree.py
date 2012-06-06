

class Tree(object):

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return self.data


if __name__ == '__main__':
    root = Tree('root', Tree('left'), Tree('right'))
    print root
    print root.left
    print root.right
