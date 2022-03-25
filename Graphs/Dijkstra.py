import queue

def Relax(u,v,distance,curr_d,w,parents):
    if distance[v]>curr_d+w:
        distance[v] = curr_d + w
        parents[v] = u
        return True
    return False

def Dijkstra(G,s,t):
    n = len(G)
    visited = [False]*n
    parents = [None]*n
    distance = [float("Inf")]*n
    Q = queue.PriorityQueue()
    Q.put((0,s))
    distance[s]=0
    visited[s]=True
    while not Q.empty():
        curr_d,u = Q.get()
        visited[u] = True
        for neighbours in G[u]:
            if not visited[neighbours[0]]:
                if Relax(u,neighbours[0],distance,curr_d,neighbours[1],parents):
                    Q.put((distance[neighbours[0]],neighbours[0]))
    return distance[t],parents

G = [ [(1,0), (2,1)] , [(3,1), (2,0)] , [(3,0)] , [] ]
print(Dijkstra( G, 0, 3 ) ) # wypisze 0