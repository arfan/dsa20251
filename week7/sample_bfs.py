       #  0  1. 2. 3  4  5. 6
graph = [[0, 1, 1, 0, 0, 0, 0],
         [1, 0, 0, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 1],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         
         ]

queue = []
visited = set()

queue.append(0) #enqueue

while queue:
    current = queue.pop(0) # dequeue
    print(current)

    visited.add(current)

    possible_way = graph[current]

    for i in range(7):
        if possible_way[i] == 1 and not i in visited:
            queue.append(i)


