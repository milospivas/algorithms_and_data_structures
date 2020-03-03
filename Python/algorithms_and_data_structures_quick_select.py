""" quick_select.py
    
    author: Miloš Pivaš, student
"""

from random import randrange
from random import shuffle

class QuickSelect:
    'A class implementing Quickselect for finding the k-th order statistic'

    version = '0.1'

    @staticmethod
    def swap(a : list, i : int, j : int) -> None:
        'Swaps elements from a at positions i and j'
        aux = a[i]
        a[i] = a[j]
        a[j] = aux
        pass


    @staticmethod
    def partition(a : list, start : int, stop : int, pivot : int) -> int:
        'Partition the list a[start:stop] around a[pivot]'
        QuickSelect.swap(a, start, pivot)

        i = start
        for j in range(start+1, stop):
            if a[j] < a[start]:
                QuickSelect.swap(a, j, i+1)
                i += 1

        QuickSelect.swap(a, start, i)
        return i

    @staticmethod
    def select(a : list, k : int, start : int = 0, stop : int = None) -> int:
        'Recursive Quickselect function'
        if stop is None:
            stop = len(a)
            
        n = stop - start
        if n == 1:
            return a[start]
        if n < 1:
            return []
    
        pivot = randrange(start, stop)
        pivot = QuickSelect.partition(a, start, stop, pivot)

        if pivot + 1 - start == k:
            return a[pivot]
        elif pivot + 1 - start > k:
            return QuickSelect.select(a, k, start, pivot)
        else:
            return QuickSelect.select(a, k - (pivot + 1 - start) , pivot+1, stop)



a = []
x = QuickSelect.select(a, len(a)//2)
assert x == []

n = 4
r = range(n)
a = list(r)

repetitions = 100
k = len(a)//2
for _ in range(repetitions):
    shuffle(a)
    x = QuickSelect.select(a, k)
    assert x == sorted(a)[k - 1]

a = a + a
k = len(a)//2
for _ in range(repetitions):
    shuffle(a)
    x = QuickSelect.select(a, k)
    assert x == sorted(a)[k - 1]