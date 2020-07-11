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

        def __init__(self, name, key):
            self.key = key
            self.name = name
            self.parent = None
            self.children = set()
            self.lost_a_child = False
            self.degree = self.BASE_DEGREE

    def __init__(self):
        self.root_list = {}
        self.node_index = {}
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

        return node


    def push(self, name, key):
        'Insert a key into the Fibonacci heap'

        new_node = self.Node(name, key)
        self.push_node(new_node)

        if name in self.node_index:
            raise Exception("Node with the same name is already in the heap!")

        self.node_index[name] = new_node
        return new_node


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
                
            if len(self.root_list[d]) == 0:
                self.root_list.pop(d)


    def pop_min(self):
        ''' Removes and returns the minimum element.
            Side-effects:
                - promotes min's children to root list;
                - performs merge();
                - updates min;
        '''
        if self.min_node is None:
            return None, None

        # else
        # store old min
        old_min_node = self.min_node
        
        # remove it from the heap
        self.root_list[old_min_node.degree].remove(old_min_node)
        self.node_index.pop(old_min_node.name)
        
        if len(self.root_list[old_min_node.degree]) == 0:
            self.root_list.pop(old_min_node.degree)

        # find new min
        self.min_node = None
        self.min = float('Inf')
        for node_list in self.root_list.values():
            for node in node_list:
                if node.key < self.min:
                    self.min = node.key
                    self.min_node = node

        # promote the children of the old min to root list
        for c in old_min_node.children:
            self.push_node(c)   # updates min
        
        self.merge()
        
        return (old_min_node.name, old_min_node.key)


# ### ----- testing -----
x = FibonacciHeap.Node('X', 42)
fh = FibonacciHeap()
fh.push('A', 333)
fh.push('B', 42)
fh.push('C', 73)
fh.push('D', 2112)

fh.merge()

name = 'X'
while name is not None:
    name, key = fh.pop_min()
    print(name, key)

print("Exiting...")
        
