"""
Algorithms for Single Source Shortest Paths:
                    |                                         |               Time complexity
    case            |              best algorithm             |    General     |  E = O(V)  |  E = O(V**2)
------------------- |---------------------------------------- | -------------- | ---------- | --------------
w[u][v] = const     |  BFS                                    |  O(V+E)        |  O(V)      |  O(V**2)
DAGs                |  Topo. sort + 1 round of Bellman-Ford   |  O(V+E)        |  O(V)      |  O(V**2)
Nonegative weights  |  Dijkstra                               |  O(VlogV + E)  |  O(VlogV)  |  O(V**2)
General             |  Bellman-Ford                           |  O(VE)         |  O(V**2)   |  O(V**3)
                    |

For All Pairs Shortest Paths:
if we ran the above algorithms for every vertex, we would end up with:
                    |                                             |                   Time complexity
    case            |              best algorithm                 |    General         |  E = O(V)     |  E = O(V**2)
------------------- |-------------------------------------------- | ------------------ | ------------- | --------------
w[u][v] = const     |  V x BFS                                    |  O(V**2+VE)        |  O(V**2)      |  O(V**3)
DAGs                |  V x Topo. sort + 1 round of Bellman-Ford   |  O(V**2+VE)        |  O(V**2)      |  O(V**3)
Nonegative weights  |  V x Dijkstra                               |  O(V**2logV + VE)  |  O(V**2logV)  |  O(V**3)
General             |  V x Bellman-Ford                           |  O(V**2E)          |  O(V**3)      |  O(V**4)

"""

"""
Dijkstra
Intro:
    Dijkstra works on DAGs without negative edges
    Having no -ve edges allows greedy behaviour.
    If we know the shortest path from s to u is of length del[s][u],
    then for node v that is the nearest unvisited neighbor of u,
    it holds true that del[s][v] = del[s][u] + w[u][v],
    where w[u][v] is the weight of the edge u-v.

    For Dijkstra we need two kinds of ADTs (abstract data structure).
    A set, and a priority queue.
    A set S is going to hold all vertices that we know shortest paths to
    A priority queue Q is going to hold all unvisited vertices.
    The priorities are the d-values - distances from source node S to all other vertices.
"""
# TODO implement and document Dijkstra