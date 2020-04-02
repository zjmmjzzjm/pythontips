x = {'a':1, 'hello': 'world'}
y = {'b':2, 'hello': 'kitty'}

z = {**x, **y}

print(z)

z = {**x, 'foo': 1, 'bar': 2, **y}
print(z)

def merge_two_dicts(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z
z = merge_two_dicts(x, y)
print(z)


#This uses the dict constructor, and is very fast and memory efficient (even slightly more-so than our two-step process) but unless you know precisely what is happening here (that is, the second dict is being passed as keyword arguments to the dict constructor), it's difficult to read, it's not the intended usage, and so it is not Pythonic.
z = dict(x, **y)
print(z)
# z = dict(x.items() + y.items())

# z3 = x | y

z= {k: v for d in [x,y] for k, v in d.items()}
print(z)


import itertools
z = dict(itertools.chain(x.items(), y.items()))
print(z)

import timeit
print(min(timeit.repeat(lambda: {**x, **y})))
print(min(timeit.repeat(lambda: dict(x, **y))))
print(min(timeit.repeat(lambda: merge_two_dicts(x, y))))
print(min(timeit.repeat(lambda: {k: v for d in (x, y) for k, v in d.items()} )))
print(min(timeit.repeat(lambda: dict(itertools.chain(x.items(), y.items())))))