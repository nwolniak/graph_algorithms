import networkx as nx
from dimacs import *
from networkx.algorithms.planarity import check_planarity
from networkx.algorithms.flow import maximum_flow
from networkx.algorithms.components import strongly_connected_components
from networkx.algorithms.dag import topological_sort


def is_SAT_2CNF(G):
    SCC = strongly_connected_components(G)
    for S in SCC:
        for v in S:
            if (-v) in S:
                return False
    return True

def SAT_2CNF_values(G):
    SCC = strongly_connected_components(G)

    H = nx.DiGraph()

    SCC_list = []
    for S in SCC:
        SCC_list.append(S)
        H.add_node(S)

    for scc in SCC_list:
        for scc_2 in SCC_list:
            if scc is not scc_2:
                for v in scc:
                    if v in scc_2:
                        H.add_edge(scc, scc_2)

    O = topological_sort(H)

    values = {}

    for v in O:
        if v not in values.keys():
            if (v < 0):
                values[v] = True
            else:
                values[v] = False

    return values







if __name__ == "__main__":

    (V, L) = loadWeightedGraph("planar_graphs/house")
    #(V, L) = loadWeightedGraph("planar_graphs/nonplanar-ex2")
    G = nx.Graph()
    for (u, v, _) in L:
        G.add_node(u)
        G.add_node(v)
        G.add_edges_from([(u,v), (v,u)])

    print(check_planarity(G))

    (V,L) = loadDirectedWeightedGraph("flow/clique100")
    G2 = nx.DiGraph()
    for (u, v, c) in L:
        G2.add_node(u)
        G2.add_node(v)
        G2.add_edge(u, v)
        G2[u][v]['capacity'] = c

    print(maximum_flow(G2, 1, G2.number_of_nodes()))

    G3 = nx.DiGraph()
    (V, L) = loadCNFFormula("sat/sat/sat5_10")
    (V, L) = loadCNFFormula("sat/sat/sat5_20")
    for (u, v) in L:
        G3.add_node(u)
        G3.add_node(v)
        G3.add_node(-u)
        G3.add_node(-v)
        G3.add_edge(-u, v)
        G3.add_edge(-v, u)

    is_SAT_2CNF(G3)



