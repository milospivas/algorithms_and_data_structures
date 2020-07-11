''' A module that implements Fibonacci Heap.

    Author: Miloš Pivaš, student
'''

class FibonacciHeap:
    '''Implements Fibonacci Heap'''

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
        '''Return the name and key of the minimum element
        
        Returns
        -------
        (str, int)
            (name, key) pair of the minimum key element
        (None, None)
            if the heap is empty
        '''

        if self.min_node is not None:
            return self.min_node.name, self.min_node.key
        else:
            return None, None

    def push_node(self, node):
        '''Insert a node into the Fibonacci heap's root list
        
        Parameters
        ----------
        node:   Node
            a node to be pushed on to the heap
        
        Returns
        -------
        Node
            the pushed node
        '''

        if node.degree not in self.root_list:
            self.root_list[node.degree] = set()

        self.root_list[node.degree].add(node)
    
        if node.key < self.min:
            self.min = node.key
            self.min_node = node
        
        node.parent = None

        return node


    def push(self, name, key):
        '''Insert a node with given name and key into the Fibonacci heap
        
        Parameters
        ----------
        name : str
            a name assigned to the node
        key : int
            a key assigned to the node
        
        Returns
        -------
        Node
            inserted node's reference

        Raises
        ------
        Exception
            If a node with the same name is already in the heap
        '''

        new_node = self.Node(name, key)
        self.push_node(new_node)

        if name in self.node_index:
            raise Exception("Node with the same name is already in the heap!")

        self.node_index[name] = new_node
        return new_node


    def merge(self):
        ''' Merge all pairs of trees of the same degree in the heap's root list.

        The degree is tree size i.e. the number of nodes in the tree.
        Starting from the smallest ones, merge all pairs of trees
        until there are no two of the same degree.
        Two trees are mereged by making the tree with the larger root
        a child of the other tree's root.
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
        ''' Removes the minimum-key element and returns its name and key.
            
        Side-effects:
            - promotes min's children to heap's root list;
            - performs merge();
            - updates min;
            
        Returns
        -------
        (str, int)
            (name, key) pair of the minimum key element
        (None, None)
            if the heap is empty
        '''

        if self.min_node is None:
            return None, None

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
        
        return old_min_node.name, old_min_node.key


    def decrease_key(self, name, new_key):
        ''' Decreases the key of the node with given name to new_key.

        If the new key doesn't maintain the heap property:
            1. Promote the node (with its children) to the root list;
            2. Decrease the parent's degree
            3. If the parent's flag was already raised,
                    goto 1. with current node's parent as the new current node
            4. Else:
                - Raise its parent's lost_a_child flag;
                - Go up the tree and decrease each parent's degree
                by the degree removed from the tree

        Parameters
        ----------
        name : str
            The name of the element who's key is to be decreased
        new_key : int
            The new, decreased key value

        Raises
        ------
        Exception
            If new_key isn't smaller than the current one
        '''
                        
        # get the node
        curr = self.node_index[name]
                
        # decrease the key
        if new_key > curr.key:
            raise Exception('New key does not decrease the old key')
        curr.key = new_key

        # check if it maintains the heap property
        if curr.parent is None or curr.parent.key <= curr.key:
            return

        degree_removed = 0
        done = False

        while not done:
            # cut the node from its parent
            parent = curr.parent
            parent.children.remove(curr)

            # add the node's degree to degree_removed accumulator
            degree_removed += curr.degree

            # promote the node to the root list
            self.push_node(curr)
            
            # go up the tree
            curr = parent

            # if we're at the root, save the degree
            if curr.parent is None:
                old_degree = curr.degree
            
            # decrease the degree
            curr.degree -= degree_removed

            if curr.parent is not None:
            # if we aren't in the root 
                if not curr.lost_a_child:
                # if the node hasn't already lost a child
                    curr.parent.lost_a_child = True
                    done = True
            else:
            # if we are in the root
                done = True
        
        # go up the tree and decrease the degree by degree_removed
        while curr.parent is not None:
            curr = curr.parent
            
            if curr.parent is None:
            # if we've reached the root of the tree
                # save the old degree
                old_degree = curr.degree

            curr.degree -= degree_removed

        # remove the tree from the old degree entry
        self.root_list[old_degree].remove(curr)
        if len(self.root_list[old_degree]) == 0:
            self.root_list.pop(old_degree)
        
        # push the tree to root list (to be in the new degree entry)
        self.push_node(curr)


# # ### ----- testing -----
# # x = FibonacciHeap.Node('X', 42)
# # fh = FibonacciHeap()
# # fh.push('A', 10)
# # fh.push('B', 11)
# # fh.push('C', 12)
# # fh.push('D', 13)
# # fh.push('E', 14)
# # fh.push('F', 15)
# # fh.push('G', 16)
# # fh.push('H', 17)

# # fh.merge()

# # # name = 'X'
# # # while name is not None:
# # #     name, key = fh.pop_min()
# # #     print(name, key)

# # fh.decrease_key('H', 7)
# # fh.decrease_key('G', 6)
# # fh.decrease_key('F', 5)
# # fh.decrease_key('E', 4)
# # # fh.decrease_key('D', 3)
# # # fh.decrease_key('B', 1)
# # # fh.decrease_key('C', 2)
# # # fh.decrease_key('A', 0)

# help(FibonacciHeap)

# print("Exiting...")
        
