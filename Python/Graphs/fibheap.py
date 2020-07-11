''' A module that implements Fibonacci Heap.

    Author: Miloš Pivaš, student
'''

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

    def push_node(self, node):
        'Add a node to the root list'

        if node.degree not in self.root_list:
            self.root_list[node.degree] = set()

        self.root_list[node.degree].add(node)
    
        if node.key < self.min:
            self.min = node.key
            self.min_node = node
        
        node.parent = None

    def push(self, key):
        'Insert a key into the Fibonacci heap'

        aux = self.Node(key)
        self.push_node(aux)

    def merge(self):
        ''' Merge all pairs of trees of the same degree.
        (the degree is tree size i.e. the number of nodes in the tree)
        Starting from the smallest ones, merge all pairs of trees
        until there are no two of the same degree.
        Two trees are mereged by making the tree with the larger root
        a child of the other tree's root.'
        '''
        degrees = list(self.root_list.keys())
        degrees.sort(key = lambda x: -x)

        while len(degrees) > 0:
            d = degrees.pop()

            while len(self.root_list[d]) >= 2:
            # until there less than 2 trees of the degree d remain

                # pop two trees
                larger = self.root_list[d].pop()
                smaller = self.root_list[d].pop()

                # identify the smaller
                if larger.key < smaller.key:
                    aux = larger
                    larger = smaller
                    smaller = aux
                
                # merge the two d-degree trees into one 2*d-degree tree
                smaller.children.add(larger)
                larger.parent = smaller
                smaller.degree = 2*d

                self.push_node(smaller)
                
                if (len(self.root_list[d]) >= 2) and ((degrees == []) or (degrees[-1] != 2*d)):
                # if there is another pair of trees of the degree d to be merged
                # and the degree 2*d isn't next to be processed
                    # push 2*d to the list of degrees to be processed
                    # (we will now have to merge at least one pair of 2*d degree trees)
                    degrees.append(2*d)

    def pop_min(self):
        ''' Removes and returns the minimum element.
            Side-effects:
                - promotes min's children to root list;
                - performs merge();
                - updates min;
        '''
        if self.min_node is None:
            return None

        # else
        old_min = self.min

        self.root_list[self.min_node.degree].remove(self.min_node)
        
        for c in self.min_node.children:
            self.push_node(c)   # this also updates min
        
        self.merge()
        
        return old_min     

# ### ----- testing -----
# x = FibonacciHeap.Node(42)
# fh = FibonacciHeap()
# fh.push(333)
# fh.push(42)
# fh.push(73)
# fh.push(2112)

# fh.merge()

# x = fh.pop_min()

# print("Exiting...")
        
