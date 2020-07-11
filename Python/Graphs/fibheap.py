''' A module that implements Fibonacci Heap.

    Author: Miloš Pivaš, student
'''

from collections import deque

class FibonacciHeap:
    '''Implements Fibonacci Heap operations:
            0. get_min()    - return the minimum element
            1. push(key)    - add a node to the root list
                            check and update min;
            2. merge()      - merge all pairs of trees of the same degree,
                (the degree is tree size i.e. the number of nodes in the tree),
                starting from the smallest ones,
                until there are no two of the same degree;
                Two trees are mereged by making the tree with the larger root
                a child of the other tree's root.
            3. pop_min()    - remove the min;
                promotes its children to root list;
                merge();
                update min;
            4. decrease(key, new_key) - decreases the key key;
                if the new value doesn't keep the heap property:
                    promotes the node (with its children) to the root list;
                    raises its parent's lost_a_child flag;
                    if the flag was already raised,
                        promote the parent (with its children) to the root list;
                decrease() method is lazy   - it doesn't clean up, it leaves the clean up to pop_min().
    '''

    v = '0.1'

    class Node:
        'Implements a Node in the Fibonacci Heap'

        BASE_DEGREE = 1     # or maybe keep it as 0

        def __init__(self, key):
            self.key = key
            self.parent = None
            self.children = set()
            self.lost_a_child = False
            self.degree = self.BASE_DEGREE

    def __init__(self):
        self.root_list = {}
        self.min = float('Inf')
        self.min_node = None

    def get_min(self):
        'Return the minimum key'

        return self.min

    def push(self, key):
        'Add a node to the root list'

        if self.Node.BASE_DEGREE not in self.root_list:
            self.root_list[self.Node.BASE_DEGREE] = set()

        aux = self.Node(key)
        self.root_list[self.Node.BASE_DEGREE].add(aux)
    
        if key < self.min:
            self.min = key
            self.min_node = aux

    def merge(self):
        ''' Merge all pairs of trees of the same degree.
        (the degree is tree size i.e. the number of nodes in the tree)
        Starting from the smallest ones, merge all pairs of trees
        until there are no two of the same degree.
        Two trees are mereged by making the tree with the larger root
        a child of the other tree's root.'
        '''
        degrees = deque(sorted(self.root_list.keys()))

        while len(degrees) > 0:
            d = degrees.popleft()

            while len(self.root_list[d]) >= 2:
            # until there is less than 2 trees of the degree d

                # pop two trees
                larger = self.root_list[d].pop()
                smaller = self.root_list[d].pop()

                # identify the smaller
                if larger.key < smaller.key:
                    aux = larger
                    larger = smaller
                    smaller = aux
                
                # merge the two trees
                smaller.children.add(larger)
                smaller.degree = 2*d


                if 2*d not in self.root_list:
                # if no trees of the 2*d degree existed
                    # init. the root list entry
                    self.root_list[smaller.degree] = set()

                    
                    if len(self.root_list[d]) >= 2:
                    # if there is another pair of trees of the degree d to be merged
                        # push 2*d to the list of degrees to be processed
                        # (we will now have to merge at least one pair of 2*d degree trees)
                        degrees.appendleft(2*d)

                # add the new tree to the root list
                self.root_list[smaller.degree].add(smaller)


# ### ----- testing -----
# x = FibonacciHeap.Node(42)
# fh = FibonacciHeap()
# fh.push(333)
# fh.push(42)
# fh.push(73)
# fh.push(2112)

# fh.merge()

# print("Exiting...")
        
