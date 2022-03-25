from dimacs import *
import queue


class Node:
    def __init__(self, v, subset=None):
        self.v = v
        self.edges = {}
        self.active = True
        if subset is None:
            self.subset = [v]
        else:
            self.subset = subset

    def addEdge(self, to, weight):
        self.edges[to] = self.edges.get(to, 0) + weight

    def delEdge(self, to):
        del self.edges[to]

    def toString(self):
        for vertexTo, weight in self.edges.items():
            print((self.subset, vertexTo, weight))

    def scal(self, y):
        self.subset.extend(y.subset)


def mergeVertices(G, x, y):
    for vertexTo, weight in y.edges.copy().items():
        # kryterium dodawania x.v != vertexTo
        if x.v is not vertexTo:
            x.addEdge(vertexTo, weight)
            G[vertexTo].addEdge(x.v, weight)
        # kryterium usuwania zawsze
        y.delEdge(vertexTo)
        G[vertexTo].delEdge(y.v)
    y.active = False
    x.scal(y)


def minimumCutPhase(G, n):
    a = G[1]
    S = {a}
    stack = [a]
    Q = queue.PriorityQueue()

    sum = [0 for i in range(len(G))]
    for elem in S:
        for vertexTo, weight in elem.edges.items():
            sum[vertexTo] = sum[vertexTo] + weight
            Q.put((-sum[vertexTo], vertexTo))

    while len(S) != n:

        edgesSum, v = Q.get()
        if (not G[v].active):
            continue
        S.add(G[v])
        stack.append(G[v])
        for vertexTo, weight in G[v].edges.items():
            if G[vertexTo] not in S:
                sum[vertexTo] += weight
                Q.put((-sum[vertexTo], vertexTo))

    t = stack.pop()
    s = stack.pop()
    minCutST = sum[t.v]
    mergeVertices(G, s, t)

    return minCutST, t


def Stoer_Wagner(G):
    minCut = float("inf")
    i = 1
    s = G[1]
    while len(G) - i > 1:
        minCutST, s2 = minimumCutPhase(G, len(G) - i)
        i += 1
        if minCutST < minCut:
            minCut = minCutST
            s = Node(s2.v, s2.subset)
    return minCut, s.subset


if __name__ == "__main__":
    # V, L = loadWeightedGraph("graphs-lab3/trivial")
    # V, L = loadWeightedGraph("graphs-lab3/simple") # 2
    # V, L = loadWeightedGraph("graphs-lab3/geo20_2c") # 1
    # V, L = loadWeightedGraph("graphs-lab3/cycle") # 2
    # V, L = loadWeightedGraph("graphs-lab3/clique100") #99
    # V, L = loadWeightedGraph("graphs-lab3/clique200") # 199
    V, L = loadWeightedGraph("graphs-lab3/rand20_100")

    G = [Node(i) for i in range(V + 1)]
    for (x, y, c) in L:
        G[x].addEdge(y, c)
        G[y].addEdge(x, c)

    print("Stoer - W ", Stoer_Wagner(G))
