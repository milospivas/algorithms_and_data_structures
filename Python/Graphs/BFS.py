from lists import LinkedList
from graph_representation import AdjacencySet

def BFS_list(s, Adj) -> (dict, dict):
    'Implementation using As seen at MIT 6.006 course'
    level = {s : 0}
    parent = {s : None}
    i = 1
    frontier = [s]
    while len(frontier) > 0:
        next = []
        for u in frontier:
            for v in Adj.neighbors(u):
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1

    return level, parent

def BFS(s, Adj) -> (dict, dict):
    'The "propper" queue version of the BFS'
    level = {s : 0}
    parent = {s : None}
    frontier = LinkedList()
    frontier.add_tail(s) # enqueue
    while len(frontier) > 0:
        u = frontier.pop_head() # dequeue
        for v in Adj.neighbors(u):
            if v not in level:
                level[v] = level[u] + 1
                parent[v] = u
                frontier.add_tail(v)

    return level, parent


# Testing --------------------------------------
c = input("Directed graph? Y/N\n")
is_directed = (c == "y") or (c == "Y")
Adj = AdjacencySet(is_directed)

n = int(input("The number of edges:\n"))
for i in range(n):
    u, v = (x for x in input("Edge "+str(i+1)+": ").split(' '))
    
    Adj.add(u, v)

print(Adj)

s = input("Input the starting vertex for BFS:\n")
level1, parent1 = BFS_list(s, Adj)

print("Levels:")
for u, lvl in level1.items():
    print(u, lvl)

print("Parents:")
for u, p in parent1.items():
    print(u, p)

# 
level2, parent2 = BFS(s, Adj)

# check if the returned dictionaries are the same:
for u, lvl in level1.items():
    assert level2[u] == lvl

for u, lvl in level2.items():
    assert level1[u] == lvl

for u, p in parent1.items():
    assert parent2[u] == p

for u, p in parent2.items():
    assert parent1[u] == p

print("Exiting...")