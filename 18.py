input = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

# Structure

class Node:
    def __init__(self, name, value):
        self.value = value
        self.edges = []
        self.name = name

    def edgeTo(self, node, cost):
        self.edges.append((node, cost))

    def __hash__(self):
        return hash((self.name))

    def __eq__(self, other):
        return (self.name) == (other.name)


class Edge:
    def __init__(self, n1, n2):
        self.fr = n1
        self.to = n2


# Build Structure

input = input.split("\n")
input = [i.split(" ") for i in input]
numbers = [[int(j) for j in i] for i in input]

start = Node("start", 0)
target = Node("target", 0)
G = [start, target]
upperLayer = [start]
for i, layer in enumerate(numbers):
    thisLayer = []
    for j, nodeValue in enumerate(layer):
        n = Node("%d,%d"%(i,j), nodeValue)
        G.append(n)
        thisLayer.append(n)
        for k, upperNode in enumerate(upperLayer): #optimizable
            if j-k == 0 or j-k==1:
                upperNode.edgeTo(n, 100-n.value) # inverse the cost
    upperLayer = thisLayer

for k, upperNode in enumerate(upperLayer):
    upperNode.edgeTo(target, 0)



def visitEdges(n):
    for to, cost in n.edges:
        print(to.value)
        visitEdges(to)
#visitEdges(start)


inf = 99999999999999999999999
def dykstra(G, start):
    Q = G
    dist = dict()
    prev = dict()
    for node in Q:
        dist[node] = inf
        prev[node] = None

    dist[start] = 0

    while Q: # while not empty
        # get min dist node
        u = Q[0]
        index = 0
        for index2, uu in enumerate(Q):
            if dist[uu] < dist[u]:
                u = uu
                index = index2
        del Q[index]

        for v, cost in u.edges:
            alt = dist[u] + cost
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    return dist, prev


dist, prev = dykstra(G,start)

costSum = 0
p = prev[target]
while p:
    print("%s: %d"%(p.name, p.value))
    costSum += p.value
    p = prev[p]

print(costSum)
exit()
#
# 1  function Dijkstra(Graph, source):
# 2
# 3      create vertex set Q
# 4
# 5      for each vertex v in Graph:             // Initialization
# 6          dist[v] ← INFINITY                  // Unknown distance from source to v
# 7          prev[v] ← UNDEFINED                 // Previous node in optimal path from source
# 8          add v to Q                          // All nodes initially in Q (unvisited nodes)
# 9
#10      dist[source] ← 0                        // Distance from source to source
#11      
#12      while Q is not empty:
#13          u ← vertex in Q with min dist[u]    // Source node will be selected first
#14          remove u from Q 
#15          
#16          for each neighbor v of u:           // where v is still in Q.
#17              alt ← dist[u] + length(u, v)
#18              if alt < dist[v]:               // A shorter path to v has been found
#19                  dist[v] ← alt 
#20                  prev[v] ← u 
#21
#22      return dist[], prev[]

