def tsp_greedy(distance_matrix):
    n = len(distance_matrix)
    start = 0
    unvisited = set(range(1, n))
    path = [start]
    while unvisited:
        last = path[-1]
        next_city = min(unvisited, key=lambda city: distance_matrix[last][city])
        path.append(next_city)
        unvisited.remove(next_city)
    path.append(start)
    return path


distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


print(tsp_greedy(distance_matrix))
