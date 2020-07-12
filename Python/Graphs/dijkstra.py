
'''
    A module that implements Dijkstra's algorithm.
    Depends on: graph_representation.py, fibonacci_heap.py

    Author: Miloš Pivaš, student
'''


from graph_representation import AdjacencySet
from fibonacci_heap import FibonacciHeap

class Dijkstra:
    '''Class that implements Dijkstra\'s algorithm
    
    Intro
    -----
        Dijkstra works on DAGs without negative edges.
        Having no -ve edges allows greedy behaviour.
        If we know the shortest path from s to u is of length d[s][u],
        then for node v that is the nearest unvisited neighbor of u,
        it holds true that d[s][v] = d[s][u] + w[u][v],
        where w[u][v] is the weight of the edge u-v.

        For Dijkstra we need some ADTs (Abstract Data Structures):
        Adj - an AdjacencySet for graph representation.
        d - a hashmap that is going to hold current (and finally shortest) distances from source to each node.
        S - a set that is going to hold all vertices that we know the shortest paths to.
        Q - a priority queue (with decrease_key() operation) that is going to hold all unvisited vertices.
            Q's priorities are the d[] values.

    Time Complexity
    ---------------
                |               |  (sparse)  |    (dense)
        case    |   General     |  E = O(V)  |  E = O(V**2)
        Time    | O(VlogV + E)  |  O(VlogV)  |  O(V**2)
    '''

    v = '0.1'

    @staticmethod
    def relax(u, v, Adj : AdjacencySet, d : dict, Pi : dict):
        '''Relax the path to v via edge u-w.

        Parameters
        ----------
        u : str/int
            The vertex to relax by.
        v : str/int
            The vertex who's path value is to be relax.
        Adj : AdjacencySet
            Datastructure for graph representation.
        d : dict
            Maps vertices to current path lengths from source.
        Pi : dict
            Maps vertices to their predecessor nodes in the paths coming from the source.

        Raises
        ------
        Exception
            'u is not in graph' if u is not in graph.
        Exception
            'v is not connected to u' if v is not connected to u.
        '''

        if not u in Adj.W:
            raise Exception('u is not in graph')
        if not v in Adj.W[u]:
            raise Exception('v is not connected to u')

        if d[u] + Adj.W[u][v] < d[v]:
            d[v] = d[u] + Adj.W[u][v]
            Pi[v] = u


    @classmethod
    def dijkstra(cls, Adj : AdjacencySet, s):
        '''Dijkstra\'s algorithm for single-source shortest paths
        
        Works in graphs without negative cycles.

        Parameters
        ----------
        Adj : AdjacencySet
            Datastructure for graph representation.
        s : str/int
            The source vertex.


        Returns
        -------
        (d : dict, Pi : dict)
            d maps vertices to shortest path lengths from source.
            Pi maps vertices to their predecessor nodes in the paths coming from the source.
        '''

        # initialization
        d = {v:float('Inf') for v in Adj.V}
        d[s] = 0

        Pi = {}
        Q = FibonacciHeap()

        S = set()
        for u in Adj.V:
            if u == s:
                Q.push(s, 0)
            else:
                Q.push(u, float('Inf'))
        
        Q.__str__()
        while not Q.empty():
            u, key = Q.pop_min()
            d[u] = key
            S.add(u)
            for v in Adj.neighbors(u):
                if v not in S:
                    cls.relax(u, v, Adj, d, Pi)
                    Q.decrease_key(v, d[v])

        return d, Pi


# ### testing

# help(Dijkstra)

# ''' Example from MIT OCW Intro to Algorithms lecture 16:
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/MIT6_006F11_lec16.pdf
# '''
# Adj = AdjacencySet(directed=True, weighted=True)
# Adj.add_directed('A', 'B', 10)
# Adj.add_directed('A', 'C', 3)
# Adj.add_directed('B', 'C', 1)
# Adj.add_directed('B', 'D', 2)
# Adj.add_directed('C', 'B', 4)
# Adj.add_directed('C', 'D', 8)
# Adj.add_directed('C', 'E', 2)
# Adj.add_directed('D', 'E', 7)
# Adj.add_directed('E', 'D', 9)

# d, Pi = Dijkstra.dijkstra(Adj, 'A')

# print(d)
# print(Pi)

# print('Exiting...')