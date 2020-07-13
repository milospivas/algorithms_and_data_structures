''' Author: Miloš Pivaš, student
'''

from graph_representation import AdjacencySet

def bellman_ford_sssp(Adj, s):
    'Bellman-Ford algorithm for single-source shortest paths from vertex s'

    N = len(Adj)

    # 0th step, copy of all weights from s to its neighbors
    dp = Adj.W[s].copy()

    dp[s] = 0   # this is optional,
                # maybe we want to find a shortest round-trip path from source

    for _ in range(1, N-1):
    # N-1 because that's the length of the longest possible path in graph

        for v in Adj.V:
        # for every vertex in the graph

            aux = []
            for u in Adj.neighbors_incoming(v):
            # for every u, an incoming neighbor of v

                if u in dp:
                # if u has already been reached by the search
                    # try a path via u to v
                    aux += [dp[u] + Adj.W[u][v]]
            

            if aux != []:
            # if there are paths to v

                # get the min path
                m = min(aux)

                # update
                dp[v] = min(m, dp[v]) if v in dp else m

    for v in Adj.V:
        if v not in dp:
            dp[v] = float('Inf')
    return dp


# # acyclic
# Adj = AdjacencySet(weighted=True)
# Adj.add(0, 1, 1)
# Adj.add(0, 2, 13)
# Adj.add(1, 3, 42)
# Adj.add(2, 3, 6)
# print(Adj)
# print(bellman_ford_sssp(Adj, 0))

# # with a cycle:
# Adj = AdjacencySet(weighted=True)
# Adj.add(0, 1, 1)
# Adj.add(1, 3, 42)
# Adj.add(2, 3, 6)
# Adj.add(2, 0, 13)
# Adj.add(1, 2, 13)
# print(Adj)
# print(bellman_ford_sssp(Adj, 0))

# # unreachable:
# Adj = AdjacencySet(weighted=True)
# Adj.add(0, 1, 1)
# Adj.add(2, 1, 42)

# print(Adj)
# print(bellman_ford_sssp(Adj, 0))

# print("Exiting...")