from itertools import *

for i in compress([-1, 0, 1, 2, -2], cycle([1, 0])):
    print 'Yielding:', i
