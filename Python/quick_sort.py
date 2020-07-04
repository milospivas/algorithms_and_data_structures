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
        'Partitions the list a[start:stop] around a[pivot]'
        
        QuickSort.swap(a, start, pivot)
        # now the pivot element is at a[start]

        # using two indices i and j,
        # we are iteratively partitioning the array into 4 parts:
        #     1. a[start]            <- the pivot element
        #     2. a[start+1 : i+1]    <- elements less than or equal to the pivot
        #     3. a[i+1 : j]          <- elements greater than the pivot
        #     4. a[j : stop]         <- elements unpartitioned
        i = start
        for j in range(start+1, stop):
            if a[j] < a[start]:
            # if element a[j] violates the property of the part 3.
                # swap it into part 2.
                i += 1
                QuickSort.swap(a, j, i)

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