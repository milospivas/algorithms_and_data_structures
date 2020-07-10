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
                    |
It turns out that for general case, V x Bellman-Ford isn't optimal.
There is:
a) Floyd-Warshall's algorithm that is O(V**3), so also O(V**3) for dense graphs.
b) Johnson's algorithm that is O(V**2logV + VE), so O(V**2logV) for sparse graphs.

Johnson's algorithm:
1. Make altered weights w_h that are nonegative.
To do that, find h[u] such that, for every u,v pair:
  w_h[u][v] = w[u][v] + h[u] - h[v] >= 0

  Finding h:
  1. Add one new "Source" node to the graph.
  2. Connect it to all other nodes with weights 0.
  3. Run Bellman-Ford to compute shortest paths d[s][u] for each u.
  4. h[u] are exactly those d[s][u]

    Why does this work?
    Well, we need this:
      w[u][v] + h[u] - h[v] >= 0
    So if we substitute in d[s][u] and d[s][v], we get:
      w[u][v] + d[s][u] - d[s][v] >= 0
      w[u][v] + d[s][u] >= d[s][v]
    Which is triangle inequality - a tautology!

2. Run V x Dijkstra to compute all d_h[u][v] shortest paths.
3. d[u][v] = d_h[u][v] - h[u] + h[v]

"""

from math import inf


def floyd_warshall(w: list) -> list:
    """ Floyd-Warshall's is a DP algorithm.
    Let's solve all pair shortest paths with DP.
    1. Subproblems
      Let's define:
        d[k][u][v] as the weight of the path from u to v whose intermediate vertices can be in range(1, k+1).
    2. Guessing
      So for each k, we guess if k is in the path u->v (for each u,v pair).
    3. Recursion
      Then:
        d[k][u][v] = min(d[k-1][u][v], d[k-1][u][k] + d[k-1][k][v])
      This min is essentially doing a relaxation.
      You can never "over-relax" a graph, so we don't really need a dimension for k.
      We can just do:
        d[u][v] = min(d[u][v], d[u][k]+d[k][v])
    4. Init. and the topological order:
      # init:
      dp[i][i] = 0
      dp[i][j] = w[i][j]
      # topo order:
      for k in range(n): # ...
    5. The original problem is solved after the k for loop is finished.

    At the end, if there is a d[i][i] < 0,
    it means that vertex i lies on a negative weight cycle. 
    """

    # init
    n = len(w)
    d = [[w[i][j] for j in range(n)] for i in range(n)]
    for i in range(n):
        d[i][i] = 0

    # main algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    # check for negative cycles:
    for i in range(n):
        if d[i][i] < 0:
            print("There is at least one negative weight cycle.")
            return None

    return d

# TODO implement Johnson's algorithm
