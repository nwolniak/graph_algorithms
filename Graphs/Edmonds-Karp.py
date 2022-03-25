from queue import *

def BFS(G,s,t,parents):
    n = len(G)
    visited = [False]*n
    Q = Queue()
    Q.put(s)
    visited[s]=True
    while not Q.empty():
        u = Q.get()
        for i in range(n):
            if G[u][i] > 0:
                if not visited[i]:
                    visited[i] = True
                    parents[i] = u
                    Q.put(i)
    if visited[t]:
        return True
    else:
        return False

def max_flow(G,s,t):
    n = len(G)
    parents = [None]*n
    max_f = 0
    while BFS(G,s,t,parents):
        bottleneck = float("Inf")
        v = t
        while v is not s:
            u = parents[v]
            bottleneck = min(bottleneck,G[u][v])
            v = u

        max_f += bottleneck

        v = t
        while v is not s:
            u = parents[v]
            G[u][v] -= bottleneck
            G[v][u] += bottleneck
            v = u
    return max_f
