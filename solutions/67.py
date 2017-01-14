input = open("63_triangle.txt").read()[:-1] # last break is silly
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
