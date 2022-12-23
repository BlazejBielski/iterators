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


class Chain:
    def __init__(self, *iterable):
        self._iterable = iterable
        self._idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx >= len(self._iterable):
            raise StopIteration

        result = list(self._iterable)[0][self._idx]
        self._idx += 1
        yield result
