def DFSVisit(G,u,n,visited,parents):
    visited[u] = True
    for i in range(n):
        if G[u][i]>0:
            if not visited[i]:
                parents[i]=u
                DFSVisit(G,i,n,visited,parents)

def DFS(G,s,t,parents):
    n= len(G)
    visited = [False]*n
    visited[s] = True
    for i in range(n):
        if G[s][i]>0:
            if not visited[i]:
                parents[i]=s
                DFSVisit(G,i,n,visited,parents)

    if visited[t]:
        return True
    else:
        return False

def max_flow( c, s, t ):
    # policz maksymalny przepływ z s do t
    # c[i][j] to przepustowość krawędzi z i do j
    # jeśli c[i][j] > 0 to c[j][i] = 0
    n = len(c)
    parents = [None]*n  # potrzebna do DFS i wyznaczenia sciezki powiekszajacej
    max_f = 0 # na poczatku flow jest 0 przez wszystkie krawedzie
    while DFS(c,s,t,parents):  # DFS wyznacza sciezke powiekszajaca
        bottleneck = float("Inf") # najmniejsza mozliwa wartosc residaulnej pojemnosci w sciezce
        v = t
        while v is not s:
            u = parents[v]
            bottleneck = min(bottleneck,c[u][v]) # tutaj wyznaczamy minimum,odtwarzajac sciezke
            v = u

        max_f += bottleneck  # max_f to suma minimalnych residualnych pojemnosci na kolejnych sciezkach powiekszajacych

        v = t
        while v is not s:
            u = parents[v]
            c[u][v] -= bottleneck
            c[v][u] += bottleneck
            v = u
            '''zmniejszamy capacity z {u,v} czyli dodajemy dany mozliwy flow = bottleneck i zmniejszamy przepustowosc na wszystkich krawedziach w sciezce powiekszajacej
             w grafie residualnym do krawedzi w przeciwna strone niz w istniejacym grafie dodajemy wartos bottleneck
             czyli jak byla 0 - nie istnieje , teraz ja tworzymy aby mozna bylo poprawnie puszczac "flow" w przeciwna strone
             i zeby DFS mogl znalesc sciezke powiekszajaca z ta wlasnie krawedzia
             gdy c[u][v] wyniesie 0 to znaczy ze puscilismy przez ta krawedz najwieksze flow takie ze f[u][v] = c[u][v](poczatkowe) i DFS juz ta krawedzia nie przejdzie'''

    return max_f


c = [[0 for j in range(4)] for i in range(4)]
c[0][1] = 2
c[0][2] = 1
c[1][2] = 1
c[1][3] = 1
c[2][3] = 2
print( max_flow( c, 0, 3 ) ) # wypisze 3