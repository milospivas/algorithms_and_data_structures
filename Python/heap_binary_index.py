""" Index heap.
    Instead of storing values, it stores indices to a given list,
    and uses values from the list for comparisons.
"""
class IndexMinHeapOps:
    'Static class that implements Index-MinHeap operations.'
    @staticmethod
    def swap(a, i, j):
        aux = a[i]
        a[i] = a[j]
        a[j] = aux

    @staticmethod
    def insert(a : list, start : int, stop : int, l : list, idx : int) -> None:
        a[stop] = idx

        if stop == start:
            return
        
        curr = stop
        parent = start + (curr - start)//2
        while parent >= start and l[a[curr]] < l[a[parent]]:
            IndexMinHeapOps.swap(a, curr, parent)
            curr = parent
            parent = start + (curr - start)//2

    @staticmethod
    def extract(a : list, start : int, stop : int, l : list) -> int:
        idx = a[start]

        IndexMinHeapOps.swap(a, start, stop-1)
        stop -= 1

        curr = start
        left = start + (curr - start)*2 + 1
        while left < stop:
            smaller = left
            right = left + 1

            if right < stop and l[a[right]] < l[a[smaller]]:
                smaller = right

            if l[a[smaller]] < l[a[curr]]:
                IndexMinHeapOps.swap(a, smaller, curr)
                curr = smaller
                left = start + (curr - start)*2 + 1
            else:
                break
        return idx

class IndexMinHeap:
    'Implements Index-MinHeap objects'
    
    def __init__(self, a, l):
        self.a = a
        self.l = l
        self.start = 0
        self.stop = 0

    def insert(self, idx) -> None:
        IndexMinHeapOps.insert(self.a, self.start, self.stop, self.l, idx)
        self.stop += 1
    
    def extract(self) -> int:
        idx = IndexMinHeapOps.extract(self.a, self.start, self.stop, self.l)
        self.stop -= 1
        return idx
    
    def peek(self) -> int:
        return self.l[self.a[self.start]]

    def __len__(self):
        return self.stop - self.start

    def __str__(self):
        return '['+', '.join(str(self.l[idx]) for idx in self.a[self.start : self.stop])+']'


def test(l):
    print("swapping")
    print(l)
    IndexMinHeapOps.swap(l, 0, -1)
    print(l)
    IndexMinHeapOps.swap(l, 0, -1)
    print(l)

    print("inserting")
    a = IndexMinHeap([0 for _ in l], l)

    for i in range(len(l)):
        a.insert(i)
        print(l[i], a)

    print("extracting")
    for i in range(len(l)):
        idx = a.extract()
        print(l[idx], a)


# Testing:
l = [4, 3, 2, 1]
test(l)

l = [4, 3, 2, 1, 5, 4, 2, 1, 2, 3, 4]
test(l)