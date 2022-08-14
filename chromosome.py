import random
import numpy as np

class Chromosome():
    def __init__(self, x, y, сoefficients = []):
        self.x = x
        self.y = y
        self.сoefficients = сoefficients
        self.fitness = None
        
    def random_initialization(self, polynomial_degree, initialization_bounds):
        self.сoefficients = []
        for _ in range(polynomial_degree+1):
            self.сoefficients.append(random.uniform(initialization_bounds[0], initialization_bounds[1]))
    
    @property
    def fitness_value(self):
        if self.fitness == None:
            self.calculate_fintess()
        return self.fitness
    
    def calculate_fintess(self):
        self.fitness = 0
        for i in range(len(self.x)):
            self.fitness += (self.y[i] - self.regression_output(self.x[i]))**2
        self.fitness /= len(self.x)
            
    def regression_output(self, x):
        res = 0
        for degree, coeff in enumerate(self.сoefficients):
            res += coeff * x**degree
        return res
            
    def crossover(self, other):
        BitMask = [random.choice([0, 1]) for _ in range(len(self.сoefficients))]
        ParentCoefficients = [self.сoefficients, other.сoefficients]
        сoefficients1 = [ParentCoefficients[BitMask[i]][i] for i in range(len(self.сoefficients))]
        сoefficients2 = [ParentCoefficients[not BitMask[i]][i] for i in range(len(self.сoefficients))]
        child1 = Chromosome(self.x, self.y, сoefficients1)
        child2 = Chromosome(self.x, self.y, сoefficients2)
        return (child1, child2)
    
    def mutate(self, MutateBounds, MutateProb):
        for i in range(len(self.сoefficients)):
            if random.random() < MutateProb:
                self.сoefficients[i] += random.uniform(MutateBounds[0], MutateBounds[1])