from dimacs import *
from queue import *


class Node:
    def __init__(self, idx):
        self.idx = idx
        self.out = set()  # zbiór sąsiadów

    def connect_to(self, v):
        self.out.add(v)


def lex_bfs(G, V):
    visit_order = []
    lex_sets = [{i for i in range(1, V + 1)}]

    while lex_sets:
        curr = lex_sets[-1].pop()
        visit_order.append(curr)

        new_vertices_set = []
        for nodes in lex_sets:
            nodes_subset = set()
            for node in nodes:
                if node in G[curr].out:
                    nodes_subset.add(node)
            nodes = nodes.difference(nodes_subset)
            if len(nodes) > 0:
                new_vertices_set.append(nodes)
            if len(nodes_subset) > 0:
                new_vertices_set.append(nodes_subset)
        lex_sets = new_vertices_set
    return visit_order


def checkLexBFS(G, vs):
    n = len(G)
    pi = [None] * n
    for i, v in enumerate(vs):
        pi[v] = i

    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            Ni = G[vs[i]].out
            Nj = G[vs[j]].out

            verts = [pi[v] for v in Nj - Ni if pi[v] < i]
            if verts:
                viable = [pi[v] for v in Ni - Nj]
                if not viable or min(verts) <= min(viable):
                    return False
        return True


def rn(G, lex_bfs_order, v):
    curr = G[v]
    rn_set = set()
    for i in range(0, lex_bfs_order.index(v)):
        if lex_bfs_order[i] in curr.out:
            rn_set.add(lex_bfs_order[i])
    return rn_set


def parent(G, lex_bfs_order, v):
    curr = G[v]
    for i in reversed(range(0, lex_bfs_order.index(v))):
        if lex_bfs_order[i] in curr.out:
            return lex_bfs_order[i]
    return None


def check_peo(G, V):
    lex_bfs_order = lex_bfs(G, V)
    rn_dict = {}
    for v in lex_bfs_order:
        rn_dict[v] = rn(G,lex_bfs_order, v)
    for v in lex_bfs_order:
        v_parent = parent(G,lex_bfs_order,v)
        if v_parent is not None and rn_dict[v].difference({v_parent}).issubset(rn_dict[v_parent]):
            return False
    return True


if __name__ == "__main__":
    (V, L) = loadWeightedGraph("chordal/cycle3")

    G = [None] + [Node(i) for i in range(1, V + 1)]  # żeby móc indeksować numerem wierzchołka

    for (u, v, _) in L:
        G[u].connect_to(v)
        G[v].connect_to(u)

    print("Lex bfs order : ",lex_bfs(G, V))
    print("Correct lex bfs : ",checkLexBFS(G, lex_bfs(G, V)))
    print("Check peo : ", check_peo(G,V))

