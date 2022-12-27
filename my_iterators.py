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
        length = len(self._iterables)
        if self._idx >= length:
            raise StopIteration

        else:
            for idx in range(length):
                idx += 1
                if length > idx:
                    return self._iterables


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
