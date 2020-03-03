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
