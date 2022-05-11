from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)
    
    def addEdge(self, u, v, h2):
        self.adj[u].append((v, h2))  
    
    def bestFirst(self, s, d, h1):
        parent = {}
        success = False 
        open = [(s, h1)]
        closed = []
        parent[s] = None
        
        while open and not success:
            t = open.pop(0)
            print(t[0])
            
            if t[0] == d:
                success = True
                closed.append(t)
            else:
                closed.append(t)
                for neighbor in self.adj[t[0]]:
                    if neighbor not in open and neighbor not in closed:
                        open.append(neighbor)
                        parent[neighbor[0]] = t[0]
                open.sort(key = lambda  t: t[1])
        
        if success:
            path = []
            n = d
            while parent[n] != None:
                path.append(n)
                n = parent[n]
            path.append(s)
            print("Path found: {}".format(path[::-1]))
        else:
            print("No path found!!!")            
    

v = int(input("Enter the no. vertices: "))
g = Graph(v)

heuristics = dict()
for i in range(v):
    ver_h = input("Enter vertex {} and its heuristic: ". format(i+1)).strip().split()
    heuristics[ver_h[0]] = int(ver_h[1])
    # print(ver_h[0], int(ver_h[1]))

e = int(input("Enter the no. edges: "))
for i in range(e):
    edge = input("Enter the vertices of edge {}: ". format(i+1)).strip().split()
    # print(heuristics[edge[0]], heuristics[edge[1]])
    g.addEdge(edge[0], edge[1], heuristics[edge[1]])

s = input("Enter the source: ")
d = input("Enter the destination: ")
g.bestFirst(s, d, heuristics[s])


'''
                         A,5                  ||
                        /  \                  ||
                       /    \                 ||
                      /      \                ||
                    B,3      C,2           \  ||  /
                    /\        /\            \    /
                   /  \      /  \            \  /
                  /    \    /    \            \/ 
                 D,2  E,3  F,2   G,4
                /\        /       /\ 
               /  \      /       /  \ 
              /    \    /       /    \ 
            H,0  I,99 J,99    K,99   L,3
'''