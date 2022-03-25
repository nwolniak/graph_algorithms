def DFSVisit(G,u,visited,parents):
    visited[u] = True
    for neighbours in G[u]:
        if not visited[neighbours]:
            parents[neighbours] = u
            DFSVisit(G,neighbours,visited,parents)


def DFS(G,s):
    n = len(G)
    visited = [False]*n
    parents = [None]*n
    DFSVisit(G,s,visited,parents)
    return parents
# test tree
G = [ [1,2], [0,3], [0,4], [1,5], [2,5], [3,4,6], [5] ]
tree = DFS(G,0)
print(tree)