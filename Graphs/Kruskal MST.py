class Node:
    def __init__(self,val=None):
        self.val = val
        self.parent = None

def MakeStructure(v):
    v = Node(v)
    return v
def Find(v):
    if v.parent == None:
        return v
    return Find(v.parent)

def Union(v,u):
    v_root = Find(v)
    u_root = Find(u)
    if v_root is not u_root:
        v_root.parent = u_root
        return True
    return False

def Kruskal(G):
    n = len(G)
    min_spanning_tree = []
    set = [None]*n
    for i in range(n):
        set[i] = MakeStructure(i)

    E = []
    for u in range(n):
        for neighbours in G[u]:
            E.append((neighbours[1], u, neighbours[0]))
    E.sort()
    print(E)
    for e in E:
        if Union(set[e[1]],set[e[2]]):
            min_spanning_tree.append((set[e[1]].val,set[e[2]].val,e[0]))
    return min_spanning_tree




G = [[[1,0], [2,1]],
    [[3,1], [2,0]],
    [[3,0]],
    []]

G2 = [[(1,1),(2,4)],[(2,4),(3,2),(4,2)],[],[(2,2),(4,1)],[(0,5)]]

print(Kruskal(G2))