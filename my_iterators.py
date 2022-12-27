class Count:
    # count(20) --> 20, 21, 22, 23 ...
    def __init__(self, start=0, step=1):
        self._start = start
        self._step = step

    def __iter__(self):
        return self

    def __next__(self):
        result = self._start
        self._start += self._step
        yield result


# not completed yet
class Chain:
    def __init__(self, *iterables):
        self._iterables = iterables
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        yield [element for sublist in self._iterables for element in sublist]


class Repeat:
    def __init__(self, element, times=None):
        self._times = times
        self._element = element
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._times is None:
            yield self._element

        else:

            if self._idx < self._times:
                self._idx += 1
                yield self._element

            else:
                raise StopIteration


class Cycle:
    def __init__(self, iterable):
        self._iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        yield [element for element in self._iterable]
