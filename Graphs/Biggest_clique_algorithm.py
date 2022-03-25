from Lex_BFS import *

def rn(G, lex_bfs_order, v):
    curr = G[v]
    rn_set = set()
    for i in range(0, lex_bfs_order.index(v)):
        if lex_bfs_order[i] in curr.out:
            rn_set.add(lex_bfs_order[i])
    return rn_set


def biggest_clique(G,V):
    lex_bfs_order = lex_bfs(G,V)
    max_size = 0
    for v in lex_bfs_order:
        rn_v = rn(G,lex_bfs_order,v)
        if len(rn_v) > max_size:
            max_size = len(rn_v)
    return max_size + 1


if __name__ == "__main__":
    (V, L) = loadWeightedGraph("chordal/AT")

    G = [None] + [Node(i) for i in range(1, V + 1)]  # żeby móc indeksować numerem wierzchołka

    for (u, v, _) in L:
        G[u].connect_to(v)
        G[v].connect_to(u)

    print("Lex bfs order : ", lex_bfs(G, V))
    print("Correct lex bfs : ", checkLexBFS(G, lex_bfs(G, V)))

    print("Biggest clique size : ", biggest_clique(G,V))