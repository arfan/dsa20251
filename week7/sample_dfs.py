
graph = [[0, 1, 0, 1],
         [0, 0, 1, 0],
         [1, 0, 0, 1],
         [0, 0, 0, 0]]

# A --> 0
# B --> 1
# C --> 2
# D --> 3

A = 0
B = 1
C = 2
D = 3

mapping = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    
}
stack = []
visited = set()

stack.append(B)

while stack:
    current = stack.pop()
    print(mapping[current])

    visited.add(current)

    possible_way = graph[current]

    for i in range(4):
        if possible_way[i] == 1 and not i in visited:
            stack.append(i)


