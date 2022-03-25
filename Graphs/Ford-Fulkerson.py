from dimacs import *

def DFSVisit(G,u,n,visited,parents):
    visited[u] = True
    for i in range(n):
        if G[u][i]>0:
            if not visited[i]:
                parents[i]=u
                DFSVisit(G,i,n,visited,parents)

def DFS(G,s,t,parents):
    n= len(G)
    visited = [False]*n
    visited[s] = True
    for i in range(n):
        if G[s][i]>0:
            if not visited[i]:
                parents[i]=s
                DFSVisit(G,i,n,visited,parents)

    if visited[t]:
        return True
    else:
        return False

def max_flow( c, s, t ):
    n = len(c)
    parents = [None]*n
    max_f = 0
    while DFS(c,s,t,parents):
        bottleneck = float("Inf")
        v = t
        while v is not s:
            u = parents[v]
            bottleneck = min(bottleneck,c[u][v])
            v = u

        max_f += bottleneck

        v = t
        while v is not s:
            u = parents[v]
            c[u][v] -= bottleneck
            c[v][u] += bottleneck
            v = u

    return max_f , c

# O(V^2 * f ) macierz sąsiedztwa
# O((E + V)*f) listy sąsiedztwa

V, L = loadDirectedWeightedGraph("flow/trivial2")
print(V,L)

G = [[0 for i in range(V)] for j in range(V)]
for edge in L:
    G[edge[0]-1][edge[1]-1] = edge[2]

print(G)

print(max_flow(G,0,5))


