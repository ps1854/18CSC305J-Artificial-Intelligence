class UnionFind:
    def __init__(self, sz):
        self.root = [i for i in range(sz)]

    def find(self, x): 
        return self.root[x]

    def union(self, x, y): 
        rootX = self.find(x) 
        rootY = self.find(y) 
        if rootX != rootY:
            for i in range(len(self.root)): 
                if self.root[i] == rootY: 
                    self.root[i] = rootX

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Graph:
    def __init__(self, V): 
        self.V = V
        self.adj = []

    def addEdge(self, x, y, w): 
        self.adj.append((x, y, w))

    def kruskals(self):
        res = [] 
        cost = 0
        uf = UnionFind(self.V)
    
        for edge in sorted(self.adj, key = lambda e: e[2]): 
            if not uf.connected(edge[0], edge[1]):
                cost += edge[2] 
                res.append(edge) 
                uf.union(edge[0], edge[1])
        return res, cost

v = int(input("Enter no. of vertices: ")) 
g = Graph(v)
e = int(input("Enter no. of edges: "))

for i in range(e):
    inp = input("Enter the vertices and weight of edge {}: ".format(i+1)) 
    edge = list(map(int, inp.split()))
    g.addEdge(edge[0], edge[1], edge[2])

r = g.kruskals()
print("Edges in minimum spanning tree: ", r[0]) 
print("Cost: ", r[1])

''' 
                 10
            0--------1
            |  \     |
           6|   5\   |15
            |      \ |
            2--------3
                4       
'''