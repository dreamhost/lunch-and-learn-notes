import random


comprehension = [random.randint(1, 100)
                 for i in xrange(3)
                 ]
print comprehension

generator = (random.randint(1, 100)
             for i in xrange(3)
             )
print generator
print list(generator)
