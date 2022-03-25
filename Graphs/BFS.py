from Queue import *

def BFS(G,S):
    n = len(G)
    visited = [False]*n
    parents = [None]*n
    distance = [None]*n
    Q = Queue()
    visited[S] = True
    Q.put(S)
    distance[S] = 0
    while not Q.is_empty():
        u = Q.get()
        for neighbours in G[u]:
            if not visited[neighbours]:
                visited[neighbours] = True
                parents[neighbours] = u
                distance[neighbours] = distance[u] + 1
                Q.put(neighbours)

    return parents, distance

# test tree
G = [ [1,2], [0,3], [0,4], [1,5], [2,5], [3,4,6], [5] ]
tree = BFS(G,0)
print(tree)