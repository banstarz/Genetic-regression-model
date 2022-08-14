import random
from chromosome import Chromosome

class GeneticAlgorithm():
    def __init__(self, x, y, population_size = 50, mutation_probability = 0.1, polynomial_degree = 1, 
                 initialization_bounds = (-10, 10), mutation_bounds = (-3, 3), max_generation_number = 1000, elite = 15):
        self.x = x
        self.y = y
        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.polynomial_degree = polynomial_degree
        self.initialization_bounds = initialization_bounds
        self.mutation_bounds = mutation_bounds
        self.population = []
        self.temporary_bounds = []
        self.max_generation_number = max_generation_number
        self.generation_number = 0
        self.history = []
        self.elite = elite
        self.best_chromosome_per_epoch = []
        
    def run(self):
        if not self.population:
            self.initialize_population()
        for i in range(self.max_generation_number):
            self.calculate_mean_population_fitness()
            self.history.append(self.mean_population_fitness)
            self.best_chromosome_per_epoch.append(self.population[0])
            self.crossover()
            self.mutation()
            self.next_generation()
            self.generation_number += 1
            
    def initialize_population(self):
        self.population = [Chromosome(self.x, self.y) for _ in range(self.population_size)]
        for i in range(self.population_size):
            self.population[i].random_initialization(self.polynomial_degree, self.initialization_bounds)
            
    def calculate_mean_population_fitness(self):
        for i in range(self.population_size):
            self.population[i].fitness_value
            
    def crossover(self):
        self.temporary_bounds = []
        for i in range(self.population_size):
            parents = self.select_parents()
            childs = parents[0].crossover(parents[1])
            for i in range(len(childs)):
                self.temporary_bounds.append(childs[i])
            
    def select_parents(self):
        Weights = [1/(i+2) for i in range(self.population_size)]
        return random.choices(self.population, weights = Weights, k = 2)
    
    def mutation(self):
        for i in range(self.population_size):
            self.temporary_bounds[i].mutate(self.mutation_bounds, self.mutation_probability)
            
    def next_generation(self):
        sorted(self.population, key = lambda x: x.fitness_value)
        sorted(self.temporary_bounds, key = lambda x: x.fitness_value)
        j = 0
        for i in range(self.elite):
            if self.temporary_bounds[j].fitness_value <= self.population[i].fitness_value:
                self.population[i] = self.temporary_bounds[j]
                j+=1
        for i in range(self.elite, self.population_size):
            self.population[i] = self.temporary_bounds[j]
            j+=1
    
    @property
    def mean_population_fitness(self):
        return sum([Ind.fitness_value for Ind in self.population])/self.population_size

    def get_best_chromosome_in_epoch(self, epoch_num):
        return self.best_chromosome_per_epoch[epoch_num]