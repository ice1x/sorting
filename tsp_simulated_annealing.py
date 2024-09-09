import random
import math


def simulated_annealing(distance_matrix, temperature=10000, cooling_rate=0.003):
    def route_length(route):
        return sum(distance_matrix[route[i]][route[i + 1]] for i in range(len(route) - 1)) + distance_matrix[route[-1]][
            route[0]]

    def swap(route):
        a, b = random.sample(range(len(route)), 2)
        route[a], route[b] = route[b], route[a]
        return route

    n = len(distance_matrix)
    current_route = list(range(n))
    random.shuffle(current_route)
    current_length = route_length(current_route)

    while temperature > 1:
        new_route = swap(current_route[:])
        new_length = route_length(new_route)

        if new_length < current_length or math.exp((current_length - new_length) / temperature) > random.random():
            current_route = new_route
            current_length = new_length

        temperature *= 1 - cooling_rate

    return current_route


distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

print(simulated_annealing(distance_matrix))
