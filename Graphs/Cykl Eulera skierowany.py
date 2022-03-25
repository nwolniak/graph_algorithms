def DFSVisit(G, u, stack):
    n = len(G[u])
    for i in range(n - 1, -1, -1):
        v = G[u][i]
        G[u].pop()
        DFSVisit(G, v, stack)
    stack.append(u)


def Euler_cycle_list_directed_graph(G):
    n = len(G)
    stack = []
    DFSVisit(G, 0, stack)
    stack.reverse()
    return stack

G = [ [1],[2,3,4],[0,5],[2,5],[3,6],[],[]]