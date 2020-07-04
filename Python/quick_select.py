""" quick_select.py
    
    author: Miloš Pivaš, student
"""

from random import randrange
from random import shuffle


class QuickSelect:
    'A class implementing Quickselect for finding the k-th order statistic'

    version = '0.1'

    @staticmethod
    def swap(a: list, i: int, j: int) -> None:
        'Swaps elements from a at positions i and j'
        
        aux = a[i]
        a[i] = a[j]
        a[j] = aux
        pass

    @staticmethod
    def partition(a: list, start: int, stop: int, pivot: int) -> int:
        'Partitions the list a[start:stop] around a[pivot]'
        
        QuickSelect.swap(a, start, pivot)
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
                QuickSelect.swap(a, j, i)

        QuickSelect.swap(a, start, i)
        return i

    @staticmethod
    def select(a: list, k: int, start: int = 0, stop: int = None) -> int:
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

        pivot_order = pivot + 1 - start
        if pivot_order == k:  # if pivot is the k-th order statistic
            return a[pivot]  # return the pivot
        elif pivot_order > k:  # if pivot is bigger than the k-th order statistic
            # search in the smaller subarray, left to the pivot
            return QuickSelect.select(a, k, start, pivot)
        else:  # if pivot is smaller than the k-th order statistic
            #   search to the right side of the pivot for the statistic
            #   whose order is equal to the distance between
            #   the pivot and the k-th order statistic
            k_new = k - pivot_order
            return QuickSelect.select(a, k_new, pivot+1, stop)


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
