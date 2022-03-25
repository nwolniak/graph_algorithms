from Queue import *
def BFS(G,s,t,parents):
    n = len(G)
    visited = [False]*n
    Q = Queue()
    Q.put(s)
    visited[s]=True
    while not Q.is_empty():
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

def Edmonds_Karp(G,s,t):
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

c = [[0 for j in range(4)] for i in range(4)]
c[0][1] = 2
c[0][2] = 1
c[1][2] = 1
c[1][3] = 1
c[2][3] = 2

G = [[0,1,1,1,0,0,0,0],
     [1,0,1,0,0,1,0,0],
     [1,1,0,0,1,0,1,0],
     [1,0,0,0,0,0,1,0],
     [0,0,1,0,0,1,0,1],
     [0,1,0,0,1,0,1,1],
     [0,0,1,1,0,1,0,1],
     [0,0,0,0,1,1,1,0]]
print( Edmonds_Karp( c, 0, 3 ) ) # wypisze 3
print( Edmonds_Karp(G,0,7))