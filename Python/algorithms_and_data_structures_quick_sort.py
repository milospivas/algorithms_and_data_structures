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
