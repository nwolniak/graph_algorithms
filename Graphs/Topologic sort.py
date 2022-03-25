def DFSVisit(G,u,visited,sorted):
    visited[u] = True
    for neighbours in G[u]:
        if not visited[neighbours]:
            DFSVisit(G,neighbours,visited,sorted)
    sorted.insert(0,u)


def DFS_Topological_sort(G):
    n = len(G)
    visited = [False]*n
    sorted = []
    for v in range(n):
        if not visited[v]:
            DFSVisit(G,v,visited,sorted)
    return sorted
G = [ [1], [2], [], [2], [3], [4,6], [], [6], [], ]
print(DFS_Topological_sort(G))  # directed acyclic graph