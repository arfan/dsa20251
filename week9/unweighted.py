G = {
    'A': ['B', 'D'],
    'B': ['D', 'E'],
    'C': ['A', 'F'],
    'D': ['F', 'G'],
    'E': ['G'],
    'F': [],
    'G': ['F'],
}

Q = []
Distance = dict()
Path = dict()
for v in G:
    Distance[v] = -1

s = 'C'
Distance[s] = 0
Q.append(s)

while len(Q) != 0:
    v = Q.pop()

    for w in G[v]:
        if Distance[w] == -1:
            Distance[w] = Distance[v]+1
            Path[w] = v
            Q.append(w)

print(Distance)
print(Path)