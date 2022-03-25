def Floyd_Warshall(G):
    n = len(G)
    for t in range(n):
        for i in range(n):
            for j in range(len(G[i])):
                G[i][j] = min(G[i][j], G[i][t] + G[t][j])
    return G

G = [ [0,0,4,2,0],
      [0,0,0,0,5],
      [0,0,0,0,0],
      [0,0,1,0,3],
      [0,0,4,0,0] ]
for i in range(len(G)):
    for j in range(len(G)):
        if G[i][j] == 0:
            G[i][j] = float("Inf")
print(Floyd_Warshall(G))