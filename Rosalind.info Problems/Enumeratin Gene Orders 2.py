import itertools

def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in itertools.permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)

x = '123456'
y = 6

print combinations(x,y)