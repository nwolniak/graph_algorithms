def DFSVisit_first(G,u,visited,stack):
    visited[u]=True
    for neighbours in G[u]:
        if not visited[neighbours]:
            DFSVisit_first(G,neighbours,visited,stack)
    stack.append(u)  # rosnaca kolejnosc czasow ukonczenia

def DFSVisit_second(G,u,visited,forest,i):
    visited[u]=True
    forest[i].append(u)
    for neighbours in G[u]:
        if not visited[neighbours]:
            DFSVisit_second(G,neighbours,visited,forest,i)

def Strongly_connected_components(G):
    n = len(G)
    visited = [False]*n
    stack = []
    for i in range(n):
        if not visited[i]:
            DFSVisit_first(G,i,visited,stack)
    # transpose G
    GT = [[] for i in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            GT[G[i][j]].append(i)
    visited = [False]*n
    forest = []
    i = -1
    while stack:
        v = stack.pop()
        if not visited[v]:
            forest.append([])
            i+=1
            DFSVisit_second(GT,v,visited,forest,i)
    return forest


G = [ [1], [4,5], [3,6], [2,7], [0,5], [6], [5,7], [], ]
print(Strongly_connected_components(G))
