import sys


def tsp_branch_and_bound(distance_matrix):
    n = len(distance_matrix)
    all_visited = (1 << n) - 1
    memo = [[None] * n for _ in range(1 << n)]

    def tsp(pos, visited):
        if visited == all_visited:
            return distance_matrix[pos][0]

        if memo[visited][pos] is not None:
            return memo[visited][pos]

        ans = sys.maxsize
        for city in range(n):
            if (visited >> city) & 1 == 0:
                ans = min(ans, distance_matrix[pos][city] + tsp(city, visited | (1 << city)))

        memo[visited][pos] = ans
        return ans

    return tsp(0, 1)


distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]


print(tsp_branch_and_bound(distance_matrix))
