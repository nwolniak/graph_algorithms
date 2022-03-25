
def DFSVisit(G,u,visited,parents,low,times,time,bridges):
    visited[u] = True

    times[u] = time
    low[u] = time
    time += 1

    for neighbours in G[u]:
        if not visited[neighbours]:
            parents[neighbours] = u
            DFSVisit(G,neighbours,visited,parents,low,times,time,bridges)

            low[u] = min(low[u],low[neighbours])

            if low[neighbours] > times[u]:
                bridges.append([u,neighbours])

        elif neighbours is not parents[u]:
            low[u] = min(low[u],times[neighbours])


def DFS(G,s):  # O(V+E) działa dla skierowanych i nieskierowanych
    n = len(G)
    visited = [False]*n
    parents = [None]*n
    times = [float("Inf")]*n
    low = [float("Inf")]*n
    time = 0
    bridges = []
    # for all vertices DFSVisit if directed
    DFSVisit(G,s,visited,parents,low,times,time,bridges)
    return bridges

G = [ [1] , [2] , [3,5] , [4] , [2] , [6] , [] ]
print(DFS(G,2))