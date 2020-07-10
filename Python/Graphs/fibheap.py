''' A module that implements Fibonacci Heap.

    Author: Miloš Pivaš, student
'''

class FibonacciHeap:
    '''Implements Fibonacci Heap operations:
            0. get_min()    - returns minimum element
            1. push(key)    - adds a node to the root list
            2. merge()      - merges all pairs of trees of the same degree,
                starting from the smallest ones,
                until there are no two of the same degree;
                Two trees are mereged by making the tree with the larger root
                a child of the other tree's root.
            3. pop_min()    - removes min;
                promotes its children to root list;
                merge();
                update min;
            4. decrease(key, new_key) - decreases the key key;
                if the new value doesn't keep the heap property:
                    promotes the node (with its children) to the root list;
                    raises its parent's lost_a_child flag;
                    if the flag was already raised,
                        promote the parent (with its children) to the root list;                                
    '''

    v = '0.1'

    class Node:
        'Implements a Node in the Fibonacci Heap'

        def __init__(self, key):
            self.key = key
            self.parent = None
            self.children = set()
            self.lost_a_child = False
            self.degree = 0

    def __init__(self):
        self.root_list = set()
        self.min = None


# ### ----- testing -----

# x = FibonacciHeap.Node(42)

# print("Exiting...")
        
