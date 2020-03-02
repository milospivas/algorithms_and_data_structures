"""
Binary heap module.
Can be passed a custom compare function cmp.

Time complexity:
Sifting, inserting and extracting are all done in O(log2(n)) time, or more precisely in O(h) time,
where h is the height of the subtree on which the operation is performed,
which itself is h = O(log2(n)).

The time complexity of heapify() is O(n) because we're using sift_down ops.
sift_down has O(h) time complexity where h is the height of the node from which we're sifting down.
Since we're going from the end of the array, it takes:
  n/2 * 1 + n/4 * 2 + n/8 * 3 + ... + 1 * log2(n) = O(n)
swaps to efficiently heapify an array with sift_down.

heap_sort() has time complexity O(n*log2(n)),
because, after heapifying, we are performing n sift_down ops from the root,
each with the time complexity O(log2(n)).

"""

class Heap:

    @staticmethod
    def swap(a: list, i: int, j: int):
        """ Swap elements from list a at positions i and j. """
        x = a[i]
        a[i] = a[j]
        a[j] = x

    @staticmethod
    def cmp_max(a: list, i: int, j: int):
        """ Default compare function, which results in having a max heap
        and heap_sort producing an ascending array. """
        if a[i] < a[j]:
            return 1
        if a[i] > a[j]:
            return -1
        return 0

    @staticmethod
    def cmp_min(a: list, i: int, j: int):
        """ Opposite of cmp_max. Results in having a min heap
        and heap_sort producing a descending array. """
        if a[i] < a[j]:
            return -1
        if a[i] > a[j]:
            return 1
        return 0

    @classmethod
    def sift_down(this_class, a: list, n: int, node: int, cmp=None) -> None:
        """ Sift down the heap a[0:n],
        starting from the element node,
        using the function cmp for comparisons.
        If cmp isn't passed or the string "max" is passed, then use cmp_max().
        If "min" is passed, use cmp_min(). """

        if cmp is None or cmp == "max":
            cmp = this_class.cmp_max
        elif cmp == "min":
            cmp = this_class.cmp_min
        p = node
        while 2 * p + 1 < n:
            l = 2 * p + 1
            r = l + 1
            last_flag = False
            if r == n:
                last_flag = True

            # if a[p] <= a[l] and (last_flag or a[p] <= a[r]):
            if cmp(a, p, l) <= 0 and (last_flag or cmp(a, p, r) <= 0):
                break
            else:
                next = l
                # if not last_flag and a[r] < a[l]:
                if not last_flag and cmp(a, r, l) == -1:
                    next = r
                this_class.swap(a, p, next)
                p = next

    @classmethod
    def sift_up(this_class, a: list, node: int, cmp=None) -> None:
        """ Sift up the heap a, starting from the element at node,
        using the function cmp for comparisons.
        If cmp isn't passed or the string "max" is passed, then use cmp_max().
        If "min" is passed, use cmp_min(). """

        if cmp is None or cmp == "max":
            cmp = this_class.cmp_max
        elif cmp == "min":
            cmp = this_class.cmp_min

        c = node
        while c // 2 >= 0:
            p = c // 2
            # if a[p] > a[c]:
            if cmp(a, p, c) == 1:
                this_class.swap(a, p, c)
                c = p

    @classmethod
    def heapify(this_class, a: list, n: int, cmp=None) -> list:
        """ Heapify the list a[0:n],
        using the function cmp for comparisons.
        If cmp isn't passed or the string "max" is passed, then use cmp_max().
        If "min" is passed, use cmp_min(). """

        for i in range(n - 1, -1, -1):
            Heap.sift_down(a, n, i, cmp)

    @classmethod
    def insert(this_class, a: list, n: int, val: int, cmp=None) -> None:
        """ Insert the value val into the heap a[0:n],
        using the function cmp for comparisons.
        If cmp isn't passed or the string "max" is passed, then use cmp_max().
        If "min" is passed, use cmp_min(). """

        a += [val]
        Heap.sift_up(a, n - 1, cmp)

    @classmethod
    def extract(this_class, a: list, n: int, cmp=None) -> "Any":
        """ Exctract the root of the heap a[0:n],
        using the function cmp for comparisons.
        If cmp isn't passed or the string "max" is passed, then use cmp_max().
        If "min" is passed, use cmp_min(). """

        if n == 0:
            return None
        val = a[0]
        a[0] = a[n - 1]
        del (a[n - 1])
        this_class.sift_down(a, n - 1, 0, cmp)
        return val

    @classmethod
    def heap_sort(this_class, a: list, n: int, cmp=None) -> None:
        """ Sort the heap a[0:n],
        using the function cmp for comparisons.
        If cmp isn't passed or the string "max" is passed, then use cmp_max().
        If "min" is passed, use cmp_min(). """

        this_class.heapify(a, n, cmp)
        for i in range(n - 1, -1, -1):
            this_class.swap(a, 0, i)
            this_class.sift_down(a, i, 0, cmp)
