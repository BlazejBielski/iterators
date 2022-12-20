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


def from_iterable(iterables):
