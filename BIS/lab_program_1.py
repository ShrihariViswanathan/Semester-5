
import random

# 1. Define the fitness function
def fitness(x):
    return x ** 2


# 2. Initialize GA parameters
POPULATION_SIZE = 10
GENERATIONS = 20
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
CHROMOSOME_LENGTH = 5


# 3. Create initial population
def create_population():
    population = []

    for i in range(POPULATION_SIZE):
        chromosome = ''.join(
            random.choice('01')
            for _ in range(CHROMOSOME_LENGTH)
        )
        population.append(chromosome)

    return population


# Convert binary chromosome into decimal
def decode(chromosome):
    return int(chromosome, 2)


# 4. Selection (Select the better individuals)
def selection(population):
    selected = random.sample(population, 2)

    if fitness(decode(selected[0])) > fitness(decode(selected[1])):
        return selected[0]
    else:
        return selected[1]


# 5. Crossover (Combine two parents)
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, CHROMOSOME_LENGTH - 1)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

        return child1, child2

    return parent1, parent2


# 6. Mutation (Randomly change bits)
def mutation(chromosome):
    chromosome = list(chromosome)

    for i in range(CHROMOSOME_LENGTH):
        if random.random() < MUTATION_RATE:
            chromosome[i] = '1' if chromosome[i] == '0' else '0'

    return ''.join(chromosome)


# 7. Main Genetic Algorithm
def genetic_algorithm():

    random.seed(42)  # For reproducible results

    population = create_population()

    best_solution = None
    best_fitness = -1

    for generation in range(GENERATIONS):

        # Evaluate fitness
        for chromosome in population:
            x = decode(chromosome)
            value = fitness(x)

            if value > best_fitness:
                best_fitness = value
                best_solution = chromosome

        print("Generation:", generation + 1,
              "| Best x:", decode(best_solution),
              "| Best Fitness:", best_fitness)

        # Create next generation
        new_population = [best_solution]  # Elitism

        while len(new_population) < POPULATION_SIZE:

            # Selection
            parent1 = selection(population)
            parent2 = selection(population)

            # Crossover
            child1, child2 = crossover(parent1, parent2)

            # Mutation
            child1 = mutation(child1)
            child2 = mutation(child2)

            new_population.append(child1)

            if len(new_population) < POPULATION_SIZE:
                new_population.append(child2)

        population = new_population

    print("\nFinal Best Solution:")
    print("Best Chromosome:", best_solution)
    print("Best x:", decode(best_solution))
    print("Maximum Fitness:", best_fitness)


# Run the algorithm
genetic_algorithm()
