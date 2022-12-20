def is_perfect_length(sequence):
    """True if sequence has length 2**n -1
       Otherwise False
    """
    n = len(sequence)
    return ((n + 1) & n == 0) and (n != 0)


class LevelOrderIterator:

    def __init__(self, sequence):
        self._sequence = self._is_perfect_length(sequence)
        self._idx = 0

    @staticmethod
    def _is_perfect_length(sequence):
        if not is_perfect_length(sequence):
            raise ValueError(f'Sequence of length {len(sequence)} does not represent a perfect binary '
                             f'tree with length 2 ** n -1')

        return sequence

    def __iter__(self):
        return self

    def __next__(self):
        if self._idx >= len(self._sequence):
            raise StopIteration

        result = self._sequence[self._idx]
        self._idx += 1

        return result


def left_child(idx):
    return 2 * idx + 1


def right_child(idx):
    return 2 * idx + 2


class PreorderIterator:
    def __init__(self, sequence):
        self._sequence = self._is_perfect_length(sequence)
        self._stack = [0]

    @staticmethod
    def _is_perfect_length(sequence):
        if not is_perfect_length(sequence):
            raise ValueError(f'Sequence of length {len(sequence)} does not represent a perfect binary '
                             f'tree with length 2 ** n -1')

        return sequence

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._stack) == 0:
            raise StopIteration

        idx = self._stack.pop()
        result = self._sequence[idx]

        right_child_index = right_child(idx)
        if right_child_index < len(self._sequence):
            self._stack.append(right_child_index)

        left_child_index = left_child(idx)
        if left_child_index < len(self._sequence):
            self._stack.append(left_child_index)

        return result


class InOrderIterator:

    def __init__(self, sequence):
        self._sequence = self._is_perfect_length(sequence)
        self._stack = []
        self._idx = 0

    @staticmethod
    def _is_perfect_length(sequence):
        if not is_perfect_length(sequence):
            raise ValueError(f'Sequence of length {len(sequence)} does not represent a perfect binary '
                             f'tree with length 2 ** n -1')

        return sequence

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._stack) == 0 and self._idx >= len(self._sequence):
            raise StopIteration

        while self._idx < len(self._sequence):
            self._stack.append(self._idx)
            self._idx = left_child(self._idx)

        index = self._stack.pop()
        result = self._sequence[index]
        self._idx = right_child(index)

        return result


class PostOrderIterator:

    def __init__(self, sequence):
        self._sequence = self._is_perfect_length(sequence)
        self._idx = 0
        self._stack = [0]

    @staticmethod
    def _is_perfect_length(sequence):
        if not is_perfect_length(sequence):
            raise ValueError(f'Sequence of length {len(sequence)} does not represent a perfect binary '
                             f'tree with length 2 ** n -1')

        return sequence

    def __iter__(self):
        return self

    def __next__(self):
        if len(self._stack) == 0 and self._idx >= len(self._sequence):
            raise StopIteration

        while self._idx < len(self._sequence):
            self._stack.append(self._idx)
            self._idx = left_child(self._idx)

        index = self._stack.pop()
        result = self._sequence[index]
        self._idx = right_child(index)

        return result


missing = object()


class SkipMissingIterator:
    def __init__(self, iterable):
        self._iterator = iter(iterable)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self._iterator)
            if item is not missing:
                return item


typesetting_table = {
    "-": "\u2212",  # Minus sign
    "*": "\u00D7",  # Multiplication sign
    "/": "\u00F7",  # Division sign
}


class TranslationIterator:
    def __init__(self, iterable, table):
        self._iterator = iter(iterable)
        self._table = table

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self._iterator)
        return self._table.get(item, item)


# r + p * q

tree = ['*', '+', '-', 'a', 'b', 'c', 'd']
iterator = PostOrderIterator(tree)
print(' '.join(iterator))
# tree = ['-', '*', '/', 'p', 'q', 'r', '+', missing, missing, missing, missing, missing, missing, 's', 't']
# iterator = TranslationIterator(SkipMissingIterator(InOrderIterator(tree)), typesetting_table)
# print(' '.join(iterator))
