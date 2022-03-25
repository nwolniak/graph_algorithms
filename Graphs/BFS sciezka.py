# najkrótsze ściezki 1-wszyscy gdy wagi małe liczby naturalne

from queue import *

def BFS(G,S):
    n = len(G)
    visited = [False]*n
    parents = [None]*n
    distance = [None]*n
    Q = Queue()
    visited[S] = True
    Q.put( (0 , S) )
    distance[S] = 0
    while not Q.empty():
        u = Q.get()

        if u[0] == 0:
            for neighbours in G[u[1]]:
                if not visited[neighbours[0]]:
                    visited[neighbours[0]] = True
                    parents[neighbours[0]] = u[1]
                    distance[neighbours[0]] = distance[u[1]] + 1
                    Q.put((distance[neighbours],neighbours[0]))
        else:
            distance[u[1]] += 1
            Q.put((u[0]-1,u[1]))
    return parents, distance

# test tree
G = [ [(1,2)] , [(2,1)] , [(3,3),(4,4),(5,5)] , [] , [] , [(6,2)], [] ]
print(BFS(G,0))