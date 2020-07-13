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

    def __init__(self, directed : bool = True, weighted : bool = False):
        self.directed = directed
        self.weighted = weighted
        self.fromto = {}    # keeps the outgoing edges
        self.tofrom = {}    # keeps the incoming edges
        self.W = {}         # keeps the weights of edges
        self.V = set()
        self.E = 0

    def add_directed(self, u : any, v : any, w = None):
        'Add a directed edge from u to v to the graph.'
        if u not in self.fromto:
            self.fromto[u] = set()
        
        if v not in self.fromto[u]:
            self.fromto[u].add(v)
            self.E += 1
        
        if v not in self.tofrom:
            self.tofrom[v] = set()
        
        if u not in self.tofrom[v]:
            self.tofrom[v].add(u)
        
        if u not in self.V:
            self.V.add(u)

        if v not in self.V:
            self.V.add(v)

        if self.weighted:
            if u not in self.W:
                self.W[u] = {}
            
            self.W[u][v] = w
        

    def add(self, u : any, v : any, w = None):
        'Add an edge u->v i.e. u-v to the graph'
        self.add_directed(u, v, w)
        if not self.directed:
            self.add_directed(v, u, w)

    def vertices(self):
        'Return the list of vertices in the graph'
        return self.V

    def neighbors(self, u : any):
        'Return the set of neighbors of u'
        if u in self.fromto:
            return self.fromto[u]
        else:
            return set()

    def neighbors_incoming(self, u : any):
        'Return the set of vertices who\'s neighbor is u'
        if u in self.tofrom:
            return self.tofrom[u]
        else:
            return set()

    def vertices_outgoing(self):
        'Return the set vertices with outgoing edges'
        return set(self.fromto.keys())
                 
    def vertices_incoming(self):
        'Return the set vertices with incoming edges'
        return set(self.tofrom.keys())

    def __str__(self):
        s = "Edges are:\n"
        for u in self.fromto:
            for v in self.fromto[u]:
                if self.directed or v >= u:
                    s += str(u) + " - " + str(v)
                    if self.weighted:
                        s += ', w = ' + str(self.W[u][v])
                    s += "\n"
        return s

    def __len__(self):
        return len(self.V)

# n = 10
# Adj = AdjacencyList(n, False)
# Adj.add(1, 2)
# Adj.add(2, 1)
# Adj.add(3, 7)
# Adj.add(5, 3)
# print(Adj)

# Adj = AdjacencySet(weighted=True)
# Adj.add(1, 2, 42)
# Adj.add(2, 1, 21)
# Adj.add(3, 7, 55)
# Adj.add(5, 3, 73)
# print(Adj)
# print(Adj.V)
# print(len(Adj))

# print("Exiting...")