def DFSVisit(G,u,edges,stack):
    for neighbours in G[u]:
        if edges[u][neighbours]:
            edges[u][neighbours] = 0
            edges[neighbours][u] = 0
            DFSVisit(G,neighbours,edges,stack)
    stack.insert(0,u)

def Euler_cycle_list(G):
    n = len(G)
    edges = [ [0 for i in range(n)] for i in range(n)]
    for i in range(n):
        for neighbours in G[i]:
            edges[i][neighbours] = 1
            edges[neighbours][i] = 1
    stack = []
    DFSVisit(G,0, edges,stack)
    print(edges)
    return stack


G = [ [1,4] , [2,4,5] , [1,5,3], [2,6], [0,1,5,6] , [1,2,4,6] , [2,3,5,4] ]

print(Euler_cycle_list(G))


def DFSVisit2(G,n,u,stack):
    for i in range(n):
        if G[u][i]:
            G[u][i] = 0
            G[i][u] = 0
            DFSVisit(G,n,i,stack)
    stack.insert(0,u)

def Euler_cycle_matrix(G): # chyba O(V^2)
    n = len(G)
    stack = []
    DFSVisit2(G,n,0,stack)
    return stack  # bo obojetnie w ktora strone pojdziemy w grafie nieskierowanym

G3 = [ [0,1,0,0,0],
       [0,0,1,1,0],
       [1,0,0,0,0],
       [0,0,0,0,1],
       [0,1,0,0,0],]