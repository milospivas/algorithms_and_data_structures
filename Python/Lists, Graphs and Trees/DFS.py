from lists import LinkedList
from graph_representation import AdjacencySet

def DFS_visit(s, Adj, parent, level):
    'DFS recursive function'
    for v in Adj.neighbors(s):
        if v not in parent:
            parent[v] = s
            level[v] = level[s] + 1
            DFS_visit(v, Adj, parent, level)

def DFS(s, Adj):
    'Depth First Search'
    parent = {s : None}
    level = {s : 0}
    DFS_visit(s, Adj, parent, level)
    
    return parent, level

def DFS_flood_fill(Adj):
    'Visit the entire graph via DFS flood-fill'
    parent = {}
    level = {}

    for s in Adj.vertices():
        if s not in parent:
            parent[s] = None
            level[s] = 0
            DFS_visit(s, Adj, parent, level)
    
    return parent, level


def DFS_iter(s, Adj):
    'Iterative version of DFS'
    parent = {s : None}
    level = {s : 0}

    stack = LinkedList()
    stack.add_head(s)

    while len(stack) > 0:
        u = stack.peek_head()

        vertex_unfinished = False
        for v in Adj.neighbors(u):
            if v not in parent:
                vertex_unfinished = True # mark the vertex as unfinished
                # and add its neighbor to the stack
                parent[v] = u
                level[v] = level[u] + 1
                stack.add_head(v)
                break
        
        if vertex_unfinished:
            continue
        else:
        # if the vertex has no neighbors to visit, pop it from the stack
            stack.pop_head()

    return parent, level


def DFS_flood_fill_iter(Adj):
    'Iterative version of flood fill'
    parent = {}
    level = {}

    stack = LinkedList()

    for s in Adj.vertices():
        if s not in parent:
            parent[s] = None
            level[s] = 0
            stack.add_head(s)

            while len(stack) > 0:
                u = stack.peek_head()
                
                vertex_unfinished = False
                for v in Adj.neighbors(u):
                    if v not in parent:
                        vertex_unfinished = True # mark the vertex as unfinished
                        # and add its neighbor to the stack
                        parent[v] = u
                        level[v] = level[u] + 1
                        stack.add_head(v)
                        break
                if vertex_unfinished:
                    continue
                else:
                # if the vertex has no neighbors to visit, pop it from the stack
                    stack.pop_head()
    return parent, level


def top_sort(Adj):
    'Top sort via iterative version of DFS'
    # collecting all starting points:    
    starting_vertices = set()
    for u in Adj.vertices():
        if u not in Adj.vertices_incoming():
        # if u is a vertex without ingoing edges,
            starting_vertices.add(u)
    
    if len(starting_vertices) == 0:
        raise AssertionError("Graph is cyclic. Topological sorting isn't possible")

    parent = {}
    # level = {}
    stack = LinkedList()
    top_sorted = LinkedList()

    for s in starting_vertices:
        parent[s] = None
        # level[s] = 0

        stack.add_head(s)

        while len(stack) > 0:
            u = stack.peek_head()

            vertex_unfinished = False
            for v in Adj.neighbors(u):
                if v not in parent:
                    vertex_unfinished = True # mark the vertex as unfinished
                    # and add its neighbor to the stack
                    parent[v] = u
                    # level[v] = level[u] + 1
                    stack.add_head(v)
                    break
            
            if vertex_unfinished:
                continue
            else:
            # if the vertex has no neighbors to visit, pop it from the stack
                u = stack.pop_head()
                top_sorted.add_head(u)

    return top_sorted

# Testing --------------------------------------
c = input("Directed graph? Y/N\n")
is_directed = (c == "y") or (c == "Y")
Adj = AdjacencySet(is_directed)

n = int(input("The number of edges:\n"))
for i in range(n):
    u, v = (x for x in input("Edge "+str(i+1)+": ").split(' '))
    
    Adj.add(u, v)

print(Adj)

# TopSort
print("TopSort:")
sorted_vertices = top_sort(Adj)
print(sorted_vertices)

# # Single source DFS
# s = input("Input the starting vertex for DFS:\n")
# print('DFS:')
# parent, level = DFS(s, Adj)
# print("parents:")
# for u, p in parent.items():
#     print(u, p)

# print("levels:")
# for u, lvl in level.items():
#     print(u, lvl)

# print('DFS_iter:')
# parent, level = DFS_iter(s, Adj)
# print("parents:")
# for u, p in parent.items():
#     print(u, p)

# print("levels:")
# for u, lvl in level.items():
#     print(u, lvl)

# print('Flood fill:')
# parent_fill, level_fill = DFS_flood_fill(Adj)
# print("parents:")
# for u, p in parent_fill.items():
#     print(u, p)

# print("levels:")
# for u, lvl in level_fill.items():
#     print(u, lvl)

# print('Flood fill iter:')
# parent_fill, level_fill = DFS_flood_fill(Adj)
# print("parents:")
# for u, p in parent_fill.items():
#     print(u, p)

# print("levels:")
# for u, lvl in level_fill.items():
#     print(u, lvl)

print("Exiting...")