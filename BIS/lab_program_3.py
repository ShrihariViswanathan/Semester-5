
import random

# Distance between 4 cities
dist = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = 4
ants = 4
iterations = 10

alpha = 1
beta = 2
rho = 0.5
Q = 100

# Initialize pheromone
p = [[1]*n for i in range(n)]

best_tour = None
best_dist = float('inf')

for t in range(iterations):

    for ant in range(ants):

        tour = [0]
        unvisited = [1, 2, 3]

        # Construct tour
        while unvisited:

            current = tour[-1]

            prob = []
            for city in unvisited:
                prob.append(
                    p[current][city]**alpha *
                    (1/dist[current][city])**beta
                )

            next_city = random.choices(
                unvisited, weights=prob
            )[0]

            tour.append(next_city)
            unvisited.remove(next_city)

        tour.append(0)

        # Calculate distance
        total = 0
        for i in range(n):
            total += dist[tour[i]][tour[i+1]]

        # Update best tour
        if total < best_dist:
            best_dist = total
            best_tour = tour.copy()

        # Deposit pheromone
        for i in range(n):
            a = tour[i]
            b = tour[i+1]
            p[a][b] += Q/total
            p[b][a] += Q/total

    # Evaporation
    for i in range(n):
        for j in range(n):
            p[i][j] *= (1-rho)

print("Best Tour:", best_tour)
print("Shortest Distance:", best_dist)
