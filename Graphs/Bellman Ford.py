
def Relax(u,v,distance,w):
    if distance[v]>distance[u]+ w:
        distance[v] = distance[u] + w
        return True
    return False


def Bellman_Ford(G,s,t):
    n = len(G)
    distance = [float("Inf")]*n
    distance[s] = 0
    parents = [None]*n
    for i in range(n-1):
        for u in range(n):
            for v in G[u]:
                if Relax(u,v[0],distance,v[1]):
                    parents[v[0]] = u

    for u in range(n):
        for v in G[u]:
            if Relax(u,v[0],distance,v[1]):
                print("Negative cycle")
                return
    return distance, parents

#G = [ [(1,0), (2,1)] , [(3,1), (2,0)] , [(3,0)] , [] ]
#print(Bellman_Ford(G,0,3))


