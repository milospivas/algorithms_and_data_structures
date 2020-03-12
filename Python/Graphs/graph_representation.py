""" 
    The module includes two variations on the adjacency lists graph representation.
    1) The 'classic' approach for graph representation via an array of linked lists.
    2) A cleaner approach for graph representation via a hashmap of hashsets.
"""

# 1) the array of linked lists approach:
from lists import LinkedList

class AdjacencyList:
    'Implements the adjacency lists as an array of linked lists.'

    def __init__(self, n : int, directed : bool = True):
        self.n = n
        self.a = [LinkedList() for _ in range(n)]
        self.directed = directed
        pass

    def add(self, u : int, v : int):
        if 0 <= u and u < self.n and 0 <= v and v < self.n:
            self.a[u].add_tail(v)
            if not self.directed:
                self.a[v].add_tail(u)
    
    def __str__(self):
        s = "Edges are:\n"
        for u, adj_u in enumerate(self.a):
            aux = adj_u.head
            while aux is not None:
                v = aux.val
                if self.directed or v >= u:
                    s = s + str(u) + " - " + str(v) + "\n"
                aux = aux.next
        return s


# 2) the cleaner approach:

class AdjacencySet:
    'Implements adjacency list as a hashmap of hashsets.'

    def __init__(self, directed : bool = True):
        self.a = {}
        self.directed = directed
        self.V = 0
        self.E = 0

    def add_directed(self, u : any, v : any):
        'Add a directed edge from u to v to the graph.'
        if u not in self.a:
            self.a[u] = set()
            self.V += 1
        
        if v not in self.a[u]:
            self.a[u].add(v)
            self.E += 1        

    def add(self, u : any, v : any):
        'Add an edge u->v i.e. u-v to the graph'
        self.add_directed(u, v)
        if not self.directed:
            self.add_directed(v, u)

    def neighbors(self, u : any):
        'Return the set of neighbors of u'
        if u in self.a:
            return self.a[u]
        else:
            return None

    def __str__(self):
        s = "Edges are:\n"
        for u in self.a:
            for v in self.a[u]:
                if self.directed or v >= u:
                    s = s + str(u) + " - " + str(v) + "\n"
        return s


# n = 10
# Adj = AdjacencyList(n, False)
# Adj.add(1, 2)
# Adj.add(2, 1)
# Adj.add(3, 7)
# Adj.add(5, 3)
# print(Adj)

# Adj = AdjacencySet()
# Adj.add(1, 2)
# Adj.add(2, 1)
# Adj.add(3, 7)
# Adj.add(5, 3)
# print(Adj)

# print("Exiting...")