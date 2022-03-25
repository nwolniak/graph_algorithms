from dimacs import *
from queue import *

def BFS(G,s,t,parents):
    n = len(G)
    visited = [False]*n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty():
        u = Q.get()
        for i in range(len(G[u])):
            if G[u][i][1] > 0:
                if not visited[G[u][i][0]]:
                    visited[G[u][i][0]] = True
                    parents[G[u][i][0]] = u
                    Q.put(G[u][i][0])

    if visited[t]:
        return True
    else:
        return False


def graph(L, V):
    G = [[] for i in range(V + 1)]
    for edge in L:
        G[edge[0]].append([edge[1], edge[2]])
    for edge in L:
        opposite = False
        for edgeG in G[edge[1]]:
            if edgeG[0] == edge[0]:
                opposite = True
        if not opposite:
            G[edge[1]].append([edge[0], 0])
    return G


def max_flow(G, s, t):
    n = len(G)
    parents = [None] * n
    max_f = 0
    while BFS(G, s, t, parents):
        bottleneck = float("Inf")
        v = t
        while v is not s:
            u = parents[v]
            for i in range(len(G[u])):
                if G[u][i][0] == v:
                    bottleneck = min(bottleneck, G[u][i][1])
            v = u

        max_f += bottleneck

        v = t
        while v is not s:
            u = parents[v]
            for i in range(len(G[u])):
                if G[u][i][0] == v:
                    G[u][i][1] -= bottleneck
            for i in range(len(G[v])):
                if G[v][i][0] == u:
                    G[v][i][1] += bottleneck
            v = u
    return max_f


names = ["clique5", "clique20", "clique100", "grid5x5", "grid100x100", "pp100", "rand20_100", "rand100_500", "simple",
         "simple2",
         "trivial", "trivial2", "worstcase"]

for i in range(len(names)):
    V, L = loadDirectedWeightedGraph("flow/" + names[i])
    print("Rozwiązanie dla" + names[i] + " wynosi : ", max_flow(graph(L, V), 1, V))
