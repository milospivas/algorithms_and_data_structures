""" quick_sort.py
    
    author: Miloš Pivaš, student
"""

from random import randrange
from random import shuffle

class QuickSort:
    'A class implementing Quicksort'

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
        QuickSort.swap(a, start, pivot)

        i = start
        for j in range(start+1, stop):
            if a[j] < a[start]:
                QuickSort.swap(a, j, i+1)
                i += 1

        QuickSort.swap(a, start, i)
        return i

    @staticmethod
    def sort(a : list, start : int = 0, stop : int = None) -> None:
        'Recursive Quicksort function'
        if stop is None:
            stop = len(a)
            
        n = stop - start
        if n <= 1:
            return
    
        pivot = randrange(start, stop)
        pivot = QuickSort.partition(a, start, stop, pivot)

        QuickSort.sort(a, start, pivot)
        QuickSort.sort(a, pivot+1, stop)


a = []
QuickSort.sort(a)
assert a == sorted(a)

n = 10
r = range(n)
a = list(r)

repetitions = 100

for i in range(repetitions):
    shuffle(a)
    # print("List:", a)
    QuickSort.sort(a)
    assert a == sorted(a)
    # print("Sorted:", a)

a = a + a

for i in range(repetitions):
    shuffle(a)
    # print("List:", a)
    QuickSort.sort(a)
    assert a == sorted(a)
    # print("Sorted:", a)