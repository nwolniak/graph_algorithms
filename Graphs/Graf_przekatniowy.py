from dimacs import *
from queue import *

class Node:
  def __init__(self, idx):
    self.idx = idx
    self.out = set()              # zbiór sąsiadów

  def connect_to(self, v):
    self.out.add(v)



def BFS(G,s,t,parents):
    n = len(G)
    visited = [False]*n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty():
        u = Q.get()
        for i in range(len(G[u])):
            if G[u][i][1] > 0:
                if not visited[G[u][i][0]]:
                    visited[G[u][i][0]] = True
                    parents[G[u][i][0]] = u
                    Q.put(G[u][i][0])

    if visited[t]:
        return True
    else:
        return False

def update_sets(sets,v):
  for set in sets:
    if len(set & {v}) > 0:
      print("new set is :",set & {v})
      i = sets.index(set)
      tmp_set = set & {v}
      if len(sets[i] - {v}) < len(tmp_set):
        sets[i] -= {v}
        sets.insert(i, tmp_set)
      elif i + 1 == len(sets):
        sets[i] -= {v}
        sets.append(tmp_set)
      else:
        sets[i] -= {v}
        sets.insert(i + 1, tmp_set)

def lexBFS(G,V):
  lex_sets = [{ i for i in range(1,V+1)}]
  visited = [False for i in range(0,V+1)]
  print(lex_sets)
  visit_order = []
  lex_order = []
  while lex_sets:
    print("lex_sets ",lex_sets)
    first_set = lex_sets[0]
    print("first_set ",first_set)
    v = first_set.pop()
    if not first_set:
      lex_sets.remove(first_set)
    visited[v] = True
    lex_order.append(v)
    print("lex_order ",lex_order)
    update_sets(lex_sets,v)
    for neighbour in G[v].out:
      if not visited[neighbour]:
        update_sets(lex_sets,neighbour)

  return lex_order


def lex_bfs(G,V):


    visit_order = []

    while vertices_sets:
        curr = vertices_sets[-1].pop()
        visit_order.append(curr)

        new_vertices_set = []
        for nodes in vertices_sets:
            nodes_subset = set()
            for node in nodes:
                if node in self.nodes[curr].edges:
                    nodes_subset.add(node)
            nodes = nodes.difference(nodes_subset)
            if len(nodes) > 0:
                new_vertices_set.append(nodes)
            if len(nodes_subset) > 0:
                new_vertices_set.append(nodes_subset)
        vertices_sets = new_vertices_set
    return visit_order


if __name__ == "__main__":
  (V, L) = loadWeightedGraph("chordal/AT")

  G = [None] + [Node(i) for i in range(1, V+1)]  # żeby móc indeksować numerem wierzchołka

  for (u, v, _) in L:
    G[u].connect_to(v)
    G[v].connect_to(u)
  print(lexBFS(G,V))