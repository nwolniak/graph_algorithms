
def DFSVisit(G,u,visited,parents,low,times,time,points):
    visited[u] = True

    times[u] = time
    low[u] = time
    time += 1

    children = 0
    for neighbours in G[u]:
        if not visited[neighbours]:
            parents[neighbours] = u
            DFSVisit(G,neighbours,visited,parents,low,times,time,points)

            low[u] = min(low[u],low[neighbours])

            if parents[u] is None and children > 1:
                points[u] = True
            elif parents[u] is not None and low[neighbours] >= times[u]:
                points[u] = True

        elif neighbours is not parents[u]:
            low[u] = min(low[u],times[neighbours])


def DFS(G,s):
    n = len(G)
    visited = [False]*n
    parents = [None]*n
    times = [float("Inf")]*n
    low = [float("Inf")]*n
    time = 0
    points = [False] * n
    # for all vertices DFSVisit if directed
    DFSVisit(G,s,visited,parents,low,times,time,points)
    return points

G = [ [1] , [2] , [3,5] , [4] , [2] , [6] , [] ]
print(DFS(G,0))