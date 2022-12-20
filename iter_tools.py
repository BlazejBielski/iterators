def count(start=0, step=1):
    # count(20) --> 20, 21, 22, 23 ...
    # count(2.5, 0.5) --> 2.5, 3.0, 3.5 ...
    n = start
    while True:
        yield n
        n += step


def chain(*iterables):
    # chain ('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element


def cycle(iterable):
    # cycle('ABCD') --> A B C D A B C D A B C D ...
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element


def repeat(obj, times=None):
    # repeat(10, 3) --> 10 10 10
    if times is None:
        while True:
            yield obj
    else:
        for i in range(times):
            yield obj


def accumulate(iterable, func=operator.add, * , initial=None):
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5]), initial=100 --> 101 103 106 110 115
    # accumulate([1,2,3,4,5]), operator.mul --> 1 2 6 24 120
    it = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return

    yield total
    for element in it:
        total = func(total, element)
        yield total


