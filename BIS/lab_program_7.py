
import random

# Fitness function
def fitness(x):
    return x ** 2


# Initialize parameters
POPULATION_SIZE = 10
NUMBER_OF_GENES = 5
GENERATIONS = 20
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8


# Create initial population
def create_population():
    population = []

    for i in range(POPULATION_SIZE):
        genes = ''.join(random.choice('01') for _ in range(NUMBER_OF_GENES))
        population.append(genes)

    return population


# Gene expression
def gene_expression(genes):
    return int(genes, 2)


# Selection
def selection(population):
    parent1, parent2 = random.sample(population, 2)

    if fitness(gene_expression(parent1)) > fitness(gene_expression(parent2)):
        return parent1
    return parent2


# Crossover
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, NUMBER_OF_GENES - 1)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

        return child1, child2

    return parent1, parent2


# Mutation
def mutation(genes):
    genes = list(genes)

    for i in range(NUMBER_OF_GENES):
        if random.random() < MUTATION_RATE:
            genes[i] = '1' if genes[i] == '0' else '0'

    return ''.join(genes)


# Main GEA
def gene_expression_algorithm():
    random.seed(42)
    population = create_population()

    best_solution = None
    best_fitness = -1

    for generation in range(GENERATIONS):

        for genes in population:
            x = gene_expression(genes)
            value = fitness(x)

            if value > best_fitness:
                best_fitness = value
                best_solution = genes

        print("Generation:", generation + 1,
              "Best Genes:", best_solution,
              "Best x:", gene_expression(best_solution),
              "Fitness:", best_fitness)

        new_population = [best_solution]

        while len(new_population) < POPULATION_SIZE:
            parent1 = selection(population)
            parent2 = selection(population)

            child1, child2 = crossover(parent1, parent2)

            child1 = mutation(child1)
            child2 = mutation(child2)

            new_population.append(child1)

            if len(new_population) < POPULATION_SIZE:
                new_population.append(child2)

        population = new_population

    print("\nFinal Best Solution")
    print("Best Genetic Sequence:", best_solution)
    print("Expressed Value:", gene_expression(best_solution))
    print("Maximum Fitness:", best_fitness)


# Run program
gene_expression_algorithm()
