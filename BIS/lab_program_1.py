import random

# Fitness function
def fitness(x):
    return x * x

# Initialize population
population = [random.randint(0, 31) for _ in range(10)]

# Genetic Algorithm
for generation in range(50):

    # Evaluate fitness
    population.sort(key=fitness, reverse=True)

    # Selection
    parents = population[:5]

    # Crossover
    offspring = []
    for i in range(5):
        p1 = random.choice(parents)
        p2 = random.choice(parents)

        child = (p1 + p2) // 2
        offspring.append(child)

    # Mutation
    for i in range(len(offspring)):
        if random.random() < 0.1:
            offspring[i] = random.randint(0, 31)

    # Create new population
    population = parents + offspring

# Best solution
best = max(population, key=fitness)

print("Best solution:", best)
print("Best fitness:", fitness(best))
